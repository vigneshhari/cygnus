from django.shortcuts import render
from accounts.models import User_Account 
import datetime
from models import Quiz_history,Quiz,Quiz_data
from django.http import HttpResponseRedirect
# Create your views here.


def dash(request):
	try:
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	quiz = Quiz_history.objects.all().filter(user_id = _id)
	quiz_info = Quiz.objects.all() 
	for h in acc:
		check = h.vericode
		name = h.name
		score = h.score
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	avail = 0
	done_quiz = []
	lis = []
	done = 0
	num = 0
	for i in quiz_info:
		hist = Quiz_history.objects.all().filter(user_id = _id , quiz_id = i.quiz_id)
		temp = 0
		for q in hist:
			if(q.quiz_id == i.quiz_id):temp = temp + 1
			if(q.score > 0):temp = 9999
		if(temp < i.attempt):
			num = num + 1
	for k in quiz:
		done = done + 1

	return render(request,'dash.html',{'name' : name , 'score' : score, 'done':done , 'avail' : num})

def attempted(request):
	try:
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	for h in acc:
		name = h.name
		check = h.vericode
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	data = Quiz_history.objects.all().filter(user_id = _id)
	dat = []
	num = 0 ;
	for n in data:
		num = num + 1
		temp = Quiz.objects.all().filter(quiz_id = n.quiz_id)
		for t in temp:
			dat.append({'name' : t.quizname , 'score' : n.score , 'date' : n.Date})
	return render(request,'quizold.html',{'name' : name , 'data' : dat , 'num' : num})

def avaliable(request):
	try:
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	for h in acc:
		name = h.name
		check = h.vericode
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	quiz = Quiz_history.objects.all().filter(user_id = _id)
	quiz_info = Quiz.objects.all() 
	lis = []
	done = 0
	num = 0
	for i in quiz_info:
		hist = Quiz_history.objects.all().filter(user_id = _id , quiz_id = i.quiz_id)
		temp = 0
		for q in hist:
			if(q.quiz_id == i.quiz_id):temp = temp + 1
			if(q.score > 0):temp = 9999
		if(temp < i.attempt):
			num = num + 1
			lis.append({ 'quizid' : i.quiz_id , 'quizname' :i.quizname })
	return render(request,'newquiz.html',{'name' : name , 'data' : lis ,'link':"/quiz/attempt?id=" , 'num' : num})

def attempt(request):
	try:
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	for h in acc:
		name = h.name
		check = h.vericode
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	quizid =request.GET.get('id')
	quizdata = Quiz_data.objects.all().filter(quiz_id = quizid)
	quizinfo = Quiz.objects.all().filter(quiz_id = quizid)
	for i in quizinfo:
		quizname = i.quizname
		link = i.quiz_link
	request.session['quizid'] = quizid
	temp = 1
	data = []
	for e in quizdata:
		ques = []
		for i in e.question.split("<>"):
			print i;
			ques.append({'question' : i})
		data.append({'qid' : temp , 'question' : ques , 'question_type' : e.question_type , 'desc' :e.question_desc ,'Option1' : e.Option1 ,'Option2' : e.Option2 ,'Option3' : e.Option3 ,'Option4' : e.Option4})
		temp = temp + 1
	return render(request,'quiz.html',{'name' : name , 'data' : data ,'quizname':quizname , 'link' : link})

def validate(request):
	try:
		quizid = request.session['quizid']
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	for h in acc:
		name = h.name
		check = h.vericode
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	
	attempt = 0
	qobj = Quiz.objects.all().filter(quiz_id = quizid)
	for obj in qobj:
		attempt = obj.attempt

	hist = Quiz_history.objects.all().filter(user_id = _id , quiz_id = quizid)
	chk = 0
	for obj in hist:
		if(int(obj.quiz_id) == int(quizid)):chk = chk + 1
		if(int(obj.score) > 0):chk = 9999
	if(chk >= attempt):
			return HttpResponseRedirect('/quiz/dash')

	acc = User_Account.objects.all().filter(user_id = _id)
	for h in acc:
		oldscore = h.score
		name = h.name
	quizdata = Quiz_data.objects.all().filter(quiz_id = quizid)
	temp = 1
	score = 0
	finscore = 0;
	qtype = 0
	sc = 0 ;

	for d in Quiz.objects.all().filter(quiz_id = quizid):
				qtime = d.creationdate;
				qtime = qtime.replace(tzinfo=None)
				diff = datetime.datetime.now() - qtime
				seconds = diff.total_seconds()
				day = seconds // (3600 * 24)

	for i in quizdata:
		check = []
		score = 10 - day 
		if(chk != 0):
			score = score - 5 
		if(i.question_type == "image"):
			qtype = 1
			val = request.GET.get(str(temp),'')
			if(i.question_clue == 0):
				score += 5
				if(i.answer.lower().strip(" ") == val.lower().strip(" ")):
					score +=10
				else:
					score = 0
			elif(i.question_clue == 1):
				if(i.answer.lower().strip(" ") == val.lower().strip(" ")):
					score += 10
				else:
					score = 0
		#check box type questions not implemented
		'''	
		if(i.question_type == "check"):
			check = request.GET.getlist(str(temp))
			answer = i.answer.split("&")
			qtype = 1 ;
			for ind,tt in enumerate(check):check[ind] = str(tt).strip(" ")
			for ind,tt in enumerate(answer):answer[ind] = str(tt).strip(" ")
			for ans in answer:
				if(ans in check):score += 10
				else:score -= 15
			for ans in check:
				if(ans not in answer):score -= 15
		'''
		
		
		if(qtype == 0):
			val = request.GET.get(str(temp),'')
			if(i.answer.lower() == val.lower()):
				score += 10
		if(score < 0):score = 0
		finscore = score + finscore
		score = 0		
		temp = temp + 1
	print score
	hist = Quiz_history(quiz_id = quizid , user_id = _id , score = finscore , Date = datetime.datetime.now())
	hist.save()
	score = finscore + oldscore
	User_Account.objects.all().filter(user_id = _id).update(score = score)
	return HttpResponseRedirect('/quiz/dash')

def rank(request):
	try:
		_id = request.session['logid']
		vericode = request.session['vericode']
		acc = User_Account.objects.all().filter(user_id = _id)
	except Exception, e:
		return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	for h in acc:
		name = h.name
		check = h.vericode
	if(check != vericode):return render(request,'login.html',{'loginmessage' : 'Please Login to Continue'  })
	Userdata = User_Account.objects.all().order_by('-score')
	temp = []
	pos = 1
	for e in Userdata:
		temp.append({'pos' : pos , 'name':e.name , 'score':e.score})
		pos = pos + 1
	return render(request,'rank.html',{'name' : name , 'data' : temp})



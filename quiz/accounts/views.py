from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from models import User_Account
from django.http import HttpResponseRedirect
import random
import datetime
import smtplib
import time 

def index(request):
	return render(request, 'main_page.html')
def login(request):
	return render(request, 'login.html')
def forpass(request):
	return render(request , 'forpass.html')
def signup(request):
	return render(request, 'signup.html' )
def loginprocess(request):
	mail =  request.POST.get("username","")
	password = request.POST.get("password","")
	if(len(mail) == 0 and len(password) == 0):
		return render(request,'login.html',{'loginmessage' : ''  })
	user_data = User_Account.objects.all().filter(mail = mail)
	got = True
	for e in user_data:
		got = False
	if(got):
		return render(request,'login.html',{'loginmessage' : 'Email id Does Not Exist Please Signup '})
	_id = 0
	_ver = 0
	for e in user_data:
		_ver = e.verified
		_id = e.user_id
		vericode = e.vericode
		if(e.password != password):
			return render(request,'login.html',{'loginmessage' : 'Password/Emailid entered is wrong please Try again' })
	if(_ver == 0):
		return render(request,'verified.html', {'id' : _id} )
	request.session['logid'] = _id  
	request.session['vericode'] = vericode
	return HttpResponseRedirect('/quiz/dash')
def signupprocess(request):
	password = request.GET.get('password','')
	name = request.GET.get('name','')
	phone = request.GET.get('phonenumber','')
	vericode = '000000'
	verified = '0'	
	mail = request.GET.get('email','')
	dict = {'name' : name , 'phonenumber' : phone,'email' : mail, 'message' : 'Error'}
	if(password == '' or  password.__len__() >= 100 or password.__len__() <= 7):
		dict['signupmessage'] = "Enter a valid password ** It should contain more than 7 charecters ** "
		return render(request,'login.html',dict)
	elif(name == ''):
		dict['signupmessage'] = "Enter a valid name"
		return render(request,'login.html',dict)
	elif(mail == '' or mail.rfind('@') == -1):
		dict['signupmessage'] = "Enter a valid Email-Address"
		return render(request,'login.html',dict)
	try:
		phone = int(phone)
	except Exception, e:
		dict['signupmessage'] = "Enter a valid phone number"
		return render(request,'login.html',dict)
	data = User_Account.objects.all();vals = 0
	email_check = User_Account.objects.all().filter(mail = mail)
	for y in email_check :
		dict['signupmessage'] = "This Email-Address is already in use . Please try again with another Email "
		return render(request,'login.html',dict)
	for e in data :vals+=1
	new_user_id = vals +  1
	sender  = 'vignesh@cecsd.esy.es'
	reciever = mail 
	vericode = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
	print vericode 
	message = """
			Hello {},  
				This is a Verification Message
				Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password
				Please Do Keep this message and the verification code for further use
					
				The verification code is  {}

					Intestellar Team :)

					 DO not Reply To this message 
				""".format(name,vericode)
	try:
   		server = smtplib.SMTP('smtp-pulse.com',2525)
		server.login('vignesh@cecsd.esy.es','nj3tLLbsK2fPRM')
		server.sendmail(sender, reciever, message)
		server.quit()
	except Exception, e:
		print e
   		dict['signupmessage'] = "Invalid Email Address or Try again Later" 
		return render(request,'login.html',dict)
	response = HttpResponse('blah') 
	response.set_cookie( 'user_id', new_user_id )
	p = User_Account(mail = mail,password=password,user_id=new_user_id,name=name,phone_no=phone,vericode=vericode,verified=0,score=0)
	p.save()
	return render(request, 'login.html' , {'loginmessage' : "Please Login To Continue"})

def verified(request):
	id = request.GET.get('id')
	vericode = request.GET.get('veri')
	dat = User_Account.objects.all().filter(id = id)
	for e in dat:
		print e.vericode
		print vericode
		if(str(e.vericode) == str(vericode)):
			User_Account.objects.filter(id = id).update(verified = 1)
			request.session['logid'] = id
			request.session['vericode'] = vericode
			return HttpResponseRedirect('/quiz/dash')
	return render(request,'verified.html',{'id' : id})

def change(request):
	email = request.GET.get('email','')
	veri = request.GET.get('veri','')
	new_pass = request.GET.get('pass','')
	if(len(new_pass) < 7):
		return render(request,"forpass.html",{'changemessage' : "Password should be longer than 7 charecters"})
	acc = User_Account.objects.all().filter(mail = email)
	for i in acc:
		vericode = i.vericode
		print vericode
	if(vericode == veri):
		User_Account.objects.all().filter(mail = email).update(password = new_pass)
	else:
		return render(request,"forpass.html",{'changemessage' : "Wrong Vericode"})
	return render(request, 'login.html' , {'loginmessage' : "Password Changed Please Login To Continue"})

def sendveri(request):
	email = request.GET.get('email','')
	user = User_Account.objects.all().filter(mail = email)
	test = True
	for i in user:
		name = i.name
		vericode = i.vericode
		test = False
	if(test):
				return render(request,"forpass.html",{'sendmessage' : "This Email Does not Exist in our Database"})
	sender  = 'vignesh@cecsd.esy.es'
	message = """
			Hello {},  
				This is a Verification Message
				Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password
				Please Do Keep this message and the verification code for further use
					
				The verification code is  {}

					Intestellar Team :)

					 DO not Reply To this message 
				""".format(name,vericode)
	try:
   		server = smtplib.SMTP('smtp-pulse.com',2525)
		server.login('vignesh@cecsd.esy.es','nj3tLLbsK2fPRM')
		server.sendmail(sender, reciever, message)
		server.quit()
	except Exception, e:
		print e
   		return render(request,"forpass.html",{'sendmessage' : "Invalid Email Address or Try again Later"})
	return render(request,"forpass.html",{'sendmessage' : "Verification Code Sent"})

def logout(request):
	request.session['logid'] = '' 
	request.session['vericode'] = ''
	return HttpResponseRedirect('/app')

    

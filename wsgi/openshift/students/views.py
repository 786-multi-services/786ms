from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect

def std_login(request):
	data={}
	msg=''
	form=LoginForm()
	if request.user.is_authenticated() and Group.objects.get(name="student") in request.user.groups.all():
		data['student']=Student.objects.get(user=request.user)
	else: #signin/signup
		print 'user not authenticated'
		if request.method=='POST':
			print 'POST'
			form=LoginForm(request.POST)
			if form.is_valid():
				print 'form valid'
				username=request.POST['username']
				password=request.POST['password']
				print username,password
				user=authenticate(username=username, password=password)
				if user is not None and Group.objects.get(name="student") in user.groups.all():
					login(request, user)
					msg='Student logged in'
				else:
					msg='No Such Student'
			else:
				pass
		else:#GET singin form
			pass
	if form:
		data['form']=form
	if msg:
		data['msg']=msg
	data['group']=Group.objects.get(name='student')
	return render(request,'students/student_login_form.html',data)
	
def view_details(request):
	return render(request,'student/details.html',{'student':'abcd'})

def signout(request):
	logout(request)
	return HttpResponseRedirect('/')

def std_register(request):
	if request.method=='POST':
		form=StudentRegisterationForm(request.POST,request.FILES)
		
		if form.is_valid():
			student=form.save(commit=False)
			#user creating 
			user=User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.last_name=form.cleaned_data['last_name']
			user.first_name=form.cleaned_data['first_name']
			user.save()
			#add to student group
			group=Group.objects.get(name="student")
			group.user_set.add(user)
			#save student
			student.user=user
			student.token=StudentToken.objects.get(token=form.cleaned_data['ttoken'],name=student.user.get_full_name())
			student.save()
			student.save_m2m()
		else:
			print 'invalid form'
		
		#Student creation
	else:#GET
		form=StudentRegisterationForm()
	return render(request,'students/registration_form.html',{'form':form})
	
def manager_login(request):
	form=LoginForm()
	data={}
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username, password=password)
		if user is not None and Group.objects.get(name="manager") in user.groups.all():
			login(request, user)
			msg='Manager logged in'
			data['students']=Student.objects.all()
		else:
			msg='No such manager'
	else:#GET
		if request.user.is_authenticated() and Group.objects.get(name="manager") in request.user.groups.all():
			data['students']=Student.objects.all()
	data['form']=form
	if msg:
		data['msg']=msg
	data['group']=Group.objects.get(name='manager')
	return render(request,'students/manager_login_form.html',data)

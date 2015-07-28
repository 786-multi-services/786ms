from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from .models import *

def std_login(request):
	if request.user.is_authenticated() and Group.objects.get(name="student") in request.user.groups.all():
		return HttpResponseRedirect("details/")
	else:
		data={}
		msg=''
		form=LoginForm()
		if request.method=='POST':
			print 'POST'
			form=LoginForm(request.POST)
			if form.is_valid():
				username=request.POST['username']
				password=request.POST['password']
				user=authenticate(username=username, password=password)
				if user is not None and Group.objects.get(name="student") in user.groups.all():
					login(request, user)
					return HttpResponseRedirect("details/")
				else:
					msg='No Such Student'
		else:
			#GET singin form
			pass
		if form:
			data['form']=form
		if msg:
			data['msg']=msg
		return render(request,'students/student_login_form.html',data)
		
	
def std_details(request):
	if request.user.is_authenticated() and Group.objects.get(name="student") in request.user.groups.all():
		data={}
		group=Group.objects.get(name="student")
		data['group']=group
		student=Student.objects.get(user=request.user)
		data['student']=student
		if request.method=='POST':
			update_form=StudentUpdateForm(request.POST,request.FILES,instance=student)
			if update_form.is_valid():
				request.user.email=update_form.cleaned_data['email']
				if update_form.cleaned_data['password1']:
					request.user.set_password(update_form.cleaned_data['password1'])
				request.user.save()
				update_form.save()
				student=Student.objects.get(user=request.user)
				data['student']=student
				update_form=StudentUpdateForm(instance=student,initial={'email':student.user.email,'photo':student.photo})
				data['update_form']=update_form
				data['msg']='Details updated successfully'
			else:	
				data['update_form']=update_form
				data['msg']='Details not valid'
		else:
			update_form=StudentUpdateForm(instance=student,initial={'email':student.user.email,'photo':student.photo})
			data['update_form']=update_form
		return render(request,'students/student_details.html',data)
	return HttpResponseRedirect("/student")


def signout(request):
	logout(request)
	return HttpResponseRedirect('/student')

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

def get_random_token():
	return ''.join([random.choice('0123456789ABCDEF') for x in range(8)])
	
def manager_panel(request):
	data={}
	if request.user.is_authenticated() and Group.objects.get(name="manager") in request.user.groups.all():
		if request.method=='POST':
			token_form=TokenForm(request.POST)
			if token_form.is_valid():
				name=token_form.cleaned_data['name']
				token=token_form.save(commit=False)
				save=False
				while(not save):
					try:
						token.save()
						save=True
					except:
						token.token=get_random_token()
				data['token']=token
				data['token_form']=TokenForm()
		else:
			data['students']=Student.objects.all()
			data['token_form']=TokenForm()
		return render(request,'students/manager_panel.html',data)
	else:
		return HttpResponseRedirect("/students/manager")

def view_std(request,pk):
	data={}
	if request.user.is_authenticated() and Group.objects.get(name="manager") in request.user.groups.all():
		data['student']=Student.objects.get(pk=pk)
		return render(request,'students/view_std.html',data)
	else:
		return HttpResponseRedirect("/students/manager")

def manager_login(request):
	if request.user.is_authenticated() and Group.objects.get(name="manager") in request.user.groups.all():
		#possibly already login
		return HttpResponseRedirect("manager-panel/")
	else:
		form=LoginForm()
		data={}
		msg=''
		if request.method=='POST':
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username, password=password)
			if user is not None and Group.objects.get(name="manager") in user.groups.all():
				login(request, user)
				return HttpResponseRedirect("manager-panel/")
			else:
				msg='No such manager'
		data['form']=form
		if msg:
			data['msg']=msg
		return render(request,'students/manager_login_form.html',data)

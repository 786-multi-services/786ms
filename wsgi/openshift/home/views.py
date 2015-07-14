from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.utils import timezone
from home.models import User,Message

from .forms import ContactForm

def index(request,tag='home'):
	return_data={'active_nav_link':tag,'title':'786 Multi Services','is_index':True,
	'zeeshan_fb':'https://www.facebook.com/zeeshankhan.1001',
	'zeeshan_tw':'https://twitter.com/zkhan1093',
	'sarfaraz_fb':'https://www.facebook.com/sarfaraz.nawaz.775',
	'sarfaraz_tw':'https://twitter.com/shaibzada',
	'daakhan_fb':'https://www.facebook.com/profile.php?id=100006601905636',
	'daakhan_tw':'#',
	}
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			try:
				user=User.objects.get(email=request.POST.get("email",""))
			except ObjectDoesNotExist:
				user=User(name=request.POST.get("name",""),email=request.POST.get("email",""))
			user.save()
			user.message_set.create(msg=request.POST.get("message"),time=timezone.now())
			return_data['success_msg']='Thank You '+user.name+', We will contact you soon.'
			form=ContactForm()
	else:
		form=ContactForm()
	return_data['form']=form
	return render(request,'home/index.html',return_data)

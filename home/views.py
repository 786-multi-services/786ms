from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import *
from .forms import ContactForm

def handler404(request):
	return render(request,'error.html',{'heading':'Error 404','content':'Requested URL '+request.build_absolute_uri()+' not found'})

def handler500(request):
	return render(request,'error.html',{'heading':'Error 500','content':'Internal server error.'})

def handler403(request):
	return render(request,'error.html',{'heading':'Error 403','content':'permission denied.'})

def handler400(request):
	return render(request,'error.html',{'heading':'Error 400','content':'Bad request.'})

def index(request):
	return index(request,'home')
def index(request,tag='home'):
	return_data={'active_nav_link':tag,'title':'786 Multi Services','is_index':True,
	'zeeshan_fb':'https://www.facebook.com/zeeshankhan.1001',
	'zeeshan_tw':'https://twitter.com/zkhan1093',
	'sarfaraz_fb':'https://www.facebook.com/sarfaraz.nawaz.775',
	'sarfaraz_tw':'https://twitter.com/shaibzada',
	'daakhan_fb':'https://www.facebook.com/profile.php?id=100006601905636',
	'daakhan_tw':'#',
	'news_list': Object.objects.filter(object_type=OBJECT_NEWS).order_by('time'),
	'programme_list': Object.objects.filter(object_type=OBJECT_PROGRAMME).order_by('time'),
	'today':datetime.date.today(),
	'travel_services':Service.objects.filter(service_type=SERVICE_TRAVEL),
	'application_services':Service.objects.filter(service_type=SERVICE_APPLICATION),
	'recharge_services':Service.objects.filter(service_type=SERVICE_RECHARGE),
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

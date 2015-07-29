from django.contrib import admin
from .models import *

class StudentTokenAdmin(admin.ModelAdmin):
	list_display=['token','name','datetime','by']

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentToken,StudentTokenAdmin)

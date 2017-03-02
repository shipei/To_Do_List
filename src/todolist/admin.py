from django.contrib import admin

# Register your models here.
from .forms import *
from .models import *

# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__", "timestamp", "updated"]
# 	form = SignUpForm
# 	# class Meta:
# 		# model = SignUp

# class ToDoAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__"]
# 	form = ToDoForm

admin.site.register(ToDoList)
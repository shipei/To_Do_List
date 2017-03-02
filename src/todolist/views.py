from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
# Create your views here.
def home(request):
	context = {}
	return render(request, "home.html", context)

def register(request):
	return render(request, "registration_form.html", context)

def about(request):
	context = {}
	return render(request, "about.html", context)

def contact(request):
	title = "Contact Us"
	form = ContactForm(request.POST or None)
	
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get('full_name')

		subject = 'site contact form'
		from_email = form_email
		to_email = [settings.EMAIL_HOST_USER]
		contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "forms.html", context)

@login_required()
def profile(request):
	title = "Build your To Do List Now!"
	form = ToDoForm(request.POST or None)
	print(form)
	if form.is_valid():
		form.save(commit=True)
	queryset = ToDoList.objects.all()
	# print(ToDoList.objects.all())
	context = {}
	if request.user.is_authenticated():
		print("user!!!")
		context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
		return render(request, "profile.html", context)
	else:
		return redirect('/accounts/login')






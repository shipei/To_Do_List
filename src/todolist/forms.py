from django import forms

from .models import *

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()
		

# class SignUpForm(forms.ModelForm):
# 	username = forms.CharField(max_length=20)
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

# 	class Meta:
# 		model = SignUp
# 		fields = ['username', 'email', 'password', 'confirm_password']
# 		# exclude = ['full_name']

# 	def clean(self):
# 		password = self.cleaned_data.get('password')

# 		confirm_password = self.cleaned_data.get('confirm_password')
# 		if password != confirm_password:
# 			raise forms.ValidationError("passwords do not match!")

class ToDoForm(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = ['task', 'due_on']
		


from django import forms
from django.contrib.auth.models import User, Group


class CreateUserForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30) #render_value=False
	first_name= forms.CharField(max_length=30)
	last_name= forms.CharField(max_length=30)
	email= forms.CharField(max_length=30)
	groups= forms.ModelMultipleChoiceField(queryset=Group.objects.all())


	def clean_username(self): # check if username dos not exist before
		try:
			User.objects.get(username=self.cleaned_data['username']) #get user from user model
		except User.DoesNotExist :
			return self.cleaned_data['username']

		raise forms.ValidationError("This user already exists")

	def save(self):
		new_user=User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.groups = self.cleaned_data['groups']
		new_user.save()

class CreateGroupForm(forms.Form):
	name = forms.CharField(max_length=30)

	def clean_name(self): 
		try:
			Group.objects.get(name=self.cleaned_data['name']) #get user from user model
		except Group.DoesNotExist :
			return self.cleaned_data['name']

		raise forms.ValidationError("This group already exists")

	def save(self):
		new_group=Group(name=self.cleaned_data['name'])
		new_group.save()
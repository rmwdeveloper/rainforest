from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(forms.ModelForm):
	username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
	first_name = forms.CharField(label='first_name',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	middle_initial = forms.CharField(label='middle_initial',widget=forms.TextInput(attrs={'placeholder':'Middle Initial'}))
	last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	birth_date = forms.DateField(label='birth_date',widget=forms.TextInput(attrs={'placeholder':'Date of Birth'}))
	street_address = forms.CharField(label='street_address',widget=forms.TextInput(attrs={'placeholder':'Street Address'}))
	city = forms.CharField(label='city',widget=forms.TextInput(attrs={'placeholder':'City'}))
	state = forms.CharField(label='state',widget=forms.TextInput(attrs={'placeholder':'State'}))
	zip_code = forms.CharField(label='zip_code',widget=forms.TextInput(attrs={'placeholder':'Zip'}))
	email = forms.CharField(label='email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'placeholder':'Password(again)'}))

	class Meta:
		model = UserProfile
		fields = ['username','middle_initial','birth_date','street_address',
				'city','state','zip_code','email','first_name','last_name']
	def clean_password2(self):
	# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			msg = "Passwords don't match"
			raise forms.ValidationError("Password mismatch")
			return password2

	def save(self, commit=True):
		if not commit:
			raise NotImplementedError("Can't create User and UserProfile without database save")
		
		user_profile = UserProfile(username = self.cleaned_data['username'], 
					first_name = self.cleaned_data['first_name'], 
					middle_initial = self.cleaned_data['middle_initial'],
					last_name = self.cleaned_data['last_name'], 
					birth_date = self.cleaned_data['birth_date'],
					street_address= self.cleaned_data['street_address'],
					city=self.cleaned_data['city'],
					state= self.cleaned_data['state'],
					zip_code= self.cleaned_data['zip_code'],
					email= self.cleaned_data['email'],
					is_active =  True )
		
		user_profile.set_password(self.cleaned_data['password1'])

		user_profile.save()
		# return user, user_profile
		return user_profile

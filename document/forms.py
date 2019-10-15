from django import forms

class Signup(forms.Form):
	FirstName = forms.CharField(max_length=100)
	LastName = forms.CharField(max_length=100)
	Email = forms.EmailField()
	Password = forms.CharField(max_length=40,widget=forms.PasswordInput)
	Cpassword = forms.CharField(max_length=40,widget=forms.PasswordInput)

class Login(forms.Form):
	Email = forms.EmailField()
	Password = forms.CharField(max_length=40)

class UploadImage(forms.Form):
	Email = forms.EmailField()
	Description = forms.CharField(max_length=100,widget=forms.Textarea)
	Myfile = forms.ImageField()

class UploadFiles(forms.Form):
	Email1 = forms.EmailField()
	Description1 = forms.CharField(max_length=100,widget=forms.Textarea)
	File = forms.FileField()

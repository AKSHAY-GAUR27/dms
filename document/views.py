from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import Signup,Login,UploadImage,UploadFiles
from .models import AddUser,Uimage,Ufiles

# Create your views here.
def index(request):
	return render(request,"index.html")

def login(request):
	if request.session.get("islogin"):
		return render(request,"home.html")
	else:
		return render(request,"login.html")

def signup(request):
	if request.session.get('islogin'):
		return render(request,"home.html")
	else:
		return render(request,"signup.html")

class Signup1(View):
	def get(self,request):
		error = "Method is not correct"
		return render(request,"signup1.html",{'error':error})
	def post(self,request):
		form = Signup(request.POST)
		if request.method == "POST":
			if form.is_valid():
				password = form.cleaned_data['Password']
				cpass = form.cleaned_data['Cpassword']
				if password == cpass:
					data = {
						'FirstName' : form.cleaned_data['FirstName'],
						'LastName' : form.cleaned_data['LastName'],
						'Email' : form.cleaned_data['Email'],
						'Password' : form.cleaned_data['Password']
					}
					new_user = AddUser.objects.create(**data)
					return render(request,"login.html")
				else:
					error = "Password does not matched"
					return render(request,"signup.html",{'error':error})
			else:
				error = "Form not valid"
				return render(request,"signup.html",{'error':error})
		else:
			error = "Method is not post"
			return render(request,"signup.html",{'error':error})


class Login1(View):
	def get(self,request):
		error = "Invalid method"
		return render(request,"login.html",{'error':error})
	def post(self,request):
		form = Login(request.POST)
		print(form)
		if request.method == "POST":
			if form.is_valid():
				data = {
					'email' : form.cleaned_data['Email'],
					'password' : form.cleaned_data['Password'],
				}
				try:
					email = form.cleaned_data['Email']
					password = form.cleaned_data['Password']
					u = AddUser.objects.get(Email=email)
					p = u.Password
					if p == password:
						request.session['email'] = email
						request.session['islogin'] = True
						return render(request,"home.html")
					else:
						error = "Password Does not matched! Try Again"
						return render(request,'login.html',{'error':error})
				except AddUser.DoesNotExist as e:
					error = "User does not exist please signup to login"
					return render(request,"signup.html",{'error':error})
			else:
				error = "Form is not valid"
				return render(request,"login.html",{'error':error})

def logout(request):
	del request.session['email']
	del request.session['islogin']
	return render(request,"login.html")

def upload(request):
	return render(request,"upload.html")

def img(request):
	return render(request,"img.html")

class Img1(View):
	def get(self,request):
		error = "No get request accepted"
		return render(request,"img.html",{'error':error})
	def post(self,request):
		form = UploadImage(request.POST,request.FILES)
		if form.is_valid():
			email = form.cleaned_data['Email']
			try:
				AddUser.objects.get(Email=email)
			except AddUser.DoesNotExist as e:
				error = "No such user Exist ask him to signup"
				return render(request,"img.html",{'error':error})
			else:
				data = {
					'Sender' : AddUser.objects.get(Email=request.session['email']),
					'Receiver' : AddUser.objects.get(Email=form.cleaned_data['Email']),
					'Description' : form.cleaned_data['Description'],
					'Pic' : form.cleaned_data['Myfile']	
				}
				newfile = Uimage.objects.create(**data)
				newfile.save()
				msg = "Successfully send"
				return render(request,"home.html",{'msg':msg})
		else:
			error = "Invalid Form"
			return render(request,"img.html",{'error':error})



def pdf(request):
	return render(request,"pdf.html")

def ppt(request):
	return render(request,"pdf.html")

class Ppt1(View):
	def get(self,request):
		error = "No get request accepted"
		return render(request,"pdf.html",{'error':error})
	def post(self,request):
		form = UploadFiles(request.POST,request.FILES)
		if form.is_valid():
			email = form.cleaned_data['Email1']
			try:
				AddUser.objects.get(Email=email)
			except AddUser.DoesNotExist as e:
				error = "No such user Exist ask him to signup"
				return render(request,"pdf.html",{'error':error})
			else:
				data = {
					'Sender1' : AddUser.objects.get(Email=request.session['email']),
					'Receiver1' : AddUser.objects.get(Email=form.cleaned_data['Email1']),
					'Description1' : form.cleaned_data['Description1'],
					'File' : form.cleaned_data['File']	
				}
				newfile = Ufiles.objects.create(**data)
				newfile.save()
				msg = "Successfully send"
				return render(request,"home.html",{'msg':msg})
		else:
			error = "Invalid Form"
			return render(request,"pdf.html",{'error':error})


def show(request):
	if request.session.get('islogin'):
		data = Uimage.objects.filter(Sender__Email=request.session['email'])
		data1 = Uimage.objects.filter(Receiver__Email=request.session['email'])
		imagedata = []
		imagedata1 = []
		for obj in data:
			u = {
				'receiver' : obj.Receiver,
				'description' : obj.Description,
				'image' : obj.Pic.url,
				}
			imagedata.append(u)
		for obj1 in data1:
			u = {
				'sender' : obj1.Sender,
				'description' : obj1.Description,
				'image' : obj1.Pic.url,
				}
			imagedata1.append(u)
		filedata = Ufiles.objects.filter(Sender1__Email=request.session['email'])
		filedata1 = Ufiles.objects.filter(Receiver1__Email=request.session['email'])
		fdata = []
		fdata1 = []
		for o in filedata:
			u = {
				'receiver1' : o.Receiver1,
				'description1' : o.Description1,
				'file' : o.File.url,
				}
			fdata.append(u)
		for o1 in filedata1:
			u = {
				'sender1' : o1.Sender1,
				'description1' : o1.Description1,
				'file' : o1.File.url,
				}
			fdata1.append(u)
		#return render(request,"data.html",{'data':imagedata,'data1':imagedata1})
		return render(request,"data.html",{'data':imagedata,'data1':imagedata1,'fdata':fdata,'fdata1':fdata1})


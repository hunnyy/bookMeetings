from django.shortcuts import render
from .models import CompanyRegister, RoomAdd, Login, HrLogin, EventAdd
from rest_framework import viewsets
from .serializers import AddcompSerializer, RoomaddSerializer, HrLoginSerializer, EventAddSerializer
from .forms import Addcomp, LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt



class Addcompview(viewsets.ModelViewSet):
	queryset = CompanyRegister.objects.all()
	serializer_class = AddcompSerializer

class Roomaddview(viewsets.ModelViewSet):
	queryset = RoomAdd.objects.all()
	serializer_class = RoomaddSerializer

class HrLoginView(viewsets.ModelViewSet):
	queryset = HrLogin.objects.all()
	serializer_class = HrLoginSerializer
	
class EventAddView(viewsets.ModelViewSet):
	queryset = EventAdd.objects.all()
	serializer_class = EventAddSerializer


@csrf_exempt
def addcomp(request):
	form_class = Addcomp
	form = form_class(request.POST or None)
	#form_class = Addcomp
    #form = form_class(request.POST or None)
	#if request.method == 'POST':
	#	form = Addcomp(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		user = authenticate(companyname=cd['Name'], credits=cd['Credits'])
		return HttpResponseRedirect('Company Added')

	return render(request, 'addcompany.html', {'form': form})

def compadd(request):
	if request.method=='POST':
		if request.POST.get('name') and request.POST.get('credit'):
			add=Compadd()
			add.name=request.POST.get('name')
			add.credit=request.POST.get('credit')
			add.save()
			return render(request,'compadd.html')
	else:
		return render(request,'compadd.html')


def login_page(request):
	form = LoginForm(request.POST or None)
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "login.html", { 'form' : form})

def register_page(request):
	form = RegisterForm(request.POST or None)
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "register.html", { 'form' : form})

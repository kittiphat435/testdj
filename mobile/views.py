from django.shortcuts import render
from django.http import HttpResponse
from .models import MobileProduct,Ems
from .forms import Askqaforms

def Home(request):
	#return HttpResponse('<h1> Hello WOrld</h1>')
	allmobile = MobileProduct.objects.all()
	mobile_number = [[i+1,mb] for i,mb in enumerate(allmobile) ]
	context = {'mobilelist':mobile_number}
	return render(request,'mobile/home.html',context)

def About(request):
	return render(request,'mobile/about.html')
# Create your views here.
def Contact(request):
	return render(request,'mobile/contact.html')

def EMS(request):
	context={'namelist':['นาย ก ','นาย ข',' นาย ค'], 'stringxx':' โอ๊ยยย ตายแล้วสุดจังเลยย'}
	return render(request,'mobile/EMS.html',context)

def Ask_qa(request):
	if request.method == 'POST':
		form = Askqaforms(request.POST)
		if form.is_valid():
			form.save()
			print('Complate submit')
	forms = Askqaforms()
	context = {'forms':forms}
	return render(request,'mobile/form.html',context)		

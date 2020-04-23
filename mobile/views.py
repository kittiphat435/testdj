from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
	#return HttpResponse('<h1> Hello WOrld</h1>')
	return render(request,'mobile/home.html')

def About(request):
	return render(request,'mobile/about.html')
# Create your views here.
def Contact(request):
	return render(request,'mobile/contact.html')

def EMS(request):
	context={'namelist':['นาย ก ','นาย ข',' นาย ค'], 'stringxx':' โอ๊ยยย ตายแล้วสุดจังเลยย'}
	return render(request,'mobile/EMS.html',context)


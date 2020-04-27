from django.shortcuts import render
from cobaapp.models import Employee
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'cobaapp/index.html')

def dua(request):
    istekler = Employee.objects.all()
    context = {'istekler':istekler}
    return render(request,'cobaapp/dua.html',context)

def format(request):
    return render(request,'cobaapp/format.html')

def contact(request):
    form = ContactForm()
    return render(request, 'cobaapp/format.html', {'form':form})

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'cobaapp/index.html')

def dua(request):
    return render(request,'cobaapp/dua.html')

def people(request):
    istekler = Employee.objects.all()
    return render(request, 'dua.html', locals())

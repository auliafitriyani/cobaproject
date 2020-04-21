from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'cobaapp/index.html')

def dua(request):
    return render(request,'cobaapp/dua.html')

def identity(request):
    istekler = Person.objects.all()
    return render(request, 'dua.html', locals())

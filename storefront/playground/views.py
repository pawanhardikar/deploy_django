from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here. Hello World For Now
def say_hello(request):
    return render(request, 'hello.html')

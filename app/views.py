from django.shortcuts import render

# Create your views here.

def jinja(request):
    d={'name':'lokesh'}
    return render(request,'jinja.html',context=d)
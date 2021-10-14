from django.shortcuts import render,HttpResponse
from Home.models import Contact

# Create your views here.
def home(request):
    context = {'name': 'sony','course':'Django'}
    # return HttpResponse("This is my home page")
    return render(request,'home.html',context)
    
def about(request):
    # return HttpResponse("This is my about page")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my projects page")
    return render(request,'projects.html')

def contacts(request):
    if request.method=="POST":
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        # print(name,email,phone,desc)
        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been written to the db")
    # return HttpResponse("This is my contact page")
    return render(request,'contacts.html')
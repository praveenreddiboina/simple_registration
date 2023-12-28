from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]          
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]

        if password!=confirmpassword:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:      
            my_user = User(name=name,email=email,password=password)
            # my_user=User.objects.create_user(name,email,password)
            my_user.save()
            return redirect('login/')

    return render(request,"signup.html") 

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        users = User.objects.all()
        for user in users :
            if user.name == username and user.password == password:
                return render(request,'home.html')
    return render(request,'login.html')

def logout(request):
      if request.method == 'POST':
           return redirect('login/')
      return redirect('login/')

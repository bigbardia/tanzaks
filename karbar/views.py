from django.contrib import messages
from django.shortcuts import render , redirect
from django.views import View
from karbar.forms import SignUpForm , LoginForm
from django.contrib.auth import login



class SignUpView(View):

    def get(self,request):
        form = SignUpForm()
        return render(request , "karbar/signup.html" , {"form":form})


    def post(self,request):

        form = SignUpForm(request.POST)

        if form.is_valid():
            
            user = form.save()
            messages.info(request , str(user.meme_id))
            login(request , user)

            
            return redirect("signup")
        return render(request , "karbar/signup.html" , context = {"form":form})
    

class LoginView(View):

    def get(self,request):

        form = LoginForm()
        return render(request , "karbar/login.html" , {"form":form})

    def post(self,request):

        form = LoginForm(request.POST)
        if form.is_valid():
            form.save(request = request)
            return redirect("meme")
        
        return render(request , "karbar/login.html" , {"form":form})

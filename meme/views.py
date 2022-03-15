from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from meme.forms import MemeForm
from meme.models import Meme
from django.contrib.auth.mixins import LoginRequiredMixin

def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH", False) == "XMLHttpRequest"


class MemeView(LoginRequiredMixin , View):

    login_url = "signup"

    def get(self,request):
        context = {}
        context["form"] = MemeForm()

        if request.session.get("NEW" , False) == "NEW":
            context["memes"] = Meme.objects.newest_memes()
            context["IS_NEW"] = True
        elif request.session.get("LIKE" , False) == "LIKE":
            context["memes"] = Meme.objects.most_liked()
            context["IS_LIKE"] = True
        else:
            context["IS_NEW"] = True
            context["memes"] = Meme.objects.newest_memes()

        

        return render(request , "meme/meme.html" , context)

    def post(self,request):


        if is_ajax(request):
        
            meme = Meme.objects.get(pk = request.POST["pk"])

            if meme.likes.filter(pk = request.user.pk).exists():
                meme.likes.remove(request.user)
            else:
                meme.likes.add(request.user)
        
    
            return JsonResponse([meme.likes.count()] ,status=200 , safe = False)
        
        
        elif request.POST.get("NEW" , False) or request.POST.get("LIKE" , False):
            
            request.session["NEW"] =  request.POST.get("NEW" , False)
            request.session["LIKE"] = request.POST.get("LIKE" , False)
        
            return redirect("meme")



            
        else:


            form = MemeForm(request.POST , request.FILES)
            if form.is_valid():
                meme = form.save(commit = False)
                meme.user = request.user
                meme.save()
                return redirect("meme")
            return redirect("meme")
            


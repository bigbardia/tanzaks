from django import forms
from karbar.models import Karbar
from django.contrib.auth import authenticate , login

class SignUpForm(forms.ModelForm):

    username = forms.CharField(label= "Enter Your username")

    class Meta:
        model = Karbar
        fields = [
            'username'
        ]

    def clean_username(self):
        usrname = self.cleaned_data["username"]
        try:
            Karbar.objects.get(username = usrname)
        except Karbar.DoesNotExist:
            return usrname
        raise forms.ValidationError("Username already taken!")
    
    def save(self, commit=True):
        user = Karbar.objects.create_user(username = self.cleaned_data["username"])
        return user


class LoginForm(forms.Form):

    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput , label="Password")


    def clean_username(self):
        usrname = self.cleaned_data["username"]

        try:
            Karbar.objects.get(username = usrname)
        except Karbar.DoesNotExist:
            raise forms.ValidationError("Username does not exist")

        return usrname

    def clean(self):
        
        usrname = self.data["username"]
        pswrd  = self.data["password"]
        if  authenticate(username = usrname , password = pswrd):
            return self.cleaned_data
        raise forms.ValidationError("the given information is wrong")
    
    def save(self , request =None):
        user = authenticate(username = self.cleaned_data["username"] , password = self.cleaned_data["password"])
        login( request=request, user = user)
        return user

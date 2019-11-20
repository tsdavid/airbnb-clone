from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # password form은 password form field가 따로 없다.
    # 그래서 CharField로 하고 그럼 보호가 안돼니까 widget으로 
    # PasswordInput을 하면 숫자를 가려준다.

    def clean(self):
        email = self.cleaned_data.get("email")      # get the data from user sent us
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is Wrong"))
        except models.User.DoesNotExist:
            self.add_error("email",forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):
    
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exist with this email")
        except models.User.DoesNotExist:
            return email
    
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

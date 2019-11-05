from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # password form은 password form field가 따로 없다.
    # 그래서 CharField로 하고 그럼 보호가 안돼니까 widget으로 
    # PasswordInput을 하면 숫자를 가려준다.

    def clean_email(self):
        """ data를 clean 하게 가지고 와야 db에 저장되있는 email 이랑 pwd를 비교할 텐데
        form에 받은 정보를 clean하게 해야한다
        clean하게 하려면 함수를 쓰는데
        함수 명이 임의로 정하는게 아니라
        clean_필드명
        으로 설정해줘야한다.
        email 필드를 clean하고 싶으면
        clean_email 해야함
        """
        email = self.cleaned_data.get("email")      # get the data from user sent us
        try:
            models.User.objects.get(username=email)     # try to find one
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    
    def clean_password(self):
        return "lulqwewqe"
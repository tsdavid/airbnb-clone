from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "tsdavid@naver.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            """ if there error on the form 
            it didnt work
            """
            print(form.cleaned_data)    
            """ 
                일단 form에서 받은 data를 장고에게 보내서
                사용허가를 받아야 
                그제서야 우리는 clean data를 사용할 수 있다.

                또한 form에서 clean_field를 하면
                form에서 설정한 데이터로 return이 된다.
            """
        return render(request, "users/login.html", {"form": form})
    
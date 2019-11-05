from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # password form은 password form field가 따로 없다.
    # 그래서 CharField로 하고 그럼 보호가 안돼니까 widget으로 
    # PasswordInput을 하면 숫자를 가려준다.
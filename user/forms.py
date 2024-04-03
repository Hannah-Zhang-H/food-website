from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# 继承UserCreationForm
class RegisterForm(UserCreationForm):
    # 添加一个额外的field：email
    email = forms.EmailField()

    # Meta class就是提供关于这个类本身信息的类,它会hold住RegisterForm的信息
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

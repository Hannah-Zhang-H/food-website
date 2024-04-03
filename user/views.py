from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user.forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # 如果是post，返回一个消息
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            # is_valid()已经帮我们做了input validation，且用户名不会重复
            # save所有的user信息
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account is created')
            return redirect('food:index')
    else:
        # form = UserCreationForm()
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form, })

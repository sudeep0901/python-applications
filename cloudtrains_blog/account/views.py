from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                print("Checking if user is none")
                if user.is_active:
                    print("Authentication Successfully")
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    print("Authentication failed")
                    return HttpResponse("Invalid login")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

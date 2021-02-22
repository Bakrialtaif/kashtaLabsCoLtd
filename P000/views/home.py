from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def show(request):
    context = {
    }
    return render(request, 'P000_login/form.html', context=context)

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect('P001:home')

            else:

                messages.error(request, _("Invalid username or password."))
        
        else:

            messages.error(request, _("Invalid username or password."))

    form = AuthenticationForm()
    return redirect('P000:website-home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('P000:home'))

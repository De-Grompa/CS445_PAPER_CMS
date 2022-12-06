from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
import hashlib

#url(r'^static/', TemplateView.as_view(template_name="pdfExample.pdf"),
    #name = "pdfExample"),

def register_user(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
            form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



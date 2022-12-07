from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
import hashlib
import datetime

#url(r'^static/', TemplateView.as_view(template_name="pdfExample.pdf"),
    #name = "pdfExample"),
    
def register_user(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            today = datetime.date.today()
            hsc = hashlib.sha1(str(today).encode()).hexdigest()
            if hsc[:6] == form.cleaned_data.get('secret_code'):
                isAdmin = True
            else:
                isAdmin = False
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, is_staff=isAdmin)
            login(request, user)
            return redirect('home')
    else:
            form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



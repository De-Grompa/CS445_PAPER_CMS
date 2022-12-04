from django_project.forms import RegistrationForm
from django.contrib.auth import login, authenticate

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        #Show error if invalid
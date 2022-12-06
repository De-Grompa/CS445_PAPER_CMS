from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    secret_code = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "secret_code")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.clearned_data['username']
        if commit:
            user.save()
        return user

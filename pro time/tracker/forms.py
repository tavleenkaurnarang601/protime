from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Role, User
class RegistrationForm(UserCreationForm):
    company_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    class Meta: model=User; fields=('company_name','first_name','email','password1','password2')
    def save(self,commit=True):
        company=Company.objects.create(name=self.cleaned_data['company_name'])
        user=super().save(commit=False); user.username=self.cleaned_data['email']; user.email=self.cleaned_data['email']; user.company=company; user.role=Role.ADMIN
        if commit: user.save()
        return user
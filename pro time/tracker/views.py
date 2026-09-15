from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import AuditLog, Project, Task, Role
class ProLoginView(LoginView): template_name='registration/login.html'; redirect_authenticated_user=True
@transaction.atomic
def register(request):
    if request.user.is_authenticated:return redirect('dashboard')
    form=RegistrationForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save(); login(request,user); AuditLog.objects.create(company=user.company,actor=user,action='REGISTER',resource='company'); return redirect('dashboard')
    return render(request,'registration/register.html',{'form':form})
@login_required
def dashboard(request):
    user=request.user; company=user.company
    if user.role==Role.EMPLOYEE: metrics=[("Today's time",'08h 25m'),('Active time','07h 10m'),('Idle time','01h 15m'),('Productivity','84%'),('Current project','E-Commerce Platform'),('Current task','Implement Authentication')]
    else: metrics=[('Total employees',company.users.filter(is_active=True).count()),('Active projects',company.projects.filter(status='ACTIVE').count()),('Open tasks',Task.objects.filter(project__company=company).exclude(status='COMPLETED').count()),('Average productivity','84%')]
    return render(request,'tracker/dashboard.html',{'metrics':metrics,'is_employee':user.role==Role.EMPLOYEE,'role_label':user.get_role_display()})
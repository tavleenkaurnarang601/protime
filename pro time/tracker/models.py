from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
class Role(models.TextChoices): ADMIN='ADMIN','Admin'; MANAGER='MANAGER','Manager'; EMPLOYEE='EMPLOYEE','Employee'
class Company(models.Model):
    name=models.CharField(max_length=100); timezone=models.CharField(max_length=64,default='Asia/Kolkata'); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class User(AbstractUser):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='users',null=True,blank=True)
    role=models.CharField(max_length=10,choices=Role.choices,default=Role.EMPLOYEE)
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'; REQUIRED_FIELDS=['username']
class Project(models.Model):
    class Status(models.TextChoices): PLANNING='PLANNING','Planning'; ACTIVE='ACTIVE','Active'; ON_HOLD='ON_HOLD','On Hold'; COMPLETED='COMPLETED','Completed'; ARCHIVED='ARCHIVED','Archived'
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='projects'); name=models.CharField(max_length=120); description=models.TextField(blank=True); client=models.CharField(max_length=120,blank=True); status=models.CharField(max_length=12,choices=Status.choices,default=Status.PLANNING); budget=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,validators=[MinValueValidator(0)]); members=models.ManyToManyField(User,blank=True,related_name='projects'); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: constraints=[models.UniqueConstraint(fields=['company','name'],name='unique_company_project')]
class Task(models.Model):
    class Status(models.TextChoices): TODO='TODO','Todo'; IN_PROGRESS='IN_PROGRESS','In Progress'; COMPLETED='COMPLETED','Completed'; ON_HOLD='ON_HOLD','On Hold'
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks'); assignee=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='tasks'); title=models.CharField(max_length=180); status=models.CharField(max_length=12,choices=Status.choices,default=Status.TODO); created_at=models.DateTimeField(auto_now_add=True)
class AuditLog(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='audit_logs'); actor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True); action=models.CharField(max_length=80); resource=models.CharField(max_length=120); ip=models.GenericIPAddressField(null=True,blank=True); created_at=models.DateTimeField(auto_now_add=True)
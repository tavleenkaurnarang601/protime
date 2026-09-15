from django.core.management.base import BaseCommand
from tracker.models import Company,Project,Role,Task,User
class Command(BaseCommand):
    help='Creates development-only PRO TIME TRACKER sample data.'
    def handle(self,*args,**kwargs):
        company,_=Company.objects.get_or_create(name='Acme Digital',defaults={'timezone':'Asia/Kolkata'})
        accounts=[('admin@protime.local','Aarav','Admin',Role.ADMIN),('manager@protime.local','Meera','Manager',Role.MANAGER),('employee@protime.local','Riya','Employee',Role.EMPLOYEE)]
        users=[]
        for email,first,last,role in accounts:
            user,created=User.objects.get_or_create(email=email,defaults={'username':email,'first_name':first,'last_name':last,'company':company,'role':role})
            if created: user.set_password('DemoPass123!'); user.save()
            users.append(user)
        project,_=Project.objects.get_or_create(company=company,name='E-Commerce Platform',defaults={'client':'Northstar Retail','description':'Customer storefront refresh','status':'ACTIVE','budget':500000})
        project.members.add(*users); Task.objects.get_or_create(project=project,title='Implement Authentication',defaults={'assignee':users[2],'status':'IN_PROGRESS'})
        self.stdout.write(self.style.SUCCESS('Development demo data ready.'))
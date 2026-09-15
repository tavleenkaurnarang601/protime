from django.test import TestCase
from .models import Company,Role,User
class AccessTests(TestCase):
    def setUp(self):
        self.company=Company.objects.create(name='Test Co'); self.user=User.objects.create_user(username='employee@test.local',email='employee@test.local',password='SafePassword123!',company=self.company,role=Role.EMPLOYEE)
    def test_dashboard_requires_login(self): self.assertRedirects(self.client.get('/'), '/login/?next=/')
    def test_employee_can_open_dashboard(self): self.client.force_login(self.user); response=self.client.get('/'); self.assertContains(response,"Today")
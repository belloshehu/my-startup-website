from django.test import TestCase, Client
from .models import Tutors

# Create your tests here.
class TutorsTests(TestCase):
    def setUp(self):
        self.client =Client()
        Tutors.objects.create(about='pythonista and django developer', phone_number='20129232292')
        #t2 = Tutors(about='Arduino purist', phone_number='33666666666' )
        
        
    def test_totors_model(self):
        t =Tutors.Objects.get(phone_number='33666666666')
        self.assertEqual(t.about,'Arduino purist')
        

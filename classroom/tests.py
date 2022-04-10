from django.test import TestCase
from .models import *

# Create your tests here.
class TestStudentModel(TestCase):
    
    def test_add_a_plus_b(self):
        a = 2
        b = 3
        
        c = a + b
        
        self.assertEqual(c, 5)
    
    def test_student_can_be_created(self):
        student_1 = Student.objects.create(
            first_name="Mehedi",
            last_name="Hasan",
            admission_number=101)
        
        student_result = Student.objects.last()  #getting the last student
        
        self.assertEqual(student_result.first_name, "Mehedi")
        
    def test_str_return(self):
        student_1 = Student.objects.create(
            first_name="Mehedi",
            last_name="Hasan",
            admission_number=101)
        
        student_result = Student.objects.last()  #getting the last student
        
        self.assertEqual(str(student_result), "Mehedi")
        
    def test_fail(self):
        student_1 = Student.objects.create(
            first_name="Mehedi",
            last_name="Hasan",
            admission_number=101,
            average_score= 35)
        
        student_result = Student.objects.last()  #getting the last student
        
        self.assertEqual(student_result.get_grade(), "Fail")
        
    def test_pass(self):
        student_1 = Student.objects.create(
            first_name="Mehedi",
            last_name="Hasan",
            admission_number=101,
            average_score= 60)
        
        student_result = Student.objects.last()  #getting the last student
        
        self.assertEqual(student_result.get_grade(), "Pass")
        
    def test_excillent(self):
        student_1 = Student.objects.create(
            first_name="Mehedi",
            last_name="Hasan",
            admission_number=101,
            average_score= 80)
        
        student_result = Student.objects.last()  #getting the last student
        
        self.assertEqual(student_result.get_grade(), "Excellent")
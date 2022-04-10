from django.test import TestCase

# Create your tests here.
class TestStudentModel(TestCase):
    def test_add_a_plus_b(self):
        a = 2
        b = 3
        
        c = a + b
        
        self.assertEqual(c, 5)
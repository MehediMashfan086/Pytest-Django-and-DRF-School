from rest_framework.generics import ListAPIView
from .serializers import *
from classroom.models import *

class ListAPIViewAPIView(ListAPIView):
    serializer_class = SrudentSerializer
    
    model = Student
    queryset = Student.objects.all()
    
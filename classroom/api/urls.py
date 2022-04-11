from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListAPIViewAPIView.as_view(), name='student_list_api'),
]

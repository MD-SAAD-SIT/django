from django.urls import path
from .views import home, submit_feedback

urlpatterns = [
    path('', home),
    path('submit/', submit_feedback),
]

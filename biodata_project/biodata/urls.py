from django.urls import path
from .views import form_view, display_view

urlpatterns = [
    path('', form_view),
    path('display/', display_view),
]

from django.urls import path
from .views import calculator, contact_form

urlpatterns = [
    path('',calculator),
    path('form/',contact_form),
]

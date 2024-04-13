from django.urls import path
from . import views

urlpatterns = [
    path('cv-info/', views.display_cv_info, name='cv_info'),]
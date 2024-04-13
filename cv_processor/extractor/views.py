from django.conf import settings
from .utils import process_cv_directory
from django.shortcuts import render
from django.shortcuts import render

cv_directory = "cv_processor\cv_files"
def display_cv_info(request): 
    cv_info = process_cv_directory(cv_directory)
    return render(request, 'cv_info.html', {'cv_info': cv_info})


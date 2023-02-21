from text_summary import views
from django.urls import path
from .views import *


urlpatterns = [
    path('' , GetSummary.as_view()),  
]
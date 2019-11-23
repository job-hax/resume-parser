from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from RP_RestAPI import views

urlpatterns = [
    path('', views.resume_parser),
]
urlpatterns = format_suffix_patterns(urlpatterns)

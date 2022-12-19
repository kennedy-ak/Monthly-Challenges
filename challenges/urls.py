#   List all the urls we support
from django.urls import path

from . import views

urlpatterns = [

#dynamic url pattern
path("", views.index, name='index'),
path("<int:month>", views.by_number),
path("<str:month>", views.monthly_challenge, name="task-month"),

]

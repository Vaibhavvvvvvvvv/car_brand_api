from django.urls import path
from .views import listcar,rld

urlpatterns = [

  path('vaibhav/',listcar.as_view()),
  path('api/<pk>',rld.as_view()),

]
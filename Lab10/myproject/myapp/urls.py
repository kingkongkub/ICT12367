from django.urls import path
from . import views

urlpatterns = [

path('',views.index),

path('form/',views.form),

path('edit/<int:id>/',views.edit),

path('delete/<int:id>/',views.delete),

]
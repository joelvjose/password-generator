from django.urls import  path
from . import views


urlpatterns = [
    path('',views.home,name='passsword_generate'),
    
]

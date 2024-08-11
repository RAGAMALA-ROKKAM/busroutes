from django.urls import path
from buses import views

urlpatterns=[
    path('routes',views.businfo,name='br'),
]
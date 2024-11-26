from django.urls import path
from . import views

urlpatterns=[
    path('create',views.create_patient,name='create_patient'),
    path('get',views.get_all_patient,name="get_all_patient"),
    path('get_patient/<int:id>',views.get_patient,name="get_patient"),
]
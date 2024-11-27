from django.urls import path
from . import views

urlpatterns=[
    path('create',views.create_patient,name='create_patient'),
    path('get',views.get_all_patient,name="get_all_patient"),
    path('get_patient/<int:id>',views.get_patient,name="get_patient"),
    path('edit_patient/<int:patient_id>',views.edit_patient,name="edit_patient"),
    path('delete_patient/<int:patient_id>',views.delete_patient,name="delete_patient"),
]
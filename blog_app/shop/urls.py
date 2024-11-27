
from django.urls import path, include
from . import views

urlpatterns = [
    path('category/create', views.create_category, name="create_category"),
    path('category/get_all_category', views.get_all_category, name="get_all_category"),
    path('category/delete/<int:category_id>', views.delete_category, name="delete_category"),
    path('category/edit/<int:category_id>',views.edit_category,name="edit_category"),
]
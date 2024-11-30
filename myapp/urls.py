from django.urls import path
from . import views

# urlpatterns = [
#     path('hello', views.hello_world),  # Map `/hello` to hello_world view
#     path('how', views.how),
#     path('user/create/', views.create_user, name='add_user'),
#     path('user/<int:user_id>/', views.getUser, name='get_user'),
#     path('user/add/<int:user_id>/', views.get_user, name='add_user'), 
#     path('user/list/', views.get_all_users, name='get_all_users'),
#     path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
#     path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
# ]

urlpatterns = [
    path('hello', views.hello_world),  # Simple hello world view
    path('how', views.how),  # Another sample view
    path('user/create/', views.create_user, name='create_user'),  # Create a new product
    path('user/<int:user_id>/', views.get_user, name='get_user'),  # View details of a single product
    path('user/list/', views.get_all_users, name='get_all_users'),  # List all products
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit a product
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login_user"),
    path("logout/",views.logout_user,name="logout_user"),
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]

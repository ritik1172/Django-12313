from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_form, name="contact_form"),
    path('submit_form/', views.submit_form, name="submit_form"),
    path('details/', views.details, name="details"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
    path('update/<int:id>/', views.update_student, name="update_student"),
    
]

# https://github.com/ritik1172/Django-12313/tree/main/my_model2
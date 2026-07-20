from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_form, name="contact_form"),
    path('submit_form/', views.submit_form, name="submit_form"),
    path('details/', views.details, name="details"),
]

# https://github.com/ritik1172/Django-12313/tree/main/my_model2
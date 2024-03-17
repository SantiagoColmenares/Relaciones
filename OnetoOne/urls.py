from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name="create"),
    path('read/<int:id>/', views.read_place, name="read"),
    path('update/<int:id>/<str:name>/', views.update_place, name="update"),
    path('delete/<int:id>/', views.delete_place, name="delete")
]

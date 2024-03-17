from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name="create"),
    path('read/<int:id>/', views.read_article, name="read"),
    path('update/<int:id>/<str:fname>/', views.update_reporter, name="update"),
    path('delete/<int:id>/', views.delete_article, name="delete")
]

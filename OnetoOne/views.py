from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, Place
# Create your views here.

def create(request):
  # p1 = Place(name="Demon Dogs", address="944 W. Fullerton")
  # p1.save()

  # r1 = Restaurant(place = p1, employees = 25)
  # r1.save()

  restaurante = Restaurant.objects.get(place_id = 4)
  return HttpResponse(print(restaurante.place.address))

def read_place(request, id):
  pla = Place.objects.get(id = id)
  return HttpResponse(f"Name: {pla.name} ---- Address: {pla.address}")


def update_place(request, id, name):
  pla = Place.objects.get(id = id)
  pla.name = name
  pla.save()
  return HttpResponse("Se actualizaron los datos")


def delete_place(request, id):
  pla = Place.objects.get(id = id)
  pla.delete()
  return HttpResponse("Se elimino")
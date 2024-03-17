from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

# Create your views here.

def create(request):
  p1 = Publication(title="HTML")
  p1.save()

  p2 = Publication(title="JS")
  p2.save()

  p3 = Publication(title="CSS")
  p3.save()

  a1 = Article(headline="Django lets you build web apps easily")
  a1.save()

  a2 = Article(headline="NASA uses Python")
  a2.save()

  a2.publications.add(p1, p2)
  a2.publications.add(p3)

  a1.publications.add(p1)

  a1.publications.remove(5)


  return HttpResponse()

def read_article(request, id):
  art = Article.objects.get(id = id)
  return HttpResponse(f"Id: {art.id} ---- Headline: {art.headline}")

def update_publication(request, id, titulo):
  publi = Publication.objects.get(id = id)
  publi.title = titulo
  publi.save()
  return HttpResponse("Se actualizaron los datos")


def delete_publication(request, id):
  pub = Publication.objects.get(id = id)
  pub.delete()
  return HttpResponse("Se elimino")

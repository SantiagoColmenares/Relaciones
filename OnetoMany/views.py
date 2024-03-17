from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Reporter
from datetime import date
#Create your views here.

def create(request):
  r = Reporter(first_name="Santiago", last_name="Colmenares", email="example@example.com")
  r.save()
  a = Article(id=None, headline="Javascript", pub_date=date(2005, 7, 27), reporter=r)
  a2 = Article(id=None, headline="CSS", pub_date=date(2005, 7, 27), reporter=r)
  a3 = Article(id=None, headline="Php", pub_date=date(2005, 7, 27), reporter=r)
  a.save()
  a2.save()
  a3.save()

  reporter = Reporter.objects.get(id = 15)
  query = reporter.article_set.all()
  return render(request, 'index.html', {
    'repo':reporter,
    'query':query
  })



def read_article(request, id):
  art = Article.objects.get(id = id)
  return HttpResponse(f"Id: {art.id} ---- Headline: {art.headline}")


def update_reporter(request, id, fname):
  publi = Reporter.objects.get(id = id)
  publi.first_name = fname
  publi.save()
  return HttpResponse("Se actualizaron los datos")


def delete_article(request, id):
  pub = Article.objects.get(id = id)
  pub.delete()
  return HttpResponse("Se elimino")

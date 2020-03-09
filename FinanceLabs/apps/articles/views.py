from django.http import Http404, HttpResponseRedirect, HttpResponse
import csv
from django.shortcuts import render
from .models import Article, Indicator
from django.urls import reverse
from django.utils import timezone

def index (request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]

    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Стаття не знайдена')
    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

def update_rate(request,article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Стаття не знайдена')
    new_rate = request.POST['new_rate']
    a.calculate_rate(new_rate)
    a.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)) )

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Стаття не знайдена')

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    
    return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)) )

def new_article(request):

    return render(request, 'articles/new_article.html')

def create_article(request):
    a = Article(article_title = request.POST['new_title'], article_text = request.POST['new_text'])
    a.save()
    return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)) )

def show_indicators(request):
    indicators_list = Indicator.objects.all()
    return render(request, 'articles/indicators.html', {'indicators_list': indicators_list} )

def add_indicators(request):
    kv = float( request.POST['kvartal'] )
    y = request.POST['year'] 
    e = float( request.POST['e'] )
    c = float( request.POST['c'] )
    v = float( request.POST['v'] )

    i = Indicator(kvartal = kv, year = y, E = e, C = c, V = v)
    i.save()
    return HttpResponseRedirect( reverse('articles:show_indicators') )

def download_indocators(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="indicators.csv"'
    #writer = csv.writer(response)
    
    fieldnames = ['Year','Kvartal','Value']
    writer =csv.DictWriter(response, dialect=csv.Dialect.escapechar, quotechar='\r', quoting=csv.QUOTE_NONE, fieldnames = fieldnames)
    writer.writeheader()

    data = Indicator.objects.filter()
    for item in data:
        y = item.year
        kv = item.kvartal
        v = item.value
        writer.writerow({'Year': y, 'Kvartal': kv, 'Value': v})
    
    #for row in data:
    #    rowobj = (row.year, row.kvartal, row.value)
    #    writer.writerow(rowobj)
    return response 
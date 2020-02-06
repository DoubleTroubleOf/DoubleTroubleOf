from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
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
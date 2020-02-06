from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('<int:article_id>/update_rate', views.update_rate, name='update_rate'),
    path('new_article', views.new_article, name='new_article'),
    path('create_article', views.create_article, name='create_article'),

    

    
]
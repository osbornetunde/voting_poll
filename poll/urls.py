from django.conf.urls import url

from . import views
app_name = 'poll'

urlpatterns = [

    # ex: /poll/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # ex: /poll/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    #ex: /poll/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    
    #ex: /poll/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
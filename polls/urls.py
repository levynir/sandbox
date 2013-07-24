#urls.py
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(template_name="polls/detail.mustache"), name='detail'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(template_name="polls/results.html"), name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
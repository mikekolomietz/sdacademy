
from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    url(r'^results/', views.results, name='results'),
)
#/quadratic/results/?a=1&b=3&c=5

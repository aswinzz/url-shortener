from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/all',views.AllUrls.as_view(),name="All_URLS"),
    url(r'^api/shorten',views.URLShortner.as_view(),name="URLShortner"),
    url(r'^api/(?P<pk>\w+)', views.GetURL.as_view(), name='GetURL'),
    url(r'^(?P<pk>\w+)', views.RedirectURL, name='RedirectURL'),  
    url(r'^',views.home,{"shorturl":None},name="home"), 
]

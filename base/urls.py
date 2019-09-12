from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^all',views.AllUrls.as_view(),name="All_URLS")
]

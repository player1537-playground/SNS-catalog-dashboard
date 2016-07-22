from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    url(r'^$', cache_page(60*15)(views.IndexView.as_view())),
]

from django.conf.urls import url
# from . import views
from accounts.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^$', views.home),
]
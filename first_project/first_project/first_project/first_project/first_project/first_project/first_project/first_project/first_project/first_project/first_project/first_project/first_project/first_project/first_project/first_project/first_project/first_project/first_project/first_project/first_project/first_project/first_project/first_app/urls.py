from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns = [
    url(r'^index1',views.index1),
    # url(r'^$',views.cnames.as_view(), name='index1'),
    # path('articles/2003/', views.cnames),
]

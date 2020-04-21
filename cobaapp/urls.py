from django.conf.urls import url
from cobaapp import views

# TEMPLATE TAGGING
app_name = 'cobaapp'

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^dua/$',views.dua,name='dua'),
]

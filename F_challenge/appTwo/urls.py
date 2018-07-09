from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'
urlpatterns = [
    url(r'^signup/',views.users,name='register'),
    url(r'^$',views.index,name='User Home'),


]

from django.conf.urls import url
from f_app import views


urlpatterns = [
    url(r'^ext/',views.extent_help,name='exthelp'),
    url(r'^$',views.help,name='help'),


]

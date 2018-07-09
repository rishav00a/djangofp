from django.conf.urls import url

from userModels import views

app_name='userModels'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/',views.register,name="register"),
    url(r'^logout/',views.user_logout,name="logout"),
    url(r'^login/',views.user_login,name="login"),
]

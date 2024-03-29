"""confrence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views,auth

urlpatterns = [
    url(r'^admin/logout/$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^login/',auth.login,name='login'),
    url(r'^logout/',auth.logout,name='logout'),
    url(r'^register/',auth.register,name='register'),

    url(r'^sessions/$',views.SessionList.as_view(),name='sessions_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$',views.SessionDetail.as_view() , name='sessions_details'),

    url(r'^sessions/create/$',views.sessioncreate.as_view(), name='sessions_create'),
    url(r'^sessions/update/(?P<pk>[0-9]+)/$',views.SessionUpdate , name='sessions_update'),
    url(r'^sessions/delete/(?P<pk>[0-9]+)/$',views.SessionDelete.as_view() , name='sessions_delete'),





    #url(r'^submit/',views.submit_session,name='submit_session'),
]

"""singosgu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

path(r'', views.APIViewSet.as_view({"get": "list", "post": "create"}), name="driver"),
path(r'file/', views.FileDownloadView.as_view({"get": "list"}), name="driverfiledownload"),
re_path(r'^(?P<pk>\d+)/$', views.APIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}), name="driver_1"),
path(r'dispatchlist/', views.DispatchListViewSet.as_view({"get": "list"}), name="dispatchlist"),
re_path(r'^dispatchlist/(?P<pk>\d+)/$', views.DispatchListViewSet.as_view({
    'get': 'retrieve',
}), name="dispatchlist_1")
]

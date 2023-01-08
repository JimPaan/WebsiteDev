from django.urls import path, reverse_lazy
from . import views
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<str:pk>', views.display, name='display'),
    path('login', views.login, name='login'),
    path('lilist', views.lilist, name='lilist'),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
]

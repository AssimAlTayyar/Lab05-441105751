from django.contrib import admin
from django.urls import path
from myapp.views import add_person, default_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_person, name='add'),
    path('', default_view, name='default'),
]
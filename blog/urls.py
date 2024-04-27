from django.urls import path
from .views import home_view, about_view, blog_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
]

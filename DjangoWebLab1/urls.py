"""
Definition of urls for DjangoWebLab1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('first_spek/', views.first_spek, name='first_spek'),
    path('second_spek/', views.second_spek, name='second_spek'),
    path('third_spek/', views.third_spek, name='third_spek'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Выполнить вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns() 

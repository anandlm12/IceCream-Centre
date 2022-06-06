from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings


admin.site.site_header = "Mickey Ice Creams Admin"
admin.site.site_title = "Mickey Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Mickey Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
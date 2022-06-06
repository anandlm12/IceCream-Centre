from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


admin.site.site_header = "Mickey Ice Creams Admin"
admin.site.site_title = "Mickey Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Mickey Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
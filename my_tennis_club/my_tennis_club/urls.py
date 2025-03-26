from django.contrib import admin
from django.urls import include, path
from members import views

urlpatterns = [
    path('', views.home, name='home'),   # Define Home em "/"
    path('', include('members.urls')),
    path('', include('authentication.urls')),
    path('', include('materiais.urls')),
    #path('', include('plan.urls')),
    path('admin/', admin.site.urls),
]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
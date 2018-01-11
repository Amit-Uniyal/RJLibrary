"""RJProj URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('', RedirectView.as_view(url='/library/'))
]

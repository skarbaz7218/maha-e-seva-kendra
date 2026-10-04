
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path("maha-panel-2026/", admin.site.urls),
    path("", include("services.urls")),
    
]
 # Error handlers
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'
 
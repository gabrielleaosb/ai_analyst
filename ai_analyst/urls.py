from django.contrib import admin
from django.urls import path, include
from analysis.views import dashboard_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),  
    path('admin/', admin.site.urls),
    path('api/', include('analysis.urls')),
]

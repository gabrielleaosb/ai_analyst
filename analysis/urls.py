from django.urls import path
from .views import AnalyzeFileView, dashboard_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('analyze/', AnalyzeFileView.as_view(), name='analyze-file'),
]
from django.urls import path
from application.theme.views import ThemeListView, ThemeDetailView

urlpatterns = [
    path('theme-list/', ThemeListView.as_view()),
    path('theme-list/<int:pk>/', ThemeDetailView.as_view()),
]

from django.urls import path

from application.category.views import CategoryListView

urlpatterns = [
    path('list/', CategoryListView.as_view()),
]

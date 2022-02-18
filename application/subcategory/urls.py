from django.urls import path
from application.subcategory.views import SubcatListView, SubcatDetailView

urlpatterns = [
    path('subcat-list/', SubcatListView.as_view()),
    path('subcat-list/<int:pk>/', SubcatDetailView.as_view()),
]

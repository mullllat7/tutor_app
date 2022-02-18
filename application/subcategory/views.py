from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from application.subcategory.models import Subcategory
from application.subcategory.serializers import SubcatSerializers, SubcatDetailSerializer


class SubcatListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcatSerializers
    pagination_class = PageNumberPagination

    def get_serializer_context(self):
        return {'request': self.request}


class SubcatDetailView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcatDetailSerializer

from django.http import Http404

from .serializers import ArticleSerializer
from .models import Article

from rest_framework import filters
from rest_framework import viewsets



class ArticleViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'created', )


from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from articles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('article', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

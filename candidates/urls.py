from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, name_search

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('name_search/<str:query>/', name_search),
]

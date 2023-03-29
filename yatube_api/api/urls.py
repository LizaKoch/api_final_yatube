from django.urls import include, path
from rest_framework import routers
from api.views import CommentViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

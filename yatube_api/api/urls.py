from django.urls import include, path
from rest_framework import routers

from api.views import APIFollowList, CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('follow/', APIFollowList.as_view()),
]

from django.urls import include, path
from rest_framework import routers

from api.views import APIFollowList, CommentViewSet, GroupViewSet, PostViewSet, ProfileList, Test500Error

router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/follow/', APIFollowList.as_view()),
    path('v1/profile/<username>/', ProfileList.as_view()),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/500', Test500Error.as_view()),  # for status_code_500
]

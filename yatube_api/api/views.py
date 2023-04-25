from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from rest_framework import filters, generics, permissions, viewsets

from api.permissions import AuthorHasChangePermission
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post


class APIFollowList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        AuthorHasChangePermission,
    )
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorHasChangePermission,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self._post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self._post)

    @cached_property
    def _post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorHasChangePermission,
    )
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProfileList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorHasChangePermission,
    )

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(author__username=username)


class Test500Error(generics.ListAPIView):
    """For status code 500."""
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        AuthorHasChangePermission,
    )

    def get_queryset(self):
        username = self.qweqwe['username']
        return Post.objects.filter(author__username=username)

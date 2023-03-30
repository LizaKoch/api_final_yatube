from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets

from api.permissions import AuthorHasChangePermission, ReadOnly
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

    def get_post(self, pk: int):
        return get_object_or_404(Post, pk=pk)

    def get_queryset(self):
        return self.get_post(pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        post = self.get_post(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (ReadOnly,)
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

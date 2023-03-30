from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.permissions import AuthorHasChangePermission
from posts.models import Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    AuthorHasChangePermission = [IsAuthenticated, AuthorHasChangePermission]
    serializer_class = CommentSerializer

    def get_post(self, pk: int):
        return get_object_or_404(Post, pk=pk)

    def get_queryset(self):
        return self.get_post(pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        post = self.get_post(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AuthorHasChangePermission)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


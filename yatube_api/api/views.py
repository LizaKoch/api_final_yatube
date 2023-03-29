from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializers import CommentSerializer, PostSerializer
from posts.models import Post


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post(self, pk: int):
        return get_object_or_404(Post, pk=pk)

    def get_queryset(self):
        return self.get_post(pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        post = self.get_post(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

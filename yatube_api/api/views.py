from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly, IsAuthorizable
from .serializers import CommentsSerializer, GroupsSerializer, PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """ViewSet для постов"""
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsOwnerOrReadOnly & IsAuthorizable]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для групп"""
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев к постам"""
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadOnly & IsAuthorizable]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

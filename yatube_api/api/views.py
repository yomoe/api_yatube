from posts.models import Group, Post
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentsSerializer, GroupsSerializer, PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsOwnerOrReadOnly]


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadOnly]

from django.contrib.auth.models import User

from rest_framework import viewsets

from example.models import Post, Comment
from example.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of posts instances made by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the posts in the system.

    As you can see, the collection of comment instances belonging to a post are
    serialized using a hyperlinked representation.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the comments in the system.

    As you can see, these are just plain fields using id's.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

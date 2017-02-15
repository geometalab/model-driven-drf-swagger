from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.utils import timezone

from rest_framework import viewsets

from example.models import Post, Comment
from example.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    list:
    List all the users. As you can see, the users posts are hyperlinked.

    retrieve:
    Retrieve a single user. As you can see, the the user's posts are hyperlinked.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the posts in the system.

    list: List all the posts.

    retrieve: Fetch a single post entry.

    create: Create a new blog post.

    Slug is a unique identifier...
    Username and the time the post has been created are automatically
    added.

    update: Update the entire post.

    Details for updating...

    partial_update: Partially update the post.

    destroy: Delete a blog post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        now = timezone.now()
        serializer.save(posted_by=self.request.user, posted_on=now)


class CommentViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the comments in the system.

    list: List all the comments.

    retrieve: Fetch a single comment entry.

    create: Create a new comment post.

    update: Update the entire comment.

    partial_update: Partially update the comment.

    destroy: Delete a comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        now = timezone.now()
        serializer.save(user=self.request.user, commented_on=now)


def overview(request):
    return render_to_response('home.html')

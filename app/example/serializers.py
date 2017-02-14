from django.contrib.auth.models import User
from rest_framework import serializers

from example.models import Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(), view_name='post-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'posts')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(queryset=Comment.objects.all(), view_name='comment-detail', many=True)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'posted_on', 'posted_by')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message', 'commented_on', 'post', 'user')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(queryset=Post.objects.all(), view_name='post-detail', many=True)

    class Meta:
        model = User
        fields = ('username', 'posts')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(view_name='comment-detail', many=True, read_only=True)
    posted_by = serializers.ReadOnlyField()
    posted_on = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'posted_on', 'posted_by', 'comments')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    commented_on = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ('message', 'commented_on', 'post', 'user')

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = (
            'author',
            'post'
        )


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'You can not subscribe to yourself'
            )
        return data

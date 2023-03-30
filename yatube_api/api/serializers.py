from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
        )
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
        model = Group
        read_only = (
            'title',
            'slug',
        )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        fields = (
            'user',
            'following',
        )
        model = Follow

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError()
        return attrs

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=(
                'user',
                'following',
            ),
        ),
    ]


class PostSerializer(serializers.ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date',
        )
        model = Post

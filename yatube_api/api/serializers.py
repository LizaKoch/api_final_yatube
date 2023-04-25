from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from drf_extra_fields.fields import Base64ImageField


from posts.models import Comment, Follow, Group, Post, User


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
        read_only = ('title', 'slug')


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

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError()
        return value

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
    author = SlugRelatedField(read_only=True, slug_field='username')
    image = Base64ImageField(required=False, allow_null=True)
    title = serializers.CharField(min_length=3)

    class Meta:
        fields = (
            'id',
            'title',
            'text',
            'author',
            'image',
            'group',
            'pub_date',
        )
        model = Post

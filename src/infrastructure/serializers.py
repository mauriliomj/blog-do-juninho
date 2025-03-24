from rest_framework import serializers
from src.infrastructure.models import UserModel
from src.infrastructure.models import PostModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
from django.contrib.auth.models import User, Group
from .models import Post, FeaturedImage, Tag, Category, Author
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedImage
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    image = FeaturedImageSerializer()
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
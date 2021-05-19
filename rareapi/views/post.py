"""View module for handling requests about events"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Post, RareUser

class PostViewSet(ViewSet):
    def list(self, request):
        """Handle GET requests to events resource
        Returns:
            Response -- JSON serialized list of events
        """
        # Get the current authenticated user
        rare_user = RareUser.objects.get(user=request.auth.user)
        posts = Post.objects.all()


        # Support filtering posts by game
        if rare_user is not None:
            posts = posts.filter(user=rare_user)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

class PostUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PostRareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = PostUserSerializer(many=False)

    class Meta:
        model = RareUser
        fields = ['user']

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    user = PostRareUserSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'user', 'category',
                  'title', 'publication_date', 'image_url', 'content', 'approved',
                  'tags', 'reactions')
        depth = 1
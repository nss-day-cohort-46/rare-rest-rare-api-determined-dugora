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
        posts = Post.objects.order_by('-publication_date')
        

        # Support filtering posts by user
        current_user = self.request.query_params.get('rareuser', None)
        if current_user is not None:
            posts = posts.filter(user=rare_user)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle DELETE requests for a single post
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id']

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

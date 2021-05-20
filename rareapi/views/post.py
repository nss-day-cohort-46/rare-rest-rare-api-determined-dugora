from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Post


class PostView(ViewSet):

    def list(self, request):
        """Handle GET requests to events resource
        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all().order_by("-publication_date")

        # Note the additional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    Arguments:
        serializer type
    """

    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date',
                  'image_url', 'content', 'approved', 'tags', 'reactions')
        depth = 1

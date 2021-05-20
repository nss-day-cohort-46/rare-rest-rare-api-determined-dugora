from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Post, Category, RareUser

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

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized post instance
        """

        # Uses the token passed in the `Authorization` header
        rareuser = RareUser.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["categoryId"])

        # Create a new Python instance of the Post class
        # and set its properties from what was sent in the
        # body of the request from the client.
        post = Post()
        post.user = rareuser
        post.category = category
        post.title = request.data["title"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.tags.set()
        # post.publication_date = currentdate

        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

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

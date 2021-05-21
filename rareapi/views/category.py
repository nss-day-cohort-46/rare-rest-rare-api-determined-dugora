"""View module for handling requests about categories"""
from rareapi.models.rareuser import RareUser
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareapi.models import Category, category, RareUser


class CategoryView(ViewSet):
    """Rare categories"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        user = RareUser.objects.get(user=request.auth.user)

        # Create a new Python instance of the Category class
        # and set its properties from what was sent in the
        # body of the request from the client.
        category = Category()
        category.label = request.data["label"]
       
        

        # Try to save the new game to the database, then
        # serialize the game instance as JSON, and send the
        # JSON as a response to the client request
        try:
            category.save()
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/categories/2
            #
            # The `2` at the end of the route becomes `pk`
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to categories resource

        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()

        # Support filtering categories
        category = self.request.query_params.get('categoryId', None)
        if category is not None:
            categories = categories.filter(category__id=category)    

        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single category
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            category = Category.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        # Serializer

class CategorySerializer(serializers.ModelSerializer):
        """JSON serializer for categories

        Arguments:serializer type """
        class Meta:
            model = Category
            fields = ('id', 'label')
            depth = 1    
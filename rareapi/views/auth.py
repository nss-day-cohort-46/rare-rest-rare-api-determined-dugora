import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rareapi.models import RareUser
from datetime import datetime


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['email'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email'],
        password=req_body['password']
    )

    # Now save the extra info in the levelupapi_gamer table
    rare_user = RareUser.objects.create(
        bio=req_body['bio'],
        profile_image_url=req_body['profile_image_url'],
        created_on=datetime.now(),
        user=new_user,
        active=True
    )

    # Commit the user to the database by saving it
    rare_user.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"valid": True, "token": token.key})
    return HttpResponse(data, content_type='application/json')
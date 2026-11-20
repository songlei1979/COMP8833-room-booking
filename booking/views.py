from django.contrib.auth import authenticate
from rest_framework.reverse import reverse

from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'Register': reverse('register', request=request),
        'Login': reverse('login', request=request),
        'Profile': reverse('profile', request=request),
        'Bookings': reverse('booking-list', request=request),
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:
        return Response(
            {"error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "message": "Login successful",
        "token": token.key,
        "username": user.username
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email
    })

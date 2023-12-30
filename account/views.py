from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer


# Create your views here.


class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = []  # Set authentication classes to an empty list
    permission_classes = []  # Set permission classes to an empty list

    # def create(self, request, *args, **kwargs):
    #     # Override the create method to customize the response if needed
    #     response = super().create(request, *args, **kwargs)
    #     # Add any additional logic here if needed
    #     return response
    #
    def create(self, request, *args, **kwargs):
        # Extract the password from the request data
        password = request.data.get('password', None)

        # Use the serializer to create the user without saving it yet
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Set the user's password and save the user
        if password:
            user.set_password(password)
            user.save()

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

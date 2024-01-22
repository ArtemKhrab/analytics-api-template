from ..services import UserService
from ..services import AuthService

from ..serializers.register_serializers import UserRegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from drf_yasg.utils import swagger_auto_schema


class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={
            HTTP_200_OK: TokenRefreshSerializer(),
            HTTP_400_BAD_REQUEST: "",
        },
    )
    def post(self, request):
        serializer_in = UserRegisterSerializer(data=request.data)
        serializer_in.is_valid(raise_exception=True)

        user_data = serializer_in.validated_data
        user = UserService.create_user(user_data=user_data)

        token_serializer = TokenRefreshSerializer(AuthService.create_token(user))

        return Response(data=token_serializer.data)

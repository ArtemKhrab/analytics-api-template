from ..services import LikeService
from ..services import PostService

from ..serializers.post_serializer import PostSerializer
from ..serializers.post_serializer import PostCreateSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND
)

from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema


class PostView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return []

    def get_authenticators(self):
        if self.request.method == "POST":
            return [JWTAuthentication()]
        return []

    @swagger_auto_schema(
        responses={
            HTTP_200_OK: PostSerializer(many=True),
            HTTP_401_UNAUTHORIZED: ""
        }
    )
    def get(self, request):
        posts = PostService.get_all_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=PostCreateSerializer,
        responses={
            HTTP_201_CREATED: "",
            HTTP_401_UNAUTHORIZED: ""
        }
    )
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        PostService.create_post(serializer.validated_data, user)
        return Response(status=HTTP_201_CREATED)


class LikePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            HTTP_204_NO_CONTENT: "",
            HTTP_401_UNAUTHORIZED: "",
            HTTP_404_NOT_FOUND: ""
        }
    )
    def put(self, request, **kwargs):
        post_id = kwargs.get("id")
        post = PostService.get_post_by_id(post_id=post_id)
        if not post:
            return Response(status=HTTP_404_NOT_FOUND)
        user = request.user
        LikeService.create_like(post=post, user=user)
        return Response(status=HTTP_204_NO_CONTENT)


class UnlikePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            HTTP_204_NO_CONTENT: "",
            HTTP_401_UNAUTHORIZED: ""
        }
    )
    def delete(self, request, **kwargs):
        post_id = kwargs.get("id")
        post = PostService.get_post_by_id(post_id)
        user = request.user
        LikeService.delete_like(post=post, user=user)
        return Response(status=HTTP_204_NO_CONTENT)

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from djoser.serializers import UserSerializer, User

from .serializers import PortfolioSerializer, ImageSerializer, CommentSerializer
from .models import Portfolio, Image, Comment
# Create your views here.


class DeleteOwnProfileView(DestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "username"

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username)


class PortfolioCreateView(CreateAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(profile=user)


class PortfolioListView(ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(profile=self.request.user)


class PortfolioUpdateView(UpdateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Portfolio.objects.filter(profile=user)


class PortfolioDeleteView(DestroyAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Portfolio.objects.filter(profile=user)


class ImageListView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'portfolio__name']


class ImageCreateView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageUpdateView(UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageDeleteView(DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageSearchView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageCreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(profile=user, image_id=self.kwargs.get('image_id'))

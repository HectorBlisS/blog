from rest_framework import generics
from ..models import Post
from .serializers import PostSerializer

class PostListView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


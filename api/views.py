from rest_framework.generics import ListAPIView,RetrieveAPIView,\
    ListCreateAPIView,RetrieveUpdateAPIView
from .models import AuthorModel,BookModel
from .serializer import BookListSerializer,BookListDetailsSerializer,\
    AutherListSerializer,AutherListDetailsSerializer
from rest_framework.filters import SearchFilter


# Create your views here.
class BookListAPIView(ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookListSerializer
    search_fields = ("title",)

class BookListDetailAPIView(RetrieveUpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookListDetailsSerializer

class AuthorListAPIView(ListAPIView):
    queryset =AuthorModel.objects.all()
    serializer_class = AutherListSerializer

class AuthorListDetailAPIView(RetrieveUpdateAPIView):
    queryset =AuthorModel.objects.all()
    serializer_class = AutherListDetailsSerializer


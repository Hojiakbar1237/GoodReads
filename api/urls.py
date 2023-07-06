from django.urls import path
from .views import BookListAPIView,BookListDetailAPIView,\
    AuthorListAPIView,AuthorListDetailAPIView



urlpatterns = [
    path("booklist/",BookListAPIView.as_view()),
    path("booklist/<int:pk>",BookListDetailAPIView.as_view()),
    path("authorlist/",AuthorListAPIView.as_view()),
    path("authorlist/<int:pk>",AuthorListDetailAPIView.as_view())

]
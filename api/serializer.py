from .models import AuthorModel,BookModel
from rest_framework import serializers


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = ["id","author","title","created_at"]

class BookListDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = ["id","author","title","description","created_at"]

class AutherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorModel
        fields = ["id","photo","full_name","created_at"]

class AutherListDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorModel
        fields = ["id","full_name","website","photo","about","created_at"]
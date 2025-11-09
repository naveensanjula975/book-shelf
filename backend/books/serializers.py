from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_year(self, v):
        if v < 1800 or v > 2100:
            raise serializers.ValidationError("Year must be between 1800 and 2100.")
        return v

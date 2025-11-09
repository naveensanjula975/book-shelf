from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=120)
    year = models.IntegerField()
    isbn = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.author})"

from django.db import models
from django.utils import timezone


CATEGORY = (
    ("WD", "Web Development"),
    ("DB", "Desktop Development"),
    ("ML", "Machine Learning"),
    ("MB", "Mobile Development"),
)
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    puplished_at = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    views_count = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY, max_length=20)


    def __str__(self):
        return self.title

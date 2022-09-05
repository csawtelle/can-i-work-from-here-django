from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class FeaturedImage(models.Model):
    title = models.CharField(max_length=100)
    alt = models.TextField()
    caption = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
         return self.title

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
         return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
         return self.tag
         
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    display_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    image = models.ForeignKey(FeaturedImage, on_delete=models.PROTECT)
    website = models.CharField(max_length=100)

    def __str__(self):
         return self.display_name
         
class Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    body = models.TextField()
    excerpt = models.TextField()
    published = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(null=True)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    image = models.ForeignKey(FeaturedImage, on_delete=models.PROTECT)
    slug = models.TextField(unique=True, blank=False, null=False, default=uuid.uuid4())

    def __str__(self):
         return self.title
         
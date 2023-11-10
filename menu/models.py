from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/category/')
    status = models.BooleanField(null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='img/product', default='blog/product.jpg')
    name = models.CharField(max_length=100)
    content = models.TextField()
    Price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='pcategory')
    status = models.BooleanField(null=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.name

    def snippets(self):
        return self.content[:200] + '...'

    def likes_count(self):
        return self.pvotes.count()

    def user_can_like(self, user):
        user_like = user.uvotes.filter(post=self)
        if user_like.exists():
            return True
        return False

    # def get_absolute_url(self):
    #     return reverse('menu:product', kwargs={'product_id':self.id})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uvotes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pvotes')

    def __str__(self):
        return f'{self.user} liked {self.product}'
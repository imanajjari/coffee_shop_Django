from django.contrib import admin
from .models import  Category, Product, Comment, Vote
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Vote)
admin.site.register(Comment)
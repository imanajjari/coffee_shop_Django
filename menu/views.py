from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Product, Vote
# Create your views here.

class CategoryView(View):
    def get(self, request):
        category = Category.objects.filter(status=True)
        product = Product.objects.filter(status=True)
        content = {'category': category, 'product': product}
        return render(request, 'MenuCategory.Html', content)

class ListProductView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(status=True, category=kwargs['cat_id'])
        content = {'products': product}
        return render(request, 'pages/cofee-page.html', content)

class ProductLikeView (LoginRequiredMixin, View):
    def get(self, request, post_id):
        product = Product.objects.get(id=post_id)
        category = Category.objects.get(name=product.category)
        like = Vote.objects.filter(user=request.user, product=product)
        if like.exists():
            like.delete()
        else:
            Vote.objects.create(user=request.user, product=product)
        return redirect('menu:list_product', category.id)

class ProductDetailView (View):
    def get(self, request, post_id):
        product = Product.objects.get(id=post_id)
        category = Category.objects.get(name=product.category)
        content = {'category': category, 'product': product}
        return render(request, 'pages/product-details.html', content)

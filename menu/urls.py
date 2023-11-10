from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.CategoryView.as_view(), name='index'),
    path('category/<int:cat_id>', views.ListProductView.as_view(), name='list_product'),
    path('product/vote/<int:post_id>', views.ProductLikeView.as_view(), name='product_like'),
    path('product/details/<int:post_id>', views.ProductDetailView.as_view(), name='product_details'),

]
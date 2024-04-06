from django.urls import path

from .views import home_view, ContactBasedView, about, account, card, electronics, fashion_child, fashion_saree, footwear, gift, \
    product_detail_child1, product_details_child2, product_details_gift, product_details_saree, product_details_shoes, \
    product_details_sound, product_details_speaker, product_details_toy
app_name = 'shop'
urlpatterns = [
    path('', home_view, name="home_page"),
    # path('home/', index, name='home-page'),
    path('contact/', ContactBasedView.as_view(), name='contact-page'),
    path('about/', about, name='about-page'),
    path('acount/', account, name='account-page'),
    path('card/', card, name='card-page'),
    path('electronics-product/', electronics, name='electronics'),
    path('fashion-child-product/', fashion_child, name='fashion-child'),
    path('fashion-saree-product/', fashion_saree, name='fashion-saree'),
    path('footwear-product/', footwear, name='footwear'),
    path('gift-product/', gift, name='gift'),
    path('product-detial-child1/', product_detail_child1, name='product-child1'),
    path('product-detials-child2/', product_details_child2, name='product-child2'),
    path('product-detial-gift/', product_details_gift, name='product-gift'),
    path('product-detial-saree/', product_details_saree, name='product-saree'),
    path('product-detial-shoes/', product_details_shoes, name='product-shoes'),
    path('product-detial-sound/', product_details_sound, name='product-sound'),
    path('product-detial-speaker/', product_details_speaker, name='product-sound'),
    path('product-detial-toy/', product_details_toy, name='product-toy'),
]

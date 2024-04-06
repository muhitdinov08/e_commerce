from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.models import About, Contact


# Create your views here.

def home_view(request):
    return render(request, 'seeyashop/index.html')


def about(request):
    abouts = About.objects.all()
    return render(request, 'seeyashop/about.html', {'abouts': abouts})


class ContactBasedView(CreateView):
    model = Contact
    context_object_name = 'contacts'
    fields = ['name', 'phone', 'subject', 'reason']
    template_name = "seeyashop/contact.html"
    success_url = reverse_lazy("shop:home_page")


def card(request):
    return render(request, 'seeyashop/card.html')


def account(request):
    return render(request, 'seeyashop/account.html')


def electronics(request):
    return render(request, 'seeyashop/electronics-product.html')


def fashion_child(request):
    return render(request, 'seeyashop/fashion-child-product.html')


def fashion_saree(request):
    return render(request, 'seeyashop/fashion-saree-product.html')


def footwear(request):
    return render(request, 'seeyashop/footwear-product.html')


def gift(request):
    return render(request, 'seeyashop/gift-product.html')


def product_detail_child1(request):
    return render(request, 'seeyashop/product-detial-child1.html')


def product_details_child2(request):
    return render(request, 'seeyashop/product-detials-child2.html')


def product_details_gift(request):
    return render(request, 'seeyashop/product-detials-gift.html')


def product_details_saree(request):
    return render(request, 'seeyashop/product-detials-saree.html')


def product_details_shoes(request):
    return render(request, 'seeyashop/product-detials-shoes.html')


def product_details_sound(request):
    return render(request, 'seeyashop/product-detials-sound.html')


def product_details_speaker(request):
    return render(request, 'seeyashop/product-detials-speaker.html')


def product_details_toy(request):
    return render(request, 'seeyashop/product-detials-toy.html')

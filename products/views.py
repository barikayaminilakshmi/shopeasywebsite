from django.shortcuts import render
from .models import Product
from cart.models import Cart, CartItem



def product_list(request):

    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(
            product_name__icontains=search
        )
    else:
        products = Product.objects.all()

    cart_count = 0


    if request.user.is_authenticated:

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        cart_count = CartItem.objects.filter(
            cart=cart
        ).count()


    return render(
        request,
        "product_list.html",
        {
            "products": products,
            "cart_count":cart_count
        }
    )



def category_products(request, category_name):

    products = Product.objects.filter(
        category__category_name=category_name
    )

    return render(
        request,
        "product_list.html",
        {
            "products": products
        }
    )
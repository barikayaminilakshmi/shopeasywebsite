from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


@login_required
def add_wishlist(request, product_id):

    product = Product.objects.get(id=product_id)

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("products")


@login_required
def wishlist_view(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        "wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )


@login_required
def remove_wishlist(request, id):

    Wishlist.objects.filter(
        id=id,
        user=request.user
    ).delete()

    return redirect("wishlist")
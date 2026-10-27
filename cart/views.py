from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from orders.models import Order, OrderItem


@login_required
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("products")


@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    total = 0

    for item in cart_items:
        total += item.total_price()

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )


@login_required
def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect("cart")


@login_required
def decrease_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


@login_required
def remove_item(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect("cart")


@login_required
def checkout(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    total = 0

    for item in cart_items:
        total += item.total_price()

    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )


@login_required
def place_order(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    total = 0

    for item in cart_items:
        total += item.total_price()

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect("order_success")
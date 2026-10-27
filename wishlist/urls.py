from django.urls import path
from . import views


urlpatterns = [

    path(
        "add/<int:product_id>/",
        views.add_wishlist,
        name="add_wishlist"
    ),


    path(
        "",
        views.wishlist_view,
        name="wishlist"
    ),


    path(
        "remove/<int:id>/",
        views.remove_wishlist,
        name="remove_wishlist"
    ),

]
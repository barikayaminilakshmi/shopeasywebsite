from django.shortcuts import render


def order_success(request):

    return render(
        request,
        "order_success.html"
    )
import os
import django
import sys
import requests

from django.core.files import File
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoppingapp.settings")
django.setup()

from products.models import Product, Category


# Create image folder
image_folder = "media/products"
os.makedirs(image_folder, exist_ok=True)


products = [

    # ---------------- ELECTRONICS ----------------

    {
        "name": "iPhone 15",
        "category": "Electronics",
        "price": 70000,
        "image": "https://dummyimage.com/600x600/000/fff&text=iPhone+15"
    },

    {
        "name": "Samsung Galaxy S25",
        "category": "Electronics",
        "price": 60000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Samsung+S25"
    },

    {
        "name": "HP Laptop",
        "category": "Electronics",
        "price": 55000,
        "image": "https://dummyimage.com/600x600/000/fff&text=HP+Laptop"
    },

    {
        "name": "Dell Monitor",
        "category": "Electronics",
        "price": 15000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Dell+Monitor"
    },

    {
        "name": "Wireless Headphones",
        "category": "Electronics",
        "price": 3000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Headphones"
    },

    {
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 5000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Smart+Watch"
    },

    {
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "price": 2500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Speaker"
    },

    {
        "name": "Keyboard",
        "category": "Electronics",
        "price": 1500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Keyboard"
    },

    {
        "name": "Gaming Mouse",
        "category": "Electronics",
        "price": 1200,
        "image": "https://dummyimage.com/600x600/000/fff&text=Gaming+Mouse"
    },

    {
        "name": "Tablet",
        "category": "Electronics",
        "price": 25000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Tablet"
    },


    # ---------------- FASHION MEN ----------------

    {
        "name": "Men Casual Shirt",
        "category": "Fashion Men",
        "price": 1200,
        "image": "https://dummyimage.com/600x600/000/fff&text=Men+Shirt"
    },

    {
        "name": "Men Jeans",
        "category": "Fashion Men",
        "price": 1800,
        "image": "https://dummyimage.com/600x600/000/fff&text=Men+Jeans"
    },

    {
        "name": "Men T Shirt",
        "category": "Fashion Men",
        "price": 800,
        "image": "https://dummyimage.com/600x600/000/fff&text=Men+Tshirt"
    },

    {
        "name": "Men Jacket",
        "category": "Fashion Men",
        "price": 2500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Men+Jacket"
    },

    {
        "name": "Men Hoodie",
        "category": "Fashion Men",
        "price": 2000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Hoodie"
    },


    # ---------------- FASHION WOMEN ----------------

    {
        "name": "Women Dress",
        "category": "Fashion Women",
        "price": 2500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Women+Dress"
    },

    {
        "name": "Women Saree",
        "category": "Fashion Women",
        "price": 3000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Saree"
    },

    {
        "name": "Women Kurti",
        "category": "Fashion Women",
        "price": 1500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Kurti"
    },

    {
        "name": "Women Handbag",
        "category": "Fashion Women",
        "price": 2200,
        "image": "https://dummyimage.com/600x600/000/fff&text=Handbag"
    },

    {
        "name": "Women Shoes",
        "category": "Fashion Women",
        "price": 2000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Women+Shoes"
    },
    # ---------------- SKINCARE ----------------

    {
        "name": "Face Cream",
        "category": "Skincare",
        "price": 500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Face+Cream"
    },

    {
        "name": "Face Wash",
        "category": "Skincare",
        "price": 350,
        "image": "https://dummyimage.com/600x600/000/fff&text=Face+Wash"
    },

    {
        "name": "Moisturizer",
        "category": "Skincare",
        "price": 600,
        "image": "https://dummyimage.com/600x600/000/fff&text=Moisturizer"
    },

    {
        "name": "Sunscreen",
        "category": "Skincare",
        "price": 450,
        "image": "https://dummyimage.com/600x600/000/fff&text=Sunscreen"
    },

    {
        "name": "Lip Balm",
        "category": "Skincare",
        "price": 200,
        "image": "https://dummyimage.com/600x600/000/fff&text=Lip+Balm"
    },


    # ---------------- ACCESSORIES ----------------

    {
        "name": "Backpack",
        "category": "Accessories",
        "price": 1500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Backpack"
    },

    {
        "name": "Wallet",
        "category": "Accessories",
        "price": 800,
        "image": "https://dummyimage.com/600x600/000/fff&text=Wallet"
    },

    {
        "name": "Sunglasses",
        "category": "Accessories",
        "price": 1200,
        "image": "https://dummyimage.com/600x600/000/fff&text=Sunglasses"
    },

    {
        "name": "Watch",
        "category": "Accessories",
        "price": 3000,
        "image": "https://dummyimage.com/600x600/000/fff&text=Watch"
    },

    {
        "name": "Cap",
        "category": "Accessories",
        "price": 500,
        "image": "https://dummyimage.com/600x600/000/fff&text=Cap"
    },

]

for item in products:

    category, created = Category.objects.get_or_create(
        category_name=item["category"]
    )

    image_name = item["name"].replace(" ", "_") + ".png"
    image_path = os.path.join(image_folder, image_name)


    # Download image only if it does not exist
    if not os.path.exists(image_path):
        response = requests.get(item["image"])

        with open(image_path, "wb") as img:
            img.write(response.content)


    # Prevent duplicate products
    product, created = Product.objects.get_or_create(
        product_name=item["name"],
        defaults={
            "category": category,
            "price": item["price"],
            "description": "Premium quality product",
            "stock": 10
        }
    )


    # Add image only for new products
    if created:
        with open(image_path, "rb") as img:
            product.image.save(
                image_name,
                File(img),
                save=True
            )

        print(item["name"], "added successfully")

    else:
        print(item["name"], "already exists")


print("30 products imported successfully!")
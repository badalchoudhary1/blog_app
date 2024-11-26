from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from users import users
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Product
from django.contrib.auth import authenticate,login,logout

# View for greeting message
def hello_world(request):
    return HttpResponse("Hello, World!")

# View for how are you message
def how(request):
    return HttpResponse("Hi, how are you?")

# View to get specific user based on user_id
def getUser(request, user_id):
    # Loop through users to find the user with the provided user_id
    user = next((user for user in users if user['id'] == user_id), None)

    if user:
        # If user found, return their name and address
        return HttpResponse(f" {json.dumps(user)}")
    else:
        # If user not found, return a not found message
        return HttpResponse("User not found")

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Safely get the values
        price = request.POST.get('price')
        category = request.POST.get('category')  # Updated field
        color = request.POST.get('color')  # New field

        if not name or not price or not category or not color:  # Validate inputs
            return HttpResponse("Missing required fields", status=400)

        # Save the data to the Product model
        Product.objects.create(name=name, price=price, category=category, color=color)
        return redirect('get_all_users')  # Ensure 'get_all_users' is a valid URL name

    return render(request, 'add_user.html')

def get_user(request, user_id):
    product = Product.objects.filter(id=user_id).first()  # Safely fetch product
    if product:
        return render(request, 'product_detail.html', {'product': product})  # Render details
    else:
        return HttpResponse("Product not found", status=404)

def get_all_users(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'get_all_user.html', {'users': products})  # Pass as 'users'

def edit_user(request, user_id):
    product = get_object_or_404(Product, id=user_id)  # Fetch the product or 404

    if request.method == 'POST':
        # Update fields based on POST data
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.category = request.POST.get('category')
        product.color = request.POST.get('color')
        product.save()  # Save the updated product

        return redirect('get_all_users')  # Redirect to the product list

    return render(request, 'edit_user.html', {'product': product})  # Render edit form

def delete_user(request, user_id):
    product = get_object_or_404(Product, id=user_id)  # Fetch the product or 404
    product.delete()  # Delete the product
    return redirect('get_all_users')  # Redirect to the product list

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user) 
            return redirect('create_user')  
        else:
            return render(request, "login.html")
    return render(request, "login.html")
def logout_user(request):
    logout(request)  
    return redirect('login_user')













from django.shortcuts import render, redirect
from .models import MenuItem, Order,OrderItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# -------------------- MENU --------------------
@login_required
def menu(request):
    items = MenuItem.objects.all()
    return render(request, "orders/menu.html", {"items": items})

# -------------------- ORDER --------------------
@login_required
def order_page(request):
    items = MenuItem.objects.all()
    item_id = request.GET.get("item_id") or request.POST.get("item_id")
    selected_item = None
    total_bill = None

    if item_id:
        selected_item = MenuItem.objects.get(id=item_id)

    if request.method == "POST":
        customer_name = request.user.username  # auto-fill from login
        phone = request.user.email or ""       # or add phone field in profile later
        quantity = int(request.POST.get("quantity", 1))

        if selected_item:
            # Create order
            order = Order.objects.create(
                user=request.user,
                customer_name=customer_name,
                phone=phone
            )
            OrderItem.objects.create(
                order=order,
                menu_item=selected_item,
                quantity=quantity
            )
            return redirect("order_success")

    # calculate bill preview if quantity entered
    if selected_item:
        q = int(request.POST.get("quantity", 1))
        total_bill = selected_item.price * q

    return render(request, "orders/order.html", {
        "items": items,
        "selected_item": selected_item,
        "total_bill": total_bill,
        "user": request.user
    })

# -------------------- ORDER SUCCESS --------------------
@login_required
def order_success(request):
    return render(request, "orders/order_success.html")

# -------------------- SIGNUP --------------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, "orders/signup.html")

# -------------------- LOGIN --------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, "orders/login.html")

# -------------------- LOGOUT --------------------
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('login')

@login_required
def order_success(request):
    # Get the latest order for the logged-in user
    order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    return render(request, "orders/order_success.html", {"order": order})


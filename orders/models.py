from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, null=True)
    items = models.ManyToManyField(MenuItem, through="OrderItem")
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price for item in self.orderitem_set.all())

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity

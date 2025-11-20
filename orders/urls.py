from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order/', views.order_page, name='order_page'),
    path("order/success/", views.order_success, name="order_success"),
]

from django.urls import path
from .views import CartItemViews, CartItemList, CreateUser, Testtest

urlpatterns = [
    path('cart-item/', CartItemViews.as_view()),
    path('cart-item/<int:id>', CartItemViews.as_view()),
    path('cart-items',CartItemList.as_view()),
    path('create-user',CreateUser.as_view()),
    path('Test-test', Testtest.as_view())
    # path('token', )
]

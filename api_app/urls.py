from django.urls import path
from .views import CartItemViews,CartItemList

urlpatterns = [
    path('cart-item/', CartItemViews.as_view()),
    path('cart-item/<int:id>', CartItemViews.as_view()),
    path('cart-items',CartItemList.as_view())
    # path('token', )
]

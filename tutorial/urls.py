from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_app.urls')),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refreshtoken', TokenRefreshView.as_view(), name='refreshtoken'),
]

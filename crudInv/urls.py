# from django.contrib import admin
from django.urls import path
from rest_framework import routers
from inventory import views
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'shippings', views.ShipppingViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TypeOfUserViewSet, UserViewSet, TicketViewSet, ReservationViewSet, 
    StatusViewSet, RefundViewSet, PaymentViewSet, NotificationViewSet, 
    CategoryEventViewSet, EventViewSet, MyTokenObtainPairView, RegisterView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'types', TypeOfUserViewSet)
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'refunds', RefundViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'categories', CategoryEventViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

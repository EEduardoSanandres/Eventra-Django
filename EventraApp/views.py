from rest_framework import viewsets, generics
from .models import TypeOfUser, User, Ticket, Reservation, Status, Refund, Payment, Notification, CategoryEvent, Event
from .serializers import (
    TypeOfUserSerializer, UserSerializer, TicketSerializer, ReservationSerializer, StatusSerializer, 
    RefundSerializer, PaymentSerializer, NotificationSerializer, CategoryEventSerializer, EventSerializer, RegisterSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class TypeOfUserViewSet(viewsets.ModelViewSet):
    queryset = TypeOfUser.objects.all()
    serializer_class = TypeOfUserSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class CategoryEventViewSet(viewsets.ModelViewSet):
    queryset = CategoryEvent.objects.all()
    serializer_class = CategoryEventSerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = []

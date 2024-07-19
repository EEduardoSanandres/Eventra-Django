from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import TypeOfUser, User, Ticket, Reservation, Status, Refund, Payment, Notification, CategoryEvent, Event

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'password', 'typeOfUser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            typeOfUser=validated_data['typeOfUser'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user

class TypeOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName', 'typeOfUser', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CategoryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEvent
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

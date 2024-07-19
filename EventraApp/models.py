from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class TypeOfUser(models.Model):
    typeId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"TypeOfUser [typeId={self.typeId}, description={self.description}]"

class UserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, firstName=firstName, lastName=lastName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstName, lastName, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, firstName, lastName, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    userId = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    typeOfUser = models.ForeignKey(TypeOfUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    objects = UserManager()

    def __str__(self):
        return self.email

class Ticket(models.Model):
    ticketID = models.AutoField(primary_key=True)
    eventID = models.BigIntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    totalAvailable = models.IntegerField(null=False)
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ticket [ticketID={self.ticketID}, eventID={self.eventID}, price={self.price}, totalAvailable={self.totalAvailable}, category={self.category}, description={self.description}]"

class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True)
    userID = models.BigIntegerField(null=False)
    ticketID = models.BigIntegerField(null=False)
    quantity = models.IntegerField(null=False)
    reservationDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation [reservationID={self.reservationID}, userID={self.userID}, ticketID={self.ticketID}, quantity={self.quantity}, reservationDate={self.reservationDate}]"

class Status(models.Model):
    statusID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"Status [statusID={self.statusID}, description={self.description}]"

class Refund(models.Model):
    refundID = models.AutoField(primary_key=True)
    paymentID = models.BigIntegerField(null=False)
    refundAmount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    refundStatus = models.ForeignKey(Status, on_delete=models.CASCADE)
    refundDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Refund [refundID={self.refundID}, paymentID={self.paymentID}, refundAmount={self.refundAmount}, refundStatus={self.refundStatus}, refundDate={self.refundDate}]"

class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    reservationID = models.BigIntegerField(null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    paymentMethod = models.CharField(max_length=50, null=False)
    paymentStatus = models.ForeignKey(Status, on_delete=models.CASCADE)
    paymentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Payment [paymentID={self.paymentID}, reservationID={self.reservationID}, amount={self.amount}, paymentMethod={self.paymentMethod}, paymentStatus={self.paymentStatus}, paymentDate={self.paymentDate}]"

class Notification(models.Model):
    notificationID = models.AutoField(primary_key=True)
    userID = models.BigIntegerField(null=False)
    message = models.TextField(null=False)
    isRead = models.BooleanField(default=False)
    sentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification [notificationID={self.notificationID}, userID={self.userID}, message={self.message}, isRead={self.isRead}, sentDate={self.sentDate}]"

class CategoryEvent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"CategoryEvent [id={self.id}, name={self.name}]"

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    organizerId = models.BigIntegerField(null=False)
    url = models.CharField(max_length=255, default='', null=False)
    categoryEvent = models.ForeignKey(CategoryEvent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Event [id={self.id}, title={self.title}, description={self.description}, startDate={self.startDate}, endDate={self.endDate}, location={self.location}, organizerId={self.organizerId}, url={self.url}, categoryEvent={self.categoryEvent}]"

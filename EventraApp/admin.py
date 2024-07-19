from django.contrib import admin
from .models import TypeOfUser, User, Ticket, Reservation, Status, Refund, Payment, Notification, CategoryEvent, Event

admin.site.register(TypeOfUser)
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(Status)
admin.site.register(Refund)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(CategoryEvent)
admin.site.register(Event)

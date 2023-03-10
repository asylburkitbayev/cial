from django.contrib import admin
from .models import Contact, Feedback, Employee, Spam, Service


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'img']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'facebook', 'twitter', 'linkedin']


class SpamAdmin(admin.ModelAdmin):
    list_display = ['email']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']


admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Spam, SpamAdmin)

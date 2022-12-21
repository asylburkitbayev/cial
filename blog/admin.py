from django.contrib import admin
from .models import Contact, Feedback, Employee, Spam


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['img', 'text']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'facebook', 'twitter', 'linkedin']


class SpamAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Spam, SpamAdmin)

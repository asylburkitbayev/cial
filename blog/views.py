from django.shortcuts import render
from .models import Feedback, Contact, Employee, Spam


def index(request):
    employee = Employee.objects.all()
    contact = Contact.objects.all()
    spam = Spam.objects.all()
    feedback = Feedback.objects.all()
    context = {'employee': employee,
               'contact': contact,
               'spam': spam,
               'feedback': feedback
               }
    return render(request, 'index.html', context=context)

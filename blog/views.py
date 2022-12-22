from django.shortcuts import render, redirect
from .models import Feedback, Contact, Employee, Spam


def index(request):
    employees = Employee.objects.all()
    list_feedback = Feedback.objects.all()
    context = {'employees': employees,
               'list_range': [i for i in range(1, len(list_feedback))],
               'feedback': list_feedback[0],
               'list_feedback': list_feedback[1:]
               }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')


def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        add_contact = Contact.objects.create(
            email=email,
            name=name,
            phone=phone,
            message=message
        )
        add_contact.save()
    return redirect('/')


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')


def about(request):
    return render(request, 'about.html')


def add_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_email = Spam.objects.create(email=email, )
        new_email.save()
    return redirect('/')

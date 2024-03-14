from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Define the Person class
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username


# Initialize the list to store Person instances
people = []


# View for adding a Person
def add(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username, password)
        people.append(new_person)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'add.html')


# View for listing all Person instances
def index(request):
    return render(request, 'index.html', {'people': people})
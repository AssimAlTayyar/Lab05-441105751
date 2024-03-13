from django.shortcuts import render, redirect

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
        return redirect('default')
    return render(request, 'add.html')

def default_view(request):
    context = {'people': people}
    return render(request, 'default.html', context)
from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Marco Bassaletti',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
                   'nisi ut aliquip ex ea commodo consequat.',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua.',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About'
    })


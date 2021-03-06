# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from srkob.models import Book, Genre, Profile
from srkob.forms import UserForm, ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User

def get_book_list():
    book_list = Books.objects.all()

    for book in book_list:
        book.url = encode_url(book.title)

    return book_list

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': " "}
    return render_to_response('srkob/index.html', context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': " "}
    return render_to_response('srkob/about.html', context_dict, context)

def genre(request):
    context =RequestContext(request)
    genre_list = Genre.objects.order_by('-genre_main')[:5]
    context_dict = {'genres': genre_list}
    for genre in genre_list:
        genre.url = encode_url(genre.genre_main)
    return render_to_response('srkob/genre.html', context_dict, context)
<<<<<<< HEAD

def genre_details(request, genre_name_url):
    context = RequestContext(request)
    genre_name = decode_url(genre_name_url)
    context_dict = {'genre_name': genre_name}
    try:
        genre = Genre.objects.get(genre_main=genre_name)
        books = Book.objects.filter(genre=genre)
        context_dict['books'] = books
        context_dict['genre'] = genre
        for book in books:
<<<<<<< HEAD
            book.url = encode_url(book.title)
=======
            book.url = book.title
>>>>>>> b0ac0410d8acb8012e960cf6db1910b8aca88c54
    except Genre.DoesNotExist:



        pass
    return render_to_response('srkob/genre_details.html', context_dict, context)

<<<<<<< HEAD
def book_details(request, book_name_url):
    context = RequestContext(request)
    book_name = decode_url(book_name_url)
    date_plus = datetime.date.today() + datetime.timedelta(days=7)
    context_dict = {'date_plus' : date_plus}
=======

def book_details(request, book_name_url):
    context = RequestContext(request)
    book_name = book_name_url
>>>>>>> b0ac0410d8acb8012e960cf6db1910b8aca88c54
    context_dict = {'book_name' : book_name}
    try:
        details = Book.objects.get(title=book_name)
        context_dict['details'] = details
<<<<<<< HEAD
        
    except Book.DoesNotExist:

        pass

        
    
        
=======
    except Book.DoesNotExist:

        pass
>>>>>>> b0ac0410d8acb8012e960cf6db1910b8aca88c54
    return render_to_response('srkob/book_details.html', context_dict, context)
 
=======


def genre_details(request, genre_name_url):
    context = RequestContext(request)
    genre_name = genre_name_url
    context_dict = {'genre_name': genre_name}
    try:
        genre = Genre.objects.get(genre_main=genre_name)
        books = Book.objects.filter(genre=genre)
        context_dict['books'] = books
        context_dict['genre'] = genre
    except Genre.DoesNotExist:

        pass
    return render_to_response('srkob/genre_details.html', context_dict, context)




>>>>>>> f807e813e81bb82e502257923495b6216a0ba557
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
         user_form = UserForm(data=request.POST)
         profile_form = ProfileForm(data=request.POST)
         if user_form.is_valid() and profile_form.is_valid():
              user = user_form.save()
              user.set_password(user.password)
              user.save()
              profile = profile_form.save(commit=False)
              profile.user = user
              profile.save()
              #dodawanie użytkownika do grupy  
              g = Group.objects.get(name='uzytkownik')
              g.user_set.add(user)
              registered = True
         else:
             print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    # 
    return render_to_response(
            'srkob/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)                  

def user_login(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/srkob/')
            else:
                context_dict['disabled_account'] = True
                return render_to_response('srkob/login.html', context_dict, context)

        else:
            print "NIepoprawna dane:  {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('srkob/login.html', context_dict, context)
    else:
        return render_to_response('srkob/login.html', {}, context)

def rent_details(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        title = request.POST['title']
        context_dict['title'] = title

        user_name = requst.POST['user_name']
        context_dict['user_name'] = user_name

        date = request.POST['date']
        context_dict['date'] = date

        state = request.POST['state']
        context_dict['state'] = state

    return render_to_response('srkob/rent_details.html', context_dict, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/srkob/')

@login_required
def user_profile(request):
    context = RequestContext(request)
    context_dict = {}
    u = User.objects.get(username=request.user)
    p = Profile.objects.get(user=u)
    context_dict['user'] = u
    context_dict['profile'] = p
    return render_to_response('srkob/user_profile.html', context_dict, context)
    
def search(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            books_list = Book.objects.filter(title__icontains=query) 
            context_dict['books_list'] = books_list
            for book in books_list:
                book.url = encode_url(book.title)           
    return render_to_response('srkob/search.html', context_dict, context)

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import (
    Book,
    Author,
    BookInstance,
    Genre
)

# Create your views here.


def index(request):
    """ View function for home page of site. """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Avaliable books (status = 'a')
    num_instances_avaliable = BookInstance.objects.filter(
        status__exact='a'
    ).count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.filter(
        name__contains='Sci'
    ).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avaliable': num_instances_avaliable,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'my_book_list'  # your own name for the list as a template valiable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the war
    template_name = 'book_list.html' # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'authors'
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

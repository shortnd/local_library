from django.shortcuts import render
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

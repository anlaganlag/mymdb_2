from django.views.generic import ListView,DetailView
from core.models import Movie,Person


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class MovieList(ListView):
    model = Movie
    paginate_by =10


class MovieDetail(DetailView):
    queryset = (Movie.objects.all_with_related_persons())


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('core:MovieList')


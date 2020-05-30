from django.views.generic import ListView,DetailView
from core.models import Moive

class MoiveList(ListView):
    model = Moive


class MoiveDetail(DetailView):
    model = Moive

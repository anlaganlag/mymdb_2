from django.views.generic import ListView
from core.models import Moive

class MoiveList(ListView):
    model = Moive
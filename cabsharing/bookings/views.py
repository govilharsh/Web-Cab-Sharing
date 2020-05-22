from django.views import generic
from .models import Bookings


class IndexView(generic.ListView):
    template_name = 'bookings/index.html'

    def get_queryset(self):
        return Bookings.objects.all()


class DetailView(generic.DetailView):
    model = Bookings
    template_name = 'bookings/detail.html'


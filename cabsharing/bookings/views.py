from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from .bookingform import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.views import generic
from .models import Bookings
from braces.views import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'bookings/index.html'

    def get_queryset(self):
        return Bookings.objects.all()


class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Bookings
    template_name = 'bookings/detail.html'


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.date < datetime.date.today():
                messages.success(request, "You can't create a booking with a date which has already passed.")
                return redirect('bookings:bookings_create')
            booking.user = request.user
            booking.creator = request.user.username
            booking.save()
            messages.success(request,  "Booking created successfully ")
            return redirect('bookings:index')
    else:
        form = BookingForm()
        return render(request, 'bookings/booking_form.html', {'form': form})

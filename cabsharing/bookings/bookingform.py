from django import forms
from .models import Bookings, Member


class BookingForm(forms.ModelForm):
    start_position = forms.CharField(label='From:', required=True)
    destination = forms.CharField(label='To:', required=True)
    date = forms.DateField(label='Date:', required=True, widget=forms.DateInput(attrs={'placeholder':'dd-mm-yyyy'}))
    time = forms.TimeField(label='Time:', required=True, widget=forms.TimeInput(attrs={'placeholder':'00:00'}), help_text ='24-hours format')
    max_members = forms.IntegerField(label='Maximum number of members:', help_text = 'maximum number of members includes you as well.', required=True)
    description = forms.CharField(label='Description:', required=False)

    class Meta:
        model = Bookings
        fields = ['start_position' ,'destination','date','time', 'max_members', 'description']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = []

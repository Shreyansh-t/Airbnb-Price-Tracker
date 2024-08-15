from django import forms

class StayDetailForm(forms.Form):

    where = forms.CharField(label="Where", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    check_in = forms.CharField(label='Check-In', widget=forms.TextInput(attrs={'placeholder': 'Check-In'}) ,max_length=100)
    check_out = forms.CharField(label='Check-Out', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Check-Out'}))
    adults = forms.IntegerField(label="Adults", widget=forms.TextInput(attrs={'placeholder': 'No. of adults travelling'}))
    children = forms.IntegerField(label="Children", widget=forms.TextInput(attrs={'placeholder': 'No. of children travelling'}))
    infants = forms.IntegerField(label="Infants", widget=forms.TextInput(attrs={'placeholder': 'Any Infants'}))
from django import forms

class CountryForm(forms.Form):
    country = forms.CharField(max_length=100, label='Country Name')

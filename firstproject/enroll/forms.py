from django import forms
class Data(forms.Form):
    name = forms.CharField(label='City Name ')
    
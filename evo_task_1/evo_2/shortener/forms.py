from django import forms
from .validators import validate_dot_com, validate_url
from django.core.validators import URLValidator

class SubmitURLForm (forms.Form):
    url = forms.CharField (label= 'Submit URL', validators=[validate_url, validate_dot_com])



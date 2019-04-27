from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url (value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError('Invalid URL for this field')
    return value

def validate_dot_com (value):
    if not 'com' and not 'org' and not 'gov' and not 'net' and not 'ua' and not 'us' and not 'ru' and not 'fr' in value:
        raise ValidationError('Invalid URL for this field')
    return value

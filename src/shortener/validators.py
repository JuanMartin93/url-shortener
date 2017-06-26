from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    value_1 = value

    if "http" not in value_1:
    	value_1 = "http://" + value_1
 
    try:
        url_validator(value_1)
    except:
        raise ValidationError("Invalid URL for this field")

    print(value_1)    
    return value_1


def validate_dot_com(value):
	if not "com" in value and not ".edu" in value:
		print("Hello no need for exception, value", value )
		raise ValidationError("Invalid URL .com or .edu missing")
	return value
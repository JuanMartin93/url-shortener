from django import forms 
from .validators import validate_url, validate_dot_com


class SubmitUrlForm(forms.Form):
	url = forms.CharField(label='', 
						  validators=[ validate_url, validate_dot_com],
						  widget=forms.TextInput(
						  		  attrs = {"placeholder": "Insert Long URL to get it shortened for u !!!", 
						  		  			"class": "form-control"
						  		  			}
						  			)
							 )


	# #cleans the form 
	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean()
	# 	url = cleaned_data['url']
	# 	print(url)

	#cleans single object
	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	urlValidator = URLValidator()

	# 	try:
	# 		urlValidator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL for this URL")
	# 	return url	
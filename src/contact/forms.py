from django import forms

from .models import Contact_form

class Contact_create_form(forms.ModelForm):
	class Meta:
		model = Contact_form
		fields = [
			'type_of_contact',
			'contact_name',
			'contact_email',
			'subject_matter',
			'text_message'
		]
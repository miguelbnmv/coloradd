from django.db import models

# Create your models here.
class Contact_form(models.Model):
	TYPE_OF_CONTACT_CHOICES = [
		('Company_Enterprise','Company/Enterprise'),
		('Municipality','Municipality'),
		('School_college','School/College'),
		('Hospital','Hospital'),
		('Individual','Individual'),
		('Other','Other'),
	]
	type_of_contact = models.CharField(
		max_length=30,
		choices=TYPE_OF_CONTACT_CHOICES,
		default='Company_Enterprise'
	)
	contact_name = models.CharField(max_length=50)
	contact_email = models.EmailField()
	SUBJECT_MATTER_CHOICES = [
		('Licensing','Licensing'),
		('Employment','Employment'),
		('ColorADD_social','ColorADD Social'),
		('Funds_donations','Funds/Donations'),
		('Other_subject','Other subject'),
	]
	subject_matter = models.CharField(
		max_length=30,
		choices=SUBJECT_MATTER_CHOICES,
		default='Licensing'
	)
	text_message = models.TextField(default='')
	
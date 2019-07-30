from django.shortcuts import render

from .forms import Contact_create_form
from .models import Contact_form
# Create your views here.

def contact_create_view(request):
	form = Contact_create_form(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "contact/contact_create.html", context)
from django.shortcuts import render

from .models import Image
# Create your views here.
def images_view(request):
	data = Image.objects.all().order_by('likes')
	context = {
		"images": data
	}
	return render(request, "images/images.html", context)
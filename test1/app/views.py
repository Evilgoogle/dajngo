from django.shortcuts import render

# Create your views here.
def index(request, var=18):

	data = {'name': 'Anton', 'age': var}
	return render(request, 'index.html', context=data)

def contact(request):

	data = {'name': 'Anton', 'age': 'contact'}
	return render(request, 'index.html', context=data)

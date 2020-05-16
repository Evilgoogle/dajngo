from django.shortcuts import render

# Create your views here.
def index(request):

	data = {'name': 'Anton', 'age': 18}
	return render(request, 'index.html', context=data)

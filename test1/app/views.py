from django.shortcuts import render
from app.forms import NameForm

# Create your views here.
def index(request):

	form = NameForm()
	data = {'name': 'Anton', 'age': 18, 'form': form}
	return render(request, 'index.html', context=data)

def contact(request):

	data = {'name': 'Anton', 'age': 'contact'}
	return render(request, 'index.html', context=data)

from django.shortcuts import render
from app.forms import NameForm, GoodsForm
from django.http import HttpResponse

# Create your views here.
def index(request):

	data = {
		'name' : 'Helena',
		'email' : 'almanal@mail.ru',
		'desc' : 'desc text ...',
	}

	form = NameForm(data, auto_id=True, label_suffix='[]')
	# auto_id false отключает label теги
	# label_suffix добавляет - Имя (суффикс)
	# error_class=myError отрабатываем ошибки через свои класс

	data = {'name': 'Anton', 'age': 18, 'form': form}
	return render(request, 'index.html', context=data)

def contact(request):

	data = {'name': 'Anton', 'age': 'contact'}
	return render(request, 'index.html', context=data)

def form(request):

	if request.method == 'POST':

		data = {
			'name' : 'Helena',
			'email' : 'almanal@mail.ru',
			'desc' : 'desc text ...',
		}
		test = NameForm(request.POST)
		#test.is_valid()
		#return HttpResponse(test.cleaned_data)
		return render(request, 'test.html', {"test": test}) #changed_data

## Форму можно зполнять
#data = {
#	'name' : 'Anton',
#	'email' : 'almanal@mail.ru',
#	'desc' : 'desc text ...',
#}
#form = NameForm(data)

## Проверка на валидность
#form = NameForm(data)
#form.is_valid() # True False

## Форма забита или не  забита данными
#form = NameForm(data)
#return HttpResponse(form.is_bound);

## На какой поле ошибка
#test = NameForm(request.POST)
#return HttpResponse(test.errors)

## Есть ли ошибка по данному полю
#error = test.has_error('email')
#return HttpResponse(error)

## Добавляем ошибки. Ошибки можно добавить в те поля которые есть во field
#test.add_error('desc', 'Добавлена error, хотя его не было в этом поле')
#error = test.errors.as_data()
#return HttpResponse(error)

## Мы можем заполнить поле передав словарь - data. Можем на через initial также передавать, она указывает на изначальные данные. Если есть initial-ы заданные при созданий формы тогда они перепишется
#form = NameForm(initial={'name': 'Anna'})

## Проверяем изминились ли нужные данные. has_changed
#data = {
#	'name' : 'Helena',
#	'email' : 'almanal@mail.ru',
#	'desc' : 'desc text ...',
#}
#test = NameForm(request.POST, initial=data) # initial указывает изначальные данные. 1 параметр данные приходящие из POST
#return HttpResponse(test.has_changed()) # Если данные не совпадают то True
# test.changed_data() увидить эти отличие в словаре

## Очищяем данные формы от шаблона cleaned_data. Получаем чистые данные в виде словаря
#test = NameForm(data)
#test.is_valid() # cleaned_data работает только после проверки
#return HttpResponse(test.cleaned_data)


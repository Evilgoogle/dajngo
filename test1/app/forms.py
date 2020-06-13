from django import forms
from django.forms import ModelForm
from app.models import goods

class MyAdminForm(ModelForm):
    pass

class NameForm(forms.Form):
    # default_renderer = MyRenderer() добавить свой шаблонизатор. По умоланию есть 2 вида DjangoTemplates и Jinja2
    error_css_class = 'my_error' # Добавляем класс для стилизация поле ошибки
    required_css_class = 'my_class' # Добавляем класс для стилизация поле
    name = forms.CharField(
        label='Your name', 
        max_length=100, 
        initial='Anton', 
        help_text='Введите Имя', 
        required=True,
        min_length=2,
    )
    email = forms.EmailField(label='Почта')
    desc = forms.CharField(widget=forms.Textarea, required=False)

    field_order = ['email','desc', 'name']

class GoodsForm(ModelForm):
    class Meta:
        model = goods
        fields = '__all__'

    desc = forms.CharField(widget=forms.Textarea)

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

from django import forms
from django.forms import ModelForm
from app.models import goods
from app.libs.form_widjets import CalendarWidget

class MyAdminForm(ModelForm):
    pass

class NameForm(forms.Form):
    # default_renderer = MyRenderer() добавить свой шаблонизатор. По умоланию есть 2 вида DjangoTemplates и Jinja2
    error_css_class = 'my_error' # Добавляем класс для стилизация поле ошибки
    required_css_class = 'box' # Добавляем класс для стилизация поле
    name = forms.CharField(
        label='Your name', # Записать label
        max_length=100, 
        initial='Anton', 
        help_text='Введите Имя', 
        required=True,
        min_length=2,
        error_messages={'required': 'Требуется имя'}, # свое сообщение
        #validators = [myValidators] # свои валидатор ошибок
        disabled=True # делает disabled
    )
    email = forms.EmailField(label='Почта')
    desc = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textin', 'required': False})
    )
    enable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'box', 'checked': False}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    calendar = forms.CharField(
        label='Date',
        help_text = 'Выберите Дату',
        widget=CalendarWidget()
    )

    CHOICES = [('1', 'First'), ('2', 'Second')]
    choice_field = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'data-id': 10}),
        choices=CHOICES,
    )

    url = forms.URLField()

    field_order = ['email','desc', 'name']

class GoodsForm(ModelForm):
    class Meta:
        model = goods
        fields = '__all__'

    desc = forms.CharField(widget=forms.Textarea)

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

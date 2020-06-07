from django.db import models
from django.utils import timezone

# Каждое тип поля таблицы соответсвуте экземпляру класса Filed и соотвественно есть готовые BooleanField CharField и другие Field указывающий тип данных.
# Create your models here.

class news(models.Model):

    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    enable = models.BooleanField(default=0) # Так делается значение поле по умолчанию, НО он в базе так не отображается, но деалется со стороны Django
    testChar_null = models.CharField(max_length=191, null=True) #null=True - он по умолчанию False. True делает поле таблицы по умолчанию Null
    testChar_blank = models.CharField(max_length=191, blank=True)

    testChar_choices = models.CharField(max_length=191, choices=SHIRT_SIZES, null=True)
    test_help_text = models.CharField(max_length=100, null=True, help_text='<b>help_text</b> - нужен для документирование')
    test_ix_unique = models.CharField(max_length=50, null=True, unique=True, help_text='unique создает индекс unique')
    test_ix_index = models.CharField(max_length=50, null=True, db_index=True, help_text='db_index создает индекс index')
    test_full_defaulname = models.CharField("person's first name", max_length=30, null=True)

class news2authors(models.Model):
    let_id = models.AutoField(primary_key = True) # Если вот так явно указать primary_key = True, то поле id не создастся по автомату, так как primary_key может только один.
    news_id = models.IntegerField(null=True, db_index=True)
    author_id = models.IntegerField(null=True, db_index=True)

class authors(models.Model):
    enable = models.BooleanField(default=0)
    access = models.IntegerField(default=1)
    name = models.CharField(max_length=191, null=True)

    def save(self, *args, **kwargs): # Предоопределяю встроенный метод - save;
        self.name = self.name + 'tree' # Расширение
        super().save(self, *args, **kwargs) # Барбара Лисков поддерживается

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('l', 'link'),
]
class goods(models.Model):
    enable = models.BooleanField(default=0)
    other_position = models.IntegerField(null=True, db_column='position') # db_column - принудельто назвает колонку таблицы, иначе он берется от переменной other_position
    title = models.CharField(max_length=191, null=True)
    url = models.CharField(max_length=191, null=True)
    image = models.CharField(max_length=191, null=True, editable=True) # editable - отклчаем данные поле для админки и Form
    date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True) # auto_now_add - задает текущая время при первом save
    updated = models.DateTimeField(auto_now=True) #auto_now - задает текущая время при каждом save
    bind = models.BinaryField(null=True, editable=True) # Создает поле с типом blob. Создает longblob
    text = models.TextField(null=True) # создает longtext поле
    decimal = models.DecimalField(max_digits=2, decimal_places=2, null=True) # создает поле типа dicimal
    email = models.EmailField(max_length = 100, blank=True)
    file = models.FileField(max_length=254, upload_to=None, null=True) # upload_to - указываем путь и файл хранение. Если хочу это надо подробно ичучить, есть много методов
    float = models.FloatField(null=True) # cоздает поле double для float данных
    ip = models.GenericIPAddressField(null=True)
    age = models.IntegerField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', null=True)

    def __str__(self):
        return self.title

    @classmethod # Так мы в __init__ можем переопределить встроенные функций модели, расширить их как нам надо. Здесь title будет всегда None когда создается запись через create
    def create(cls, title):
        title = cls(title='None')
        return title

    class Meta:
        # app_label = 'TestApp' # Если данная модель относится к другому приложению, то его название тут надо указать.
        # base_manager_name = 'TestManager' # Если у нас есть свои манеджер расширенный на основе стандартного манаджера, то определяем этот манеджер для этой модели. Обработка будет идти от нестандартного манеджера
        db_table = 'my_goods' # Указываем свое имя таблицы. По умолчанию django берет имя от приложение и название моделя - app_goods
        # db_tabelespace = '' # Этого для рядовых проектов не нужно. Нужно для особых проектов, где надо разделять память базы.
        get_latest_by = 'created' # для функций objects.latest() задает значение для выборки objects.latest('created'). Можно будет просто objects.latest() дать и получить последное изминение
        managed = True # Он по умолчаню True. False отключает миграций для этой моделей. Это полезно если данная таблица в базе есть или мы не хотим создовать такую таблицу или изменять.
        indexes = [ # indexes это meta для создание индексов.
            models.Index(fields=['title', 'email'], name='ixIndex'), # Index это специальный класс которая создает тип index в базе
            models.Index(fields=['ip'], name='ixTExt')
        ]
        ordering = ['-created'] # Добавляте order by к запросу
        unique_together = ['ip'] # Дать unique индекс

        # Meta нужен для информация о данном моделе. Он не вводит нечего в поля
    #class Meta:
    #ordering = ["horn_length"]
    #verbose_name_plural = "oxen"

    # Пользовательские методы. Свои методы как дополнение.
    # Точнее сказать мы в наш класс news унаследовали все методы от models.Model
    # и тут к нему еще и добавляем свои ползовательсие
    def baby_boomer_status(self):
        return "Pre-boomer"

class dummy(models.Model):
    enable = models.BooleanField(default=0)
    title = models.CharField(max_length=191, null=True)

    class Meta:
        managed = False

## Наследоваание классов (возможность не писать лишний код)
class options(models.Model): # Этот содержит поля что нужны для рахных видов покупок
    enable = models.BooleanField(default=0)
    position = models.IntegerField(null=True)
    title = models.CharField(max_length=191, null=True)
    image = models.CharField(max_length=191, null=True)
    price = models.IntegerField(null=True)
    present = models.BooleanField(default=0)

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.present = 1
        super().save(self, *args, **kwargs)

    class Meta:
        abstract = True; # abstract деалет данную модель как болванку для копирование. Он не будет появляться с базе

class buy_clothe(options): # наследую чтоб не писать лишный код
    size = models.IntegerField(null=True)
    brand = models.CharField(max_length=191, null=True)

class buy_food(options): # наследую чтоб не писать лишный код
    ingredients = models.CharField(max_length=191, null=True)

# Наследование методов
class CommonInfo(models.Model):

    title = models.CharField(max_length=191, null=True)

    class Meta:
        abstract = True
        ordering = ['title'] # Означает отдать сортированно при выборке

class Student(CommonInfo):
    pass
    #class Meta(CommonInfo.Meta): # Вот так мы унаследуем Meta от CommonInfo расширяя его и этот модель станет abstract
    #    db_table = 'student_info'

# Многостволовое наследование
class Place(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=80, blank=True)
    enable = models.BooleanField(default=0)

class Restaurant(Place): # Здесь создается спец поле в таблице указывающей связь Один ко Многим - place_ptr_id
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# Meta Proxy - это свойтсва не позволит моделю сделать миграцию, произойдет обычное наследовние методов, в следсвий мы может через эту модель вызывать методы моделя Place и дополнительными методами типа has_enable
class othePlace(Place):

    class Meta:
        proxy = True

    def has_enable(self):
        if self.enable == 1:
            return True
        else:
            return False

#verbose_name - В Dajngo мы может полю дать его полное описание (models.CharField('здесь будет имя человека', max_length=50, blank=True)),
#елси на дать берет имя переменной. Если используется  ForeignKey, ManyToManyField и OneToOneField, то описание пишем в verbose_name

## Валидаторы
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class validate_table (models.Model):
    enable = models.BooleanField(default=0)
    position = models.IntegerField(null=True)
    title = models.CharField(max_length=191, null=True)
    even_field = models.IntegerField(null=True, validators=[validate_even])

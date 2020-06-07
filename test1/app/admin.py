from django.contrib import admin
from app.models import goods, news
from app.forms import MyAdminForm

# Register your models here.
##---- Регистрация моделей ---##
#--## 1 вариант
#class GoodsAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(goods, GoodsAdmin)

##--## 2 вариант. Через декоратор
#@admin.register(goods, news)
#class DeafaultAdmin(admin.ModelAdmin):
#    pass

def set_link(modeladmin, request, queryset):
    queryset.update(status='l') # Сделает status равным link для выбранного поле
set_link.short_description = "Сделать ссылкой"

class GoodsAdmin(admin.ModelAdmin):
    actions = [set_link] # Так мы добавим дополнительные действий в админку. По умолчанию в списке есть одно действие - удалить. Мы его расширим.
    date_hierarchy = 'created' # Делаем сортировку по полям DateField или DateTimeField
    empty_value_display = 'Пустой' # В списке в пустые или null поле запишается это значени - Пустой
    #exclude = ('other_position', 'bind', 'decimal', 'float', 'ip', 'age', 'status') # исключить на ADD|EDIT # есть fields которая наборот указывает какие поля показать
    list_display = ['title', 'status', 'created', 'ip'] # Показать в списке
    #fields = ('enable', ('title', 'url'), ('email', 'age'), 'text', 'file') # Показываем какие поля надо редактировать
    fieldsets = (
        ('Основные', {
            'fields': ('enable', ('title', 'url'), ('email', 'age'), 'file'),
            'classes': ('wide', 'dummy'),
            'description' : 'Основные важные поля для заполнение!'
        }),
        ('Текста', {
            'fields': ('text',),
            'description' : 'Внутренный текст товара'
        }),
        ('Дополнительно', {
            'fields': (('ip', 'float'), ('decimal', 'status')),
            'description' : 'Дополнительные поля. Заполнение не обязательно'
        })
    ) # fieldsets настраиваемые поля с описанием и своими стилями
    form = MyAdminForm # Меняем поведение формы что идет по умолчанию

admin.site.register(goods, GoodsAdmin)
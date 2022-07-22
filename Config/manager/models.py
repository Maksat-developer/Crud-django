from django.utils.timezone import now as timezonenow
from django.db import models


class Categories(models.Model):
    category_name = models.CharField(verbose_name="Наименование Категории:", max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория:"
        verbose_name_plural = "Категории:"


class ProductSize(models.Model):
    size = models.IntegerField(verbose_name="Размер продукта:", default=35, help_text="Размеры начинаються с 35р")

    class Meta:
        verbose_name = "Размер цифрами"
        verbose_name_plural = "Размеры цифрами"


class ProductSizeXML(models.Model):
    size = models.CharField(verbose_name="Размер продукта:", max_length=3, help_text="Введите в верхнем регистре: ABC...")

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Размер буква"
        verbose_name_plural = "Размеры буквами"


class ProductStatus(models.Model):
    status = models.CharField(verbose_name="Статус продукта:", max_length=50, help_text="Есть в наличии или нет?")

    def __str__(self):
        return self.status
 
    class Meta:
        verbose_name = "Статус продукта:"
        verbose_name_plural = "Статус продуктов:"

        
class Product(models.Model):
  
    title = models.CharField(verbose_name="Заглавление:", max_length=100)
    model = models.CharField(verbose_name="Модель продукта:", max_length=50)
    price = models.DecimalField(verbose_name="Стоимость продукта:", max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name="Изображение продукта:", upload_to="M_Product/%Y/%m/%d")
    create_time = models.DateTimeField (verbose_name = 'create time', default=timezonenow)
    update_time = models.DateTimeField (auto_now = True, verbose_name= 'время обновления')


    status_product = models.ManyToManyField('ProductStatus', verbose_name="Статус продукта:")
    size = models.ManyToManyField('ProductSize',verbose_name="Размер продукта:")
    product_size = models.ManyToManyField('ProductSizeXML', verbose_name="Размеры одежд:")
    category = models.ForeignKey('Categories', verbose_name="Категория:", on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Продукт:"
        verbose_name_plural = "Продукты:"




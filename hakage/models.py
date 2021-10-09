from django.db import models
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def get_all_product(self):
        return Category.objects.all()

class products(models.Model):
    photo=models.ImageField(upload_to='hacaton5/media', null=True, blank=True)
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=1000)
    # data =models.CharField('data',max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # def str(self):
        # return self.name
    def __str__(self):
        return self.name
    # def register(self): #сохранить данные
        # self.save()

    def get_all_categories(self):
        return Category.objects.all()


    def get_all_product(self):
        return products.objects.all()
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Feature(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Type(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(max_length=15)
    discount_price = models.FloatField(max_length=15)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    feature_id = models.ManyToManyField(Feature)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    image1 = models.ImageField()
    image2 = models.ImageField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact(BaseModel):
    ContactChoice = (
        ("buy", "Buy"),
        ("sell", "Sell"),
        ("promotion", "Promotion"),
        ("order", "Order")
    )
    name = models.CharField(max_length=28)
    phone = PhoneNumberField(region="UZ")
    reason = models.CharField(max_length=34, choices=ContactChoice)
    subject = models.TextField()

    def __str__(self):
        return self.name


class About(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.title

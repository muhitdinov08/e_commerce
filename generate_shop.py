import random
import requests
# from django.contrib.sites import requests
from faker import Faker

faker = Faker()


def fake_test():
    # print(faker.date())
    # print(faker.cryptocurrency_name())
    # print(faker.type())
    # print(faker.user_name())
    # print(random.choice(Category.objects.all()))
    # print(random.choice(Type.objects.all()))
    # print(faker.company())
    # print(faker.localized_ean8()[:2])
    # print(faker.iban()[:4])
    print(faker.paragraph())


def main():
    # ---------Category--------
    # for i in range(0, 6):
    #     category_names = ["Child-clothes", "Saree", "Footwear", "Gift", "Electronics", "Toys"]
    #     Category.objects.create(name=category_names[i])
    # print(Category.objects.all())
    #
    #
    #
    #
    #
    # -----------Feature-----------
    #
    # for i in range(8):
    #     feature_name = faker.cryptocurrency_name()
    #     Feature.objects.create(name=feature_name)
    # print(Feature.objects.all())
    #
    #
    #
    #
    #
    # --------Type--------
    #
    # for i in range(8):
    #     type_name = "Book_shelf"
    #     Type.objects.create(name=type_name)
    # print(Type.objects.all())
    #
    #
    #
    #
    #
    # ----------Product------------
    #
    # for i in range(50):
    #     name = faker.user_name()
    #     category = random.choice(Category.objects.all())
    #     price = random.uniform(1, 1000)
    #     discount_price = price / 2
    #     rating = random.randint(1, 5)
    #     product_type = Type.objects.get(id=random.randint(1, 5))
    #     brand = faker.company()
    #     model = faker.iban()[:4]
    #     description = faker.paragraph()
    #     product = Product.objects.create(name=name, category=category, price=price,
    #                                      discount_price=discount_price, rating=rating, type=product_type,
    #                                      brand=brand, model=model,
    #                                      description=description)
    # for _ in range(random.randint(1, 4)):
    #     feature_id = Feature.objects.get(id=random.randint(1, 8))
    #     product.feature_id.add(feature_id)
    # product.save()
    # print(Product.objects.all())
    #
    #
    #
    # -----------Images---------------
    #
    # for i in range(100):
    #     url = "https://picsum.photos/600"
    #     data = requests.get(url).content
    #     # os.chdir("templates/images")
    #     with open(f"templates/images/{i}.jpg", "wb") as f:
    #         f.write(data)
    #         f.close()
    # for i in range(50):
    #     product_id = Product.objects.get(id=random.randint(1, 50))
    #     with open(f'templates/images/{random.randint(1, 100)}.jpg', 'rb') as f:
    #         image1 = f.readable()
    #     with open(f'templates/images/{random.randint(1, 100)}.jpg', 'rb') as f:
    #         image2 = f.readable()
    #     ProductImage.objects.create(product_id=product_id, image1=image1, image2=image2)
    #
    # print(ProductImage.objects.all())

    pass


if __name__ == '__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce.settings")
    application = get_wsgi_application()

    from shop.models import Category, Type, Product, Feature, ProductImage

    # fake_test()
    main()

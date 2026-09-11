from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Предварительное удаление и добавление продуктов для тестов.'

    def handle(self, *args, **options):

        all_category = Category.objects.all()
        all_category.delete()
        all_product = Product.objects.all()
        all_product.delete()

        category, _ = Category.objects.get_or_create(name='Мясные изделия')

        products = [{
                "name": "Колбаса \"Вязанка\"",
                "description": "Это продукт под названием - колбаса \"Вязанка\"",
                "category": category,
                "buying_price": "95.00"
        },
        {
                "name": "Колбаса \"Красная\"",
                "description": "Это продукт под названием - колбаса \"Красная\"",
                "category": category,
                "buying_price": "78.00"
            },
        {
                "name": "Колбаса \"Дорогая\"",
                "description": "Это продукт под названием - колбаса \"Дорогая\"",
                "category": category,
                "buying_price": "65.00"
        },
        {
                "name": "Сосиски",
                "description": "Это продукт под названием - сосиски \"Классические\"",
                "category": category,
                "buying_price": "42.00"
        },
        {
                "name": "Сардельки",
                "description": "Это продукт под названием - сардельки",
                "category": category,
                "buying_price": "120.00"
        },
                   ]

        for product_data in products:
            product, create = Product.objects.get_or_create(**product_data)
            if create:
                self.stdout.write(self.style.SUCCESS(f'Объект: {product} успешно добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Объект: {product} уже в наличии'))
                # Если я правильно понял условия задания, то мне необходимо сделать так, чтобы удалялись
                # данные перед добавлением новых продуктов, поэтому второе условие никогда не выполнится.
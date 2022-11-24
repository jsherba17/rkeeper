import factory
class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cafe.Food'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('title','price')

    title = 'Ice cream'
    price = 200

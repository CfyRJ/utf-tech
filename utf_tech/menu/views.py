from rest_framework import generics

from .models import FoodCategory, Food
from .serializers import FoodListSerializer

from django.db.models import Prefetch


class FoodList(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        categories_publish_foods = FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct()

        annotated_categories = categories_publish_foods.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )

        return annotated_categories

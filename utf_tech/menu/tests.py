import json
from django.test import TestCase, Client
from .models import FoodCategory, Food


class InitialTests(TestCase):

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.publish_all = FoodCategory.objects.create(name_ru='publish_all')
        cls.publish_part = FoodCategory.objects.create(name_ru='publish_part')
        cls.not_publish = FoodCategory.objects.create(name_ru='not_publish')
        cls.empty = FoodCategory.objects.create(name_ru='empty')

        cls.publ_1 = Food.objects.create(category=cls.publish_all,
                                         code=1,
                                         name_ru='publ_1',
                                         cost=1)
        cls.publ_2 = Food.objects.create(category=cls.publish_all,
                                         code=1,
                                         name_ru='publ_2',
                                         cost=1)
        cls.publ_3 = Food.objects.create(category=cls.publish_all,
                                         code=1,
                                         name_ru='publ_3',
                                         cost=1)
        
        cls.part_1 = Food.objects.create(category=cls.publish_part,
                                         code=2,
                                         name_ru='part_1',
                                         cost=2,
                                         is_publish = True)
        cls.part_2 = Food.objects.create(category=cls.publish_part,
                                         code=2,
                                         name_ru='part_2',
                                         cost=2,
                                         is_publish = False)

        cls.not_publ = Food.objects.create(category=cls.not_publish,
                                         code=3,
                                         name_ru='not_publ',
                                         cost=3,
                                         is_publish = False)

    def test_json(self):
        response = self.client.get('/api/v1/foods/')

        status_code = response.status_code
        self.assertEqual(status_code, 200)


        with open('tests/check_date/check_date.json', 'r') as file:
            expected_data = json.load(file)
        expected_data_bytes = json.dumps(expected_data, separators=(',', ':')).encode('utf-8')

        self.assertEqual(response.content, expected_data_bytes)

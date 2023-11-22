# import os
# import django
# from faker import Faker
# from settings import BASE_DIR
# from mysite.myapp.models import Person
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# django.setup()
#
# fake = Faker()
#
# def populate_data(n=10):
#     for _ in range(n):
#         person = Person(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             email=fake.email(),
#         )
#         person.save()
#
# if __name__ == "__main__":
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     os.chdir(script_dir)  # Измените текущий рабочий каталог на тот, где находится скрипт
#     try:
#         populate_data()
#         print("Data populated successfully.")
#     except Exception as e:
#         print(f"Error populating data: {e}")
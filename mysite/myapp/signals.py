# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django_telegram.models import Message
# from mysite.myapp.models import Person
# from telegram import Bot
#
# @receiver(post_save, sender=Person)
# def handle_person_save(sender, instance, created, **kwargs):
#     if created:
#         action = "created"
#     else:
#         action = "updated"
#
#     message = f"Person {action}: {instance}"
#
#     # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = 'https://t.me/+eMw1h5TlCPljOTBi'
#     bot.send_message(chat_id=chat_id, text=message)
#
#     # Также, если вы хотите сохранять сообщения в базу данных Django
#     Message.objects.create(text=message)
#
# @receiver(post_delete, sender=Person)
# def handle_person_delete(sender, instance, **kwargs):
#     message = f"Person deleted: {instance}"
#
#     # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = 'https://t.me/+eMw1h5TlCPljOTBi'
#     bot.send_message(chat_id=chat_id, text=message)
#
#     # Также, если вы хотите сохранять сообщения в базу данных Django
#     Message.objects.create(text=message)
#
#
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from myapp.models import Person
# from telegram import Bot
#
# @receiver(post_save, sender=Person)
# def handle_person_save(sender, instance, created, **kwargs):
#     if created:
#         action = "created"
#     else:
#         action = "updated"
#
#     message = f"Person {action}: {instance}"
#
#
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = '+eMw1h5TlCPljOTBi'
#     bot.send_message(chat_id=chat_id, text=message)
#
# @receiver(post_delete, sender=Person)
# def handle_person_delete(sender, instance, **kwargs):
#     message = f"Person deleted: {instance}"
#
#
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = '+eMw1h5TlCPljOTBi'
#     bot.send_message(chat_id=chat_id, text=message)


#
#
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import Person
# from telegram import Bot
#
# @receiver(post_save, sender=Person)
# async def handle_person_save(sender, instance, created, **kwargs):
#     if created:
#         action = "created"
#     else:
#         action = "updated"
#
#     message = f"Person {action}: {instance}"
#
#     # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = '+eMw1h5TlCPljOTBi'
#     await bot.send_message(chat_id=chat_id, text=message)
#
# @receiver(post_delete, sender=Person)
# async def handle_person_delete(sender, instance, **kwargs):
#     message = f"Person deleted: {instance}"
#
#     # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
#     bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
#     chat_id = '+eMw1h5TlCPljOTBi'
#     await bot.send_message(chat_id=chat_id, text=message)


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Person
from telegram import Bot

@receiver(post_save, sender=Person)
async def handle_person_save(sender, instance, created, **kwargs):
    if created:
        action = "created"
    else:
        action = "updated"

    message = f"Person {action}: {instance}"

    # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
    bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
    chat_id = '+eMw1h5TlCPljOTBi'
    await bot.send_message(chat_id=chat_id, text=message)

@receiver(post_delete, sender=Person)
async def handle_person_delete(sender, instance, **kwargs):
    message = f"Person deleted: {instance}"

    # Замените 'YOUR_BOT_TOKEN' и 'YOUR_CHAT_ID' на реальные значения
    bot = Bot(token='6841993749:AAG8XB3bgtMVootua7Wc6Ft5DhbTkf5hHZY')
    chat_id = '+eMw1h5TlCPljOTBi'
    await bot.send_message(chat_id=chat_id, text=message)

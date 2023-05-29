from __future__ import annotations

from typing import Union, Optional, Tuple

from django.db import models
from django.db.models import QuerySet, Manager
from telegram import Update
from telegram.ext import CallbackContext

# from beauty_salon.tgbot.handlers.utils.info import extract_user_data_from_update
# from beauty_salon.utils.models import CreateUpdateTracker, nb, CreateTracker, GetOrNoneManager

from functools import wraps
from typing import Dict, Callable

import telegram
from telegram import Update

# from beauty_salon.tgbot.main import bot


class Clients(models.Model):
    td_id = models.PositiveIntegerField(
        verbose_name='telegram ID клиента',
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )
    client_phone_number = models.TextField(
        verbose_name='Номер телефона клиента',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    @classmethod
    def get_user_and_created(cls, update: Update, context: CallbackContext) -> Tuple[Clients, bool]:
        """ python-telegram-bot's Update, Context --> User instance """
        data = extract_user_data_from_update(update)
        u, created = cls.objects.update_or_create(user_id=data["user_id"], defaults=data)

        if created:
            # Save deep_link to User model
            if context is not None and context.args is not None and len(context.args) > 0:
                payload = context.args[0]
                if str(payload).strip() != str(data["user_id"]).strip():  # you can't invite yourself
                    u.deep_link = payload
                    u.save()

        return u, created


class Salon(models.Model):
    name = models.TextField(
        verbose_name='Название салона',
    )
    adress = models.TextField(
        verbose_name='Адрес салона',
    )
    salon_phone_number = models.TextField(
        verbose_name='Номер телефона салона',
    )
    master = models.TextField(
        verbose_name='Имя мастера',
    )
    service = models.TextField(
        verbose_name='Наименование услуги',
    )
    price = models.IntegerField(
        verbose_name='Цена услуги',
    )
    visit_time = models.TextField(
        verbose_name='Время визита',
    )

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    name = models.TextField(
        verbose_name='Имя мастера',
    )
    working_hours = models.TextField(
        verbose_name='Расписание мастера',
    )

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


def extract_user_data_from_update(update: Update) -> Dict:
    """ python-telegram-bot's Update instance --> User info """
    user = update.effective_user.to_dict()

    return dict(
        user_id=user["id"],
        is_blocked_bot=False,
        **{
            k: user[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user and user[k] is not None
        },
    )

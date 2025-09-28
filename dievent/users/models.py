from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Клиент'),
        ('manager', 'Менеджер'),
        ('event_planner', 'Организатор мероприятий'),
        ('admin', 'Администратор'),
    ]
    
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='client',
        verbose_name="Роль"
    )
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name="Телефон"
    )
    company = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="Компания"
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Аватар"
    )
    bio = models.TextField(
        blank=True,
        verbose_name="О себе"
    )
    telegram_messenger = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Telegram"
    )
    whatsapp_messenger = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="WhatsApp"
    )
    max_messenger = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Max"
    )
    email_verified = models.BooleanField(
        default=False,
        verbose_name="Email подтвержден"
    )
    phone_verified = models.BooleanField(
        default=False,
        verbose_name="Телефон подтвержден"
    )
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_manager(self):
        return self.role in ['manager', 'admin', 'event_planner']

    @property
    def is_client(self):
        return self.role == 'client'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

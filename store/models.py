from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import EmployeeManager


class Employee(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, verbose_name="Имя")
    phone = models.CharField(max_length=150, unique=True, verbose_name="Номер телефона")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name',]

    objects = EmployeeManager()

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'



class TradingPoint(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='trading_points', verbose_name="Работник")

    def __str__(self):
        return f'{self.name} - {self.employee}'

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата посещения")
    trading_point = models.ForeignKey(TradingPoint, on_delete=models.CASCADE, related_name='visits', verbose_name="Торговая точка")
    latitude = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Широта")
    logitude = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Долгота")
    
    def __str__(self):
        return f'{self.date} - {self.trading_point}'

    class Meta:
        verbose_name = 'Посещения'
        verbose_name_plural = 'Посещении'
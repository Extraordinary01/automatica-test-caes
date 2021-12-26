from django.contrib.auth.models import BaseUserManager


class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, phone, password=None, **extra_fields):

        if not phone:
            raise ValueError("Поле для номера телефона должно быть заполнено")
        elif not phone.isdecimal():
            raise ValueError("Поле для номера телефона должен содержать только числа")
        
        if not name:
            raise ValueError("Поле с именем должно быть заполнено")

        # phone = self.clean(phone)
        user = self.model(name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(name, phone, password, **extra_fields)
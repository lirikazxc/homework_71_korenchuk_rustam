from django.contrib.auth.base_user import BaseUserManager
from django.core.files.base import ContentFile


class UserManager(BaseUserManager):
    def create_user(self, username, password, gender, **extra_fields):
        if not username:
            raise ValueError('Enter an email address')
        user = self.model(username=username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password, gender=0)
        with open('webapp/static/images/admin_avatars/smile.png', 'rb') as avatar_file:
            user.avatar.save('default_avatar.png', ContentFile(avatar_file.read()))
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

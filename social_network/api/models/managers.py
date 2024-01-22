from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_account(self, username, password):
        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_account(
            username=username, password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

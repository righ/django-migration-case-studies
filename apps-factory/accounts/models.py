import os
import functools
import uuid
import unicodedata

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


def make_path_factory(prefix):
    def wrapper(f):
        @functools.wraps(f)
        def unique_path(instance, filename):
            path = [prefix.strip('/')]
            path += [instance.id.hex[i:i+4] for i in range(0, 32, 4)]
            path += [unicodedata.normalize('NFC', filename)]
            return os.path.join(*path)
        return unique_path
    return wrapper


@make_path_factory('user')
def make_user_path():
    """ユーザIDを元に添付ファイルを保存するパスを生成する"""


@make_path_factory('group')
def make_group_path():
    """グループIDを元に添付ファイルを保存するパスを生成する"""


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    file = models.FileField(upload_to=make_user_path)


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to=make_group_path)


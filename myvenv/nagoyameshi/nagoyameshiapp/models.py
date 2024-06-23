from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name        = models.CharField(verbose_name="名前", max_length=15)
    created_at  = models.DateTimeField(verbose_name="作成日時", default=timezone.now)
    updated_at  = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    category    = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    name        = models.CharField(verbose_name="名前", max_length=50)
    image       = models.ImageField(verbose_name="画像", upload_to="nagoyameshiapp/restaurant/image/",blank=True,null=True)
    description = models.CharField(verbose_name="店舗説明", max_length=500)
    start_at    = models.TimeField(verbose_name="営業開始時間", default=timezone.now)
    end_at      = models.TimeField(verbose_name="営業終了時間", default=timezone.now)

    def __str__(self):
        return self.name
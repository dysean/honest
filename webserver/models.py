from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User')
    # destination_account = models.ForeignKey('accounts.Account')
    amount = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def execute(self):
        self.save()



from django.db import models


class User(models.Model):
    bc_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=False)
    storeusers = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.bc_id


class StoreUser(models.Model):
    store_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.store_id


class Store(models.Model):
    store_hash = models.CharField(max_length=100, null=True, blank=True)
    access_token = models.CharField(max_length=100, null=True, blank=True)
    scope = models.CharField(max_length=100, null=True, blank=True)
    admin_storeuser_id = models.IntegerField(null=True, blank=True)
    storeusers = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.store_hash

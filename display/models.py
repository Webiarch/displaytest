from django.db import models


class Store(models.Model):
    store_hash = models.CharField(max_length=1000, null=True, blank=True)
    access_token = models.CharField(max_length=1000, null=True, blank=True)
    scope = models.TextField(max_length=255, null=True, blank=True)
    admin_storeuser_id = models.IntegerField(null=True, blank=True, default=True)
    storeusers = models.ManyToManyField('StoreUser',)

    def __str__(self):
        return self.store_hash


class User(models.Model):
    bc_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=False)
    storeusers = models.ManyToManyField('StoreUser',)

    def __str__(self):
        return self.email


class StoreUser(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.store_id)

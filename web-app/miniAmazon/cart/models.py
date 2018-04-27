from django.db import models
from shop.models import Good

class Cart(models.Model):
    cart_id = models.CharField(max_length=120, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.amount

    def __str__(self):
        return self.good


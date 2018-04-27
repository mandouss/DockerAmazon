from django.db import models

from goods.models import Good

class CartItem(models.Model):
    good = models.ForeignKey(Good, verbose_name='good_item')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')

    class Meta:
        verbose_name = 'cart_item'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

class Cart(object):
    def __init__(self):
        self.items = []

    def add(self, good):
        for item in self.items:
            if item.good.id == good.id:
                item.quantity +=1
                return
            else:
                self.items.append(CartItem(good=good, quantity=1))

# from django.conf import settings
# from django.db import models

# from django.db.models.signals import pre_save, post_save, m2m_changed

# from goods.models import Good

# User = settings.AUTH_USER_MODEL

# class CartManager(models.Manager):

    # def new_or_get(self, request):
        # cart_id = request.session.get("cart_id", None)
        # qs = self.get_queryset().filter(id=cart_id)
        # if qs.count() == 1:
            # new_obj = False
            # cart_obj = qs.first()
            # if request.user.is_authenticated() and cart_obj.user is None:
                # cart_obj_user = request.user
                # cart_obj.save()
        # else:
            # cart_obj = Cart.objects.new(user=request.user)
            # new_obj = True
            # request.session['cart_id'] = cart_obj.id
        # return cart_obj, new_obj


    # def new(self, user=None):
        # user_obj = None
        # if user is not None:
            # if user.is_authenticated():
                # user_obj = user
        # return self.model.objects.create(user=user_obj)


# class Cart(models.Model):
    # user      = models.ForeignKey(User, null=True, blank=True)
    # goods     = models.ManyToManyField(Good, blank=True)
    # updated   = models.DateTimeField(auto_now=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    # objects = CartManager()
    
    # def __str__(self):
        # return str(self.id)


# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    # if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        # goods = instance.goods.all()
        # instance.save()

# m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.goods.through)

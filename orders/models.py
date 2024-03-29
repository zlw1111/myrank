from django.db import models
from rank.models import Product
class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    calculate = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product,
                    related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return '{}'.format(self.id)
        
    def get_cost(self):
        return self.price * self.quantity


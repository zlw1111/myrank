from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Restaurant(models.Model):
	 name = models.CharField(max_length=200,
							      db_index=True)
	 slug = models.SlugField(max_length=200,
	                        db_index=True,
							       unique=True)
	 class Meta:
		  ordering = ('name',)
		  verbose_name = 'restaurant'
		  verbose_name_plural = 'restaurants'
 
	 def __str__(self):
		  return self.name
	 def get_absolute_url(self):
		  return reverse('rank:product_list_by_restaurant',
                        args=[self.slug])


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, 
                                 related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    grade = models.FloatField(default=0.00)
    myrank = models.FloatField(default=0.00)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('rank:product_detail',
            args=[self.id, self.slug])


class Myself(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    psw = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
  
    class Meta:
        ordering = ('name',)
        verbose_name = 'myself'
        verbose_name_plural = 'myselfs'
 
    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product,related_name='comments')
    myself = models.ForeignKey(Myself,related_name='comments')
    slug = models.SlugField(max_length=200, db_index=True)
    des = models.TextField(blank=True)
    score = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
   
    #def __str__(self):
     #   return self.name
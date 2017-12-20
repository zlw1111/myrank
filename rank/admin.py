from django.contrib import admin

# Register your models here.
from .models import Restaurant, Product,Myself,Comment



class CommentInline(admin.TabularInline):
    model=Comment
class ProductAdmin(admin.ModelAdmin):
    inlines=[CommentInline]
    list_display = ['name', 'slug', 'price', 'stock', 
                    'available', 'created', 'updated','grade','myrank']
    list_filter = ['available', 'created', 'updated','grade','myrank']
    list_editable = ['price', 'stock', 'available','grade','myrank']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['des', 'slug', 'score',  
                     'created', 'updated']
    list_filter = ['created', 'updated','score']
    list_editable = ['score']
admin.site.register(Comment, CommentAdmin)
class ProductInline(admin.TabularInline):
    model=Product

class MyselfAdmin(admin.ModelAdmin):
    inlines=[CommentInline]
    list_display = ['name', 'psw','slug', 'image', 'created', 
                    'updated', 'balance']
    list_filter = ['name', 'created', 'updated','balance']
    list_editable = ['balance']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Myself, MyselfAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    inlines=[ProductInline]
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Restaurant, RestaurantAdmin)

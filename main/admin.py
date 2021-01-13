from django.contrib import admin
from main.models import mail_verification,Person,Product,Seller
from checkout.models import Cart
admin.site.register(mail_verification)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Cart)
# Register your models here.

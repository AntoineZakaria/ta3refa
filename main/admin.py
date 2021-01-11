from django.contrib import admin
from main.models import mail_verification,Person,Product,Seller
admin.site.register(mail_verification)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Seller)
# Register your models here.

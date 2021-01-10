from django.contrib import admin
from main.models import mail_verification,Person,Product
admin.site.register(mail_verification)
admin.site.register(Person)
admin.site.register(Product)
# Register your models here.

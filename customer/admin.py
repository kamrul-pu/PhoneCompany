from django.contrib import admin
from customer.models import *
# Register your models here.


admin.site.register(Company)
admin.site.register(PhoneNumber)
admin.site.register(Customer)
admin.site.register(CustomerNumber)
admin.site.register(Plan)
admin.site.register(CustomerActivatedPlan)
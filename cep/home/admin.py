from django.contrib import admin
from .models import Buyer, Customer, Employee, Inventory, Manager, Manufacturer, Payment, Renter, Salesperson, Servicerecord, Supplier, Technician, Vehicle

# Register your models here.

admin.site.register(Buyer)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Manager)
admin.site.register(Manufacturer)
admin.site.register(Payment)
admin.site.register(Renter)
admin.site.register(Salesperson)
admin.site.register(Servicerecord)
admin.site.register(Supplier)
admin.site.register(Technician)
admin.site.register(Vehicle)

from django.db import models

# Create your models here.

class Buyer(models.Model):
    buyerid = models.IntegerField(db_column='BuyerID', primary_key=True)  # Field name made lowercase.
    custid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustID', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='VehicleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buyer'


class Customer(models.Model):
    custid = models.IntegerField(db_column='CustID', primary_key=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CustName', max_length=45)  # Field name made lowercase.
    custcontact = models.IntegerField(db_column='CustContact')  # Field name made lowercase.
    custcity = models.CharField(db_column='CustCity', max_length=20)  # Field name made lowercase.
    custhouse = models.CharField(db_column='CustHouse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    custdob = models.DateField(db_column='CustDOB')  # Field name made lowercase.
    custemail = models.CharField(db_column='CustEmail', max_length=30)  # Field name made lowercase.
    custgender = models.CharField(db_column='CustGender', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

class Employee(models.Model):
    empid = models.IntegerField(db_column='EmpID', primary_key=True)  # Field name made lowercase.
    empname = models.CharField(db_column='EmpName', max_length=45)  # Field name made lowercase.
    empemail = models.CharField(db_column='EmpEmail', max_length=30)  # Field name made lowercase.
    empgender = models.CharField(db_column='EmpGender', max_length=1)  # Field name made lowercase.
    empcity = models.CharField(db_column='EmpCity', max_length=20)  # Field name made lowercase.
    emphouseno = models.CharField(db_column='EmpHouseNo', max_length=45)  # Field name made lowercase.
    empdob = models.DateField(db_column='EmpDOB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'
        db_table_comment = '\t\t\t\t\t\t'


class Inventory(models.Model):
    inventid = models.IntegerField(db_column='InventID', primary_key=True)  # Field name made lowercase.
    availability = models.CharField(db_column='Availability', max_length=255, blank=True, null=True)  # Field name made lowercase.
    noofvehicles = models.IntegerField(db_column='NoOfVehicles', blank=True, null=True)  # Field name made lowercase.
    spid = models.ForeignKey('Salesperson', models.DO_NOTHING, db_column='SPID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'


class Manager(models.Model):
    mgrid = models.IntegerField(db_column='MgrID', primary_key=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Manufacturer(models.Model):
    manid = models.IntegerField(db_column='ManID', primary_key=True)  # Field name made lowercase.
    manname = models.CharField(db_column='ManName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mancity = models.CharField(db_column='ManCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mancontact = models.CharField(db_column='ManContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manemail = models.CharField(db_column='ManEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manufacturer'

class Payment(models.Model):
    payid = models.IntegerField(db_column='PayID', primary_key=True)  # Field name made lowercase.
    dateofpayment = models.DateField(db_column='DateOfPayment', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Renter(models.Model):
    renterid = models.IntegerField(db_column='RenterID', primary_key=True)  # Field name made lowercase.
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustID', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='VehicleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'renter'


class Salesperson(models.Model):
    spid = models.IntegerField(db_column='SPID', primary_key=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesperson'


class Servicerecord(models.Model):
    service_id = models.IntegerField(db_column='Service_ID', primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    techid = models.ForeignKey('Technician', models.DO_NOTHING, db_column='TechID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicerecord'

class Supplier(models.Model):
    supid = models.IntegerField(db_column='SupID', primary_key=True)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supcity = models.CharField(db_column='SupCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supcountry = models.CharField(db_column='SupCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supcontact = models.CharField(db_column='SupContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supemail = models.CharField(db_column='SupEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sparepartname = models.CharField(db_column='SparePartName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class Technician(models.Model):
    techid = models.IntegerField(db_column='TechID', primary_key=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'technician'


class Vehicle(models.Model):
    vehicleid = models.IntegerField(db_column='VehicleID', primary_key=True)  # Field name made lowercase.
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='Manufacturer_ID', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    mileage = models.IntegerField(db_column='Mileage', blank=True, null=True)  # Field name made lowercase.
    fueltype = models.CharField(db_column='FuelType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'

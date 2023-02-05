from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class PhoneNumber(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    number = models.CharField(max_length=20,unique=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}"

class Customer(models.Model):
    primary_phone = models.CharField(max_length=20,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    registraton_date = models.DateTimeField(auto_now_add=True)
    #Other customer attributes can be added if required
    # plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Customer owns phone numbers
class CustomerNumber(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    phone_number = models.ForeignKey(PhoneNumber,on_delete=models.SET_NULL,null=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone_number}"

class Plan(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"

class CustomerActivatedPlan(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
    months = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
        
    )

    payment_month = models.CharField(choices=months,max_length=40)
    payment_status = models.BooleanField(default=False)
    activation_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return f"{self.customer} "


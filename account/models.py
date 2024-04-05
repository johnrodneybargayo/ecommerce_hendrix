from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# STRIPE MODEL
class StripeModel(models.Model):
    email = models.EmailField(null=True, blank=True)
    name_on_card = models.CharField(max_length=200, null=True, blank=True)
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    card_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    exp_month = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{0,9}$')], null=True, blank=True)
    exp_year = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{0,9}$')], null=True, blank=True)
    card_id = models.TextField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, related_name="stripemodel", on_delete=models.CASCADE, null=True, blank=True)
    address_city = models.CharField(max_length=120, null=True, blank=True)
    address_country = models.CharField(max_length=120, null=True, blank=True)
    address_state = models.CharField(max_length=120, null=True, blank=True)
    address_zip = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{0,9}$')], null=True, blank=True)

    def __str__(self):
        return self.email


class BillingAddress(models.Model):
    firstname = models.CharField(max_length=100, null=False, blank=False) 
    lastname = models.CharField(max_length=100, null=False, blank=False)  
    user = models.ForeignKey(User, related_name="billing_addresses", on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')], null=False, blank=False)
    zip_code = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{0,9}$')], null=False, blank=False) 
    house_no = models.CharField(max_length=300, null=False, blank=False) 
    apartment = models.CharField(max_length=100, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=120, null=False, blank=False)  
    city = models.CharField(max_length=120, null=False, blank=False)
    state = models.CharField(max_length=120, null=False, blank=False)
    country = models.CharField(max_length=120, null=False, blank=False)  
    email = models.EmailField(max_length=254, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"



class OrderModel(models.Model):
    name = models.CharField(max_length=120)
    ordered_item = models.CharField(max_length=200, null=True, blank=True, default="Not Set")
    card_number = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    paid_status = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
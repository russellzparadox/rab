from django.db import models

# Create your models here.

from django.db import models
import phonenumbers
from rest_framework.exceptions import ValidationError


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        try:
            phone = phonenumbers.parse(value, "IR")
            if not phonenumbers.is_valid_number(phone):
                raise ValidationError("Invalid phone number format.")
        except phonenumbers.NumberParseException:
            raise ValidationError("Invalid phone number.")

    def get_prep_value(self, value):
        return value


class Company(models.Model):
    id_number = models.IntegerField(primary_key=True)
    date_start = models.DateField()


class Clients(models.Model):
    na_code = models.CharField(max_length=10, primary_key=True)


class Interview(models.Model):
    id_number = models.IntegerField()
    na_code = models.CharField(max_length=10)
    date_interview = models.DateField()

    class Meta:
        unique_together = ('date_interview', 'id_number', 'na_code')

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.IntegerField()
    personal_code = models.IntegerField(unique=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    skill = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.FloatField()
    picture_pro = models.BinaryField()
    samat = models.CharField(max_length=50)
    end_madrak = models.CharField(max_length=50)
    shba = models.CharField(max_length=30)
    date_start = models.DateField()
    date_accept = models.DateField()
    number_accept = models.IntegerField()
    na_code_accept = models.CharField(max_length=10)

    date_accept_interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='date_accept_interview')
    number_accept_interview = models.ForeignKey(Interview, on_delete=models.CASCADE,
                                                related_name='number_accept_interview')
    na_code_accept_interview = models.ForeignKey(Interview, on_delete=models.CASCADE,
                                                 related_name='na_code_accept_interview')


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name_de = models.CharField(max_length=25)
    id_manag = models.IntegerField()
    date_start = models.DateField()
    date_start_manag = models.DateField()

    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)


class WorksOn(models.Model):
    id_department = models.IntegerField(primary_key=True)
    id_employee = models.IntegerField(unique=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Driver(models.Model):
    ph_number = PhoneNumberField(primary_key=True)
    identifi_code = models.IntegerField(unique=True)
    age = models.IntegerField()
    sc_cart_na = models.BinaryField()
    sc_cart_g = models.BinaryField()
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    sex = models.CharField(max_length=5)
    picture_pro = models.BinaryField()
    na_code = models.CharField(max_length=10, unique=True)
    shba = models.CharField(max_length=30)
    welt = models.FloatField()
    status_d = models.CharField(max_length=15)
    mileage_per_month = models.FloatField()
    id_employ = models.IntegerField()
    date_certificate = models.DateField()
    date_acc_final = models.DateField()
    date_acc_bad_luck = models.DateField()
    identifi_code_super = models.IntegerField()
    l_x = models.FloatField()
    l_y = models.FloatField()

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE)


class Nutablty(models.Model):
    nutablty_driver = models.CharField(max_length=50, primary_key=True)
    ph_number = PhoneNumberField()

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Customer(models.Model):
    ph_number = PhoneNumberField(primary_key=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    sex = models.CharField(max_length=5)
    welt = models.FloatField()
    status_c = models.CharField(max_length=15)
    registration_date = models.DateField()


class Address(models.Model):
    ph_number = PhoneNumberField(primary_key=True)
    f_x = models.FloatField()
    f_y = models.FloatField()
    e_x = models.FloatField()
    e_y = models.FloatField()
    name_sdd = models.CharField(max_length=50)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


# Continue the rest of the models...
class OTP(models.Model):
    otp_pass = models.CharField(max_length=15)
    costumer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField()
    exp_date = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    message_id = models.CharField(max_length=10, db_index=True, null=True)

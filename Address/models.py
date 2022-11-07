from django.db import models
import uuid
from account.models import User
from django.core.exceptions import ValidationError
import re
# Create your models here.

def LimitedValue(value):
    if len(value) > 50:
        raise ValidationError(f"{value} is not greater than 50 characters.")

def CheckIstext(value):
    if len(re.findall('[0-9]',value)) > 0:
        raise ValidationError(f" Numbers {value} is not allowed .")

def IsVlaidPostCode(value):
    if value.isnumeric()  == False:
        raise ValidationError(f"{value} is not valid postal code")
    elif len(re.findall('[0-9]',value)) > 6:
        raise ValidationError(f"{value} must be 6 character long")

class address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key =True,editable=False)
    state = models.CharField(validators=[CheckIstext,LimitedValue],max_length=50)
    city = models.CharField(validators=[CheckIstext,LimitedValue],max_length=50)
    country_name = models.CharField(validators=[CheckIstext,LimitedValue],max_length=50)
    address_line = models.CharField(validators=[LimitedValue],max_length=50)
    address_line2 = models.CharField(validators=[LimitedValue],max_length=50)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    postal_code = models.CharField(validators=[IsVlaidPostCode],max_length=6)

    def __str__(self):
        return self.address_line
    
     

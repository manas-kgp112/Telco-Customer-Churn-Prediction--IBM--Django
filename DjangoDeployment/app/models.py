from django.db import models

# Create your models here.


class CustomerData(models.Model):

    # choices
    COUNTRY = (
        ('United States', 'United States'),
    )
    STATE = (
        ('California', 'California'),
    )
    CITY = (
        ('Los Angeles', 'Los Angeles'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    INTERNET_SERVICE = (
        ('No', 'No'),
        ('DSL', 'DSL'),
        ('Fiber optic', 'Fiber optic')
    )
    MULTIPLE_LINES=(
        ('No phone service', 'No phone service'),
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    ONLINE_SECURITY = (
        ('No internet service', 'No internet service'),
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    CONTRACT = (
        ('Month-to-month', 'Month-to-month'),
        ('Two year', 'Two year'),
        ('One year', 'One year')
    )
    PAYMENT = (
        ('Electronic check', 'Electronic check'),
        ('Mailed check', 'Mailed check'),
        ('Bank transfer (automatic)', 'Bank transfer (automatic)'),
        ('Credit card (automatic)', 'Credit card (automatic)')
    )
    COUNT = (
        (0, '0'),
        (1, '1')
    )
    BINARY_FIELDS = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    CustomerID = models.CharField(max_length=200, primary_key=True)
    Count = models.IntegerField(null=True, choices=COUNT)
    Country = models.CharField(max_length=200, null=True, choices=COUNTRY)
    State = models.CharField(max_length=200, null=True, choices=STATE)
    City = models.CharField(max_length=200, null=True, choices=CITY)
    ZipCode = models.CharField(max_length=200, null=True)
    # LatLong = models.CharField(max_length=200, null=True)
    Latitude = models.CharField(max_length=200, null=True)
    Longitude = models.CharField(max_length=200, null=True)
    Gender = models.CharField(max_length=200, null=True, choices=GENDER)
    SeniorCitizen = models.CharField(max_length=200, null=True, choices=BINARY_FIELDS)
    Partner = models.CharField(max_length=200, null=True, choices=BINARY_FIELDS)
    Dependents = models.CharField(max_length=200, null=True, choices=BINARY_FIELDS)
    TenureMonths = models.IntegerField(null=True)
    PhoneService = models.CharField(max_length=200, null=True, choices=BINARY_FIELDS)
    MultipleLines = models.CharField(default='No', max_length=200, null=True, choices=MULTIPLE_LINES)
    InternetService = models.CharField(max_length=200, null=True, choices=INTERNET_SERVICE)
    OnlineSecurity = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    OnlineBackup = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    DeviceProtection = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    TechSupport = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    StreamingTV = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    StreamingMovies = models.CharField(default='No', max_length=200, null=True, choices=ONLINE_SECURITY)
    Contract = models.CharField(max_length=200, null=True, choices=CONTRACT)
    PaperlessBilling = models.CharField(max_length=200, null=True, choices=BINARY_FIELDS)
    PaymentMethod = models.CharField(max_length=200, null=True, choices=PAYMENT)
    MonthlyCharges = models.FloatField(null=True)
    TotalCharges = models.FloatField(null=True)
    # ChurnLabel = models.CharField(max_length=200, null=True)
    # ChurnValue = models.CharField(max_length=200, null=True)
    # ChurnScore = models.CharField(max_length=200, null=True)
    CLTV = models.IntegerField(null=True)
    # ChurnReason = models.CharField(max_length=200, null=True)



    def save(self, *args, **kwargs):
        if not self.PhoneService:
            self.MultipleLines = 'No phone service'
        if self.InternetService == 'No':
            self.OnlineSecurity = 'No internet service'
            self.OnlineBackup = 'No internet service'
            self.DeviceProtection = 'No internet service'
            self.TechSupport = 'No internet service'
            self.StreamingTV = 'No internet service'
            self.StreamingMovies = 'No internet service'
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.CustomerID
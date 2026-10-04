from django.db import models


class Service(models.Model):

    CATEGORY_CHOICES = [
        ('aadhaar', 'Aadhaar'),
        ('pan', 'PAN Card'),
        ('voter', 'Voter ID'),
        ('passport', 'Passport'),
        ('income', 'Income Certificate'),
        ('caste', 'Caste Certificate'),
        ('domicile', 'Domicile Certificate'),
        ('nationality', 'Nationality Certificate'),
        ('age', 'Age Certificate'),
        ('ews', 'EWS Certificate'),
        ('non-creamy', 'Non-Creamy Layer'),
        ('minority', 'Minority / Alpabhudharak'),
        ('women', 'Women Reservation'),
        ('farmer', 'Farmer Certificate'),
        ('bhumihin', 'Bhumihin Certificate'),
        ('ration', 'Ration Card'),
        ('eshram', 'E-Shram Card'),
        ('holding', '7/12 Holding'),
        ('crop', 'Crop Insurance'),
        ('shop', 'Shop Act / Udyog'),
        ('food', 'Food License'),
        ('gazette', 'Gazette'),
        ('driving', 'Driving Licence'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)

    name_marathi = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Marathi Name"
    )

    description = models.TextField()

    documents_required = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name="Service Category"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
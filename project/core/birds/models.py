from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

from birds.species_list import species_list
from profiles.models import User
from stations.models import Net

SEX_LIST = (
    ('U', 'Unknown'),
    ('M', 'Male'),
    ('F', 'Female')
)
SEX_HOW_LIST = (
    ('BO',  'Behavioral observation'),
    ('BP',  'Brood patch'),
    ('CC',  'Combination of characteristics/measurements'),
    ('CL',  'Cloaca'),
    ('DN',  'DNA/chromosome analysis'),
    ('EG',  'Egg in oviduct'),
    ('EY',  'Eye color'),
    ('FS',  'Feather Shape (Primaries or tail)'),
    ('IC',  'Inconclusive, Conflicting'),
    ('LL',  'Laparotomy/laparoscopy'),
    ('MB',  'Mouth/bill'),
    ('NA',  'Not attempted'),
    ('OT',  'Other'),
    ('PL',  'Body Plumage'),
    ('RC',  'Sexed upon recapture'),
    ('TL',  'Tail length'),
    ('WL',  'Wing length')
)

AGE_LIST = (
    ('U',   'Unknown'),
    ('AHY', 'After Hatching Year'),
    ('HY',  'Hatching Year'),
    ('J',   'Juvenile'),
    ('L',   'Local'),
    ('SY',  'Second Year'),
    ('ASY', 'After Second Year'),
    ('TY',  'Third Year'),
    ('ATY', 'After Third Year')
)

AGE_HOW_LIST = (
    ('AM', 'Auxiliary Marker'),
    ('BO', 'Behavioral observation'),
    ('BP', 'Brood patch'),
    ('BU', 'Bursa of Fabricius'),
    ('CA', 'Calendar'),
    ('CC', 'Combination of characteristics/measurements'),
    ('CL', 'Cloaca'),
    ('EG', 'Egg in oviduct'),
    ('EY', 'Eye color'),
    ('FB', 'Fault bar'),
    ('FF', 'Flight feathers (remiges), condition or color'),
    ('IC', 'Inconclusive, Conflicting   '),
    ('LP', 'Molt limit present  '),
    ('MB', 'Mouth/bill  '),
    ('MR', 'Actively-molting remiges'),
    ('NA', 'Not attempted'),
    ('NF', 'Nestling recently fledged, incapable of powered flight'),
    ('NL', 'No molt limit'),
    ('NN', 'Nestling in nest (altricials), downy young (precocials)'),
    ('OT', 'Other'),
    ('PC', 'Primary covert wear and/or shape'),
    ('PL', 'Body Plumage'),
    ('RC', 'Re-captured bird with USGS band'),
    ('SK', 'Skull'),
    ('TL', 'Tail length'),
    ('TS', 'Tail shape or wear')
)

MOLT_CHOICES = (
    # need molt choice options
)

SKULL_CHOICES = (
    # need skull choice options
)


class Bird(models.Model):
    species = models.CharField(choices=species_list, max_length=10)
    created = models.DateTimeField(editable=False)
    band_number = models.CharField(max_length=32)
    wing_size = models.FloatField()
    sex = models.CharField(choices=SEX_LIST, max_length=5, default='U')
    sex_how = models.CharField(choices=SEX_HOW_LIST, max_length=10, default='NA', verbose_name="Method used to determine sex")
    age = models.CharField(choices=AGE_LIST, max_length=5, default='U')
    age_how = models.CharField(choices=AGE_HOW_LIST, max_length=10, default='NA', verbose_name="Method used to determine age")
    culmen = models.FloatField(verbose_name='Bill or beak measurement', null=True)
    corrugation = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    weight = models.FloatField()
    molt_flight = models.CharField(max_length=10, choices=MOLT_CHOICES)
    molt_body = models.CharField(max_length=10, choices=MOLT_CHOICES)
    gorget = models.IntegerField()
    skull = models.CharField(max_length=10, choices=SKULL_CHOICES)
    # p10 = models.
    # white_patch = models.
    net = models.OneToOneField(Net, on_delete=models.CASCADE, null=True)
    bander = models.OneToOneField(User, related_name='bander', on_delete=models.CASCADE, null=True)
    data_manager = models.OneToOneField(User, related_name='data_manager', on_delete=models.CASCADE, null=True)
    notes = models.TextField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        """
        On initial save, add created datetime
        """
        if not self.id:
            self.created = timezone.now()
        return super(Bird, self).save(*args, **kwargs)

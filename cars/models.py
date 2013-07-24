from django.db import models
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class CarMaker(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2)
    def __unicode__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=200)
    carmaker = models.ForeignKey(CarMaker)
    def __unicode__(self):
        return str(self.carmaker) + " " + self.name

class Car(models.Model):
    carmodel = models.ForeignKey(CarModel)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(timezone.now().year),MinValueValidator(timezone.now().year-10)])
    owners = models.PositiveSmallIntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])

    pub_date = models.DateTimeField( default=timezone.now())


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return str(self.carmodel) + " " + str(self.year)
    
    class Meta:
        ordering = ('pub_date',)
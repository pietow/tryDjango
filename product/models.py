from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Product(models.Model):
    title       = models.CharField(_("title"), max_length=50)
    description = models.TextField(blank=False, null=False) #field can be blank; blanke->rendering; null-> db-level
    price       = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    summary     = models.TextField(blank=True, null=True)
    features    = models.BooleanField(_("features"))

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(_("title"), max_length=120)
    # field can be blank; blank->rendering; null-> db-level
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    features = models.BooleanField(_("features"), default=True)

    def get_absolute_url(self):
        return reverse("product:product-detail", kwargs={"my_id": self.id}) #f"product/{self.id}/"
        print('bla')
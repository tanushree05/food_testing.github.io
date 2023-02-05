'''from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

class Organization(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

class OrganizationAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Organization API key"

        verbose_name_plural = "Organization API keys"
        '''
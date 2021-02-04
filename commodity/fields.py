from django.db import models
from django.core import checks


class ImmutableCharField(models.CharField):
    def _check_max_length_attribute(self, **kwargs):
        if self.max_length is None:
            return [
                checks.Error(
                    "CharFields must define a 'max_length' attribute.",
                    obj=self,
                    id='fields.E120',
                )
            ]
        elif (not isinstance(self.max_length, int) or isinstance(self.max_length, bool) or
              self.max_length != self.max_length):
            return [
                checks.Error(
                    "The length must be fixed.",
                    obj=self,
                    id='fields.E121',
                )
            ]

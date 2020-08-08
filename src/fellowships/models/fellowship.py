from django.conf import settings
from django.db import models
from django.utils.text import slugify

from accounts.models import Cleric, Member

class Fellowship(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='fellowships/photos/%Y/%m/%d/', null=True, blank=True)
    cleric = models.OneToOneField(Cleric, related_name="fellowship", on_delete=models.CASCADE, blank=True)
    members = models.ManyToManyField(Member, related_name="fellowships", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'fellowship'
        verbose_name_plural = 'fellowships'

    def save(self, *args, **kwargs):
        if not self.slug:
            today = datetime.today()
            title_slugified = slugify(self.name)
            self.slug = f'{today:%Y%m%d%M%S}-{title_slugified}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def get_cleric_avatar(self):
        return f"{settings.MEDIA_URL}{self.cleric.get_avatar}"

    @property
    def get_cleric_name(self):
        return self.cleric.name
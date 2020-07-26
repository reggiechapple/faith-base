from django.conf import settings
from django.db import models
from django.utils.text import slugify

from . import choices

class MemberManager(models.Manager):
    use_for_related_fields = True


class Member(models.Model):
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="member", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    objects = MemberManager()

    @property
    def get_username(self):
        return self.user.username

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_avatar(self):
        return f"{settings.MEDIA_URL}{self.user.photo}"

    @property
    def get_name(self):
        return self.user.name

    @property
    def get_dob(self):
        return self.user.date_of_birth

    @property
    def get_sex(self):
        return self.user.sex

class Church(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='church/photos/%Y/%m/%d/', null=True, blank=True)
    cleric = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="chruch", on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'church'
        verbose_name_plural = 'churches'

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
        return f"{settings.MEDIA_URL}{self.cleric.photo}"

    @property
    def get_cleric_name(self):
        return self.cleric.name
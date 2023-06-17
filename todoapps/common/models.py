import uuid
from django.db import models

from .utils import unique_slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)


# pylint: disable=E1101 # SlugModel has no 'name' member, no 'title' member
class SlugModel(models.Model):
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        abstract = True

    def _get_slug_text(self):
        assert any([hasattr(self, 'name'), hasattr(self, 'title')])
        slug_text = ''
        if hasattr(self, 'name'):
            slug_text = self.name.lower()
        elif hasattr(self, 'title'):
            slug_text = self.title.lower()
        return slug_text

    # pylint: disable=W0221 # Parameters differ from overridden 'save' method
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = self._get_slug_text()
            unique_slugify(self, slug_text)
        return super().save(*args, **kwargs)


class UUIDBaseModel(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta(BaseModel.Meta):
        abstract = True


def get_file_upload_path(_, filename):
    import os
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('uploads/', filename)


class File(UUIDBaseModel):
    file = models.FileField(upload_to=get_file_upload_path)
    name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

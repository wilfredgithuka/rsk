import uuid

from django.conf import settings
from django.db import models
from django.utils import text

import fields


class TimeStampedModel(models.Model):

    """
    An abstract base class model. Provides self-updating ``created`` and
    ``modified`` field.
    """

    created = models.DateTimeField(auto_now_add=True,
                                   help_text='The time when this entity was created.')
    changed = models.DateTimeField(auto_now=True,
                                   help_text='The time when this entity was most recently saved.')

    class Meta:
        abstract = True


class TitleModel(models.Model):

    title = models.CharField(max_length=255,
                             help_text='The title of this entity, always treated as non-markup plain text.')

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True


class BaseModel(TitleModel):

    """
    Abstract model for main entities. Provides a ``title`` and ``shortuuid``
    field. Inherits `TitleModel`
    """

    uuid = models.CharField('UUID', max_length=255, unique=True,
                            help_text='Unique Key: Universally unique identifier for this entity.')
#    shortuuid = ShortUUIDField(verbose_name='Short UUID',
#                                      max_length=255, unique=True,
#                                      help_text='Unique Key: Universally unique identifier for this entity.')

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()

        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class AuthorModel(models.Model):

    """
    Abstract model for content entities. Provides a ``author`` field.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                               help_text='The user that owns this entity; Initially, this is the user that created it.')
    class Meta:
        abstract = True


class PublicModel(models.Model):

    """
    Abstract model for public entities. Provides a ``slug``, ``reviewed`` field
    and code property.
    """

    slug = models.SlugField('SEO slug', max_length=255)
    reviewed = models.BooleanField(
        help_text='Boolean indicating whether the entity has been reviewed (QC).')

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)

        super(PublicModel, self).save(*args, **kwargs)

    @property
    def code(self):
        return "%04d" % self.id

    class Meta:
        abstract = True


class ImageModel(models.Model):

    """
    Abstract base class model for Image fields.
    """

    reviewed = models.BooleanField(
        help_text='Boolean indicating whether the entity has been reviewed (QC).')
    status = models.BooleanField(default=True,
                                 help_text='Boolean indicating whether the entity is published (visible to non-administrators).')
    thumbnail = models.BooleanField(
        help_text='Boolean indicating whether the entity is the main thumbnail.')

    class Meta:
        abstract = True


class CommentModel(models.Model):

    """
    Abstract model for content entities. Provides a ``enable_comments`` field.
    """

    enable_comments = models.BooleanField(default=True)

    class Meta:
        abstract = True

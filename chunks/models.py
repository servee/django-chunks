from django.db import models
from django.core.cache import cache


class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(help_text="A unique name for this chunk of content", blank=False, max_length=255, unique=True)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s" % (self.key,)

    def save(self, *args, **kwargs):
        cache.delete('chunk_%s' % self.key)
        return super(Chunk, self).save(*args, **kwargs)

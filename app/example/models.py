from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField()
    content = models.TextField(verbose_name=_("content"))
    posted_on = models.DateTimeField(verbose_name=_("post date"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("posted by"))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField(verbose_name=_("message"))
    commented_on = models.DateTimeField(verbose_name=_("post date"))
    post = models.ForeignKey(Post, related_name='comments', verbose_name=_("post"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), related_name='comment_user')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['commented_on']

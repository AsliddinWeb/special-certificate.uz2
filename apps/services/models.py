from django.db import models


class Service(models.Model):
    title = models.CharField('Nomi', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    short_description = models.CharField('Qisqa tavsif', max_length=300)
    description = models.TextField('Batafsil tavsif')
    icon = models.CharField('Ikona', max_length=50, default='clipboard-check',
                           help_text='Heroicons nomi: clipboard-check, beaker, shield-check va h.k.')
    order = models.PositiveIntegerField('Tartib', default=0)
    is_active = models.BooleanField('Faol', default=True)
    created_at = models.DateTimeField('Yaratilgan', auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
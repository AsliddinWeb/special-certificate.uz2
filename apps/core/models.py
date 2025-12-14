from django.db import models


class ContactMessage(models.Model):
    name = models.CharField('Ism', max_length=100)
    phone = models.CharField('Telefon', max_length=20)
    email = models.EmailField('Email', blank=True, null=True)
    message = models.TextField('Xabar')
    created_at = models.DateTimeField('Yuborilgan vaqt', auto_now_add=True)
    is_read = models.BooleanField('O\'qilgan', default=False)

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"

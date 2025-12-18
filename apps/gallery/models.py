from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='gallery/photos/', verbose_name="Rasm")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    youtube_url = models.URLField(verbose_name="YouTube havola")
    description = models.TextField(blank=True, null=True, verbose_name="Tavsif")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_youtube_id(self):
        """YouTube video ID ni olish"""
        url = self.youtube_url

        # youtu.be/VIDEO_ID formatida
        if 'youtu.be' in url:
            video_id = url.split('/')[-1]
            # ?si= yoki boshqa parametrlarni olib tashlash
            return video_id.split('?')[0]

        # youtube.com formatlarida
        elif 'youtube.com' in url:
            # watch?v=VIDEO_ID
            if 'v=' in url:
                video_id = url.split('v=')[1]
                return video_id.split('&')[0].split('?')[0]

            # embed/VIDEO_ID
            elif 'embed/' in url:
                video_id = url.split('embed/')[-1]
                return video_id.split('?')[0].split('&')[0]

            # shorts/VIDEO_ID
            elif 'shorts/' in url:
                video_id = url.split('shorts/')[-1]
                return video_id.split('?')[0]

        return url

    def get_embed_url(self):
        """YouTube embed URL"""
        video_id = self.get_youtube_id()
        return f"https://www.youtube.com/embed/{video_id}"

    def get_thumbnail(self):
        """YouTube thumbnail URL"""
        video_id = self.get_youtube_id()
        return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

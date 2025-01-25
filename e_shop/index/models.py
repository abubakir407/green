from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(upload_to='pictures/', verbose_name="Картинка")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def str(self):
        return self.title

class Like(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Комментарий к {self.picture.title}"

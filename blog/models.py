from django.db import models


class Post(models.Model):
    # Данные о посте
    title = models.CharField('Название', max_length=100)
    descriptio = models.TextField('Текст записи')
    author = models.CharField('Имя втора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображения', upload_to='blog/img/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        
        
class Comments(models.Model):
    # Комментарий
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comements = models.TextField('Текст комментария', max_length=3000)
    post = models.ForeignKey(Post, verbose_name='Публикации', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

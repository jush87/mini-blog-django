from django.db import models

# Create your models here.
class Post(models.Model):
    '''post information'''
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Content')
    author = models.CharField('Author Name', max_length=100)
    date = models.DateField('Date')
    img = models.ImageField ('Image', upload_to = 'image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

class Comments(models.Model):
        '''Comments'''
        email = models.EmailField()
        name = models.CharField('Name', max_length=50)
        text_comments = models.TextField('Comments', max_length=2000)
        post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.name}, {self.post}'

        class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'

class Likes(models.Model):
    '''Likes'''
    ip = models.CharField('IP-address', max_length=100)
    pos = models.ForeignKey(Post, verbose_name="Publication", on_delete=models.CASCADE)




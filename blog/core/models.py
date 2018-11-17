from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #pega quem ta logado / deleta todos os posts caso a conta seja deletada
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural =  'Publicações' #avisa para o django que tem plural

    def __str__(self):
        return self.title
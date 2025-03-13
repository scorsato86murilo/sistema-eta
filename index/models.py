from datetime import timezone

from django.db import models
from django.core.validators import RegexValidator



class Index(models.Model):
    cidade_estado = models.CharField(max_length=100)
    rua_numero = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    img = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.cidade_estado


class Avisos(models.Model):
    mensagem = models.TextField()
    def __str__(self):
        return self.mensagem


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Video(models.Model):
    video_link = models.URLField(
        validators=[RegexValidator(
            regex=r'^https://(www\.)?youtube\.com/.*$',
            message='A URL deve ser do YouTube.'
        )]
    )
    titulo = models.CharField(max_length=100, default='Assista ao vídeo!')
    mensagem = models.CharField(max_length=100, default='Dúvidas? Entre em contato')

    def __str__(self):
        return self.titulo

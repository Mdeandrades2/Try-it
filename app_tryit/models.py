from django.db import models

class Login(models.Model):
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.nome, self.senha)
    
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=8)
    culinarias_preferidas = models.ManyToManyField('Culinaria')

    def __str__(self):
        return self.usuario

class Culinaria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Filtrarreceita(models.Model):
    alergia = models.CharField(max_length=50)
    intolerancia = models.CharField(max_length=50)
    comidadetestavel = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
class Receita(models.Model):
    nome = models.CharField(max_length=255)
    ingredientes = models.TextField()

    def __str__(self):
        return self.nome    
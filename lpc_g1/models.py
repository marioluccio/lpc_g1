from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    idPessoa = models.AutoField(primary_key=True)
    nomePessoa = models.CharField('nomePessoa',max_length=100)
    emailPessoa = models.EmailField('email',max_length(100))
class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    nomeEvento = models.CharField('nomeEvento',max_length=100)
    eventoPrincipal = models.TextField('eventoPrincipal',max_length=150)
    sigla = models.CharField('sigla',max_length=10)
    dataEHoraDeInicio = models.DateTimeField()
    palavraChave = models.TextField('palavraChave')
    logoTipo = models.TextField('logoTipo')
    realizador = models.Pessoa('realizador')
    cidade = models.TextField('cidade',max_length=20)
    uf = models.CharField('uf',max_length = 4)
    endereco = models.TextField('enderecoS')
    cep = models.CharField('cep',max_length=9)
class Autor(models.Model):
    idAutor = AutoField(primary_key=True)
    curriculo = models.TextField('curriculo')
    artigos = models.list('artigos',Artigo)
class PessoaJuridica(models.Model, Pessoa()):
    cnpj = models.CharField('cnpj',max_length=15)
    razaoSocial = models.TextField('razaoSocial',max_length=100)
class PessoaFisica(models.Model, Pessoa()):
    cpf = models.CharField('cpf',max_length=11)
class ArtigoCientifico(models.Model,EventoCientifico()):
    titulo = models.TextField('titulo')
    autores = models.list('autores',Autor)
    evento = models.EventoCientifico('evento')
class EventoCientifico(models.Eveto()):
    issn = models.TextField('issn')

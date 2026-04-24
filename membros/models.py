from django.db import models

# Criando uma tabela no banco de dados.
class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    is_lideranca = models.BooleanField(default=False)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
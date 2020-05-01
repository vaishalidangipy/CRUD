from django.db import models


class Fundo(models.Model):
    id_fundo = models.IntegerField(primary_key=True, unique=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fundo'
        managed = False

    def __str__(self):
        return '{}'.format(self.id_fundo)


class GrupoEconomico(models.Model):
    id_grupo_economico = models.IntegerField(primary_key=True, unique=True)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    cadastro_grupo  = models.CharField(max_length=8)
    nome = models.CharField(max_length=450)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grupo_economico'
        managed = False

    def __str__(self):
        return '{}'.format(self.id_grupo_economico)


class Cedente(models.Model):
    id_cedente = models.IntegerField(primary_key=True, unique=True)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    grupo_economico_id_grupo_economico = models.ForeignKey(
        GrupoEconomico, null=True, blank=True,
        on_delete=models.SET_NULL, db_column='grupo_economico_id_grupo_economico')
    cadastro_grupo = models.CharField(max_length=9)
    cadastro = models.CharField(max_length=14)
    nome = models.CharField(max_length=250)
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cedente'
        managed = False

    def __str__(self):
        return '{}'.format(self.id_cedente)


class LimiteCreditoCedente(models.Model):
    id_limite_credito_cedente = models.IntegerField(primary_key=True, unique=True)
    fundo_id_fundo = models.ForeignKey(
        Fundo, null=True, blank=True, db_column='fundo_id_fundo',
        on_delete=models.SET_NULL)
    cedente_id_cedente = models.ForeignKey(
        Cedente, null=True, blank=True, db_column='cedente_id_cedente',
        on_delete=models.SET_NULL)
    data_concessao = models.DateField(null=True, blank=True)
    valor_nominal_limite = models.FloatField()
    valor_percentual_limite = models.FloatField()
    data_atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'limite_credito_cedente'
        managed = False

    def __str__(self):
        return '{}'.format(self.id_limite_credito_cedente)

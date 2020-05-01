from rest_framework import serializers

class GrupoEconomicoSerializer(serializers.Serializer):
    id_grupo_economico = serializers.IntegerField(read_only=True)
    r1 = serializers.IntegerField(read_only=True)
    r2 = serializers.IntegerField(read_only=True)
    r3 = serializers.IntegerField(read_only=True)
    cadastro_grupo = serializers.CharField(max_length=30, read_only=True)
    nome = serializers.CharField(max_length=450, read_only=True)
    data_atualizacao = serializers.DateTimeField(format="%m-%d-%Y", read_only=True)


class CedenteSerializer(serializers.Serializer):
    id_cedente = serializers.IntegerField(read_only=True)
    r1 = serializers.IntegerField(read_only=True)
    r2 = serializers.IntegerField(read_only=True)
    r3 = serializers.IntegerField(read_only=True)
    grupo_economico_id_grupo_economico = serializers.CharField(max_length=20, read_only=True)
    cadastro_grupo = serializers.CharField(max_length=9, read_only=True)
    cadastro = serializers.CharField(max_length=14, read_only=True)
    nome = serializers.CharField(max_length=250, read_only=True)
    data_atualizacao = serializers.DateTimeField(format="%m-%d-%Y", read_only=True)


class LimiteCreditoCedenteSerializer(serializers.Serializer):
    id_limite_credito_cedente = serializers.IntegerField(read_only=True)
    fundo_id_fundo = serializers.CharField(max_length=20, read_only=True)
    cedente_id_cedente =  serializers.CharField(max_length=20, read_only=True)
    data_concessao = serializers.DateField(format="%m-%d-%Y", read_only=True)
    valor_nominal_limite = serializers.FloatField(read_only=True)
    valor_percentual_limite = serializers.FloatField(read_only=True)
    data_atualizacao = serializers.DateTimeField(format="%m-%d-%Y", read_only=True)

import json

# Dados de faturamento diário (exemplo)
faturamento_json = '''
{
  "faturamento_diario": [0, 22174.1664, 24537.6698, 26139.6134, 0, 0, 26742.6612, 0, 0, 0, 42889.2258, 46251.174, 11191.4722, 0, 0, 0, 15804.1002, 0, 0, 0, 25876.168, 0, 0, 0, 0, 0, 48412.1377, 0, 0, 0]
}
'''

# Carregar dados do JSON
dados = json.loads(faturamento_json)
faturamento_diario = dados["faturamento_diario"]

# Filtra dias com faturamento maior que 0
faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

# Calcula o menor e maior valor de faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calcula a média mensal de faturamento
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Calcula o número de dias com faturamento superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

# Exibe os resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

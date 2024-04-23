# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    
# Solicita ao usuário que insira o consumo médio mensal de dados:

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

planos_fibra = {
    'basico': {'nome': 'Plano Essencial Fibra','velocidade': '50Mbps', 'limite': 10},
    'medio': {'nome': 'Plano Prata Fibra','velocidade': '100Mbps', 'limite': 20},
    'top': {'nome': 'Plano Premium Fibra', 'velocidade': '300Mbps', 'limite': 'acima de 20GB'}}

sites = ['www.vivo.com.br', 'www.vivo.com.br/para-empresas']

mensagem_inicial = '''Nós da Vivo estamos sempre preocupados em oferecer o produto certo para os nossos clientes!
Então, por favor, informe seu consumo médio mensal de dados em Gigabytes (GB) para indicarmos o melhor plano para o seu perfil:
=> '''

consumo = float(input(mensagem_inicial))

def recomendar_plano(gb):
    while True:
        if gb < 0:
            gb = float(input('''\nDesculpe, mas valor digitado é inválido!
Por favor, informe seu consumo médio mensal de dados em Gigabytes (GB) para indicarmos o melhor plano para o seu perfil:
=> '''))
        
        elif gb >= 0 and gb <= planos_fibra['basico']['limite']:
            return f"\nO mais indicado para o seu perfil é o {planos_fibra['basico']['nome']}, que atinge velocidade de até {planos_fibra['basico']['velocidade']}."
            

        elif gb > planos_fibra['basico']['limite'] and gb <= planos_fibra['medio']['limite']:
            return f"\nO mais indicado para o seu perfil é o {planos_fibra['medio']['nome']}, que atinge velocidade de até {planos_fibra['medio']['velocidade']}."

        elif gb > planos_fibra['medio']['limite']:
            return f"\nO mais indicado para o seu perfil é o {planos_fibra['top']['nome']}, que atinge velocidade de até {planos_fibra['top']['velocidade']}."
        
print(recomendar_plano(consumo))

print(f'''\nAgora, basta acessar {sites[0]} para ter a melhor fibra do Brasil na sua residência!!!
Sua empresa também pode ter nossa fibra e outros produtos. Acesse {sites[1]} e confira!!!
E se preferir, você pode visitar uma das lojas Vivos presentes em todo o Brasil. Nossos consultores estão sempre prontos para ajudar!!! 
 ''')

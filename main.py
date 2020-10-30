import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# ler arquivo dos projetos do Kickstarter
dataFrame = pd.read_csv('ks-projects-201801.csv')

projects = dataFrame[['ID', 'main_category', 'deadline', 'goal', 'launched', 'state', 'backers', 'country', 'usd pledged']]

# estrutura do data frame
print('Estrutura dos Projetos:')
print(projects.dtypes)
print(projects.shape)
print(projects.head())

# coluna state
print()
print('Coluna state:')
print(projects['state'].unique())

# failed     - 0
# canceled   - 1
# successful - 2
# live       - 3
# undefined  - 4
# suspended  - 5

projects['state_values'] = np.select([
    (projects['state'] == 'failed'),
    (projects['state'] == 'canceled'),
    (projects['state'] == 'successful'),
    (projects['state'] == 'live'),
    (projects['state'] == 'undefined'),
    (projects['state'] == 'scheduled')
], [
    0,
    1,
    2,
    3,
    4,
    5
])

print(projects.head())

# # Uma figura permite que sejam inseridos diversos gráficos
# # Na criação de um objeto figure é possível definir as dimensões
# image = plt.figure(figsize=[20,6])
# # Serão dois gráficos, um com uma plotagem de pontos em eixos e o outro uma distribuição de frequencia
# # São adicionadas duas subplotagens
# # 1,2 indica que a imagem terá uma linha com duas colunas e o terceiro parâmetro é a posição onde ficará a subplotagem
# graph1 = image.add_subplot(1,2,1)
# graph2 = image.add_subplot(1,2,2)
# # Cria um gráfico de dispersão com as séries idade e nota 1
# graph1.plot(avaliacoes.Idade, avaliacoes.Nota1, 'o')
# # Define título do gráfico
# graph1.set_title('Nota 1 por idade')
# # Define o nome do eixo X
# graph1.set_ylabel('Nota')
# # Define o nome do eixo Y
# graph1.set_xlabel('Idade')
# # A segunda subplotagem é um histograma
# graph2.hist(avaliacoes.Media)
# # Define os nomes como para o gráfico 1
# graph2.set_title('Distribuição da média final')
# graph2.set_xlabel('Contagem')
# graph2.set_ylabel('Media')
# # Mostra os gráficos
# image.show()


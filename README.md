# Mineração de dados - Kickstarter Projects

Universidade do Vale do Taquari – Univates

Inteligência Artificial 2020/B

Autores: Arthur Meurer Saraiva, Marcelo Zerbieli Nicaretta e Matheus Michels

## Seleção

Usaremos a base de projetos do Kickstarter, o maior site de financiamento coletivo do mundo, para identificar os motivos do sucesso ou fracasso dos projetos.

O Dataset está disponível na plataforma [Kaggle](https://www.kaggle.com/kemical/kickstarter-projects).

### Atributos
Desta base de projetos usaremos os seguintes atributos:
- main_category = área de atuação do projeto;
- deadline = data limite para o objetivo ser alcançado;
- goal = quantidade esperada de arrecadação para desenvolvimento do projeto (objetivo);
- launched = data de lançamento do projeto na plataforma;
- state = estado do projeto (sucesso, cancelamento, falha, em progresso e indefinido);
- backers = número de doadores do projeto;
- country = país dos autores da ideia;
- usd_pledged = quantidade arrecadada convertida para dólares.

Além disso, criaremos um novo atributo de duração do projeto:
- duration = diferença entre deadline e launched.

#### Data types
```
ID                         int64
main_category             object
deadline                  object
goal                     float64
launched                  object
state                     object
backers                    int64
country                   object
usd pledged              float64
duration         timedelta64[ns]
```

#### Shape
378661 x 10

#### Head
|   |         ID | main_category |   deadline |    goal |   launched |    state | backers | country | usd_pledged | duration |
| - | ----------:| -------------:| ----------:| -------:| ----------:| --------:| -------:| -------:| -----------:| --------:|
| 0 | 1000002330 |    Publishing | 2015-10-09 |  1000.0 | 2015-08-11 |   failed |       0 |      GB |         0.0 |  59 days |
| 1 | 1000003930 |  Film & Video | 2017-11-01 | 30000.0 | 2017-09-02 |   failed |      15 |      US |       100.0 |  60 days |
| 2 | 1000004038 |  Film & Video | 2013-02-26 | 45000.0 | 2013-01-12 |   failed |       3 |      US |       220.0 |  45 days |
| 3 | 1000007540 |         Music | 2012-04-16 |  5000.0 | 2012-03-17 |   failed |       1 |      US |         1.0 |  30 days |
| 4 | 1000011046 |  Film & Video | 2015-08-29 | 19500.0 | 2015-07-04 | canceled |      14 |      US |      1283.0 |  56 days |

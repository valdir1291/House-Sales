<h1 align="center">House-Rocket Business Solution</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/102424643/206324286-beb786a2-5e2b-4ee4-a04e-84f92a9549b2.JPG" alt="logo" style="zoom:100%;" />

<p align="center">Buscar através de Insigths melhores oportunidades de compra e venda de imóveis dentro da empresa House Rocket.</p> 

  *Obs: A empresa em questão é ficticia,porem o dataset usado é real*
  
  
  
  Dashboard do Projeto: [streamlit](https://valdir1291-house-sales-house-sale-10oabc.streamlit.app/)

# 1. **Problema de Negócio:**

House Rocket é uma empresa especializada em detectar os melhores custos para compra de imóveis. Sua linha de negócio é vender os melhores imóveis com custo beneficio.

Atualmente o processo de busca é realizado de forma manual pela equipe de especialistas, dado a complexidade e o tamanho dos dados acaba demandando muito tempo, o que acarreta na perca de bons negócios.

A empresa então contrata um **cientista de dados** para ajudar a encontrar **insights** de negócio. Como cliente, duas principais questões devem ser respondidas.

  - **Quais imóveis a empresa deveria comprar e por qual preço?**
  - **Após comprada, qual o melhor momento para vendê-las?** 

# 2. **Descrição dos Atributos**

Dados extraídos do [Kraggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)

| Atributo | Descrição |
|---|---|
| id | numeração única dos Imóveis vendidos|
| date | Data dos Imóveis vendidos |
| price | Preço por Imóveis vendidos |
| bedrooms | Número de quartos |
| bathrooms | Número de banheiros ( 0.5 é um banheiro no quarto)|
| sqft_living | Medida em pés quadrados do apartamento |
| sqft_lot | Medida em pés quadrados do espaço terrestre |
| floors | número de quartos |
| waterfront | Variavel se possui vista para água ou não |
| view | índice de 0 a 4 para a qualidade da vista para água |
| condition  | índice de 1 a 5 para a condição do apartamento |
| grade  | índice de 1 a 13, onde 1-3 é para construção e  qualidade de design pequeno, 7 é para construção e design médio, de 11-13 para alta qualidade e construção     de design |
| sqft_above | Metros quadrados do interior acima do nivel do solo |
| sqft_basement | Metros quadrados do interior da casa abaixo do nivel do solo |
| yr_built | Ano em que o imóvel foi constrúido |
| yr_renovated | Ano em que o imóvel foi renovado |
| zipcode | Numeração do CEP do Imóvel |
| lat | Lattitude |
| long | Longitude |
| sqft_living15 | Metros quadrados do espaço interno da habitação para os 15 vizinhos mais próximos |
| sqft_lot15 | Metros quadrados dos lotes de terra dos 15 vizinhos mais próximos |




# 3. **Premissas de Negócio:**

As premissas seguidas neste projeto foram:

- A quantidade e localidade dos Imóveis foram cruciais para a recomendação de compra e venda de imóveis.
- O custo da venda dos imóveis irá se basear de acordo com a média de custo por estação do ano.
- Imóveis com o índice de condição até 2 será classificado como "ruim", entre 3 e 4 são "regulares" e acima de 5 é "bom".
- Apenas casas com o índice de condição "bom" entrará como indicação de vendas.
- Imóveis com atributos de 33 quartos e ID duplicados será desconsiderado por se tratar de um ero.
- Será considerado imóveis sem vista para água, quanto imóveis com vista para água.


# 4. **Estratégia para Solução:**

Minha estratégia para solucionar este desafio é:

**Passo 1. Extração de Dados:** Extrair dados disponibilizados do Kraggle.

**Passo 2. Descrição dos Dados:** Através de métricas Estastíticas, encontrar dados fora do escopo de negócios.

**Passo 3. Filtrar Dados:** Selecionar dados voltados para a solução do negócio.

**Passo 4. Analisar Dados:** Explorar e analisar dados para encontrar Insights para o negócio.

**Passo 5. Modelo de Negócio:** transformar a análise em um modelo sustentável de negócio.

**Passo 6. Deploy do Modelo em Produção:** Modelo de Negócio disponibilizado no [streamlit](https://valdir1291-house-sales-house-sale-10oabc.streamlit.app/).


# 5. **TOP Insights para o Negócio:**

**Hipótese 1:** Imóveis que possuem vista para água, são 30% mais caros, na média.

**Verdadeiro**: Imóveis com vista para água são cerca de 68% mais caros na média.

**Hipótese 2:** Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.

**Falso**: Não há diferença de preço entre os imóveis mais antigos e mais novos.

**Hipótese 3:** Imóveis sem porão com maior área, são 50% mais caros do que com porão.

**Falso**: Os imóveis com maior área e com porão são cerca de 17% mais caros do que sem porão.

**Hipótese 4:** O crescimento do preço dos imóveis YoY ( Year over Year ) é de 30%.

**Verdadeiro**: O crescimento dos preço dos imóveis é acima de 30%, chegando ao dobro do ano anterior.

**Hipótese 5:** Imóveis com 3 banheiros tem um crescimento MoM( Month over Month ) de 15%.

**Falso**: Os imóveis com 3 banheiros tem crescimento mês a mês entre 8 e 10%.

**Hipótese 6:** Imoveis com condição regular são 20% mais baratos no verão.

**Falso**: Imóveis com condição regular são 16% mais baratos no verão na média.

**Hipótese 7:** Em media, os imoveis mais caros por região são 30% acima da media.

**Falso**: Apenas o zipcode: 98039 é 30% mais caro do que a média, por ser uma região com vista para água.

**Hipótese 8:** imoveis renovados sao 30% acima da media.

**Verdadeiro**: OImóveis renovados são 30% mais caros que imóveis não renovados.

**Hipótese 9:** Imoveis com vista para água em Fevereiro são 40% mais baratos que agosto.

**Verdadeiro**: Os imóveis de Fevereiro são cerca de 50% mais baratos do que Agosto.

**Hipótese 10:** Imóveis com 3 cômodos tem um crescimento MoM( Month over Month ) de 30%

**Falso**: Apenas em Janeiro de 2015 houve um crescimento acima da média.


# 6. **Resultado para o Negócio:**

Recapitulando 2 questões que esse projeto teve como objetivo:

1 - **Quais imóveis a empresa deveria comprar e por qual preço?**

Através do agrupamento de imóveis baseado na mediana do preço pelo CEP e a condição do imóvel, resulta em um total de 933 imóveis que são abaixo do preço da mediana da região, gerando em um custo total de $ 404.064,045.

2 - **Após comprada, qual o melhor momento para vendê-las?**

Os imóveis serão vendidos baseado na estação do ano, caso o valor do imóvel esteja abaixo da média naquela estação, será vendido com acréscimo de 30%. Caso seja acimado valor, será acrescentado 10% na venda. Desta forma, o lucro total de Vendas será de $ 72.439,464. Dito isto o melhor momento para vendê-las é na primavera, pois é onde há mais lucro.


# 6. **Conclusão**

Este projeto conseguiu responder as principais perguntas de negócio, o que aumenta a receita da empresa. Contudo há melhorias a longo prazo que podem ser fundamentais futuramente, como:

 - Prever o preço baseado na quantidade de imóveis por região.
 - Como não há um custo acentuado nos imóveis renovados atualmente, pode gerar uma previsão de custo em caso de reforma dos imóveis não reformados.




<h1 align="center">House-Rocket Business Solution</h1>

<p align="center">Buscar através de Insigths melhores oportunidades de compra e venda de imóveis dentro da empresa House Rocket.</p> 

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




# 2. **Premissas de Negócio:**

As premissas seguidas neste projeto foram:

- A quantidade e localidade dos Imóveis foram cruciais para a recomendação de compra e venda de imóveis.
- O custo da venda dos imóveis irá se basear de acordo com a média de custo por estação do ano.
- Imóveis com o índice de condição até 2 será classificado como "ruim", entre 3 e 4 são "regulares" e acima de 5 é "bom".
- Apenas casas com o índice de condição "bom" entrará como indicação de vendas.
- Imóveis com atributos de 33 quartos e ID duplicados será desconsiderado por se tratar de um ero.


# 3. **Estratégia para Solução:**

Minha estratégia para solucionar este desafio é:

**Passo 1. Extração de Dados:** Extrair dados disponibilizados do Kraggle.

**Passo 2. Descrição dos Dados:** Através de métricas Estastíticas, encontrar dados fora do escopo de negócios.

**Passo 3. Filtrar Dados:** Selecionar dados voltados para a solução do negócio.

**Passo 4. Analisar Dados:** Explorar e analisar dados para encontrar Insights para o negócio.

**Passo 5. Modelo de Negócio:** transformar a análise em um modelo sustentável de negócio.

**Passo 6. Deploy do Modelo em Produção:** Disponibilizar o modelo em Cloud para que outras pessoas possam usar o mesmo modelo em seus negócios.


# 4. **TOP 5 Insights para o Negócio:**








# 5. **Resultado para o Negócio:**







# 6. **Conclusão**



from itertools import groupby
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium
import geopandas
from datetime import datetime

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data


@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile

def drop_duplicate (data):
    df = df.drop_duplicates(subset = ['id'], keep = 'last')
    return data


def drop_value (data):
    df = df.drop(15870)
    return data

# NEW FEATURES

def set_feature(data):
    data['price_m2'] = data['price'] / data['sqft_lot']

    data['condition'] = data['condition'].astype(int)
    data['condition_type'] = data['condition'].apply(lambda x:
                                                     'bad' if x <= 2 else
                                                     'regular' if (x == 3) | (x == 4) else 'good')

    data['month'] = pd.to_datetime(data['date']).dt.strftime('%m')
    data['month'] = data['month'].astype(int)

    data['season'] = data['month'].apply(lambda x: 'Primavera' if (x > 3) & (x < 6) else
                                         'Verão' if (x > 6) & (x < 9) else
                                         'Outono' if (x > 9) & (x < 12) else 'Inverno')

    data['yr_mean'] = data['yr_built'].apply(
        lambda x: '> 1955' if x > 1955 else '< 1955')

    data['waterfront_is'] = data['waterfront'].apply(
        lambda x: 'Possui' if x == 1 else 'Não possui')

    data['basement'] = data['sqft_basement'].apply(
        lambda x: 'sim' if x > 0 else 'não')

    data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')

    data['month_year'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m')

    data['renovated'] = data['yr_renovated'].apply(
        lambda x: 'Yes' if x > 0 else 'no')

    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    pd.set_option('display.float_format', '{:.2f}'.format)

    return data

def overview_data(data):

    st.title('Bem vindo a House Rocket!')
    st.write('Nesta página você irá encontrar as recomendações de compra e venda de imóveis, além dos insights para negócio.')

    c1, c2, c3 = st.columns((1, 1, 1))

    # average metrics
    df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data[['sqft_living', 'zipcode']].groupby(
        'zipcode').mean().reset_index()
    df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    df.columns = ['ZIPCODE', 'TOTAL HOUSE', 'PRICE', 'SQFT LIVING', 'PRICE/m2']





    # Statistic Descriptive
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))
    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))
    df1 = pd.concat([max_, min_, media, mediana, std],
                    axis=1).reset_index()

    df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

    if c1.checkbox('Mostre o dataset'):
        c1.dataframe(data.head())

    if c2.checkbox('Mostre a média de valores'):
        c2.dataframe(df, height=800)

    if c3.checkbox('Mostre a Análise Descritiva'):
        c3.dataframe(df1, height=800)



    return None

def hipoteses(data):
    st.title('Hipoteses para o negócio')

    c1, c2 = st.columns((1, 1))

    # H1
    c1.subheader(
        'Hipótese 01: Imóveis que possuem vista para água, são 30% mais caros, na média.')

    df = data[['price', 'waterfront_is']].groupby(
        'waterfront_is').mean().reset_index()
        
    df['waterfront_is'] = df['waterfront_is'].astype(str)
    
    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    
    fig = px.bar(df, x='waterfront_is', y='price', color='waterfront_is', text_auto='.2s', text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), labels={'waterfront_is': 'Visão para água',
                                                                                                    'price': 'Preço',
                                                                                                    'text': 'Percentual'},
                  template='simple_white')

    
    c1.plotly_chart(fig, use_container_width=True, width=800, height=400)
    c1.write('Verdadeiro: Imóveis com vista para água são cerca de 68% mais caros na média ')
   
    # H2
    c2.subheader(
        'Hipótese 02: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')

    df = data[['price', 'yr_mean']].groupby('yr_mean').mean().reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig2 = px.bar(df, x='yr_mean', y='price', color='yr_mean', text_auto='.2s', text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), labels={'yr_mean': 'ano de construcao',
                                                                                        'price': 'Preço',
                                                                                        'text': 'Percentual'},
                  template='simple_white')

    c2.plotly_chart(fig2, use_container_width=True, width=800, height=400)
    c2.write('Falso: Não há diferença de preço entre os imóveis mais antigos e mais novos')

    c3, c4 = st.columns((1, 1))

    # H3
    c3.subheader(
        'H3: Imóveis sem porão com maior área, são 50% mais caros do que com porão.')

    df = data[['sqft_lot', 'basement','price']].groupby(
        'basement').sum().sort_values('price', ascending=True).reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

   
    fig3 = px.bar(df, x='basement', y='sqft_lot', color='basement', text_auto='.2s', text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), labels={'basement': 'Possui Porão',
                                                                                                                                   'sqft_lot': 'Loteamento',
                                                                                                                                   'text': 'Percentual' },
                  template='simple_white')

    c3.plotly_chart(fig3, use_container_width=True, height=800)
    c3.write('Falso: Os imóveis com maior área e com porão são cerca de 17% mais caros do que sem porão.')
    # H4
    c4.subheader(
        'H4: O crescimento do preço dos imóveis YoY ( Year over Year ) é de 30%')

    df = data[['price', 'year']].groupby('year').sum().sort_values(
        'price', ascending=True).reset_index()
    
    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig4 = px.bar(df, x='year', y='price', color='year', text_auto='.2s', text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), labels={'year': 'Ano',
                                                                                                                        'price': 'Preço',
                                                                                                                        'text': 'Percentual'},
                  template='simple_white')

    c4.plotly_chart(fig4, use_container_width=True, width=800, height=400)
    c4.write('Verdadeiro: O crescimento dos preço dos imóveis é acima de 30%, chegando ao dobro do ano anterior')
    # H5
    st.subheader(
        'H5:  Imóveis com 3 banheiros tem um crescimento MoM( Month over Month ) de 15%')

    df = data.loc[data['bathrooms'] == 3, ['price', 'month_year']
                   ].groupby('month_year').mean().reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig5 = px.line(df, x='month_year', y='price',
                     text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)),labels={'month_year': 'Mês do ano',
                                                                                   'price': 'Preço',
                                                                                   'text': 'Percentual'} , 
                                                                                   template='simple_white')

    st.plotly_chart(fig5, use_container_width=True, width=800, height=400)
    st.write('Falso: Os imóveis com 3 banheiros tem crescimento mês a mês entre 8 e 10%')

    c6, c7 = st.columns((1, 1))

    # H6 -
    c6.subheader('H6: Imoveis com condição regular são 20% mais baratos no verão')
 

    df = data.loc[data['condition'] == 2, ['price', 'season']].groupby(
        'season').mean().sort_values('price', ascending=True).reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig6 = px.bar(df, x='season', y='price', text_auto='.2s', color='season', text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), labels={'season': 'Estação',
                                                                                                                                              'price': 'Preço',
                                                                                                                                              'text': 'Percentual'},
                  template='simple_white')

    c6.plotly_chart(fig6, use_container_width=True, width=800, height=400)
    c6.write('Falso: Imóveis com condição regular são 16% mais baratos no verão na média')
    
    # H7
    c7.subheader(
        'H7: Em media, os imoveis mais caros por região são 30% acima da media ')

    df = data[['zipcode', 'price']].groupby('zipcode').mean(
    ).sort_values('price', ascending=True).reset_index()

    df['zipcode'] = df['zipcode'].astype(str)

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    df = df.nlargest(3, 'price')[['zipcode', 'price', 'pct']]

    fig7 = px.bar(df, x='zipcode', y='price', text_auto='.2s', color='zipcode',
                  text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), template='simple_white',labels={'season': 'Estação',
                                                                                                                'price': 'Preço',
                                                                                                                'text': 'Percentual'})

    c7.plotly_chart(fig7, use_container_width=True, width=800, height=400)
    c7.write('Falso: Apenas o zipcode: 98039 é 30% mais caro do que a média, por ser uma região com vista para água')

    c8, c9 = st.columns((1, 1))

    # H8
    c8.subheader('H8: imoveis renovados sao 30% acima da media')

    df = data[['renovated', 'price']].groupby('renovated').mean(
    ).sort_values('price', ascending=True).reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig8 = px.bar(df, x='renovated', y='price', text_auto='.2s', color='renovated',
                  text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)), template='simple_white', labels={'renovated': 'renovado',
                                                                                                                'price': 'Preço',
                                                                                                                'text': 'Percentual'})

    c8.plotly_chart(fig8, use_container_width=True, width=800, height=400)
    c8.write('Verdadeiro: Imóveis renovados são 30% mais caros que imóveis não renovados')

    # H9 -
    c9.subheader(
        'H9: Imoveis com vista para água em Fevereiro são 40% mais baratos que agosto ')

    df1 = data.loc[(data['waterfront'] == 1) & (data['month'] == 2), [
        'price', 'month']].groupby('month').mean().reset_index()

    df2 = data.loc[(data['waterfront'] == 1) & (data['month'] == 8), [
        'price', 'month']].groupby('month').mean().reset_index()

    df = pd.concat([df1, df2]).sort_values('price', ascending=False)
    df['month'] = df['month'].astype(str)

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig9 = px.bar(df, x='month', y='price', text_auto='.2s',text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)),
                   color='month', template='simple_white',  labels={'month': 'Mês',
                                                                    'price': 'Preço',
                                                                    'text': 'Percentual'})

    c9.plotly_chart(fig9, use_container_width=True, width=800, height=400, )
    c9.write('Verdadeiros: Os imóveis de Fevereiro são cerca de 50% mais baratos do que Agosto')

    # H10
    st.subheader(
        'H10: Imóveis com 3 cômodos tem um crescimento MoM( Month over Month ) de 30%')

    df = data.loc[data['floors'] == 3, ['price', 'month_year']
                   ].groupby('month_year').mean().reset_index()

    df['diff'] = df['price'].diff(1)
    df.fillna(0,inplace=True)
    df['pct'] = round(df['diff']/df['price']*100, 2)

    fig9 = px.line(df, x='month_year', y='price',
                   text=df['pct'].apply(lambda x: '{0:1.2f}%'.format(x)),labels={'month_year': 'Mês do Ano',
                                                                                 'price': 'Preço',
                                                                                 'text': 'Percentual'}, 
                                                                                 template='simple_white')

    st.plotly_chart(fig9, use_container_width=True, width=800, height=400)
    st.write('Falso: Apenas em Janeiro de 2015 houve um crescimento acima da média')
    return None

def recomendacao(data,geofile):
     
    c10, c11 = st.columns((1, 1))
    

    # data filtering
    st.sidebar.title('Opção Comercial ')



    #dataframe compras
    df_compra = data[['id', 'zipcode','waterfront_is','season', 'lat','long', 'price', 'condition_type','yr_built','date']]
    df_compra['average price'] = df_compra.groupby(
        'zipcode')['price'].transform('mean')
    df_compra['status'] = df_compra.apply(lambda x:
                                          'compra' if x['condition_type'] == 'good' and
                                                      x['price'] - x['average price'] < 0 else 'não compra', axis=1)
    
    

    f_zipcode = st.sidebar.multiselect(
    'Filtrar pelo zipcode', df_compra['zipcode'].unique() )

    if (f_zipcode != []): 
        df_compra = df_compra.loc[df_compra['zipcode'].isin(f_zipcode)]
    elif (f_zipcode != []):
        df_compra = df_compra.loc[df_compra['zipcode'].isin(f_zipcode), :]
    else:
        df_compra = df_compra.copy() 


    f_status = st.sidebar.multiselect(
    'Sugestão de Compra', df_compra['status'].unique() )

    if (f_status != []): 
        df_compra = df_compra.loc[df_compra['status'].isin(f_status)]
    elif (f_zipcode != []):
        df_compra = df_compra.loc[df_compra['status'].isin(f_status), :]
    else:
        df_compra = df_compra.copy() 
 
 # filter
    min_price = int(df_compra['price'].min())
    max_price = int(df_compra['price'].max())
    avg_price = int(df_compra['price'].mean())

    f_price = st.sidebar.slider('Preço de Compra', min_price, max_price, avg_price)
    df_compra = df_compra.loc[df_compra['price'] < f_price]
    # dataframe vendas 
    
    df_venda = df_compra[['id', 'lat', 'long', 'zipcode', 'price', 'season']]
    df_venda['average price'] = df_compra.groupby( 'season')['price'].transform('mean')
    df_venda['preco_venda'] = df_venda.apply(lambda x:
                                             x['price']*1.10 if x['price'] > x['average price'] else x['price']*1.30, axis=1)
    df_venda['lucro'] = df_venda['preco_venda'] - df_venda['price']

    #show dataframe
    C11, C12 = st.columns((1, 1))
    
    c10.subheader('Recomendação de compra')
    c11.subheader('Recomendação de venda')
    
    c10.dataframe(df_compra[['id','zipcode','price','average price','condition_type','status']],width = 500)
    c11.dataframe(df_venda[['id','zipcode','season','average price','preco_venda','lucro']],width = 500)
    
    
    
    C11.metric(label = 'Total de Imóveis', value = np.round(df_compra['id'].count(),2) )
    C12.metric(label = 'Valor Custo Total', value = 'R$ {:,.0f}'.format(np.round(df_compra['price'].sum(),2) ))
 
    col1, col2 = st.columns(2)
    col1.metric(label = 'Valor Venda Total', value = 'R$ {:,.0f}'.format(np.round(df_venda['preco_venda'].sum(),0) ))
    col2.metric(label = 'Lucro Total', value = 'R$ {:,.0f}'.format(np.round(df_venda['lucro'].sum(),0) ))
    #C12.metric(label = 'Valor Venda Total', value = 'R$ {:,.0f}'.format(np.round(df_venda['preco_venda'].sum(),1) ) )
    

    # mapa_compra
    c13, c14 = st.columns((1, 1))

    c13.subheader('Imóveis para compra')


    houses = df_compra[['id','price','zipcode','status','lat','long','condition_type']]
    
    
    
    map = px.scatter_mapbox(houses, 
                             lat='lat', 
                             lon='long', 
                             hover_name='id',
                             hover_data = ['price','zipcode','condition_type'],
                             color = houses['status'].sort_values( ascending = True),
                             zoom=8.5, 
                             height=400)
    map.update_layout(mapbox_style="open-street-map")
    map.update_layout(height=500, width=500 ,margin={"r": 0, "t": 0, "l": 0, "b": 0})
    c13.plotly_chart(map)

    # densidade venda
    c14.subheader('Densidade imóveis para venda')

    dfmap2 = df_venda[['preco_venda', 'zipcode']].groupby(
        'zipcode').mean().reset_index()
    dfmap2.columns = ['ZIP', 'preco_venda']

    geofile = geofile[geofile['ZIP'].isin(dfmap2['ZIP'].tolist())]

    region_sell_map = folium.Map(location=[data['lat'].mean(),
                                           data['long'].mean()],
                                 default_zoom_start=15)

    region_sell_map.choropleth(data=dfmap2,
                               geo_data=geofile,
                               columns=['ZIP', 'preco_venda'],
                               key_on='feature.properties.ZIP',
                               fill_color='YlOrRd',
                               fill_opacity=0.7,
                               line_opacity=0.2,
                               legend_name='AVG SELL PRICE')

    with c14:
     folium_static(region_sell_map, height=500, width=500)

   
    


if __name__ == "__main__":
    # ETL
    # data extration
    path = 'kc_house_data.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
   
    geofile = get_geofile(url)
    data = get_data(path)

    # transformation
    data = set_feature(data)

    overview_data(data)

    recomendacao(data, geofile)
   
    hipoteses(data)

    

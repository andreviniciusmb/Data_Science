# Segmentação de mercado

<img src=imgs/segmentation.jpg widht=400 height=200>
A segmentação de mercado/clientes é importante para conhecer melhor o comportamento dos consumidores, desta maneira, as empresas podem focar melhor sua propaganda em determinado grupo e traçar novas estratégias de vendas, por exemplo.
<p>
Os dados usados neste trabalho foram coletados por <a href='https://www.kaggle.com/seetzz/market-segmentation'>Sheetharan Indurti</a> no site Kaggle. O dataset contém 10.000 entradas e 5 colunas ( reps - representando o representante da venda, product - produto, qty - quantidade de produtos da compra, revenue - receita da compra e region - região que foi efetuada a compra).
<p>
Para identificar a segmentação dos dados, foi utilizado o algoritmo de aprendizagem não supervisionada KMeans, e para escolher um possível número de clusters foi aplicado o método do cotovelo e a análise da silhueta. Ao aplicar tais métodos, foi visualizado que um possível melhor número de clusters é 4, chamados de cluster A, B, C e D. A seguir temos as características principais de cada grupo:
<ol>
  <li>Grupo A</li>
  Tamanho do grupo: 3.368</br>
  Qtd média de compras: 3</br>
  Regiões que se encontram: Leste e Sul</br>
  Preço média da receita:  90,5</br>
  <li>Grupo B</li>
  Tamanho do grupo: 3.408</br>
  Qtd média de compras: 2</br>
  Regiões que se encontram: Norte</br>
  Preço média da receita:  64,36</br>
  <li>Grupo C</li>
  Tamanho do grupo: 2.961</br>
  Qtd média de compras: 3</br>
  Regiões que se encontram: Oeste</br>
  Preço média da receita:  76,49</br>
  <li>Grupo D</li>
  Tamanho do grupo: 263</br>
  Qtd média de compras: 20</br>
  Regiões que se encontram: Norte e Oeste</br>
  Preço média da receita:  588,97</br>
</ol>

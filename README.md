# Project Scrapy ML

Este README fornece uma visão geral clara e detalhada do projeto, incluindo a arquitetura, a estrutura de diretórios, as instruções de instalação e uso, além dos módulos específicos para extração, transformação e visualização de dados.

Uma ETL em Python para Monitoramento de Preço de Carros do Mercado Livre.


### **Uma ETL em Python para Monitoramento de Preço**
Solução em Python para estratégias de pricing. Temos uma pipeline e uma ETL em Python que coleta, consolida e gera insights sobre Carros dentro do valor do 30K.


### **Arquitetura**
Uma ETL em Python para Web Scraping

* Extração - Scrapy
* Transformação e Load - DuckDB
* Dashboard - Streamlit
* Banco de dados - Postgres(DBeaver)

<table>
    <td>
    <img src="docs\arquitetura-local.png"
></img></td></tr>
</table>

### Estrutura de Diretórios
```
src/
├──── coleta/
│   ├──── spiders/
│   │   └──── mercadolivre.py
│   ├──── pipelines.py
│   ├──── items.py
│   └──── settings.py
|
├──── transformacao/
│   └──── main.py
|
├──── dashboard/
│   └──── app.py
|
├──── scrapy.cfg
├──── requirements.txt
└──── README.md
```

### **Caso de Uso**
Para rodar o webscraping

- O bash precisa estar dentro do dir `src/` para a execução.
 
```bash
$ scrapy crawl mercadoLivre -o ../data/data.jsonl
```


- Para rodar a transformação com o duckdb, é preciso executar o comando abaixo, na seguinte pasta `src`.
```bash
$ python transformacao/main.py
```


- Para Executar o Dashboard, é preciso executar o comando abaixo, na seguinte pasta `src`.
```bash
$ streamlit run dashboard/app.py
```
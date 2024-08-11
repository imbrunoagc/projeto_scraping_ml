# projeto_scraping_ml

Para rodar o webscraping

- O bash precisa estar dentro do dir `src/` para a execução.
 
```bash
$ scrapy crawl mercadoLivre -o ../data/data.jsonl
```


- Para rodar a transformação com o duckdb, é preciso executar o comando abaixo, na seguinte pasta `src`.
```bash
$ python transformacao/main.py
```


-- Para Executar o Dashboard, é preciso executar o comando abaixo, na seguinte pasta `src`.
```bash
$ streamlir run dashboard/app.py
```
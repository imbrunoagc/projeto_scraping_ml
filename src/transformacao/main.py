import pandas as pd
import duckdb
from datetime import datetime

# Ler os dados do arquivo JSONL
#df = duckdb.read_json('data/data.jsonl',  format = 'newline_delimited')
conn = duckdb.connect('data/output.db')
conn.execute("""
CREATE TABLE mercadolivre_item_carros AS 
SELECT 
    *, 
    'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/_PriceRange_0-30000' AS _source,
    current_date() AS _date_extract
FROM 
    read_json_auto('data/data.jsonl');
""")

conn.close()
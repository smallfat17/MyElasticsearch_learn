from elasticsearch_dsl import connections,Search
from elasticsearch import Elasticsearch
import json
# connections.create_connection(alias = "my_connection",hosts = ['localhost'],timeout = 20)

client = Elasticsearch(["http://192.168.43.18:9200"])
s = Search(using=client,doc_type="tweet").query("match",date="2014-09-24")

response = s.execute()

for hit in response:
    print(hit)
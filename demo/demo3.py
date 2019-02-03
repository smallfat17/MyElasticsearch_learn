# coding=utf-8
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['192.168.43.18'])

s = Search(index='steam',doc_type='game').query("match",Cname='孤岛惊魂')
response = s.execute()

for hit in response:
    print(hit.Cname)
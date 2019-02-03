# coding=utf-8
from datetime import datetime
from elasticsearch_dsl import Document,Date,Integer,Keyword,Text,Float
from elasticsearch_dsl.connections import connections
from pymongo import MongoClient
import re
connections.create_connection(hosts=['192.168.43.18'])

class Game(Document):
    Cname = Text(analyzer='ik_max_word')
    Ename = Text(analyzer='english')
    developer = Keyword()
    publisher = Keyword()
    pub_date = Date()
    game_type = Keyword()
    station = Keyword()
    lang = Keyword()
    label = Keyword()

    class Index:
        name = 'steam'
        doc_type = 'game'
        settings = {
            "number_of_shards": 2,
        }

    class Meta:
        doc_type = 'game'

    def is_published(self):
        return datetime.now() >= self.pub_date

def put_game(Cname,Ename,developer,publisher,pub_date,game_type,station,lang,label):
    game = Game(Cname=Cname,developer=developer,publisher=publisher,label=label, pub_date=pub_date,game_type=game_type,station=station,lang=lang)
    if Ename:
        game.Ename = Ename[0]
    game.save()


if __name__ == '__main__':
    mongoclient = MongoClient(host='master')
    database = mongoclient.test
    database.authenticate("jmw", "jmw123")
    coll = database.game
    Game.init()
    for one in coll.find():
        label = one['label']
        labels = []
        for l in re.split('[\',\[\]]+?', label):
            if l != '' and l != ' ':
                labels.append(l)
        put_game(one['Cname'],one['Ename'],one['developer'],one['publisher'],one['pub_date'],one['game_type'],one['station'],one['lang'],labels)






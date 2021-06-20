# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"
from pymongo import MongoClient
import requests
import json
from configparser import ConfigParser

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 

class ValidaTituloBusca(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_pesquisa_form"
    
    def validate_pesquisa(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        pesquisa = slot_value

        print(pesquisa)
        
        #Lendo o arquivo de configuração, que irá proteger a chave da API
        config = ConfigParser()
        config.read('config.ini')

        #O mongo por padrão esta conectado na porta 27017
        client = MongoClient('localhost', 27017)
        db = client.YoutubeResultados
        
        def mostrar_resultado(video):
            dispatcher.utter_message(image=(video['Thumbnail']))
            dispatcher.utter_message(text=(video['TituloDoVideo']))
            dispatcher.utter_message(text=('https://www.youtube.com/watch?v=' + video['VideoId']))

        # Checando se a pesquisa existe no mongo
        if db.resultados.count_documents({'CacheKey':pesquisa}) > 0:
            print('Essa pesquisa já existe na nossa cache!')
            print(slot_value)
            resultado_do_banco = db.resultados.find({'CacheKey': pesquisa})
            
            for item in resultado_do_banco:
                dispatcher.utter_message(text=mostrar_resultado(item)) 
                
        else:
            # Se a pesquisa não existe no mongo, será feito a busca direto da api
            # parametros para serem usados no request
            params = {
                'key': config['YOUTUBE_API']['apiKey'], 
                'part': 'snippet', 
                'q': pesquisa,
                'type' : 'video'
            }
            
            request = requests.get(
                config['YOUTUBE_API']['url'], 
                params=params
            ).json()
            print(slot_value)
            print('Dados buscado direto da API do Google!')
            
            for item in request['items']:
            
                video = {
                    'CacheKey': pesquisa,
                    #Em uma aplicação web pode ser usada a thumbnail
                    'Canal' : item['snippet']['channelTitle'],
                    'VideoId' : item['id']['videoId'],
                    'Thumbnail' : item['snippet']['thumbnails']['medium']['url'],
                    'TituloDoVideo' : item['snippet']['title'],
                    'Descricao' : item['snippet']['description']
                }

            db.resultados.insert_one(video)
            dispatcher.utter_message(text=mostrar_resultado(video))  
        
        return {}
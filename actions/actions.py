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

class ValidaNomeForm(FormValidationAction):
    """Verifica o nome do usuário"""

    ##### Nome do form para o Rasa
    def name(self) -> Text:
        """Identifica o form na estória do Rasa."""
        return "validate_nome_form"

    ##### Validação do nome
    def validate_nome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valida nome."""

        print("NOME")
        print(slot_value)
        nome = slot_value
        sai = tracker.get_slot("senderid")
        if(sai == None):
            volta = "!"
            sai = tracker.sender_id
        else:
            volta = ", fico feliz com tua volta!"

        texto = "Olá "+nome+volta
        dispatcher.utter_message(text=texto)

        return {"nome": nome, "senderid": sai}


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
        config = ConfigParser()
        config.read('config.ini')

        #O mongo por padrão esta conectado na porta 27017
        client = MongoClient('localhost', 27017)
        db = client.YoutubeResultados
        
        def mostrar_resultado(video):
            dispatcher.utter_message(text=('Título: ' + video['TituloDoVideo']))
            dispatcher.utter_message(text=('Url: https://www.youtube.com/watch?v=' + video['VideoId']))
            dispatcher.utter_message(text=('================================================================================'))
        
        if db.resultados.count_documents({'CacheKey':pesquisa}) > 0:
            print('Essa pesquisa já existe na nossa cache!')
            print(slot_value)
            resultado_do_banco = db.resultados.find({'CacheKey': pesquisa})

            for item in resultado_do_banco:
                dispatcher.utter_message(text=mostrar_resultado(item)) 
                
        else:
            
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
                    'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
                    'TituloDoVideo' : item['snippet']['title'],
                    'Descricao' : item['snippet']['description']
                }

            db.resultados.insert_one(video)
            dispatcher.utter_message(text=mostrar_resultado(video))  
        
        return {}
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from pymongo import MongoClient
import pymongo
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#criando# 
hostname = "mongodb://localhost:27017/"
banco = "covid-19"
collection = "dino"
url = "https://covid19-brazil-api.vercel.app/api/report/v1?fbclid=IwAR0aJUgRlTxnHkXoVoVzdWaxuoZL1oIrMQaBT4oi8vU91-g4sTfol2dKsKU.json"

site = requests.get(url)
#gravando#
meuCliente = pymongo.MongoClient(hostname)
meubanco = meuCliente[banco]
minhaColecao = meubanco[collection]
minhaColecao.insert_one(site.json())
# Formulário 
class ValidaNomeForm(FormValidationAction):
    """Verifica o nome do usuário"""

    # Nome do form para o Rasa
    def name(self) -> Text:
        """Identifica o form na estória do Rasa."""
        return "validate_nome_form"

    # Validação do nome
    def validate_nome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valida nome."""

class ActionHelloWorld(Action):
   
    def name(self) -> Text:
        return "action_ola!"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Bem vindo!")

        return []

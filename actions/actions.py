# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 

import requests
import pymongo

envs = ['capsules', 'dragons', 'info']

apiCompleta = {}
hostname = "mongodb://localhost:27017/"
banco = "spacex"

meuCliente = pymongo.MongoClient(hostname)
minhaDatabase = meuCliente[banco]

minhaColecaoCapsulas = minhaDatabase[envs[0]]
minhaColecaoDragons = minhaDatabase[envs[1]]
minhaColecaoInfo = minhaDatabase[envs[2]]

class capturaMongo(Action):

    def name(self) -> Text:
        return "consulta_mongo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        for env in envs:
            url = "https://api.spacexdata.com/v3/" + env
            apiCompleta[env] = requests.get(url)

        minhaColecaoCapsulas.insert_many(apiCompleta[envs[0]].json())
        minhaColecaoDragons.insert_many(apiCompleta[envs[1]].json())
        minhaColecaoInfo.insert_one(apiCompleta[envs[2]].json())

        return []


class ValidaNomeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_option_form"

    def validate_option(self, slot_value: Any, dispatcher: CollectingDispatcher, 
        tracker: Tracker,
        domain: DomainDict,) -> Dict[Text, Any]:

        print("Opção: " + slot_value)
        option = slot_value

        if str(option) == str(envs[2]):

            retorno = minhaColecaoInfo.find_one()

            texto = "Nome da empresa: " + retorno['name']
            texto += "\n"
            texto += "Fundador: " + retorno['founder']
            texto += "\n"
            texto += "Endereço: " + retorno['headquarters']['address'] + " "
            texto += "- Cidade: " + retorno['headquarters']['city'] + " "
            texto += "- Estado: " + retorno['headquarters']['state'] + " "

            dispatcher.utter_message(text = texto)
            texto = ""
        
        if str(option) == str(envs[1]):

            retorno = minhaColecaoDragons.find_one()

            texto = "Nome da Dragon: " + retorno['name']
            texto += "\n"
            texto += "Tipo: " + retorno['type']
            texto += "\n"
            texto += "Descrição: " + retorno['description']


            dispatcher.utter_message(text = texto)
            texto = ""

        if str(option) == str(envs[0]):

            retorno = minhaColecaoCapsulas.find_one()

            texto = "Nome da Capsula: " + retorno['capsule_id']
            texto += "\n"
            texto += "Status: " + retorno['status']
            texto += "\n"
            texto += "Tipo da capsula: " + retorno['type']
            texto += "\n"
            texto += "Detalhes da capsula: " + retorno['details']

            dispatcher.utter_message(text = texto)
            texto = ""

        return {"option" : option}

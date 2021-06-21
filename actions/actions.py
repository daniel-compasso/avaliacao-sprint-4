# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 
import requests

import json
import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017) 
db     = client.jbassi_avaliacao4

class ActionPegandoDB(Action):

    def name(self) -> Text:
        return "action_pegando_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        if db.digimons.count_documents({})> 0:
            print("O bando de dados ja existe\n")
        else:
            request = requests.get('https://digimon-api.herokuapp.com/api/digimon')
            todos   = json.loads(request.content)
            db.digimons.insert_many(todos)
            print("Dados salvos!")

        return []

# pegando nome do digimon

class ValidaNomeForm(FormValidationAction):
    """Verifica o nome do usuário"""

    def name(self) -> Text:
        """Identifica o form na estória do Rasa."""
        return "validate_nome_form"

    def validate_nome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(slot_value)
        nome = slot_value

        dispatcher.utter_message(text='Você quer fotos do '+ nome)

        link = 'https://digimon.shadowsmith.com/img/'
        imagem_digimon = link + nome.lower() + ''.join('.jpg')

        dispatcher.utter_message(text=f'Aqui está:')
        dispatcher.utter_message(image=imagem_digimon)

        return ''

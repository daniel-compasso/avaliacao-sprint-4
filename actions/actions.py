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


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_get_card"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        print("Olá mundo funcionou!")

        return []

##################### Formulário para pegar o nome do usuário

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

        url = "https://api.hearthstonejson.com/v1/86314/enUS/cards.json"
        json_data = requests.get(url).json()
        client = pymongo.MongoClient("localhost", 27017)
        name = "hs"
        db = client[name]
        collection = db[name]
        
        print("NOME")
        print(slot_value)
        nome = slot_value

        names = [k['name'] for k in json_data]
        for i in range(len(names)):
            if nome == names[i]:
                if json_data[i]['type'] == 'MINION':
                    card = f"""
                    Ataque : {json_data[i]['attack']}
                    Vida : {json_data[i]['health']}
                    Custo : {json_data[i]['cost']}
                    Classe : {json_data[i]['cardClass']}
                    Mecânica : {json_data[i]['mechanics']}
                    Raridade : {json_data[i]['rarity']}
                    Tipo : {json_data[i]['type']}
                    """
                    break
                elif json_data[i]['type'] == 'SPELL':
                    card = f"""
                    Classe : {json_data[i]['cardClass']}
                    Custo : {json_data[i]['cost']}
                    Raridade : {json_data[i]['rarity']}
                    Tipo : {json_data[i]['type']}
                    """
                    break
                elif json_data[i]['type'] == 'WEAPON':
                    card = f"""
                    Ataque : {json_data[i]['attack']}
                    Durabilidade : {json_data[i]['durability']}
                    Custo : {json_data[i]['cost']}
                    Classe : {json_data[i]['cardClass']}
                    Raridade : {json_data[i]['rarity']}
                    Tipo : {json_data[i]['type']}
                    """
                    break
                else:
                    dispatcher.utter_message(text="Desculpa, não entendi.")
        
        dispatcher.utter_message(text=card)
    
        return {"nome" : nome}

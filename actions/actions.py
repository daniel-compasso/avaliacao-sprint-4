# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import pymongo
import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

url = "https://retoolapi.dev/7IRN2r/data"

api = requests.get(url)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["API"]
mycol = mydb["Sprint"]

mycol.insert_many(api.json())

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        print("Olá mundo funcionou")

        return []

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
        
        name = api.json()
        nomes = [['NOME'] for i in api]
        for x in range(len(nomes)):
            if name == nomes[x]:
                if API[x]['type'] == 'Objetos':
                    dados_pessoais = f"""
                    ID: {id}
                    NOME: {name}
                    """
                
        return {"nome": nomes }
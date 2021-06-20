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
import urllib.request as consulta 
import json
from pymongo import MongoClient
import pymongo

class ActionBemVindo(Action):

    def name(self) -> Text:
        return "action_bem_vindo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Esse é nosso bot Busca Cep , vamos começar ?")

        print("Esse é nosso bot Rasa, vamos começar ?")

        return []


class ValidaNomeForm(FormValidationAction):
    
    def name(self) -> Text:
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
        sai = tracker.get_slot("senderid")
        if(sai == None):
            volta = "!"
            sai = tracker.sender_id
        else:
            volta = ", fico feliz com tua volta!"

        return {"nome": nome}

class ValidaCepForm(FormValidationAction):
    """Verifica o nome do usuário"""

    def name(self) -> Text:
        return "validate_cep_form"

    def validate_cep(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(slot_value)
        cep = slot_value
        try:
            #consutando a api do via cep
            resultadocep = cep
            resultadocep = resultadocep.replace('-','').replace('.','').replace(' ','').replace('_','').replace('/','').replace('*','')
            site = 'https://viacep.com.br/ws/%s/json/' % resultadocep
            cabecalho = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
            requisicao = consulta.Request(
                site, headers=cabecalho, method='GET') 
            cliente = consulta.urlopen(requisicao)
            retornoconsulta = cliente.read().decode('utf-8')
            cliente.close()
            endereco = json.loads(retornoconsulta) 

            # consutando informações de cada elemento

            rua = "Endereço: "+endereco['logradouro']
            bairro = "Bairro: "+endereco['bairro']
            cidade = "Cidade: "+endereco['localidade']

            # conversando os uf com nome do estado mais sigla
            if endereco['uf'] == 'SP':
                uf = "Estado: São Paulo - SP"
            elif endereco['uf'] == 'MG':
                uf = "Estado: Minas Gerais - MG"
            elif endereco['uf'] == 'RJ':
                uf = "Estado: Rio de Janeiro - RJ"
            elif endereco['uf'] == 'BA':
                uf = "Estado: Bahia - BA"
            elif endereco['uf'] == 'RS':
                uf = "Estado: Rio Grande do Sul - RS"
            elif endereco['uf'] == 'PR':
                uf = "Estado: Paraná - PR"
            elif endereco['uf'] == 'PE':
                uf = "Estado: Pernambuco - PE"
            elif endereco['uf'] == 'CE':
                uf = "Estado: Ceará - CE"
            elif endereco['uf'] == 'PA':
                uf = "Estado: Pará - PA"
            elif endereco['uf'] == 'MA':
                uf = "Estado: Maranhão - MA"
            elif endereco['uf'] == 'SC':
                uf = "Estado: Santa Catarina - SC"
            elif endereco['uf'] == 'GO':
                uf = "Estado: Goiás - GO"
            elif endereco['uf'] == 'PB':
                uf = "Estado: Paraíba - PB"
            elif endereco['uf'] == 'ES':
                uf = "Estado: Espírito Santo - ES"
            elif endereco['uf'] == 'AM':
                uf = "Estado: Amazonas - AM"
            elif endereco['uf'] == 'RN':
                uf = "Estado: Rio Grande do Norte - RN"
            elif endereco['uf'] == 'AL':
                uf = "Estado: Alagoas - AL"
            elif endereco['uf'] == 'PI':
                uf = "Estado: Piauí - PI"
            elif endereco['uf'] == 'MT':
                uf = "Estado: Mato Grosso - MT"
            elif endereco['uf'] == 'DF':
                uf = "Estado: Distrito Federal - DF"
            elif endereco['uf'] == 'MS':
                uf = "Estado: Mato Grosso do Sul - MS"
            elif endereco['uf'] == 'SE':
                uf = "Estado: Sergipe - SE"
            elif endereco['uf'] == 'RO':
                uf = "Estado: Rondônia - RO"
            elif endereco['uf'] == 'TO':
                uf = "Estado: Tocantins - TO"
            elif endereco['uf'] == 'AC':
                uf = "Estado: Acre - AC"
            elif endereco['uf'] == 'AP':
                uf = "Estado: Amapá - AP"
            elif endereco['uf'] == 'RR':
                uf = "Estado: Roraima - RR"
            else:
                uf = "Estado: Não Consta" 

            #imprimindo informações na tela do bot
            dispatcher.utter_message(text=rua)
            dispatcher.utter_message(text=bairro)
            dispatcher.utter_message(text=cidade)
            dispatcher.utter_message(text=uf)


            # Gravando dados no mongo db
            cliente = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.rrlac.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            banco = cliente['BuscaCep']  # buscando o nome do banco
            gravando = banco["Consultas"]  # buscando a tebale do banco

            dados = {
                    "Endereço:": endereco['logradouro'],
                    "Bairro:": endereco['bairro'],
                    "Cidade:": endereco['localidade'],
                    "Estado:": endereco['uf'],
                }

            if not gravando.find_one(dados):       
                gravando.insert_one(dados)
                print(f"Gravado com sucesso: - {dados}")
            else:
                print(f'Já Existe')

        except:
            dispatcher.utter_message(text='Desculpa tente novamente!')


        
        




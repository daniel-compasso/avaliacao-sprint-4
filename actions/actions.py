from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 
import requests
import pymongo

#criando banco e coleções
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BOT_SW"]
col_filmes = mydb["filmes"]
col_pessoas = mydb["pessoas"]
col_planetas = mydb["planetas"]
col_especies = mydb["especies"]
col_naves = mydb["naves"]
col_veiculos = mydb["veiculos"]

#lista de opções
options = ['films', 'people', 'planets',
           'species', 'starships', 'vehicles']

# essa classe conecta com a api e salva dados no bd
class api(Action):
    def name(self) -> Text:
        return "consulta_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ##listas para armazenar dados da api
        dic_filmes = []
        dic_pessoas = []
        dic_planetas = []
        dic_especies = []
        dic_naves = []
        dic_veiculos = []

        #verifica se os dados já foram cadastrados no mongodb
        if col_filmes.find_one():
            print('Dados já cadastrados')
        else:
        ##coletando dados e armazenando no mongodb
            for option in options:
                sw_info = requests.get(f'https://swapi.dev/api/{option}/?format=json')
                dados = sw_info.json()

                if option == 'films':
                    for filme in dados['results']:
                        dic = {"Tipo": option, "Titulo": filme['title'],
                            "Episódio": filme['episode_id'], "Data de lançamento": filme['release_date']}
                        dic_filmes.append(dic)
                    if not col_filmes.find_one({"Filmes": dic_filmes}):  
                        col_filmes.insert_one({"Filmes": dic_filmes})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

                elif option == 'people':
                    for pessoa in dados['results']:
                        dic = {"Tipo": option, "Nome": pessoa['name'],
                            "Altura": pessoa['height'], "Peso": pessoa['mass']}
                        dic_pessoas.append(dic)
                    if not col_pessoas.find_one({"Pessoas": dic_pessoas}):  
                        col_pessoas.insert_one({"Pessoas": dic_pessoas})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

                elif option == 'planets':
                    for planeta in dados['results']:
                        dic = {"Tipo": option, "Nome": planeta['name'], "Clima": planeta['climate'],
                            "Diâmetro": planeta['diameter'], "Gravidade": planeta['gravity']}
                        dic_planetas.append(dic)
                    if not col_planetas.find_one({"Planetas": dic_planetas}):  
                        col_planetas.insert_one({"Planetas": dic_planetas})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

                elif option == 'species':
                    for especie in dados['results']:
                        dic = {"Tipo": option, "Nome": especie['name'], "Classificação": especie['classification'],
                            "Idioma": especie['language'], "Média de peso": especie['average_height']}
                        dic_especies.append(dic)
                    if not col_especies.find_one({"Especies": dic_especies}):  
                        col_especies.insert_one({"Especies": dic_especies})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

                elif option == 'starships':
                    for nave in dados['results']:
                        dic = {"Tipo": option, "Nome": nave['name'], "Modelo": nave['model'],
                            "Valor": nave['cost_in_credits'], "Passageiros": nave['passengers'], "Capacidade de carga": nave['cargo_capacity']}
                        dic_naves.append(dic)
                    if not col_naves.find_one({"Naves": dic_naves}):  
                        col_naves.insert_one({"Naves": dic_naves})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

                elif option == 'vehicles':
                    for veiculo in dados['results']:
                        dic = {"Tipo": option, "Nome": veiculo['name'], "Modelo": veiculo['model'],
                            "Valor": veiculo['cost_in_credits'], "Passageiros": veiculo['passengers'], "Classe": veiculo['vehicle_class']}
                        dic_veiculos.append(dic)
                    if not col_veiculos.find_one({"Veículos": dic_veiculos}):  
                        col_veiculos.insert_one({"Veículos": dic_veiculos})
                        print(f"Salvo com sucesso!")
                    else:
                        print(f'Já Existe')

        return []

#essa classe cria o menu para escolhas
class menu(Action):
    def name(self) -> Text:
        return "cria_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='''
[1] - Para escolha dos Filmes
[2] - Para escolha das Pessoas
[3] - Para escolha dos Planetas
[4] - Para escolha das Espécies
[5] - Para escolha das Naves
[6] - Para escolha dos Veículos''')

        return []

#classe para coletar a opção do slot e coletar dados do mongodb
class dados(FormValidationAction):
    def name(self) -> Text:
        """Identifica o form na história do Rasa."""
        return "validate_option_form"
    
    def validate_option(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print("OPTION")
        print(slot_value)
        option = slot_value
        sai = tracker.get_slot("senderid")

        ## Imprimindo valores do mongodb
        if option == '1':
            for x in col_filmes.find():
                for i in x["Filmes"]:
                    dispatcher.utter_message(text=f'''Título: {i["Titulo"]}
Episódio: {i["Episódio"]}
Data de lançamento: {i["Data de lançamento"]}
''')
        elif option == '2':
            for x in col_pessoas.find():
                for i in x["Pessoas"]:
                    dispatcher.utter_message(text=f'''Nome: {i["Nome"]}
Altura: {i["Altura"]}
  Peso: {i["Peso"]}
''')
        elif option == '3':
            for x in col_planetas.find():
                for i in x["Planetas"]:
                    dispatcher.utter_message(text=f'''Nome: {i["Nome"]}
Clima: {i["Clima"]}
Diâmetro: {i["Diâmetro"]}
Gravidade: {i["Gravidade"]}
''')       
        elif option == '4':
            for x in col_especies.find():
                for i in x["Especies"]:
                    dispatcher.utter_message(text=f'''Nome: {i["Nome"]}
Classificação: {i["Classificação"]}
Idioma: {i["Idioma"]}
Média de peso: {i["Média de peso"]}
''')
        elif option == '5':
            for x in col_naves.find():
                for i in x["Naves"]:
                    dispatcher.utter_message(text=f'''Nome: {i["Nome"]}
Modelo: {i["Modelo"]}
Valor: {i["Valor"]}
Passageiros: {i["Passageiros"]}
Capacidade de carga: {i["Capacidade de carga"]}
''')
        elif option == '6':
            for x in col_veiculos.find():
                for i in x["Veículos"]:
                    dispatcher.utter_message(text=f'''Nome: {i["Nome"]}
Modelo: {i["Modelo"]}
Valor: {i["Valor"]}
Passageiros: {i["Passageiros"]}
Classe: {i["Classe"]}
''')
        else:
            dispatcher.utter_message(text="valor incorreto!!!")
    
        return {"option": option, "senderid": sai}

# Avaliação sprint 4 - Caio Gabriel Ferreira

## Pré requisitos

* Python3
* pip
* Rasa
* Spacy
* Mongo DB ()
* Pymongo
* Sua IDE/Editor de texto favorito

## Obtendo uma chave da API do YouTube

### Criando um projeto no google cloud

link: https://cloud.google.com



* Vá até à página da Google cloud e no canto * superior direito, clique na opção Console;

* No canto superior, vai haver uma opção para * selecionar ou criar um projeto do Google Cloud;

* Após criar um projeto, no menu do canto * esquerdo, selecione APIs e serviços e depois * Credenciais;

* Nessa página, terá uma opção de criar uma credencial, nessa opção, deve selecionar Chave de API. Essa opção irá gerar uma chave de API para ser usada em seu projeto.

### Validando a chave da API

* Selecione a opção de biblioteca no canto esquerdo da página e no campo de busca que se abrir, digite YouTube;

* Dentre as opções que aparecer, selecione YouTube Data API v3 e clique em habilitar para poder ter acesso à API.

## Criando arquivo de configuração

* Crie um arquivo na raiz do projeto chamado config.ini seguindo a estrutura abaixo, apenas modificando o que for necessário.

```py
[YOUTUBE_API]
apiKey = <<Aqui vai a sua chave gerada do google cloud>>
url = https://www.googleapis.com/youtube/v3/search
```

## Rodando o projeto

* O primeiro passo é treinar o modelo executando o comando :
```
rasa train
```

* Agora, vamos rodar o servidor do rasa:
```
rasa run actions
```

* Agora, para conversar com o bot, você pode executar o comando abaixo e conversar com ele por linha de comando:
```
rasa shell
```

* Também é possível conversar com o web através de um web chat. Para isso, você deve executar o comando abaixo

```
rasa run -m models --enable-api --cors "*" --debug
```

* Depois de executar esse comando, vá até a pasta public do projeto e abra o arquivo index.html no seu navegador

## Desenvolvimento

* Os arquivos .yml, será onde as respostas do bot, intenções, ações e fluxo irão ser construidos.

### nlu.yml

* O nlu, é onde irá ficar as intenções. Ou seja, é o que o usuário irá escrever para o bot.

Exemplos:

```
nlu:
- intent: greet
  examples: |
    - Ei
    - Olá
    - Oi
    - Fala ae
    - Eae
    - Oiee
    - oi
- intent: goodbye
  examples: |
    - Tchau
    - Até mais
    - Flw
    - adeus
    - Até mazes
    - Fui
```

### domain.yml

* O arquivo domain.yml, é onde irá ser declarado as respostas do bot, as ações, slots para armazenar as informações e o formulário

Exemplo:

```
# Respostas do bot
responses:
  utter_ask_pesquisa:
  - text: Qual video gostaria de ver?
  utter_ask_pesquisa_novamente:
  - text: Gostaria de ver mais algum outro video?

# Formulário para fazer a pesquisa no YouTube
forms:
  pesquisa_form:
    required_slots:
      pesquisa:
      - type: from_text
        entity: pesquisa


actions:
- utter_ask_pesquisa_novamente
- utter_goodbye
- utter_iamabot
- utter_show_result
- utter_desculpa

slots:
  pesquisa:
    type: text
    influence_conversation: true
```

### stories.yml e rules.yml

* O stories, vai ser o fluxo que será tomado durante a conversa do bot com o usuário

O exemplo abaixo, mostra uma apresentação do bot para o usuário:

```
- story: apresentacao
  steps:
  - intent: greet
  - action: utter_iamabot
  - intent: goodbye
  - action: utter_goodbye
```

* O rules, é a regra para executar tal ação. No exemplo abaixo, verá uma regra para que seja acessado a despedida do bot, e a apresentação do bot:

```
- rule: Say goodbye anytime the user says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye

- rule: Say 'I am a bot' anytime the user challenges
  steps:
  - intent: bot_challenge
  - action: utter_iamabot
```

### Actions:

* A action, é onde irá ficar a programação em python.

* No caso desse projeto, vamos criar uma ação, para que quando o usuário fizer uma pesquisa de um video, o bot vai acessar a API do YouTube e armazenar os dados no MongoDB

* Caso o usuário digite o mesmo video, será acessado os dados armazenados direto do mongo, e não irá consultar a API do YouTube denovo.

* A programação é feita normalmente, porém, a variavel de pesquisa, será um slot

* Para que o resultado seje mostrado no chatbot, no lugar de print, deve ser usado:

```py 
dispatcher.utter_message(text='...')
```

* No caso do YouTube, pode retornar a thumbnail do video também, para isso, ao invez de text, use image.

```py
dispatcher.utter_message(image=(video['Thumbnail']))
```


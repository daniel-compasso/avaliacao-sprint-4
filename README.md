# Chatbot com Rasa

Este bot retorna a temperatura. Exemplos de perguntas:
- o dia está ensolarado no Rio de Janeiro?
- vai chover hoje São Paulo?

Para realização desse chatboot foi necessário criar uma conta no website (https://openweathermap.org/) e (https://developer.tomtom.com/), para ter acesso as devidas KEY das APi, para poder coletar as informações do clima e coordenadas geográficas de cada local mencionado.

Após conseguir as keys adicionar no arquivo actions.py dentro das variaveis openweathermap_KEY e tomtom_KEY

Este bot atende os seguintes requisitos:

Os comandos para execução foram:
rasa train
rasa run actions (Manter)

Aberto outro cmd e executado:
Rasa shell 

Ou se preferir no webchat por:
rasa run -m models --enable-api --cors "*" --debug

Após isto, foi aberto o arquivo index.html.



# Chatbot com Rasa

Este bot retorna a temperatura. Exemplos de perguntas:
- o dia está ensolarado no Rio de Janeiro?
- vai chover hoje São Paulo?


Para realização desse chatboot foi necessário criar uma conta no website (https://openweathermap.org/) e (https://developer.tomtom.com/), para ter acesso as devidas KEY das APi, para poder coletar as informações do clima e coordenadas geográficas de cada local mencionado.

Este bot atende os seguintes requisitos:
-Com base no trabalho da primeira Sprint (https://github.com/daniel-compasso/avaliacao-sprint-1), crie um chatbot para consulta às informações disponibilizadas no banco de dados MongoDB. Caso o trabalho já seja voltado a questões,
-Ao iniciar o bot, obtenha os dados da api e grave no banco;
-O bot deve ser implementado em Rasa e deve usar o Spacy em Português;
-O bot deve estar preparado para responder a qualquer momento qual é sua função e responde caso não entende o que foi solicitado.
-Deve ser possível usar como webchat. 

Os comandos para execução foram:
rasa train
rasa run actions (Manter)

Aberto outro cmd e executado:
Rasa shell 

Ou se preferir no webchat por:
rasa run -m models --enable-api --cors "*" --debug

Após isto, foi aberto o arquivo index.html.


Entrega: 20/06/2021

Criar uma branch no repositório com o nome avalicao-nome-sobrenome (Exemplo: avaliacao-daniel-muller);
Subir o desafio na branch com um readme.md, explicando sobre o que foi feito no desafio;
Subir o desafio até às 13h do dia 21/06/2021 neste repositório (https://github.com/daniel-compasso/avaliacao-sprint-4/).
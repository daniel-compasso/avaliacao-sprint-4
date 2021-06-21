# avaliacao-sprint-4
![rasa-4](https://user-images.githubusercontent.com/26391241/122766670-33afcd80-d278-11eb-97e2-8e7723290719.png)


## Como usar Rasa Chatbot
1. Treine um modelo Rasa Open Source contendo os modelos Rasa NLU e Rasa Core executando:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.

2. Execute um servidor de ação Rasa SDK com
    ```
    rasa run actions
    ```
Inicie o servidor Rasa em uma terceira janela do console:
   ```
   rasa run --enable-api
   ```

Você pode então enviar mensagens para o bot por meio do endpoint do canal de retorno de chamada:
   ```
   curl -XPOST http://localhost:5005/webhooks/callback/webhook \
      -d '{"sender": "tester", "message": "hello"}' \
      -H "Content-type: application/json"
      

Para obter mais informações sobre os comandos individuais, verifique nossa
[documentação](http://rasa.com/docs/rasa/command-line-interface).

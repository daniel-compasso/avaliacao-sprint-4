# avaliacao-sprint-4
Projetos chatbot Rasa
![rasa-4](https://user-images.githubusercontent.com/26391241/122766670-33afcd80-d278-11eb-97e2-8e7723290719.png)


## Como usar Rasa Chatbot
1. Train a Rasa Open Source model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.

2. Run a Rasa SDK action server with
    ```
    rasa run actions
    ```

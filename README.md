# desafiobackend

```
desafiobackend
├── application
│   ├── Dockerfile
│   ├── db.sqlite3
│   ├── impusers
│   │   └── [..]
│   ├── manage.py
│   ├── picpay
│   │   └── [..]
│   └── requirements.txt
├── data
│   ├── users.csv
│   ├── lista_relevancia_1.txt
│   └── lista_relevancia_2.txt
├── docker-compose.yml
└── init.sql
```

1 - Entrar na pasta desafiobackend


2 - executar `docker-compose pull`, isso vai puxar a imagem da aplicação;


3 - executar `docker-compose up`, isso vai levantar os 2 containers, o do banco de dados que importará os dados da pasta data e em seguida o container da aplicação, é necessáro aguardar o processo de importação terminar;

4 - após a conclusão do processo de importação, você poderá acessar a aplicação na url [`http://127.0.0.1:8883/admin/`](http://127.0.0.1:8883/admin/) ou a API na url [`http://127.0.0.1:8884/api/`](http://127.0.0.1:8884/api/);

Obs1: o arquivo users.csv está com apenas 200 linhas, é necessário baixar o original [users.csv.gz], descompactar e subsitituir na pasta data, antes de executar o passo item 3;

Obs2: a url da API possui um painel que pode ajudar a construir a url de consultas, mas caso deseje acesso direto à API para consultar 1 nome, utilize http://127.0.0.1:8884/api/importedUsers/search/findByNameIgnoreCaseContainingOrderByPriority?name=Wallysson , onde o ultimo parâmetro é o nome procurado

Obs3: o retorno está acontecendo no padrão Hypermedia (HAL), padrão HATEOAS.

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

4 - após a conclusão do processo de importação, você poderá acessar a aplicação na url [`http://127.0.0.1:8883/admin/`](http://127.0.0.1:8883/admin/);

Obs: o arquivo users.csv está com apenas 200 linhas, é necessário baixar o original ( [https://s3.amazonaws.com/careers-picpay/users.csv.gz](users.csv.gz) ) e subsitituir na pasta data, antes de executar o passo item 3;

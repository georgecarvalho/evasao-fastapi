import requests

to_predict_dict = {"campus":"mtc",
                   "curso":"bacharelado em sistemas de informacao",
                   "anoingresso":2017,
                   "periodoingresso":1,
                   "rendabruta":2000,
                   "ira":8.25,
                   "modalidade":"bacharelado",
                   "genero":"m",
                   "ficou_tempo_sem_estudar":False,
                   "companhia_domiciliar":"parentes",
                   "estado_civil":"solteiro(a)",
                   "idade":27,
                   "trabalha":"nunca trabalhou"
}

url = 'http://127.0.0.1:8000/predict'
r = requests.post(url,json=to_predict_dict); r.json()
from pprint import pprint

miDiccionario = {
    "Alemania" : "Berlin",
    "Francia" : "Paris",
    "España" : "Madrid",
    "Peru": "Lima",
    "Argentina": "Buenos Aires",
    "otrosDatos": {
        "poblacion": "45 millones",
        "presidente": "Luis Alberto",
        "tags": ["pequeño", "capital"]
    }
}


print(miDiccionario["Peru"])

miDiccionario["Italia"] = "Roma"

pprint(miDiccionario)
from requests.exceptions import HTTPError
import requests

base = "https://api.tamako.tech/api"

def chatbot(username, app_id, app_secret, userid, message):
    url =  f'{base}/chat?username={username}&appid={app_id}&appsecret={app_secret}&user={userid}&message={message}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    responce = (jsonResponse["response"])
    return responce

def joke():
    url = f"https://api.tamako.tech/api/joke"
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    joke = (jsonResponse["joke"])
    return joke

def lyrics(song_name):
    url = f"{base}/lyrics?name={song_name}"
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    lyrics = (jsonResponse["lyrics"])
    return lyrics

def animal_fact(animal):
    url = f"{base}/animalfact?name={animal}"
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    fact = (jsonResponse["fact"])
    return fact

def pokedex_fact(pokemon):
    url = f"{base}/pokedex?pokemon={pokemon}"
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    pokedex_type = (jsonResponse["type"])
#<----------------------------------->
    generation = (jsonResponse["generation"])
#<----------------------------------->
    abilities = (jsonResponse["abilities"])
#<----------------------------------->
    description = (jsonResponse["description"])
#<----------------------------------->
    height = (jsonResponse["height"])
#<----------------------------------->
    weight = (jsonResponse["weight"])
#<----------------------------------->
    gender = (jsonResponse["gender"])
#<----------------------------------->
    egg_groups = (jsonResponse["egg_groups"])
#<----------------------------------->
    species = (jsonResponse["species"])
#<----------------------------------->
    family = (jsonResponse["family"])
#<----------------------------------->
    evolutionStage = (jsonResponse["evolutionStage"])
#<----------------------------------->
    evolutionLine = (jsonResponse["evolutionLine"])
#<----------------------------------->
    return {"pokedex_type": pokedex_type,
             "generation": generation,
             "abilities": abilities,
             "description": description,
             "height": height,
             "weight": weight,
             "gender": gender,
             "egg_groups": egg_groups,
             "species": species,
             "family": family,
             "evolutionStage": evolutionStage,
             "evolutionLine": evolutionLine}
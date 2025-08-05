# API - Fête du jour (Calendrier Français)

***Le code de cette API est 100% en français***

## Installation des dépendances 

```
sudo apt update && sudo apt install python3-venv
python3 -m venv venv 
source venv/bin/activate
```
Sinon, vous pouvez directement passez à l'étape suivante 

```
python3 -m pip install -r requirements.txt
```
## Éxecution du programme 

```
python3 api.py
```

## Exemples 

### GET <code>/fetes</code>

```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s 'localhost:5000/fetes' | jq
{
  "mois": {
    "1": [
      "1",
      "Jour de l'an",
      "Basile",
      "Geneviève",
      "Odilon",
      "Edouard",
      "Mélaine",
      "Raymond",
      "Lucien",
      "Alix",
      "Guillaume",
      "Pauline",
      "Tatiana",
      "Yvette",
      (...)
    ]
  }
}
```


### GET <code>/fetes?mois=12</code>

```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s 'localhost:5000/fetes?mois=12' | jq 
{
  "Décembre": [
    "12",
    "Florence",
    "Viviane",
    "François-Xavier",
    "Barbara",
    "Gérald",
    "Nicolas",
    "Ambroise",
    "Immaculée Conception",
    "Pierre Fourier",
    "Romaric",
    "Daniel",
    "Jeanne-Françoise de Chantal",
    "Lucie",
    "Odile",
    "Ninon",
    "Alice",
    "Gaël",
    "Gatien",
    "Urbain",
    "Théophile",
    "Hiver",
    "Françoise-Xavière",
    "Armand",
    "Adèle",
    "Noël",
    "Etienne",
    "Jean",
    "Innocents",
    "David",
    "Roger",
    "Sylvestre"
  ]
}
```

### GET <code>/fete/{nom}</code>

``` 
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/fete/philippe | jq     
{
  "result": [
    "La fête de Philippe est le 03/05"
  ]
}
```
### GET <code>/fete/{jour}/{mois}</code>

```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/fete/31/12 | jq 
{
  "result": [
    "Le 31/12 nous fêtons : Sylvestre"
  ]
}
```

### GET <code>/fete/aujourdhui</code>

``` 
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/fete/aujourdhui | jq 
{
  "result": [
    "Le 21/03 nous fêtons : Clémence"
  ]
}
```
### GET <code>/fete/demain</code>
```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/fete/demain | jq     
{
  "result": [
    "Le 22/03 nous fêtons : Léa"
  ]
}
```
### GET <code>/fete/hier</code>
```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/fete/hier | jq   
{
  "result": [
    "Le 20/03 nous fêtons : Printemps/Rameaux"
  ]
}
```
### GET <code>/fete/bissextile</code>

```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/bissextile | jq  
{
  "2024": true
}
```
### GET <code>/fete/bissextile/{année}</code>

```
kali@kali ~/perso/api_fetes_prenoms_france (main*) $ curl -s localhost:5000/bissextile/2025 | jq 
{
  "2025": false
}
```
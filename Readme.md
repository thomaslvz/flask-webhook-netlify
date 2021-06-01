# Flask webhook for Netlify forms

Application Flask exposant un webhook capable de traiter une notification Netlify (Outgoing webhook) sécurisée par un JWT.

Cas d'usage : 
* un site statique utilise Netlify Forms
* on veut traiter les réponses au formulaire via Python
* on utilise cette application Flask pour traiter le contenu du formulaire (JSON)
* on connecte le formulaire à l'application via `Netlify Forms > Outgoing Webhooks`


## Paramétrage

**Du côté de Netlify** 

Utiliser Netlify Forms et les webhook : Netlify > Site Settings > Forms > Form notifications > Add webhook.
* url = url du webhook
* jws = `<SECRET>` à proposer

Dans ce cas, chaque soumission de formulaire appelera le webhook avec un jeton de signature dans les headers, et le contenu du formulaire dans le payload.

**Du côté de l'app**

Créer les variables d'environnement suivantes :

```.env
NETLIFY_FORM_HOOK_SECRET='<SECRET>'
NETLIFY_FORM_HOOK_ISSUER='netlify'
NETLIFY_FORM_HOOK_ALG="HS256"
```


## Exécuter en local

```sh
flask run #default runs on port 5000
```

```sh
#use of ngrok to map http to local environment
export PATH="$PATH:$HOME/Applications/ngrok" #if needed add ngrok to PATH
ngrok http 5000 #tunnel from http to localhost:5000
```

## Pyenv commands
```sh
# créer l'environnement
pyenv virtualenv my-flask-webhook

# activer l'environnement
pyenv activate my-flask-webhook

#charger les dépendances
pip install -r requirements.txt
```

## Ressources

* [Webhook tester](https://webhook.site/#!/c6d96a11-8ee4-40d9-a8c1-2f3d86b4553a)
* ngrok pour tester le webhook en local
* Postman, logiciel pour simuler des requetes

# Progettare e distribuire applicazioni su Raspberry Pi con Docker – Organizzare container e dipendenze con docker-compose

Questa repository contiene il progetto esposto su antima.it nell'articolo raggiungibile al [seguente link](https://antima.it/progettare-e-distribuire-applicazioni-su-raspberry-pi-con-docker--organizzare-container-e-dipendenze-con-docker-compose/).


## Installazione
Il codice è scaricabile tramite git clone ed eseguibile utilizzando docker compose, come descritto nell'articolo.
```bash
git clone https://github.com/Antimait/tutorial-docker-compose
cd tutorial-docker-compose
docker-compose up --build -d
```

## Utilizzo

La webapp è raggiungibile all'indirizzo http://localhost:5000, i dati vengono presentatti in una semplice tabella.
Per interagire con l'applicazione, si possono simulare i nodi sensori di cui si parla nell'articolo utilizzando 
*mosquitto_pub*:

```bash
# Il comando qui di seguito installa mosquitto_pub
sudo apt install mosquitto-clients

# Ad esempio, per simulare l'arrivo di dati dai sensori della categoria 'luci'
mosquitto_pub -t topic/luci -m on
```

# TP 2022-2

## Automatización de envió de datos de glucómetro


## Ejecución

Levantar Broker ActiveMQ:

    cd apache-activemq-5.17.2/bin/
    ./activemq start

Iniciar consumidor:

    python consumidor.py
    ||
    python3 consumidor.py

Iniciar Productor:

    python stomp_producer.py
    ||
    python3 stomp_producer.py

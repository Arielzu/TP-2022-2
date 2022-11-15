import stomp
import time
import random

#Producer Glucometro

conn = stomp.Connection()
conn.connect('admin', 'password', wait=True)
while True:
    #niveles de glicemia normales(mg/dl) 90-130
    glicemia = str(random.randint(70,200))
    if glicemia < 90:
        glicemia += " - Bajo"
    elif glicemia > 130:
        glicemia += " - Alto"
    else:
        glicemia += " - Normal"

    conn.send(body=' '.join(glicemia), destination="/queue/test")
    time.sleep(2)
conn.disconnect()
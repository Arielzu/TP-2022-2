import stomp
import time
import random

#Producer Glucometro

conn = stomp.Connection()
conn.connect('admin', 'password', wait=True)
while True:
    #niveles de glicemia normales(mg/dl) 90-130
    glicemia = random.randint(70,200)
    if glicemia < 90:
        glicemia = str(glicemia) + " - Bajo"
    elif glicemia > 130:
        glicemia = str(glicemia) + " - Alto"
    else:
        glicemia = str(glicemia) + " - Normal"

    conn.send(body=' '.join(glicemia), destination="/queue/test")
    time.sleep(5)
conn.disconnect()
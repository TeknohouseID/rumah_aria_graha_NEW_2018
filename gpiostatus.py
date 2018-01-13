import wiringpi

# One of the following MUST be called before using IO functions:
wiringpi.wiringPiSetup()      # For sequential pin numbering (wPi numbering)

# Definisi pin yang terhubung ke relay dengan sistem penomoran WiringPi
status_pin = [7, 0, 2 ,3, 4]


#Penyusuan fungsi untuk membaca status tiap perangkat (pin)

def status_kos_lampu_luar():
    status1 = wiringpi.digitalRead(status_pin[0])
    if status1 == 1:
        return 'menyala'
    elif status1 == 0:
        return 'mati'

def status_kos_lampu_dalam_cewek():
    status2 = wiringpi.digitalRead(status_pin[1])
    if status2 == 1:
        return 'menyala'
    elif status2 == 0:
        return 'mati'

def status_kos_lampu_dalam_cowok():
    status3 = wiringpi.digitalRead(status_pin[2])
    if status3 == 1:
        return 'menyala'
    elif status3 == 0:
        return 'mati'

def status_dispenser_cewek():
    status4 = wiringpi.digitalRead(status_pin[3])
    if status4 == 1:
        return 'menyala'
    elif status4 == 0:
        return 'mati'

def status_dispenser_cowok():
    status5 = wiringpi.digitalRead(status_pin[4])
    if status5 == 1:
        return 'menyala'
    elif status5 == 0:
        return 'mati'




#Penyesuaian penomoran wPi dengan Physical

#pin 7 = pin 7  = relay 1 = kos_lampu_luar
#pin 0 = pin 11 = relay 2 = kos_lampu_dalam_cewek
#pin 2 = pin 13 = relay 3 = kos_lampu_dalam_cowok
#pin 3 = pin 15 = relay 4 = dispenser_cewek
#pin 4 = pin 16 = relay 5 = dispenser_cowok


#Coded by Faisal Candrasyah H, Founder of Teknohouse.ID

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_lampu = [7,11,13]	#definisi pin GPIO yg terhubung ke relay lampu
GPIO.setup(pin_lampu, GPIO.OUT)

def lampu_on(pin):		#fungsi untuk menyalakan lampu (NC)
	GPIO.output(pin, 1)

def lampu_off(pin):		#fungsi untuk mematikan lampu (NC)
	GPIO.output(pin, 0)




#Coded by Faisal Candrasyah H, Founder Teknohouse.ID, Co-founder and former CTO Indisbuilding

#pin 7  = relay 1 = kos_lampu_luar
#pin 11 = relay 2 = kos_lampu_dalam_cewek
#pin 13 = relay 3 = kos_lampu_dalam_cowok

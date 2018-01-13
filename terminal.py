import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_terminal = [15,16]	#definisi pin GPIO yg terhubung ke relay terminal
GPIO.setup(pin_terminal, GPIO.OUT)

def terminal_on(pin):		#fungsi untuk menyalakan lampu (NC)
	GPIO.output(pin, 1)

def terminal_off(pin):		#fungsi untuk mematikan lampu (NC)
	GPIO.output(pin, 0)



#Coded by Faisal Candrasyah H, Founder Teknohouse.ID, Co-founder and former CTO of Indisbuilding

#pin 15 = relay 4 = dispenser_cewek
#pin 16 = relay 5 = dispenser_cowok

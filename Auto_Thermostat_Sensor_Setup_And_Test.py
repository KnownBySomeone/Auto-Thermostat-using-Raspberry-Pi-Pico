# By, Known By Someone (Jeremiah B.)
# MicroPython

# Portions of code used from:  https://github.com/geeekpi/picokitadv
# Project_4_OLED096_alien_invater.py
# Project_15_DHT11_sensor.py
# Project_16 _1_channel_relay_module.py

# Automatic Thermostat using Raspberry Pi Pico

from machine import Pin, ADC, PWM
import utime as time
from dht import DHT11, InvalidChecksum
from time import sleep


# GPIO Pins used:
# GPIO #4 as ADC with internal temperature sensor
# GPIO #25 as togle for onboard LED
# GPIO #18 as ???? for Buzzer
# GPIO #11 and #15 as I2C data pins for DHT Temperature/Humidity sensor
# GPIO #0 as input "on" or "off" state for Rain Drop sensor
# GPIO #4 as togle for AC relay


# Buzzer setup
buzzer = PWM(Pin(18))

# Setup DHT Temperature/Humidity sensor !!!{Requires about one second after setup to read}!!!
# Pins 11, and 15 have the same capabilities.  11 is 15 on the board.  15 is 20 on the board.
DHTPin = Pin(15, Pin.OUT, Pin.PULL_DOWN)

# Setup Onboard LED
led = Pin(25, Pin.OUT)

# Setup internal Temperature sensor
sensor_temp = machine.ADC(4)

# Setup for Rain Drop sensor
water_sensor_DO = Pin(0, Pin.IN)

# Setup for Relay Signal pin
relay_pin = Pin(4, Pin.OUT)
# Try other pins beside #4 to reduce confusion with internal Temperature sensor which is also on #4


# Silence Buzzer
buzzer.duty_u16(0)
# Buzz Buzzer
buzzer.freq(2000)
buzzer.duty_u16(4000)

# Once Buzzer is started, this sleep() indicates how long to hold the buzz for this cycle.
sleep (1)
# Silence Buzzer
buzzer.duty_u16(0)


# Toggle Onboard LED using True and False 
led.value(True)


# I am not sure what it is converting for at this stage
conversion_factor = 3.3 / (65535)
# This part converts to Celsius(sp?)
reading = sensor_temp.read_u16() * conversion_factor
temperature_c = 27 - (reading - 0.706)/0.001721

print(temperature_c, "°C    Onboard")


# Setup DHT Temperature/Humidity sensor !!!{Requires about one second after setup to read}!!!
# Pins 11, and 15 have the same capabilities.  11 is 15 on the board.  15 is 20 on the board.
DHTPin = Pin(11, Pin.OUT, Pin.PULL_DOWN)

# Read from DHT Temperature/Humidity sensor
# About 1 second is a necessary wait before reading from a DHT.
time.sleep(1)
sensor = DHT11(DHTPin)
  
indoor_temp = (sensor.temperature)
indoor_humid = (sensor.humidity)
    
print("Indoor Temperature: " + str(indoor_temp))
print("Indoor Humidity: " + str(indoor_humid))


# Setup DHT Temperature/Humidity sensor !!!{Requires about one second after setup to read}!!!
# Pins 11, and 15 have the same capabilities.  11 is 15 on the board.  15 is 20 on the board.
DHTPin = Pin(15, Pin.OUT, Pin.PULL_DOWN)

# Read from DHT Temperature/Humidity sensor
# About 1 second is a necessary wait before reading from a DHT.
time.sleep(1)
sensor = DHT11(DHTPin)
  
outdoor_temp = (sensor.temperature)
outdoor_humid = (sensor.humidity)
    
print("Outdoor Temperature: " + str(outdoor_temp))
print("Outdoor Humidity: " + str(outdoor_humid))


# Rain Drop sensor input
if water_sensor_DO.value() == 0:
    print("It is raining")
else:
    print("It is not raining...")
    

# Control Relay Signal pin
print("turn on relay!")
relay_pin.value(1)
sleep(5)
print("turn off relay!")
relay_pin.value(0)
sleep(5)


# Turn off LED when done
led.value(False)

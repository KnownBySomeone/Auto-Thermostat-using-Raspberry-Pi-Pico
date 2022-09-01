# Auto-Thermostat-using-Raspberry-Pi-Pico
Using a Raspberry Pi Pico and MicroPython to regulate when an outlet turns on with a relay based on an outdoor DHT22 Temperature/Humidity sensor and an LM393 Rain Drop Sensor, and an indoor DHT22 Temperature/Humidity sensor.

This is a Work in Progress


This project requires(makes use of) the dht.py library that can be found at https://github.com/geeekpi/picokitadv/blob/main/libs/dht.py .
For a NOOB like me.  Copy the code from the link and save it as a new program on your Raspberry Pi Pico with the name "dht.py".  The rest of the code will be saved in separate programs than this dht.py program, because the dht.py will act as an extention of the libraries called for at the beginning of the other programs.

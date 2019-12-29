from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

pin = 33

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)

@app.route('/turnon', methods=['GET'])
def turnon():
    # To turn on pin
    GPIO.output(pin,GPIO.HIGH)
    return "Lights Turned ON!!"
    
@app.route('/turnoff', methods=['GET'])
def turnoff():
    # To turn off pin
    GPIO.output(pin,GPIO.LOW)
    return "Lights Turned OFF!!"    
    


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=8000)
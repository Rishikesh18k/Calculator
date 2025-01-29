import eel
import os 

eel.init("Calculator")
os.system('start msedge.exe --app="http://localhost:8000/Calculator.html"')
eel.start('index.html', mode=None, host='localhost', block=True) 
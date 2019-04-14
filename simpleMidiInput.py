#from mido import Message
import mido

#print(mido.get_input_names())

#inport = mido.open_input('Babyface Midi Port 1 0') 

with mido.open_input('Babyface Midi Port 1 0') as inport:
    for msg in inport:
        print(msg)




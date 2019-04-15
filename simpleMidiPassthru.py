import mido

outport = mido.open_output('Springbeats vMIDI1 2')

with mido.open_input('Babyface Midi Port 1 0') as inport:
    for msg in inport:
        print(msg)
        outport.send(msg)  #just send the message right through









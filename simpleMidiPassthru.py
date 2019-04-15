# SOME OTHER HELPFUL CODE THAT GOT ME THERE
#   print(mido.get_input_names())
#   inport = mido.open_input('Babyface Midi Port 1 0') 
# Output Ports available on my "TOWER DEV MACHINE": 
# ['Babyface Midi Port 1 1', 'Microsoft GS Wavetable Synth 0', 'Springbeats vMIDI1 2', 'Springbeats vMIDI2 3', 'Springbeats vMIDI3 4', 'Springbeats vMIDI4 5', 'Springbeats vMIDI5 6', 'Springbeats vMIDI6 7', 'Springbeats vMIDI7 8', 'Springbeats vMIDI8 9']

import mido

outport = mido.open_output('Springbeats vMIDI1 2')

with mido.open_input('Babyface Midi Port 1 0') as inport:
    for msg in inport:
        print(msg)
        outport.send(msg)  #just send the message right through









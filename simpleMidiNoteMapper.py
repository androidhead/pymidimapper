import mido

#you can add to these in the console with something like:
# noteMap.update({62:61})
noteMap = {
    75:76,
    77:78    
}

def transform(midiMessage):
    midiMessage.note = noteMap.get(midiMessage.note, midiMessage.note) #map to note in noteMap.  If not found, simply pass-thru.    
    return midiMessage

outport = mido.open_output('Springbeats vMIDI1 2')
with mido.open_input('Babyface Midi Port 1 0') as inport:
    for msg in inport:
        print("before transform:")
        print(msg)
        msg = transform(msg)  #transform message
        print("after transform:")
        print(msg)
        outport.send(msg)  #just send the message right through


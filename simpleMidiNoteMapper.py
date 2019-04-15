import mido

#show which ports are available.
print("INPUT PORTS:")
inputs = mido.get_input_names()
print(mido.get_input_names())
print("")
print("OUTPUT PORTS:")
outputs = mido.get_output_names()
print(mido.get_output_names())
print("")

#get config
import json
with open('config.json', 'r') as f:
    config = json.load(f)
    inportName = config["INPUT_PORT"]
    outportName = config["OUTPUT_PORT"]

# the actual note maps.  probably should be loaded via file(s) at some point
#   you can add to these in the console with something like:
#   noteMap.update({62:61})
noteMap = {
    75:76,
    77:78    
}

def transform(midiMessage):
    if hasattr(midiMessage, 'note'):
        midiMessage.note = noteMap.get(midiMessage.note, midiMessage.note) #map to note in noteMap.  If not found, simply pass-thru.        
    return midiMessage

outport = mido.open_output(outportName)
with mido.open_input(inportName) as inport:
    for msg in inport:
        print("before transform:")
        print(msg)
        msg = transform(msg)  #transform message
        print("after transform:")
        print(msg)
        outport.send(msg)  #just send the message right through

 
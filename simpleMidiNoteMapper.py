import mido

#show which ports are available.
print('INPUT PORTS:')
inputs = mido.get_input_names()
print(mido.get_input_names())
print('')
print('OUTPUT PORTS:')
outputs = mido.get_output_names()
print(mido.get_output_names())
print('')

#get config
import json
with open('config.json', 'r') as f:
    config = json.load(f)
    inportName = config['INPUT_PORT']
    outportName = config['OUTPUT_PORT']

#import note map from config file
noteMap = {}
allNoteRoutes = config['NOTE_MAP']
for noteRoute in config['NOTE_MAP']:
    print('load route:', noteRoute, allNoteRoutes[noteRoute])
    noteMap.update({int(noteRoute): allNoteRoutes[noteRoute]}) #add to noteMap

def transform(midiMessage):
    if hasattr(midiMessage, 'note'):
        midiMessage.note = noteMap.get(midiMessage.note, midiMessage.note) #map to note in noteMap.  If not found, simply pass-thru.        
    return midiMessage

outport = mido.open_output(outportName)
with mido.open_input(inportName) as inport:
    for msg in inport:
        print('before transform:')
        print(msg)
        msg = transform(msg)  #transform message
        print('after transform:')
        print(msg)
        outport.send(msg)  #just send the message right through

 
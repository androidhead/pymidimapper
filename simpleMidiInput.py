#to get this working I had to do the following installs:
#    pip install mido
#    pip install --user --pre python-rtmidi ##(which I think provides the 'backend' for the above)
# SOME OTHER HELPFUL CODE THAT GOT ME THERE
#   print(mido.get_input_names())
#   inport = mido.open_input('Babyface Midi Port 1 0') 

#from mido import Message
import mido

with mido.open_input('Babyface Midi Port 1 0') as inport:
    for msg in inport:
        print(msg)



#keyinputevent



from pymitter import EventEmitter

ee = EventEmitter()

#responsible for mapping
def map(input):
    return input + "processed"

# decorator usage
@ee.on("myevent")
def handler1(arg):
   print("your input was " + map(arg))


# emit some basic keyboard input
keyInput = input("what's your input?")
ee.emit("myevent", keyInput)




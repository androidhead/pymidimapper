from pymitter import EventEmitter

#responsible for mapping
def map(input):
    #return input + "processed"
    if input == "a":
        return "b"
    else:
        return input

#event handling
ee = EventEmitter()
@ee.on("myevent")
def handler1(arg):
   print("your input was " + map(arg))


# use some basic keyboard input as data source to map
keyInput = input("what's your input?")
ee.emit("myevent", keyInput)




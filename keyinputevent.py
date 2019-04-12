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
@ee.on("handleInput")
def handler1(input):
   print("your input was " + map(input))


# use some basic keyboard input as data source to map
run = True
while run:
    keyInput = input("input (type X to end): ")
    if keyInput == "X":
        run = False
    else: 
        ee.emit("handleInput", keyInput)

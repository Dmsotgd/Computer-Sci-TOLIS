#Even or Odd parity
add_library('controlP5') 

def setup():
    size(600, 300)
    # changes text size
    textSize(36)
    
    #creates the object for buttons and textfields
    global inputBox
    inputBox = ControlP5(this)
    #creates a input box called "input" and changes some display parameters
    inputBox.addTextfield("input") \
      .setFocus(True) \
      .setSize(120, 20) \
      .setAutoClear(False) \
      .setPosition(92, 35)

    #Creates a button
    inputBox.addButton("clear") \
      .setPosition(215, 35) \
      .setSize(225, 20) \
      .getCaptionLabel() \
      .align(ControlP5.CENTER, ControlP5.CENTER)
    #determines wich function to call when the button is pressed
    inputBox.getController("clear").addListener(buttonPressed)

# This funtion established what the button will do
def buttonPressed(object):
    inputBox.get(Textfield, "input").clear()    


def draw():
    background(0)
    fill(255)
    # get the value from the text box and displays
    try: 
        x=int(inputBox.get(Textfield, "input").getText())
    except:
       x=0 
    text(bitwise(x),92, 155)

#Check Bitwise Function
def bitwise(x):
    value= x&1
    if value==1:
        return "Odd"
    else:
        return "Even"

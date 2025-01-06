### GUI imports
from guizero import *
from kuba_main import *

### GUI functions
def my_first_gui_function():

    try:
        weight = int(txtbox_weight.value)
    except ValueError:
        text_weight.value = "Weight je špatně zadaná"
        return
    
    try:
        activity_factor = int(txtbox_af.value)

    except:
        text_af.value = "Activity factor je špatně zadaný"
        return


    bmr = weight * 24
    cml = round(float(bmr * activity_factor),2)
    text_cml.value = "cml je",cml,"kcal/den"
    


### GUI App
app = App(title="My App", width=775, height=650)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(window1,text=("Please enter your activity factor for today:"))
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(window1,text=(f"Please enter your weight in kilograms (kg):"))
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

button = PushButton(window1, command=my_first_gui_function)

app.display()


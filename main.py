import turtle,csv,pandas,time
from os import remove

screen = turtle.Screen()
t = turtle.Turtle()
background_image = "canada_provinces.gif"

score=0
guessed_provinces = []
game = True

print("Click to exit")

#set turtle screen
screen.title("rumeza's province guessing game")
screen.addshape(background_image)
turtle.shape(background_image)



#adding all provinces to list and creating sep unguessed and guessed list
data = pandas.read_csv("province_names.csv")
provinces = data.province.to_list()
guessed_provinces = []
unguessed = data.province.to_list()



#finding coords of provinces
def extracting_cords(x,y):
    province_row = data[data.province == input]
    province_xcord = int(province_row.x)
    province_ycord = int(province_row.y)
    cords.append(province_xcord)
    cords.append(province_ycord)

#move turtle for winning and exitting
def turtle_moves():
    t.penup()
    t.goto(-40, 0)
    t.pendown()
    if score==13:
        t.write("Game Ended\nYou Won!", font=50)
    else:
        t.write("Game Ended", font=50)




while game==True:
    cords = []

    if score==13:
        turtle_moves()

    #userinputs province name
    user_input = turtle.textinput(title="Guess the Province", prompt=f"Enter the full province name\n{score}/13 Correct")

    #return if province is incorrect
    if user_input not in provinces and not "exit":
        print("province not found")

    #return in province has been repeated
    elif user_input in guessed_provinces:
        print("Province has been guessed already.")

    #write province if input==province
    elif user_input in provinces:
        score += 1
        guessed_provinces.append(user_input)
        extracting_cords(user_input)
        t.hideturtle()
        t.penup()
        t.goto(cords)
        t.pendown()
        t.pencolor("red")
        t.write(user_input)
        unguessed.remove(user_input)

    #make exit available
    if user_input == "exit":
        unguessed = "\n".join(unguessed)
        print(f"You missed the following Provinces:\n{unguessed}")
        turtle_moves()

    if score==13:
        turtle_moves()



screen.mainloop()

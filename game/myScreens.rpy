label myScreens:

screen mapScreen:
    add "hell bg.png"

    #Room1
    imagebutton:
        focus_mask True
        idle "r1-idle.png"
        hover "r1-hover.png"
        action Jump("room1")

    #Room2
    imagebutton:
        focus_mask True
        idle "r2-idle.png"
        hover "r2-hover.png"
        action Jump("room2")

screen backButton:
    imagebutton:
        xpos 100
        ypos 100
        idle "arrow-idle.png"
        hover "arrow-hover.png"
        action Jump("map")
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

    #Room3
    imagebutton:
        focus_mask True
        idle "r3-idle.png"
        hover "r3-hover.png"
        action Jump("room3")

screen backButton:
    imagebutton:
        xpos 100
        ypos 100
        idle "arrow-idle.png"
        hover "arrow-hover.png"
        action Jump("map")
        
screen countdown_bar:
    bar:
        xalign 0.95 yalign 0.15
        bar_vertical True
        value countdown_value
        range 100
        thumb None
        thumb_shadow None
        xysize(100,400)
    add "bar-frame.png" align (0.975, 0.1)
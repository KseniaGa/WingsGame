label myScreens:

screen mapScreen:
    add "map bg.png"

    #Room1
    imagebutton:
        focus_mask True
        idle "map room 1 idle.png"
        hover "map room 1 hover.png"
        action Jump("room1")

    #Room2
    imagebutton:
        focus_mask True
        idle "map room 2 idle.png"
        hover "map room 2 hover.png"
        action Jump("room2")

    #Room3
    imagebutton:
        if wing_strength >= 2:
            focus_mask True
            idle "map room 3 idle.png"
            hover "map room 3 hover.png"
            action Jump("room3")
        else:
            idle "map room empty.png"
            hover "map room empty.png"
        
    #Room4
    imagebutton:
        if wing_strength >= 2:
            focus_mask True
            idle "map room 4 idle.png"
            hover "map room 4 hover.png"
            action Jump("room4")
        else:
            idle "map room empty.png"
            hover "map room empty.png"
        
    #Top Room
    imagebutton:
        if wing_strength >= 3:
            focus_mask True
            idle "map top room idle.png"
            hover "map top room hover.png"
            action Jump("toproom")
        else:
            idle "map room empty.png"
            hover "map room empty.png"

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
        value darkness_value
        range 100
        thumb None
        thumb_shadow None
        xysize(100,400)
    add "bar-frame.png" align (0.975, 0.1)

#Add a polunytsa joke

#ref: https://en.wikipedia.org/wiki/Lady_Midday

#Poludnitsa is a noon demon in Slavic mythology. She can be referred to in English as "Lady Midday", "Noonwraith" or "Noon Witch". 
#She was usually pictured as a young woman dressed in white that roamed field bounds.[3] She assailed folk working at noon, 
#causing heatstrokes and aches in the neck; sometimes she even caused madness.

#Poludnitsa, who makes herself evident in the middle of hot summer days, takes the form of whirling dust clouds
# and carries a scythe, sickle or shears; most likely the shears would be of an older style, not akin to modern scissors. 
#She will stop people in the field to ask them difficult questions or engage them in conversation. If anyone fails to answer 
#a question or tries to change the subject, she will cut off their head or strike them with illness. She may appear as an old hag,
# a beautiful woman, or a 12-year-old girl, and she was useful in scaring children away from valuable crops. 
#She is only seen on the hottest part of the day and is a personification of a sun-stroke.[5]

#Poludnitsa, according to beliefs, loves to dance. If she sees a girl lying down to rest in the field, she will wake her 
#up and begin to persuade her to dance. If the girl agrees, she will be forced to dance until the «evening dawn». 
#Poludnitsa cannot be beaten in dancing; however, if such a girl is found, the noon spirit will present her with a rich dowry.[8]


label room2:
    # scene room hell bg

    default poludnicia_attitude = 0 
    default poludnicia_visited = False
    default poludnicia_joined = False

    if poludnicia_joined:
        jump poludnicia_already_joined  
    elif poludnicia_visited:
        jump poludnicia_already_visited  
    else: 
        jump poludnicia_intro

label poludnicia_already_joined:
    b "*Looks at tumbleweed passing*"
    call screen backButton

label poludnicia_already_visited:
    show berehynia at right with dissolve
    # b "Poludnytsa is not in the mood indeed. But you dealt with Mara, so this shoudl be doable too!"
    b "You dealt with my sister already, so persuading Poludnytsa would be like snacking on sunflower seeds..." #як насі́ння луза́ти

    show poludnicia at center with dissolve
    show vila at left with dissolve
    hide berehynia at right with dissolve
    show poludnicia at rightly with move 
    
    jump poludnicia_greet


label poludnicia_intro:
    show poludnicia at center with dissolve
    show vila at left with dissolve
    pause 0.1
    show berehynia at rightly with dissolve

    b "Poludnytsa is a spirit of the fields. She may have a strong character - don't we all?"
    b "After all it is quite a toll to protect the fields from the sun...and unwanted visitors."
    b "But now, you know, who wouldn't be angry from everything that happened to us? May luck be with you."

    call screen backButton

    hide berehynia at rightly with dissolve
    show poludnicia at rightly with move 

    p "This darkness is driving me mad!"
    p "It was ME who was driving others mad. Not vice versa!"
    p "I cannot even threaten anyone with... whatever I used to threaten with!" # (the power of the sun)
    p "* walks angrilly back and forth * "


label poludnicia_greet: 
    menu:
        "Greet gently":
            v "TODO"
            $ poludnicia_attitude+=5
            jump poludnicia_remind
            

        "Tell to calm down":
            v "Woah woah woah, someone needs to chill here..."
            p "TODO"
            $ poludnicia_attitude-=10
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_remind
            

        "Stay quiet":
            v "..."
            p "*continues*"
            v "..."
            p "You're not triggered by my anger?"
            p "How are you staying so calm?"
            p "I ahven't experienced calmness in ages!"
            v "..."
            p "Hm, I like you.. kind of."
            $ poludnicia_attitude+=10
            jump poludnicia_remind

            
label poludnicia_remind:
    menu:
        "The sun god":
            v "TODO"
            $ poludnicia_attitude+=5
            jump poludnicia_reassure

        "The field queen":
            v "TODO"
            $ poludnicia_attitude+=10
            jump poludnicia_reassure

        "The scarecrow":
            v "TODO"
            $ poludnicia_attitude-=5
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_reassure


label poludnicia_reassure:
    menu:
        "Let's dance!":
            # ref: "P"oludnitsa, according to beliefs, loves to dance. If she sees a girl lying down to rest in the field, she will wake her 
            #up and begin to persuade her to dance. If the girl agrees, she will be forced to dance until the «evening dawn». 
            #Poludnitsa cannot be beaten in dancing; however, if such a girl is found, the noon spirit will present her with a rich dowry.[8]"

            v "TODO"
            $ poludnicia_attitude+=10

        "Let's play contact": #with Berehynia (need 3 people)
            # ref "She will stop people in the field to ask them difficult questions or engage them in conversation. 
            # If anyone fails to answer a question or tries to change the subject, she will cut off their head or strike 
            # them with illness."
            v "TODO"
            $ poludnicia_attitude+=5 

        "Let's play heatstrokes/faint (OR with sickle?)": #pretend her poer are still with her
            v "TODO pretend her powers still work"

            $ poludnicia_attitude-=5 #cannot do because there is not sun here, powerless without it?

label poludnicia_invite:
    if poludnicia_attitude>=15:
        "TODO"

    else:
        "TODO"
        
    $ poludnicia_attitude = 0
    $ poludnicia_visited = True 

    call screen backButton 

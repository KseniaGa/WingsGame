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

#ref: https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D1%83%D0%B4%D0%BD%D0%B8%D1%86%D1%8F
# Загальне заняття полудниць — карати тих, хто працюють у полі в полудень. Людям, яких вони зустрічали на полі,
# загадували загадки, які неможливо відгадати[2], і за відповідями вирішували вбити чи скалічити своїх жертв. 
#Також душили женців, які спали в полі, викрадали дітей, які гралися на краю поля[4], покидали дім чи крали плоди. 
#Часом били по ногах тих, хто їм не вклоняється[2][3]. В Україні, на Житомирщині, вірили, що полудниця змушує людину
# блукати по лісу в полудень[6].

#Лужичани, проте, наділяли полудницю і корисними функціями. Вони вважали, що полудниця крім того охороняє поле від злодіїв[2],
# косить поле замість людей[8]; вірили, що хто насміхатиметься з потворної полудниці, тому вона нашле виразки, але хто її 
#похвалить або щось подарує — отримає від полудниці нескінченний клубок пряжі[9]. Як охоронниця полів, вона могла випробовувати
#женців, розпитуючи їх як ростити збіжжя, та карала тих, хто не давали правильної відповіді[10].



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

    b "Poludnytsa is a spirit living in the fields. She may have a strong character - don't we all?"
    b "After all it is quite a toll to protect the fields...and unwanted visitors from being there at a wrong time."
    b "But now, you know, who wouldn't be angry from everything that happened to us? May luck be with you."

    call screen backButton

    hide berehynia at rightly with dissolve
    show poludnicia at rightly with move 

    p "This darkness is driving me mad!"
    p "It was ME who was driving others mad. Not vice versa!"
    p "I cannot even threaten anyone with... whatever I used to threaten with!" # (the power of the sun? the scythe?)
    p "* walks angrilly back and forth * "


label poludnicia_greet: 
    menu:
        "Greet gently":
            v "Hi..."
            p "*still preoccupied with her emptions*"
            v "Poludnytsa, hello. I... I am Vila."
            p "I had met enough villains in my life! No, thank you." #TODO adapt for uktrainian maybe, smth like Вили - для поля?
            v "Vi-la. Not a villain."
            p "What do you want, 'Viii-laaa'?"
            $ poludnicia_attitude+=5
            jump poludnicia_remind
            

        "Tell to calm down":
            v "Woah woah woah, someone needs to chill here..."
            p "Chill?!"
            p "Are you kidding me?! Look where we are! And besides..."
            p "..who, in Mara's name, are you?"
            v "Khmm, I am Vila.. I just recently realized the state of things myself!"
            v "You must believe me."
            p "?!"
            $ poludnicia_attitude-=10
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_remind
            

        "Wait quietly":
            v "..."
            p "*continues*"
            v "..."
            p "You're not triggered by my anger?"
            p "How are you staying so calm?"
            p "I haven't experienced calmness in ages!"
            v "..."
            p "Hm, I like you.. kind of. What is your name?"
            v "I am Vila.. Hello Polydnytsa!"
            $ poludnicia_attitude+=10
            jump poludnicia_remind

            
label poludnicia_remind:
    v "I can help you remember who you are!"
    
    menu:
        "The sun master":
            v "You control the sun going up and down over our villages."
            v "Thus, it hits the fields ~exactly~ how it needs to, at Midday!"
            p "I do remember being more active at the hottest hour of the hottest summer days!"
            p "I don't control its movement though. His name is Dazhbog, or something."
            p "So, you must be mistaken."
            v "*fearful inhale*"
            p "Good try! .. What sense talking of the sun, when we are stuck in this freaking cave!!!"
            $ poludnicia_attitude-=5
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_reassure

        "The field goddess":
            v "You are the goddess of the fields and protect them from the thieves."
            p "How come you know me, but I don't know you at all?!"
            p "Anywho, it does hit home."
            p "For most of the time, I remember, I used to fly around, disquised as dust carried by the wind."
            p "And then I come as myself..."
            v "...at Midday."
            p "When the sun is at its highest. High time for me.."
            v "..No work for others."
            p "Exactly! Good times... The times that are gone now!"
            $ poludnicia_attitude+=10
            jump poludnicia_reassure

        "The scarecrow woman":
            v "Essentially, you scare away any visitors of fields at Midday. So I've heard."
            v "You are known to protect the fields, but your methods are, hmm, pretty rough, to put midly."
            p "'Scarecrow'... This is a bold statement, Vila!!"
            v "*oh-oh*"
            p "I like this compliment! Feels like true me."
            p "NO WORK AT MIDDAY - is it so hard to follow that rule?! They keep coming and coming. The small ones, the big ones. Someone needs to stop it."
            v "That's why you use ... the scythe or a sickle?"
            p "Ha, this is outdated. Now it's just about fashion."
            p "What I do now is, ask reapers difficult questions. EaThesy ones, like how to sow, and when to reap? You know, the field stuff."
            v "And if they don't answer?"
            p "That you don't wanna know..."
            p "There are worse things happenig now. Field was no safe place for humans at midday. Well now, for nobody.. even me."
            # reapers in the field - ask them questions about how to take care of the fields.
            $ poludnicia_attitude+=5
            jump poludnicia_reassure


label poludnicia_reassure:
    v "I feel your frustartion, Poludnytsa. Things are not easy now indeed... "
    v "Would you want to do some of your favourite activities?"
    menu:
        "Let's dance!":
            # ref: "P"oludnitsa, according to beliefs, loves to dance. If she sees a girl lying down to rest in the field, she will wake her 
            #up and begin to persuade her to dance. If the girl agrees, she will be forced to dance until the «evening dawn». 
            #Poludnitsa cannot be beaten in dancing; however, if such a girl is found, the noon spirit will present her with a rich dowry.[8]"

            v "Do you hear the wind howling? What a beat!"
            v "*starts dancing*"
            show vila at rightly with move 
            show vila at left with move 
            p "* a moment of shock*"
            show poludnicia at left with move 
            show poludnicia at rightly with move 
            $ poludnicia_attitude+=10

        "Let's ask difficult questions!": 
            # ref "She will stop people in the field to ask them difficult questions or engage them in conversation. 
            # If anyone fails to answer a question or tries to change the subject, she will cut off their head or strike 
            # them with illness."
            v "TODO"
            v "Say 'Polunytsa."

            $ poludnicia_attitude+=5 

        "Let's fence with sickles!": #pretend her poer are still with her
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

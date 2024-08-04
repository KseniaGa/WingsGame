label room3:
    # scene room hell bg

    hide all
    scene rusalkabg

    default rusalka_attitude = 0 


    if rusalka_joined:
        jump rusalka_already_joined  
    elif rusalka_visited:
        jump rusalka_already_visited  
    else: 
        jump rusalka_intro


label rusalka_already_joined:
    b "One could say 'Not even a wet spot left' (І мокрого місця не залишилось?)'. Although I can see it here clearly."
    call screen backButton

label rusalka_already_visited:
    show berehynia at right with dissolve
    b "Rusalka's sensitivity might be a strength, but it requires patience to get through to her. Good luck!"

    show rusalka at center with dissolve
    show vila at left with dissolve
    hide berehynia at right with dissolve
    show rusalka at rightly with move 
    
    jump rusalka_guess
    

label rusalka_intro:
    show rusalka at center with dissolve
    show vila at left with dissolve
    pause 0.1
    show berehynia at rightly with dissolve

    b "Rusalka's is a water spirit. Deep down here not even an underground stream passes."
    b "Instead, the only water you can find here are her tears..."
    b "Be kind to her, Vila!"

    hide berehynia at rightly with dissolve
    show rusalka at rightly with move 

    pause 0.1

    r "Hello, stranger..."

    $ show_progress_bar()

    r "What brought you here to my peaceful ... home?"

    menu:

        "Attempt an ice-breaker joke":
            v "Your home seems too dry at the moment, Rusalka. Looks like someone needs a drink hehe!" 
            r ""
            r "Never felt as thirsty in my life as here."
            r "Pointing to that does NOT help..."
            v ""
            #Consider not punishing the first encounter...
            $ rusalka_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen

            "*Rusalka feels self-aware and hides her face in her used-to-be golden hair*. Good job, Vila."
            pause 1.0
            jump rusalka_remember

        "Introduce yourself carefully":
            v "I am Vila! I am finding a way out of this darkness, and can help you too!"
            r "*overwhelmed*"
            v "No worries-no worries! All we need to do is to find the real YOU within you."
            r "The real me? But I am here.. This is my life.."
            r "You.. You can help me?"
            $ rusalka_attitude+=10
            jump rusalka_remember


        "Ask directly what happened":
            v "Home? What happened to you, Rusalka? How did you get here?"
            r "I know terrible-terrible things happened. But I don't know what..."
            v "I know, rusalka. We all were affected by it, though in different ways."
            r "It feels like poison swallowed me... "
            v "It sure could be described that way."
            r "Thank you for undertsanding, stranger."
            $ rusalka_attitude+=5
            jump rusalka_remember

    call screen backButton


label rusalka_remember:
    r "Somehow my name carries a painful resemblence with what hurt us so much. What was my existence outside of this darkness?" #would need to come up with good tranlsation to Ukrainian

    # show vila at left with dissolve 

    menu:
        "Bringing laughter and light in our waters":
            v "You used to be full of light and laugh, until they came. Filling our waters with life."
            # hide vila with dissolve
            r "Laughter?"
            r "I haven't laughed in ages!"
            # show hopefull rusalka's face
            "Rusalka glances at you - a sudden, yet quick, moment of light and hope. Then quickly looks back down, and turns quiet."
            v "Yes, laughter. In fact, your tickling could even be some sort of weapon."
            r "Hmm, I remember the tickling... Ah, swimming was always so much fun!"
            # show back the sad rusalka
            $ rusalka_attitude += 10
            jump make_rusalka_feel_better

        "Using rain to enrich our soils and help the crops":
            v "You used to come down to earh in the rain droplets. Enriching our soils, bringing life."
            # hide vila with dissolve
            r "You must be confusing me with somebody else. "
            r "I like fresh water..."
            r "... but not up in the skies."
            $ rusalka_attitude-=5
            $ darkness_value+=5
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump make_rusalka_feel_better 

        "Stealing young boys and girls like a witch":
            v "You used to roam our fields and steal young girls and boys, like a witch." 
            v "That did bring a lot of harm."
            # ref: на Поліссі русалок зближували з відьмами, вони начебто лякають людей, псують посіви і шкодять худобі, 
            # source https://uk.wikipedia.org/wiki/%D0%A0%D1%83%D1%81%D0%B0%D0%BB%D0%BA%D0%B0
            # we can choose if to keep 'good' or 'bad' traits of the characters. I'm inclined to keep the good ones?
            # "На відміну від інших подібних істот, зустріч з русалкою в українців зазвичай все ж вважалася доброю 
            # ознакою чи свідчила про високі моральні якості людини, безгрішність. Тому здатність бачити русалок 
            # приписувалася малим дітям, «достойним» людям[6]. В російській міфології образ русалки більш негативний. 
            # Ці істоти збиткуються з людей, кидають у них каміння, лоскочуть до смерті, зваблюють хлопців і топлять їх"
            # r "I was once a young girl myself.. And still bare the memories of her human life."
            # ref: https://en.wikipedia.org/wiki/Rusalka "Slavic peoples [...] did not consider rusalki evil before the 19th century"
            # hide vila with dissolve
            r "People always fear what they don't know and falsely believe us to be evil."
            r "We only come out of water in the spring to help nurture the crops. "
            r "How harmful is that?"
            v "I suppose, those were rumors, sorry..."
            $ rusalka_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump make_rusalka_feel_better

label make_rusalka_feel_better:
    # show vila with dissolve
    r "Remembering can be so painful at times.."
    v "I am here for you and would like to make you feel better!"

    menu:
        "Remind about her past self":
            #ref: https://uk.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%96_%D1%81%D0%B2%D1%8F%D1%82%D0%B0
            #ref: https://uk.wikipedia.org/wiki/%D0%A0%D1%83%D1%81%D0%B0%D0%BB%D0%BA%D0%B0
            # ENG: https://en.wikipedia.org/wiki/Green_week
            v "In reality, your name is associated with the Green Week, or Rusalii (Rosalii) celebrations.."
            v "These spring festivities are full of fertility rituals and even funeral rites!"
            # hide vila with dissolve
            r "I remember young human girls wearing flower crowns."
            r "They invoked us during Rusalii in an attempt to bring the moisture and vigor to the fields."
            $ rusalka_attitude += 10
            jump rusalka_invite
        
        "Give hope for future":
            v "In reality, the damage done to you is not as bad as it seems.."
            v "The fields you're nurtuting are being reborn."
            r "The fields were flooded..."
            r "One should not underestimate the power of water. It brings both destruction and rebirth."
            r "But I keep forgetting about the latter."
            $ rusalka_attitude += 5
            jump rusalka_invite

        "Pull realist/pessimist card": #not sure how to call this option
            # idk, I wanna add a 'wrong answer' but not sure what fits, and if should be here
            v "In reality, it all could have been worse, at least you're alive and still here."
            v "That is how much we know."
            # hide vila with dissolve
            r "I did not manage to save anybody..."
            r "...so I shall stay here, perhaps forever."
            r "I thought..I thought you would help.."
            "Rusalka starts humming a sad song and turns away."
            # v "But Rusalka.."
            pause 1.0
            $ rusalka_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump rusalka_invite
            #TODO: consider setting a flag inc ase player returns to Rusalka, so that RUsalka 'remebers the last encounter'

label rusalka_invite:
    if rusalka_attitude >= 15:
        v "Rusalka, the hope is not lost yet! If you join me, we can find the way to our homes together? What do you say?"
        r "I sense the warmth of your kind heart. Thank you for that."
        r "I do want to join you.. What's next?"

        "TODO: show Rusalka radiant, turns into magic, dissolves"
        "TODO: show vila's wings getting stronger?"
        $ wing_strength+=1

        jump map
    else:
        v "Rusalka, the hope is not lost yet! If you join me, we can find the way to our homes together? What do you say?"

        r "I am not so sure... The darkness weighs heavy on me."
        r "You raised my hopes but it lead nowhere..."

        $ increase_darkness()

    $ rusalka_attitude = 0
    $ rusalka_visited = True 

    call screen backButton

# label game_over_darkness:
#     scene black
#     hide all
#     $ hide_progress_bar()
#     "The darkness has consumed you. You must start over."
#     # Reset variables or provide options to restart the game
#     $ wing_strength = 0
#     $ darkness_value = 0
#     jump start

# label game_over_light: 
#     scene happy_ending
#     "Congrats! You win!"
#     # На цьому гра закінчується.
#     return
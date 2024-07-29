label room3:
    scene room hell bg
    
    show vila at left with dissolve
    pause 0.1
    show rusalka at rightly with dissolve

    r "Hello, stranger..."

    # flashback scene about rusalka?

    $ show_progress_bar()

    r "What brought you here to my peaceful ... home?"

    menu:
        "Your home seems too dry at the moment, Rusalka. Looks like you need a drink.": 
            r "Never felt as thirsty in my life as here"
            r "Pointing to that does NOT help..."
            # $ increase_darkness()
            # $ increase_darkness()
            #Consider not punishing the first encounter...

            "Rusalka feels self-aware and hides her face in her used-to-be golden hair. Good job, Vila."
            jump rusalka_remember

        "Home? What happened to you, Rusalka? How did you get here?":
            jump rusalka_remember

    call screen backButton


label rusalka_remember:
    r "Somehow my name carries a painful resemblence with what hurt us so much. What was my existence outside of this darkness?" #would need to come up with good tranlsation to Ukrainian

    # show vila at left with dissolve 

    menu:
        "You used to be full of light and laugh, until they came. Filling our waters with life.":
            $ wing_strength += 1
            # hide vila with dissolve
            r "Laughter?"
            r "I haven't laughed in ages!"
            # show hopefull rusalka's face
            "Rusalka glances at you - a sudden, yet quick, moment of light and hope. Then quickly looks back down, and turns quiet."
            # show back the sad rusalka
            jump make_rusalka_feel_better

        "You used to come down to earh in the rain droplets. Enriching our soils, bringing life.":
            # hide vila with dissolve
            r "You must be confusing me with somebody else. "
            r "I like fresh water..."
            r "... but not up in the skies."
            $ increase_darkness()
            jump rusalka_remember

        "You used to roam our fields and steal young girls and boys, like a witch. That did bring a lot of harm.":
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
            $ increase_darkness()
            jump rusalka_remember


label make_rusalka_feel_better:
    # show vila with dissolve
    v "I am here for you and would like to make you feel better!"

    menu:
        #ref: https://uk.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%96_%D1%81%D0%B2%D1%8F%D1%82%D0%B0
        #ref: https://uk.wikipedia.org/wiki/%D0%A0%D1%83%D1%81%D0%B0%D0%BB%D0%BA%D0%B0
        # ENG: https://en.wikipedia.org/wiki/Green_week
        "In reality, your name is associated with the Green Week, or Rusalii (Rosalii) celebrations..":
            v "These spring festivities are full of fertility rituals and even funeral rites!"
            # hide vila with dissolve
            r "I remember young human girls wearing flower crowns."
            $ wing_strength += 1
            r "They invoked us during Rusalii in an attempt to bring the moisture and vigor to the fields."
            # show rusalka radiant at rightly with dissolve #this does not work yet
            # jump make_rusalka_feel_better
            jump map
        
        "In reality, the damage done to you is not as bad as it seems..":
            v "The fields you're nurtuting are being reborn."
            # hide vila with dissolve
            r "One should not underestimate the power of water. It brings both destruction and rebirth."
            r "But I keep forgetting about the latter."
            $ wing_strength += 1
            # show rusalka radiant at rightly with dissolve #this does not work yet
            # jump make_rusalka_feel_better
            jump map

        # idk, I wanna add a 'wrong answer' but not sure what fits, and if should be here
        "In reality, it all could have been worse, at least you're alive and still here.":
            # hide vila with dissolve
            r "I did not manage to save anybody..."
            r "...so I shall stay here, perhaps forever."
            "Rusalka starts humming a sad song and turns away."
            # # v "But Rusalka.."
            $ increase_darkness()
            jump make_rusalka_feel_better
            #TODO: consider setting a flag inc ase player returns to Rusalka, so that RUsalka 'remebers the last encounter'


# label mara_remember:
#     m "Remember... I used to guide souls and bring peace to the restless."
    
#     menu:
#         "Yes, you ensured peace in the transition.":
#             $ wing_strength += 1
#             m "Thank you for reminding me. I can feel my strength returning."
#             show mara radiant at rightly with dissolve
#             "Mara transforms into a radiant form, and a part of her essence is absorbed into Vila's wings."
#             hide mara with dissolve
#             show berehynia at rightly with dissolve
#             b "Well done. Your wings have grown stronger."
#             b "Now you need to rescue more of us, so we can all escape together."
#             jump map
        
#         "You protected the souls from harm.":
#             m "No, that is not quite right. I brought peace, not protection from harm."
#             $ increase_darkness()
#             jump mara_remember
        
#         "You brought fear to the living.":
#             m "No, that is not who I am. Try to remember more clearly."
#             $ increase_darkness()
#             jump mara_remember

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
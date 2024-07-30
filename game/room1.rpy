default kikimora_attitude = 0  # Track Kikimora's attitude toward Villa

label room1:
    scene room hell bg

    show vila at left with dissolve
    # pause 0.1
    # show kikimora at right with dissolve

    # scene bg_kiki with dissolve

    "The room is dimly lit, filled with old, rustic furniture and shadows dancing on the walls as the flickering candlelight struggles to illuminate the space."
    
    show kikimora at center with dissolve
    show berehynia at right with dissolve

    b "Kikimora, the spirit of the home. She was one of the first to get trapped here."
    b "But you can help her dear, I know you can. Good luck"

    hide berehynia at right with dissolve
   
    ki "Must keep tidying, must keep clean..."
    ki "Never clean, never clean enough..."
    ki "They all left, they up and left..."
    

    menu:
        "Introduce yourself":
            v "Hi there, Kikimora, is it? I am Villa."
            $ kikimora_attitude += 5
            ki "Villa? Why are you here?"
            jump remind_her

        "Ask for Household Advice":
            v "Hey there, do you know someone who can help me with a household problem, I can't seem to..."
            $ kikimora_attitude += 5
            ki "..."
            jump remind_her

        "Stress Urgency":
            v "Kikimora, you must come with me at once."
            $ kikimora_attitude -= 5
            
            $ darkness_value += 10
            if darkness_value >= 100:
                jump game_over_darkness
            # jump dim_screen
            
            ki "Leave home... No, I cannot leave... What if they return"
            v "Who's 'they', Kiki?"
            
            jump remind_her
            

label remind_her:
    menu:
        "Show Don't Tell":
            v "*Start Sweeping/Tidying Up*"
            "Villa starts sweeping and tidying up the room."
            $ kikimora_attitude += 5
            ki "What are you doing?.."
            v "Tidying up with you. We can do it together."
            jump reassure_her

        "Tell Her who she is":
            v "Kikimora, you are a spirit of the home, something terrible happened to you that made you forget who you are, but I'm here to remind you."
            $ kikimora_attitude += 5
            ki "Spirit of the home... Forgot... You're here to remind me..."
            jump reassure_her

label reassure_her:
    menu:
        "Look to Future":
            v "There will be new places to tend to, new families to look after."
            $ kikimora_attitude += 5
            ki "New places... New families..."
            jump invite_kikimora

        "Look to the past":
            v "I am here and I will help you find those you have lost."
            $ kikimora_attitude += 5
            ki "You will help me find them..."
            jump invite_kikimora
            
        "Look at the present":
            v "Tere are those who can use your help now. Like me"
            $ kikimora_attitude += 5
            ki "..."
            jump invite_kikimora

label invite_kikimora:

    if kikimora_attitude >= 30:
        v "Hey, I am planning to move to a new place with friends soon and I think we would need someone to make this place a home.., are you interested, Kiki?"
        
        ki "A new home... A new family... I will join you."
        "Kikimora begins to glow, her form brightening as she finds hope and remembers who she is."
        $ wing_strength += 1
        $ darkness_value -= 20
    else:
        v "Hey, I am planning to move to a new place with friends soon and I think we would need someone to make this place a home.., are you interested, Kiki?"
        
        ki "I... I need to get back to work"
        "Kikimora looks uncertain, still struggling with her memories and the darkness."
        ki "Never clean, never clean enough..."
        ki "They all left, they up and left..."
        
        # $ darkness_value += 20
        
    $ kikimora_attitude = 0
    #kiki_visited = True 



    

    call screen backButton
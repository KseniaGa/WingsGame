# Alconost, boss

init python:
    import random

    def random_jump():
        choices = []
        if kiki_joined:
            choices.append("kiki_hope")
        if po_joined:
            choices.append("po_hope")
        if lis_joined:
            choices.append("lis_hope")
        if r_joined:  # Assuming r_joined should be considered as well
            choices.append("r_hope")
        
        return random.choice(choices)
    
    def flashing_bgs():
        bgs = ["bg_kiki", "bg_po", "bg_lis", "bg_default"]
        for bg in bgs:
            renpy.show(bg, at_list=None, layer='master', what=None)
            renpy.pause(0.1)  # Pause for 0.1 seconds
            renpy.hide(bg)
        #renpy.show()
       

label toproom:
    scene black
    
    show vila at left with dissolve

    v "There is noone here. Should we just escape?"
    b "She'll be here any second, dear, you won't make it past her by force, she'll only listen to reason."
    b "Please be careful wit her. Don't show too much emotion, especislly sadness."

    pause 0.5
    show alkonost at center with dissolve

    a "Ah.Greetings Vila."
    a "Radiant as always."
    a "Who do you have with you today?"

    v "Alkonost. So you're the reason for this darkness..."

    a "Hm. It's a bit too crowded here."

    v "Wait!" 
    #SOUND: CAN BE A THUMP? 
    #Mara and Berehynia are banished 

    # SOUND: HEARTBEAT? 
    a "That's better."
    v "ahdsafdgsdg"
    v "No, no, no."
    
    a "I will give you an easy way out, Vila."
    a "You have been puppeteered by the two sisters and thus, I will give you the benefit of the doubt."
    a "Choose."
    jump choice1

label choice1: 

    menu:
        "Keep Sleeping (it is easier) ": 
            v "I'm so tired..."
            b "I know you're tired, dear, but we can't give up here."
            jump toproom 

        "RESIST": 
            v "No, oblivion is not an option for me, Alkonost. Not anymore."
            a "Hm"
            jump choice2 

label choice2:

    menu:
        "Keep Sleeping (it is less painful)": 
            v "A little nap wouldn't hurt..."
            b "I'm sorry, Vila, I can't let this happen..."
            jump toproom 
        "RESIST": 
            v "No."
            v "No, I didn't come all this way, jsut to give up now. This is not going to happen, Alkonost."
            a "Hm"
            jump choice3 

label choice3:

    menu:
        "Keep Sleeping (it is what you want deep inside)": 
            v "It is what I want deep inside."
            b "No, it's not, dear."
            b "You will see that your only option is to keep going, you will see eventually..."
            jump toproom 
        "RESIST": 
            v "No!"
            v "What I want deep inside is to return home and help my friends."
            a "Hm"
            jump resist 

label resist: 

    a "Very well."
    a "Plead you case, Vila."
    v "This is not a life, Alkonost. We are not living, we're barely even existing."
    a "If you had all your memories back, Vila, if you knew in what a  state I found the others... You wouldn't want to leave, believe me."
    v "I can't speak of the memories I've lost, but I can speak of the friends I've gained. Together we will percevere. I know it."
    a "Alright. Let's speak of the 'friends' you have gained, Vila."
    a "Let's see, who should we choose..."

    #  image overlaybg1 =
    $ flashing_bgs()

    $ jump_target = random_jump()
    jump jump_target

# Convince Alkonost that Kiki is better off free ! 
# The room is illiminated with Kikimora's symbol! 
label kiki_hope: 
    a "Ah. Kikimora. Poor creature longs for a new home, for someone to care for."
    a "How do you plan exactly on making her life better?"

    menu:
        "Promise to Rebuild":
            v "By keeping my promise to her. We will rebuild together, giving her a new family and a home to care for."
        "Provide Companionship":
            v "By being there for her. She will have a new family and friends who will care for her and make her feel valued."

    a "You are just one small creature. Are you ready to take on this kind of responsibility?"

    v "I will not be alone. We will do it together."

    jump alk_stirs_drama



label po_hope:
#Convince Alkonost that Poludnicja is better off free ! 
# The room is illiminated with Pol's symbol!
    a "Ah. Poludnicja. She has an angry exterior, but inside her hurt runs deeper than others."
    a "How do you plan exactly on making her life better?"

    menu:
        "Find Balance":
            v "By helping her find balance and peace. She will no longer be tormented by the past and will find a new purpose."
        "Support Her Journey":
            v "By supporting her journey to self-discovery. She will find new ways to thrive and be happy."

    a "You are just one small creature. Are you ready to take on this kind of responsibility?"

    v "Yes, with the help of my friends, I can."

    jump alk_stirs_drama
 

#Convince Alkonost that Lisovyk is better off free ! 
# The room is illiminated with Lisovyk's symbol!
label lis_hope:
    a "Ah Lisovyk. Grumpy old guys with a heart of gold."
    a "How do you plan exactly on making his life better?"

    menu:
        "Restore Forests":
            v "By restoring the forests and lands he once protected. Together, we will heal the wounds of the past."
        "Create New Habitats":
            v "By creating new habitats for him to protect and nurture. He will find new purpose in caring for these lands."

    a "You are just one small creature. Are you ready to take on this kind of responsibility?"
    v "Yes, with the strength we all share."

    jump alk_stirs_drama


#Convince Alkonost that Rusalka is better off free ! 
# The room is illiminated with Rusalka's symbol!
label r_hope:
    a "Ah. Rusalka. This poor unfrtunate sooul."
    a "How do you plan exactly on making his life better?"

    menu:
        "Grant Freedom":
            v "By giving her the freedom to explore the waters and find peace. She will no longer be bound by the past."
        "Provide New Adventures":
            v "By offering her new adventures and places to discover. She will find joy in the journey and the new experiences."

    a "You are just one small creature. Are you ready to take on this kind of responsibility?"

    v "Yes, I know I am strong enough."
    jump alk_stirs_drama

label alk_stirs_drama: 
    a "Well, I guess there is only one person left to vouch for."
    a "The one creature at the heart of all of this."
    v "The one creature who has been the most resisting to my help throughout my reign over the this dimention."
    v "Why do you speak as though we've met before? I've only just met you."
    a "I'm afraid not, child."
    a "You see, Berehynia has tried this many times before. Maybe you're the same Vila, or maybe you're one of the others. Each time, you fail, your memories erased, and you return."
    v "What are you saying?"
    a "Yes, dear Vila, you have been here before. Many times. And each time, you couldn't handle it. You fell into despair, your memories wiped clean."
    a "So, tell me, how will this time be any different? Why should I believe you will succeed now?"

    show dim_overlay with dissolve
    pause 0.1

    jump vila_hope

#Convince Alkonost that you, Vila, are better off free ! 
label vila_hope: 
    
    # a "Now, prove to me that you, Vila, will be fine with your memories intact."

    # show dim_overlay with dissolve
    v "No, no, no..."
    v "No... this can't be true..."
    v "Have I really been through this before?"
    v "Is there no hope? Are we doomed to repeat this cycle forever?"
    "Vila begins to lose hope, the darkness creeping in as she struggles to resist the darkness."
    
    # The screen dims to almost black to represent Vila's despair
    show black with dissolve
    pause 1.0

    # EPIC MUSIC STARTS ? 
    # The screen gets darker and darker and the only thing we can see is the "menu" choices: Hope, Accept Help, Keep Going, Fight, Persevere
    "A cacophony of familiar voices:"
    "We're here, dear Vila. We're all here for you. Don't give up now."
    menu: 
        "Hope":
            "You don't have to be the only one responsible for us. We are all responsible for each other, we will all care for each other."
    menu:
        "Keep Going":
            "And if we must repeat this journey again, so we will."
    menu: 
        "Persevere": 
            "It won't be in vain, butterfly."
    menu: 
        "Accept Help": 
            "The closeness we feel towards each other will not be erased, it will only grow stronger."

    hide black with dissolve
    hide dim_overlay with dissolve

    v "You're right... I can't give up. Not now. Not ever. We will break this cycle, together."
    v "If not now, then next time! If not next time, then on a 100th time, but I know we will do it!"

    a "Curious development. Very curious."
    
    jump alk_chill


label alk_chill: 
    a "I see."
    a "Perhaps my services are no longer needed here."
    a "You have convinced me. For now."
    pause 0.3
    a "You are free to go."
    # SOUND OF RELIEF ? 

    # Vila is shining and all of the others appear? 

    v "I want to say goodbye to Mara and Berehynia."
    a "Very well."

    

    jump game_over_light





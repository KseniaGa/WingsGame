# Alconost, boss

label toproom:
    scene black
    
    hide all
    
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
    #Mara and Berehynia are banished 

    a "That's better. "

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
            v ""
            jump choice2 

label choice2:

    menu:
        "Keep Sleeping (it is less painful)": 
            v "A little nap wouldn't hurt..."
            b "I'm sorry, I can't let this happen"
            jump toproom 
        "RESIST": 
            v ""
            jump choice3 

label choice3:

    menu:
        "Keep Sleeping (it is what you want deep inside)": 
            v "It is what I want deep inside"
            b "No, it's not, dear, you can't give up"
            jump toproom 
        "RESIST": 
            v ""
            jump resist 

label resist: 

    a "Very well."
    a "Plead you case, Vila."
    v "This is not a life, Alkonost. We are not living, we're barely even existing."
    a "If you had all your memories back, Vila, if you knew in what a  state I found the others... You wouldn't want to leave, believe me."
    v "I can't speak of the memories I've lost, but I can speak of the friends I've gained. Together we will percevere. "
    a "Alright. Let's speak of the 'friends' you have gained, Vila."
    a "Let's see, who should we choose..."

    # Symbols of the characters interchange in the background 
    # choose a random companion 
    # comment if you failed to recruit someone 

#make a random function
if kiki_already_joined: 
    jump kiki_hope
elif po_already_joined: 
    jump po_hope 
elif lis_already_joined: 
    jump lis_hope 
else:
    jump r_hope 

# Convince Alkonost that Kiki is better off free ! 
# The room is illiminated with Kikimora's symbol! 
label kiki_hope: 
    a "Ah. Kikimora."
    a "How do you plan exactly on making her life better?"

    v "By keeping my promise to her..."
    # We will rebuild together 
    # We will give her a new family

    a "You are just one small creature."

    a "Are you ready to take on this kind of responsibility?"

    v ""



label po_hope:
#Convince Alkonost that Poludnicja is better off free ! 
# The room is illiminated with Pol's symbol!
    a "Poludnicja."

    a "How do you plan exactly on making her life better?"

    a "Are you ready to take on this kind of responsibility?"
 

#Convince Alkonost that Lisovyk is better off free ! 
# The room is illiminated with Lisovyk's symbol!
label lis_hope:
    a "Lisovyk."

    a "How do you plan exactly on making his life better?"

    a "Are you ready to take on this kind of responsibility?"


#Convince Alkonost that Rusalka is better off free ! 
# The room is illiminated with Rusalka's symbol!
label r_hope:
    a "Rusalka."
    a "How do you plan exactly on making her life better?"

    a "Are you ready to take on this kind of responsibility?"

label alk_stirs_drama: 
    a "Well, I guess there is only one person left to vouch for."
    a "The one creature at the heart of all of this."
    a "..."

    v "Why do you speak as though we've met before?"
    a "Ha-ha I see. Why don't you ask your guardian angel, Vila?"
    a "I can still feel her presence looming nearby."
    a "Come on, Berehynia, share with the class."

    #$ increase_darkness()
    show dim_overlay with dissolve
    pause 0.1
    #hide dim_overlay with dissolve

    "We're here Vila, there's still hope, we're here for you! "

    jump vila_hope

#Convince Alkonost that you, Vila, are better off free ! 
label vila_hope: 
    v "Why does anything matter? I will just be back here again without any memory. So will we all. What's the point?"
    # The characters try to reassure her

    # Epic music? 
    # The screen gets darker and darker and the only thing we can see is the "menu" choices: Hope, Accept Help, Keep Going, Fight, Persevere
    
    jump alk_chill

label alk_chill: 
    a "I see."
    a "Perhaps my services are no longer needed here."
    a "You have convinced me. For now."
    pause 0.3
    a "You are free to go."

    # Vila is shining and all of the others appear? 

    v "I want to say goodbye to Mara and Berehynia."
    a "Very well."





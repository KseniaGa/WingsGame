# ref: https://uk.wikipedia.org/wiki/%D0%9B%D1%96%D1%81%D0%BE%D0%B2%D0%B8%D0%BA

# Лісовик уявлявся як бородатий сірий дід, часто одягнений у звірині шкури чи червоний одяг. Йому притаманні атрибути, 
# пов'язані з лівим боком — ліва частина одягу покриває праву, ліве взуття одягнуто на правій нозі тощо. Може змінювати зріст, 
# стаючи то нижчим від трави, то вищим за дерева. Очі цього духа зелені й палають[6][7]. Також лісовик здатний постати в подобі 
# вовка, сови, або вітру[8]. Вважалося, лісовик не має тіні. Влітку ходить лісом, а взимку спить у землі[7].

# Може лякати людей, що заходять до лісу, своїм сміхом, збивати зі шляху, забрати дитину. Вважався покровителем вовків та дрібних 
# звірів[6], що випасає зайців і оленів, а ведмеді служать йому як охоронці[8]. В пізніх уявленнях лісовики полюбляють грати в 
# карти і коли один лісовик програється, то віддає іншому своїх звірів[7]. Жіночий відповідник лісовика — лісунка, що уявлялася як 
# жінка з довгими грудьми[6], є дружиною лісуна-чоловіка. За уявленнями словʼян, лісовики мають своє військо й підданих, коли 
# воюють люди, між собою воюють і лісовики[7].

# За народними уявленнями слов'ян, лісовика можна задобрити, лишивши для нього частування. Наприклад, мисливцям за це дух 
# приганятиме звірів, а худобі пастухів не дає загубитися в лісі. Вважалося, лісовик не любить тих, хто лається в його володіннях, 
# хто відпочиває на стежці, заходить до лісу в певні дні. Особливо лісовики начебто активні на Іванів день, Воздвиження і Єрофія[8].

# Серед українців було повір'я, що лісовик зимує в барлозі, поруч із ведмедем, і з носа у нього стирчить бурулька. Існувало повір'я: 
# якщо смикнути полісуна за бурульку, вона розсиплеться золотими грішми[9].
default lisovyk_attitude = 0 
default lisovyk_visited = False
default lisovyk_joined = False
default lisovyk_banana_joke = False

label room4:
    scene room hell bg

    if lisovyk_joined:
        jump lisovyk_already_joined  
    elif lisovyk_visited:
        jump lisovyk_already_visited  
    else: 
        jump lisovyk_intro


    # jump lisovyk_guess

label lisovyk_already_joined:
    b "There is nothing left here, except the old dry leaves."
    call screen backButton

label lisovyk_already_visited:
    show berehynia at right with dissolve
    b "I know he is old and grumpy, but you got it!"

    show lisovyk at center with dissolve
    show vila at left with dissolve
    hide berehynia at right with dissolve
    show lisovyk at rightly with move 
    
    jump lisovyk_guess

label lisovyk_intro:
    show lisovyk at center with dissolve
    show vila at left with dissolve
    pause 0.1
    show berehynia at rightly with dissolve

    b "Lisovyk is a fighter at heart. Till the very end was he defending the nature and all that lives in the shadows of the woods."
    b "Now he himself is in the deep shadows where no sun ray reaches. However, I am sure you can help him too, Vila.."
    b "And yes, beware of something... "
    b "Sometimes his memory fails due to his age, but he does not like when people remind him that! Be kind!"

    # flashback scene about Lisovyk?

    hide berehynia at rightly with dissolve

    $ show_progress_bar()

    l "This is not looking good, not looking good, I'm telling ya."

    show lisovyk at rightly with move 

    v "Lisovyk? Lisovyk, I am Vila."

    v "Lisovyk..?"
    # l "Liso-what? Speak louder, child. The voices of leaves keep whispering into my ears, I forget myself."
    l "Lyso-what? Speak louder, child. The voices around keep whispering into my ears, I forget myself."

label lisovyk_guess: 
    
    menu:
        "Make a fun joke":
            v "Do you have bananas in your ears?"
            # "Presence of Lisovyk makes Vila feel like an actual child, even though she is hundreds years old, maybe older than him!"
            l "Excuse me?"
            l "Bananas?"
            l "Bananas don't grow where I come from. The father of the jungles takes care of them. "
            v "The father of the jungles???"
            l "Hmm. I haven't spoken to him in ages...He's a good fellow. Don't know why I feel I know him."
            l "*Experiences a sudden sense of nostalgia*"
            v "*Has no clue what he is talking about*"
            $ lisovyk_attitude+=5 #for sudden nostalgia
            $ lisovyk_banana_joke=True
            jump lisovyk_remind_who_he_is

        "Ask directly about escape":
            v "I've travelled these caves for a while.."
            v "And I learned there is a way out.. But you need to remember who you are, Lisovyk!!!"
            l "Brhhhkmmm. What?!"
            l "I just had a cup of morning dew now. Or, I think it was dew.."
            l "Or, i think I did..."
            v "..."
            $ lisovyk_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump lisovyk_remind_who_he_is

        "Tell him he's trapped":
            v "You forget yourself because of the darkness that came upon us."
            l "I am lost, child."
            v "How long have you spent in this depth?"
            l "I have zero clue how long it's been, nor what happened... Time flies!"
            l "At the same time, for me it always flies differently...One year for you is like a day for me - this much I can remember."
            l "But I wonder why.. What am I?"
            l "*questions himself*"
            $ lisovyk_attitude+=10
            jump lisovyk_remind_who_he_is

    call screen backButton


label lisovyk_remind_who_he_is:
    v "Lisovyk? You hear me? I can help you remember!"

    menu:
        # "Father of the foxes": #Cause 'FOX' is LYS
        "Father of the bananas":
            v "Lee-sooh-vyyyk, you are the father of bananas. " 
            if lisovyk_banana_joke:
                l "Again you with your bananas, khekhe."
                l "I know I like them - who doesn't - but it does not quite feel like home..."
                l "I miss my dear friends.."
                v "*self-conscious about Vila's repeated jokes*"
                $ lisovyk_attitude-= 10
                $ darkness_value+= 10
                if darkness_value>= 100:
                    jump game_over_darkness
                # jump dim_screen
                jump get_to_know_more
            else:
                l "Bananas..? I like all the plants."
                l "But mostly trees. Did you know banana is not a tree, but a grass?"
                v "Trees, bush, grass - compared to me they all are gigantic! Let's focus..."
                $ lisovyk_attitude -= 5
                $ darkness_value+= 5
                if darkness_value >= 100:
                    jump game_over_darkness
                # jump dim_screen
                jump get_to_know_more
        
        "Master of the forests":
            v "Lee-sooh-vyyyk, you are the master of the forests."
            l "Forests have trees."
            l "Trees have leaves. "
            l "Leaves rustle..."
            l "Those are not voices, but the leaves!"
            v "Exactly!"
            l "What are the leaves whispering about, Vila?"
            v "You used to protect all the woods and all that lives there!"
            l "Ah yess, that sounds about right. TODO add actual info!"
            v "This place does not look like your home at all.."
            l "Is there a way out?"
            "Lisovyk turns his head left and right, a sound of sqeeky wood follows..."
            $ lisovyk_attitude+= 10
            jump get_to_know_more

        "Patron of the bolds": #Cause BOLD is LYSYY
            v "Lee-sooh-vyyyk, you are the patron of the bolds."
            l "Khe-khe. Bolds?"
            l "My dress might be getting drier every season, and the leaves on my head are falling, yes..." 
            l "...but this is nothing but a natural process."
            v "*whoops*"
            $ lisovyk_attitude -= 10
            $ darkness_value+= 10
            if darkness_value >= 100:
                jump game_over_darkness
            # jump dim_screen
            jump get_to_know_more

        "Friend of the frogs":
            v "Lee-sooh-vyyyk, you are the friend of the frogs." # Cause he sits like a frog, and there's a small frog 
            l "Frogs sure.. But not only."
            l "As i said - I think I said - I like ~all~ the animals."
            l "I do sit like a frog on Wednesdays occasionally, spent a lot of time with 'em. "
            l "*looks at his frog freind*"
            $ lisovyk_attitude+=5 #seems too much, need to check if numbers make sense here!
            jump get_to_know_more

label get_to_know_more:
    menu:
        "Ask about his past life":
            v "What else do you remember, Lisovyk?"
            if lisovyk_attitude >= 5:
                l "I remember it used to be different from now."
                v "I know, Lisovyk... I am sorry. What was is like?"
                l "My home was shared with many others - the birds, the wolves, the bears.."
                l "I'd walk the same old paths, and cherish the peace of the woods, protect it."
                $ lisovyk_attitude+= 5
            else:
                l "I remember nothing, but the sounds."
                v "What were they like? The birds? The hares?"
                l "The latest memories seem dark, very dark. Fire cracking, screams and smoke, smoke everywhere..."
                l "Cannot recall what life before was like."
                v "Oh..."
                $ lisovyk_attitude-=5

            jump invite_lisovyk

        "Tell about his past life:":
            v "You used to rest at the foot of the Forest, and play cards with your friends!"
            l "Games with friends - ha. Something so foreign here. You are the first visitor I had in ages.."
            v "That was your leisure. And at other times, you took care of the cattle, so it does not get lost in your woods.."
            v "You also helped the people, but often only if they leave a snack."
            l "I am starting liking you, Vila. What are YOU doing here?"
            v "I'm helping spirits like us to escape the darkness...Or, at least that's what I'm trying to do.."
            $ lisovyk_attitude+= 5
            jump invite_lisovyk

label invite_lisovyk:
    if lisovyk_attitude >= 20: #make the level harder?
        v "I know there is a way out, up there, to the sun. Do you want to hear the birds and rustle of the leaves again? Do you wanna join me?"

        l "Oh, I would do anything to see my forest again, to protect it and its inhabitants from what is still upon us, and provide shade in the time of peace..."

        $ lisovyk_joined = True
        $ wing_strength+= 1
    
    else:
        v "I know there is a way out, up there, to the sun. Do you want to hear the birds and rustle of the leaves again? Do you wanna join me?"

        l "I don't comprehend what you want of me, child."
        l "You somehow made me more confused about myself."
        l "Well, I guess I will forget about this encounter soonk, brhmsss."
        l "*falls asleep*"   

        $ increase_darkness()
    
    $ lisovyk_attitude = 0
    $ lisovyk_visited = True 

    call screen backButton
    
    
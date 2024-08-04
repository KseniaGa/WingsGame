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

    hide all
    scene poludniciabg

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
    b "*Спосерігає перекотиполе...*"
    call screen backButton

label poludnicia_already_visited:
    show poludnicia at center with dissolve
    show berehynia at right with dissolve
    # b "Poludnytsa is not in the mood indeed. But you dealt with Mara, so this shoudl be doable too!"
    b "Ти вже впоралася з моєю сестрою, тож переконати Полудницю буде як насіння лузати..." #як насі́ння луза́ти

    show vila at left with dissolve
    hide berehynia at right with dissolve
    show poludnicia at rightly with move 
    
    jump poludnicia_greet


label poludnicia_intro:
    show poludnicia at center with dissolve
    show vila at left with dissolve
    pause 0.1
    show berehynia at rightly with dissolve

    b "Полудниця — це дух, що живе у полях. Характер в неї може так собі - але хто з нас ідеальний?"
    b "Захищати поля і не пускати туди непроханих гостей — дуже нелегка справа."
    b "Але, знаєш що? Хто б на її місці не розлютився після всього, що з нами сталося? Удачі, Віло!"


    hide berehynia at rightly with dissolve
    show poludnicia at rightly with move 

    p "Ця темрява зводить мене з розуму!"
    p "Це Полудниця зводить людей з розуму, а ніяк не навпаки!"
    p "Навіть не можу нікому пригрозити ... Але чим? Вже й не згадати! Це.Просто.Зводить.Мене.З.Розуму!" # (the power of the sun? the scythe?)
    p "* сердито ходить туди-сюди * "
    show poludnicia at center with move 
    show poludnicia at rightly with move 

    jump poludnicia_greet



label poludnicia_greet: 
    menu:
        "Тихенько привітати":
            v "Привіт..."
            p "* досі занурена у свої емоції *"
            v "Полуднице, привіт. Я... я Віла."
            p "Вили? Як вили для сіна? Ха. Якось підозріло. Ні, дякую!! Я надаю перевагу іншим знаряддям." #TODO adapt for uktrainian maybe, smth like Вили - для поля?
            v "'Віла', а не 'вила'."
            p "Ай, яка різниця! Ну, і шо ти тут забула?"
            $ poludnicia_attitude+=5
            jump poludnicia_remind
            

        "Сказати заспокоїтися":
            v "Йой-йой-ой. Комусь тут треба охолонути..."
            p "Охолонути?!"
            p "Ти серйозно?! Подивися, де ми! І крім того.."
            p "..хто, в ім'я Мари, ти така?"
            v "Я Віла... І сама тільки нещодавно усвідомила всю ситуацію!"
            v "Повір мені."
            p "?!"
            $ poludnicia_attitude-=10
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_remind
            

        "Почекати мовчки":
            v "..."
            show poludnicia at center with move 
            p "* продовжує сердитися *"
            show poludnicia at rightly with move 
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
            p "What I do now is, ask reapers difficult questions. The ones, like how to sow, and when to reap? You know, the field stuff."
            v "And if they don't answer?"
            p "That you don't wanna know..."
            p "There are worse things happenig now. Field was no safe place for humans at midday. Well now, for nobody.. even me."
            # reapers in the field - ask them questions about how to take care of the fields.
            $ poludnicia_attitude+=5
            jump poludnicia_reassure


label poludnicia_reassure:
    v "I feel your frustartion, Poludnytsa. Things are not easy now indeed... "
    v "So..."
    # v "Would you want to do some of your favourite activities?"
    menu:
        "Let's dance!":
            # ref: "P"oludnitsa, according to beliefs, loves to dance. If she sees a girl lying down to rest in the field, she will wake her 
            #up and begin to persuade her to dance. If the girl agrees, she will be forced to dance until the «evening dawn». 
            #Poludnitsa cannot be beaten in dancing; however, if such a girl is found, the noon spirit will present her with a rich dowry.[8]"

            v "Do you hear the wind howling? What a beat!"
            v "*starts dancing*"
            show vila at rightly with move 
            show poludnicia at left with move 
            show vila at left with move 
            show poludnicia at rightly with move 
            p "* a moment of shock*"
            # show poludnicia at left with move 
            # show poludnicia at rightly with move 
            p "I don't remember the last time I danced!!!"
            p "I will not force you to dance till the dawn, like we would usually. We don't even know when the dawn comes deep in this darkness."
            p "*Poludnytsa looks up*"
            $ poludnicia_attitude+=10
            jump poludnicia_invite

        "Let's ask difficult questions!": 
            # ref "She will stop people in the field to ask them difficult questions or engage them in conversation. 
            # If anyone fails to answer a question or tries to change the subject, she will cut off their head or strike 
            # them with illness."
            v "Just like you ask reapers difficult questions, could I ask you one?"
            p "Noot sure I like the reversed game, noone dared yet to do it.. But go on!"
            v "Say 'Polunytsa'."
            p "'Polunytsa'? Why?"
            v "That's the answer."
            v "*smiles*"
            p "Ha, that was too easy!!"
            p "Your turn!"
            p "Can you tell me.. Where is Zhytomyr?"
            v "👀"
            p "One of my favourites. I wonder what's up with it now?"
            p "I wish I could revenge for it! If needed, of course... If there is anything to revenge for still?"
            $ poludnicia_attitude+=5 
            jump poludnicia_invite

        "Let's fence with sickles!": #pretend her powers are still with her
            v "If your sickle has no good use now... Then how about we play with it?"
            v "I'll be the reaper, and you play yourself!"
            p "Outrageous! Sickles are not toys!"
            p "And I thought I was the one driven mad by the darkness!"
            $ poludnicia_attitude-=5 
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_invite

label poludnicia_invite:
    if poludnicia_attitude>=15:
        v "Poludnytsa, I know there is way out of here. There will be the sun, and hot summer days, there will be new fields to watch. Do you want to come along?"
        p "If I am mad, then this is part of it, and I lose nothing."
        p "I want to let my anger go, I want to fly, and fly, and scream, till everyone can hear me. I'll join you, Vila!"

        "TODO show radiant Poludnytsa"
        $ wing_strength+=1
        jump map

    else:
        v "Poludnytsa, I know there is way out of here. There will be the sun, and hot summer days, there will be new fields to watch. Do you want to come along?"
        p "I see no point in going anywhere!"
        p "These are empty promises, it seems. The past me is the past, whatever she was like..."
        v "Poludnytsa..."
        $ increase_darkness()

    $ poludnicia_attitude = 0
    $ poludnicia_visited = True 

    call screen backButton 

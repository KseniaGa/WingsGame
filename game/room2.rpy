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
            p "Тебе не дратує мій гнів?"
            p "Як ти зберігаєш свій спокій?"
            p "Я вже сто років не відчувала спокою!"
            v "..."
            p "Хм, а ти мені подобаєшся. Трошки. Як тебе звати?"
            v "Я Віла... Привіт, Полуднице!"
            $ poludnicia_attitude+=10
            jump poludnicia_remind

            
label poludnicia_remind:
    v "Я можу допомогти тобі згадати, хто ти!"
    
    menu:
        "Володарка сонця":
            v "Ти контролюєш рух сонця над нашими землями."
            v "Щоб воно освітлювало поля так, як потрібно, в ~полудень~!"
            p "Хм, я пригадую тепер, що дійсно була завжди активнішою в найспекотнішу годину найспекотніших літніх днів!"
            p "Але я не керую його, цебто сонця, рухом. Це робить Дажбог, чи як там його кличуть."
            p "Таким чином, ти помиляєшься!"
            v "*Віла затамувала подих*"
            p "Гарна була спроба... "
            p "Але! Який сенс говорити про сонце, коли ми застрягли в цій клятій печері!!!"
            $ poludnicia_attitude-=5
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_reassure

        "Дух полів":
            v "Ти дух полів і захищаєш їх від злодіїв."
            p "Як так виходить, що ти мене знаєш, а я тебе - ну взагалі ніяк?!"
            p "Ну, будь як там, це близько до істини."
            p "Більшість часу, я потрохи пригадую, літала я навколо над полями, і маскувалася під пил, що несеться вітром."
            p "А потім з'являлася у своїй справжній подобі.."
            v "...в полудень."
            p "Коли сонце в зеніті. Це час мого(!) дійства..."
            v "...а для інших - час відпочинку."
            p "Саме так! Чудові буди часи... Часи, що минули!"
            $ poludnicia_attitude+=10
            jump poludnicia_reassure

        "Леді-Опудало":
            v "По суті, ти відлякуєш будь-яких відвідувачів полів в полудень. Я чула таке."
            v "Ти дійсно захищаєш поля, але твої методи, гм, доволі суворі, м'яко кажучи.."
            p "'Опудало'... Це трохи грубо. Та правдиво! Сміливо з твого боку, Віло!!"
            v "*oй-oй*"
            p "Мені подобається цей комплімент!"
            p "НІЯКОЇ РОБОТИ ОПІВДНІ - хіба це так важко, дотримуватись цього правила?! А вони все приходять.. Дорослі, малі. Хтось має це зупиняти! Хто, як не я?!!"
            v "Це тому ти з собою носиш ... косу або серп?"
            p "Ха, ні, це застарілі методи. Зараз це просто модно. Серед полудниць..."
            p "Тепер же я просто ставлю женцям складні запитання. Наприклад, як сіяти і коли жати? Ти знаєш, всяке таке, про поля."
            v "А якщо вони відповідають невірно, то?"
            p "Цього тобі краще не знати..."
            p "Набагато гірші речі відбуваються навколо зараз. Поля ніколи не були безпечними для людей опівдні.. Ну, а зараз вони є небезпечні для всіх нас, навіть для мене."
            p "Але час помсти ще прийде..."
            # reapers in the field - ask them questions about how to take care of the fields.
            $ poludnicia_attitude+=5
            jump poludnicia_reassure


label poludnicia_reassure:
    v "Я розумію твоє розчарування, Полуднице. Зараз справді нелегко..."
    v "Тож..."
    # v "Would you want to do some of your favourite activities?"
    menu:
        "Гайда танцювати!":
            # ref: "P"oludnitsa, according to beliefs, loves to dance. If she sees a girl lying down to rest in the field, she will wake her 
            #up and begin to persuade her to dance. If the girl agrees, she will be forced to dance until the «evening dawn». 
            #Poludnitsa cannot be beaten in dancing; however, if such a girl is found, the noon spirit will present her with a rich dowry.[8]"

            v "Чуєш, як вітер завиває?"
            v "*починає танцювати*"
            show vila at rightly with move 
            show poludnicia at left with move 
            show vila at left with move 
            show poludnicia at rightly with move 
            p "* мить шоку *"
            # show poludnicia at left with move 
            # show poludnicia at rightly with move 
            p "Не пам'ятаю, коли востаннє танцювала!!!"
            p "Не буду змушувати тебе танцювати до світанку... Я навіть не знаю, коли буде світанок, і чи він ще взагалі існує."
            p "*Poludnytsa looks up*"
            $ poludnicia_attitude+=10
            jump poludnicia_invite

        "Задати складне питання!": 
            # ref "She will stop people in the field to ask them difficult questions or engage them in conversation. 
            # If anyone fails to answer a question or tries to change the subject, she will cut off their head or strike 
            # them with illness."
            v "Знаєш як ти задаєш складні питання женцям в полях? Чи можу я задати тобі одне?"
            p "Не впевнена, що мені подобається ця гра з перевертанням ролей, ніхто ще не наважувався на це... Але давай!"
            v "Скажи 'Полуниця'."
            p "'Полуниця'? І що?"
            v "Ось і відповідь."
            v "*усміхається*"
            p "Ха, це було занадто легко!!"
            p "Твоя черга!"
            p "Чи можеш ти мені сказати... де Житомир?"
            v "👀"
            p "Одне з моїх улюблених. Цікаво, що там зараз?"
            p "Хотілося б помститися за нього! Якщо потрібно, звісно... Якщо ще є, за що мститися.."
            $ poludnicia_attitude+=5 
            jump poludnicia_invite

        "Грати серпами!": #pretend her powers are still with her
            v "Якщо твій серп зараз не має доброго застосування... Як щодо того, щоб пограти з ним?"
            v "Я буду жницею, а ти будь собою!"
            p "Це безглуздя! Серпи — не іграшки!"
            p "А я думала, що це я зійшла з розуму від цієї темряви!"
            $ poludnicia_attitude-=5 
            $ darkness_value+= 10
            if darkness_value>= 100:
                jump game_over_darkness
            # jump dim_screen
            jump poludnicia_invite

label poludnicia_invite:
    if poludnicia_attitude>=15:
        v "Полуднице, я знаю, що звідси є вихід. Там буде сонце, спекотні літні дні, нові поля, які треба охороняти! Хочеш піти зі мною?"
        p "Якщо я вже зійшла з розуму, то це теж частина цього...  Думаю, я нічого не втрачу, якщо скажу так."


        show poludnicia radiant

        pause 0.1

        if wing_strength < wing_strength_threshold:
            $ wing_strength += 1
        play sound tone
        
        p "Я хочу відпустити свій гнів, хочу літати, літати і кричати, щоб мене всі чули. Я приєднаюсь до тебе, Віло!"
        
        $ poludnicia_attitude = 0
        $ poludnicia_visited = True 
        $ poludnicia_joined = True

        jump map

    else:
        v "Полуднице, я знаю, що звідси є вихід. Там буде сонце, спекотні літні дні, нові поля, які треба охороняти! Хочеш піти зі мною?"
        p "Я не бачу сенсу кудись йти!"
        p "Це все порожні балачки і обіцянки. Минуле — в минулому... Трясця!"
        v "Полуднице..."
        $ increase_darkness()

    $ poludnicia_attitude = 0
    $ poludnicia_visited = True 

    call screen backButton 

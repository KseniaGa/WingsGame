# Alconost, boss

init python:
    import random

    def random_jump():
        choices = []
        if kiki_joined:
            choices.append("kiki_hope")
        if poludnicia_joined:
            choices.append("po_hope")
        if lisovyk_joined:
            choices.append("lis_hope")
        if rusalka_joined:  
            choices.append("r_hope")
        
        return random.choice(choices)
    
    def flashing_bgs():
        bgs = ["kikimorabg", "poludniciabg", "lisovykbg", "rusalkabg"]
        for bg in bgs:
            renpy.show(bg)
            renpy.pause(1.0)  # Pause for 0.1 seconds
            renpy.hide(bg)
        #renpy.show()
       

label toproom:
    scene black
    
    hide all

    show vila at left with dissolve:
        xzoom 0.5
        yzoom 0.5
        yalign 0.7

    v "Тут нікого немає. Може, просто втечемо поки є час?"
    b "Вона буде тут за мить, люба, ти не зможеш пройти повз неї силою, вона вислухає тільки розум."
    b "Будь обережна з нею. Не показуй занадто багато емоцій, особливо смутку."

    #pause 0.5
    play sound "dragon-wings.ogg"
    pause 3.0
    show alkonost at center with dissolve:
        xzoom 0.9
        yzoom 0.9

    a "Ах, вітаю, Віло."
    a "Сяюча, як завжди."
    a "Хто сьогодні з тобою?"

    v "Алконост. То ти причина цієї темряви..."

    a "Хм. Тут трохи занадто людно."

    v "Зачекай!" 

    "Віла відчуває, як присутність Берегині зникає..." 
    $ play_random_thump()


    # SOUND: HEARTBEAT? play sound heartbeat
    a "Тепер краще."
    v "арвіпврпв"
    v "ні, ні, ні."
    
    a "Я дам тобі легкий вихід, Віло."
    a "Тобою керувала Берегиня, тому я дам тобі останню можливість."
    a "Обирай."
    jump choice1

label choice1: 
#START PLAYING NORMAL MUSIC HERE
    play music bgm loop

    menu:
        "Спати далі (так легше) ": 
            v "Я так втомилася..."
            b "Я знаю, що ти втомлена, люба, але ми не можемо здатися тут."
            jump toproom 

        "ОПИРАТИСЯ": 
            v "Ні, забуття вже не варіант для мене, Алконост."
            a "Хм"
            jump choice2 

label choice2:

    menu:
        "Спати далі (так менш боляче)": 
            v "Трохи поспати не зашкодить..."
            b "Вибач, Віло, я не можу цього допустити..."
            jump toproom 
        "ОПИРАТИСЯ": 
            v "Ні."
            v "Ні, я не пройшла весь цей шлях, щоб здатися зараз. Цього не станеться, Алконост."
            a "Хм"
            jump choice3 

label choice3:

    menu:
        "Спати далі (це те, чого ти хочеш в глибині душі)": 
            v "Це те, що я хочу в глибині душі."
            b "Ні, це не так, люба."
            b "Ти побачиш, що твій єдиний варіант - продовжувати рухатися вперед, ти побачиш це зрештою..."
            jump toproom 
        "ОПИРАТИСЯ": 
            v "Ні!"
            v "Те, чого я хочу в глибині душі - повернутися додому і допомогти своїм друзям."
            a "Хм"
            jump resist 

label resist: 

    a "Добре."
    a "Я слухаю тебе, Віло."
    v "Це не життя, Алконост. Ми не живемо, ми ледь існуємо."
    a "Якщо б ти мала всі свої спогади, Віло, якби ти знала, в якому стані я знайшла інших... Ти б не хотіла залишити потойбіччя, повір мені."
    v "Я не можу говорити про спогади, які я втратила, але я можу говорити про друзів, яких я здобула. Разом ми вистоїмо. Я знаю це."
    a "Добре. Поговоримо про 'друзів', яких ти здобула, Віло."
    a "Подивимось, кого ж ми виберемо..."
    #  image overlaybg1 =
    scene black
    $ flashing_bgs()
    #$ flashing_bgs()
    #hide all
    scene black 
    $ jump_target = random_jump()
    $ renpy.jump(jump_target)


# Convince Alkonost that Kiki is better off free ! 
# The room is illiminated with Kikimora's symbol! 
label kiki_hope: 
    scene kikimorabg
    show kikimora at center with dissolve:
        xzoom 0.75
        yzoom 0.75 

    #bgs = ["kikimorabg", "poludniciabg", "lisovykbg", "rusalkabg"]
    a "А, Кікімора. Бідолашна істота прагне нового дому, когось, хто буде піклуватися про неї."
    a "Як ти плануєш зробити її життя кращим?"

    menu:
        "Обіцяти відбудувати":
            v "Виконуючи свою обіцянку їй. Ми відбудуємо разом, дамо їй нову родину і дім, про який вона буде піклуватися."
        "Надати компанію":
            v "Бути поруч з нею. Вона матиме нову родину і друзів, які піклуватимуться про неї і зроблять її щасливою."

    a "Ти всього лише одна маленька істота. Чи готова ти взяти на себе таку відповідальність?"

    v "Так, я дала їй обіцянку. Я маю намір її виконати."


    scene black 
    jump alk_stirs_drama



label po_hope:
#Convince Alkonost that Poludnicja is better off free ! 
# The room is illiminated with Pol's symbol!
    scene poludniciabg
    show poludnicia at center with dissolve:
        xzoom 0.75
        yzoom 0.75 
    a "А, Полудниця. Вона має злий вигляд, але всередині її біль глибший, ніж у інших."
    a "Як ти плануєш зробити її життя кращим?"

    menu:
        "Знайти баланс":
            v "Допомагаючи їй знайти баланс і мир. Вона більше не буде мучитися минулим і знайде нову мету."
        "Підтримувати її шлях":
            v "Підтримуючи її шлях до самопізнання. Вона знайде нові способи процвітання і бути щасливою."

    a "Ти всього лише одна маленька істота. Чи готова ти взяти на себе таку відповідальність?"

    v "Так, я пройшла цей шлях, я знаю, що можу зробити все."
    scene black
    jump alk_stirs_drama
 

#Convince Alkonost that Lisovyk is better off free ! 
# The room is illiminated with Lisovyk's symbol!
label lis_hope:
    scene lisovykbg
    show lisovyk at center with dissolve:
        xzoom 0.75
        yzoom 0.75 
    a "А, Лісовик. Старий буркотун із золотим серцем."
    a "Як ти плануєш зробити його життя кращим?"

    menu:
        "Відновити ліси":
            v "Відновлюючи ліси і землі, які він колись захищав. Разом ми зцілимо рани минулого."
        "Створити нові середовища":
            v "Створюючи нові середовища, які він буде захищати і доглядати. Він знайде нову мету в піклуванні про ці землі."

    a "Ти всього лише одна маленька істота. Чи готова ти взяти на себе таку відповідальність?"
    v "Так! Я знаю, що я стійка, я знаю, що я готова до всього."

    scene black
    jump alk_stirs_drama


#Convince Alkonost that Rusalka is better off free ! 
# The room is illiminated with Rusalka's symbol!
label r_hope:
    scene rusalkabg
    show rusalka at center with dissolve:
        xzoom 0.75
        yzoom 0.75 
    a "А, Русалка. Ця бідна нещасна душа."
    a "Як ти плануєш зробити її життя кращим?"

    menu:
        "Надати свободу":
            v "Даючи їй свободу досліджувати води і знайти мир. Вона більше не буде прив'язана до минулого."
        "Надати нові пригоди":
            v "Пропонуючи їй нові пригоди і місця для відкриття. Вона знайде радість у подорожах і нових враженнях."

    a "Ти всього лише одна маленька істота. Чи готова ти взяти на себе таку відповідальність?"

    v "Так, я знаю, що свою силу."
    scene black
    jump alk_stirs_drama

label alk_stirs_drama: 
    a "Зрозуміла тебе, Віло. Дякую за співпрацю."
    show alkonost at center with dissolve:
        xzoom 0.9
        yzoom 0.9
    a "Здається, залишилася лише одна істота, щоб свідчити."
    show vila at left with dissolve :
        xzoom 0.5
        yzoom 0.5
        yalign 0.7
    a "Та істота, яка була найбільш опірною до моєї допомоги протягом мого правління в цьому вимірі."
    v "Чому ти говориш, наче ми вже зустрічалися? Я щойно зустріла тебе."
    a "Боюся, що ні, дитя."
    a "Бачиш, Берегиня пробувала це багато разів. Можливо, ти та ж сама Віла, а можливо, одна з інших. Кожного разу ви зазнаєте поразки, ваші спогади стираються, і ви повертаєтесь знову."
    stop music  
    # HEART BEAT SOUND 
    v "Про що ти говориш? Це неможливо..."
    a "Так, дорога Віла, ти була тут раніше. Багато разів. І кожного разу ти не могла з цим впоратися. Ти впадала в розпач, твої спогади стиралися."
    a "Отже, скажи мені, чим цей раз буде іншим? Чому я повинна вірити, що цього разу ти досягнеш успіху?"

    show dim_overlay with dissolve
    pause 0.1

    jump vila_hope

#Convince Alkonost that you, Vila, are better off free ! 
label vila_hope: 
    
    # a "Now, prove to me that you, Vila, will be fine with your memories intact."
    hide alkonost with dissolve 
    show vila at center with move 
    v "Ні, ні, ні..."
    v "Ні... це не може бути правдою..."
    v "Невже я справді проходила через це раніше?"
    v "Чи немає надії? Чи ми приречені повторювати цей цикл вічно?"
    "Віла починає втрачати надію, темрява повзе в її душу."
    hide vila with dissolve 
    # The screen dims to almost black to represent Vila's despair
    #show black with dissolve
    

    pause 2.0

    # EPIC MUSIC STARTS ? play music smth 
    play music bgm loop 
    play ambience boss loop
    # The screen gets darker and darker and the only thing we can see is the "menu" choices: Hope, Accept Help, Keep Going, Fight, Persevere
    "Какофонія знайомих голосів:"
    "Ми тут, люба Віло. Ми всі тут з тобою, ти не сама. Не здавайся!"
    menu: 
        "Надія":
            p "Тобі не потрібно бути відповідальною за нас. Ми всі відповідальні одне за одного, ми будемо всі піклуватися одне про одного."
    menu:
        "Продовжувати":
            l "І якщо нам доведеться повторювати цю подорож знову, так і буде."
    menu:
        "Вистояти": 
            ki "Це не буде марно, метелик."
    menu:
        "Прийняти допомогу": 
            r "Близькість, яку ми відчуваємо одне до одного, не буде стерта, вона тільки зростатиме."

    #hide black with dissolve
    hide dim_overlay with dissolve
    scene black 
    show vila at left with dissolve

    v "Ви праві... Я не можу здатися. Не зараз. Ніколи. Ми зламаємо цей цикл разом."
    v "Якщо не зараз, то наступного разу! Якщо не наступного разу, то на сотий раз, але я знаю, що ми зробимо це!"

    a "Цікавий розвиток подій. Дуже цікавий."

    
    jump alk_chill


label alk_chill: 

    a "Хм."
    a "Можливо, мої послуги більше не потрібні тут."
    a "Ти переконала мене. Поки що."
    pause 1.0
    a "Ви можете йти."
    scene marabg
    # Vila is shining and all of the others appear? 
    "Віла відчуває радість усіх своїх друзів, вона переповнює все оточування."

    show kikimora radiant with dissolve
    ki "Ти зробила це, метелик, я знала, що ти зможеш!"
    hide kikimora radiant with dissolve
    show poludnicia radiant with dissolve
    p "Твоя мужність і рішучість вражають, Віла. Ми тепер вільні завдяки тобі."
    hide poludnicia radiant with dissolve

    show lisovyk radiant with dissolve
    l "Твоя сила і відданість допомогли нам усім, дякую тобі, Віла."
    hide lisovyk radiant with dissolve

    show rusalka radiant with dissolve
    r "Ти принесла світло в наші життя і звільнила нас від темряви. Ми ніколи не забудемо це, Віла."
    hide rusalka radiant with dissolve

    show vila at left with dissolve
    v "Алконост, я хочу попрощатися з Берегинею."
    a "Добре."

    show berehynia at right with dissolve

    b "Я бачу, ти досягла успіху, люба."
    b "Вітаю, я знала, що ти зможеш!"

    v "Я відчуваю, що не можу довіряти твоїм справжнім намірам, Берегине, але незалежно від твоїх методів, це закінчилося нашою свободою, і за це я хочу подякувати тобі."
    hide berehynia at right with dissolve
    play sound "evil-laugh.ogg" 
    show mara at right with dissolve
    m "Ха-ха-ха"
    hide mara at right with dissolve
    show berehynia at right with dissolve 
    b "Просто виконую свою роботу, люба. Бажаю тобі всього найкращого."
    hide berehynia at right with dissolve


    jump game_over_light





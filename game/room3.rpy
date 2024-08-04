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
    b "Як то кажуть, 'і мокрого місця не залишилося'. Хоча тут трошки слизько від води."
    call screen backButton

label rusalka_already_visited:
    show berehynia at right with dissolve
    b "Сила Русалки - дійсно в її чутливісті, але потрібне терпіння, щоб достукатися до неї. Удачі!"

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

    b "Русалка — це водяний дух. А тут, глибоко під землею навіть і підземного струмка нема."
    b "Натомість, єдина вода, яку ти тут знайдеш, — це її сльози..."
    b "Стався до неї з розумінням, Віло!"

    hide berehynia at rightly with dissolve
    show rusalka at rightly with move 

    pause 0.1

    r "Привіт, незнайомко..."

    #$ show_progress_bar()

    r "Що привело тебе до мого мирного ... дому?"

    menu:

        "Розрядити обстановку жартом"":
            v "Твій дім зараз здається занадто сухим, Русалко. Комусь точно потрібно випити хехе!"
            r ""
            r "Ніколи не відчувала такої спраги, як тут."
            r "Вказувати на це НЕ допомагає..."
            v ""
            #Consider not punishing the first encounter...
            $ rusalka_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen

            "*Русалка відчуває ніяковість і ховає обличчя у своє, колись золоте, волосся*. Молодець, Віло."
            pause 1.0
            jump rusalka_remember

        "Обережно представитися":
            v "Я Віла! І шукаю шлях з цієї темряви. Я можу допомогти тобі!"
            r "*переповнена емоціями*"
            v "Не хвилюйся, не хвилюйся! Все, що нам потрібно зробити, це знайти справжню ТЕБЕ. Вона захлвана десь в тобі, я знаю."
            r "Справжню мене? Але я тут... Це моє життя..."
            r "Ти.. Ти можеш мені допомогти?"
            $ rusalka_attitude += 10
            jump rusalka_remember

        "Прямо запитати, що сталося":
            v "Дім? Що сталося з тобою, Русалко? Як ти сюди потрапила?"
            r "Здається, сталися жахливі-жахливі речі. Але я не знаю, що саме..."
            v "Я знаю, Русалко. Це вплинуло на всіх нас, хоча і по-різному."
            r "Ніби якась отрута поглинула мене..."
            v "Гм, це дійсно можна описати так."
            r "Дякую за розуміння, незнайомко."
            $ rusalka_attitude += 5
            jump rusalka_remember

    call screen backButton


label rusalka_remember:
    r "Чомусь моє ім'я несе болісну схожість з тим, що завдало нам так багато шкоди. Яким було моє існування поза цією темрявою?" 

    # show vila at left with dissolve 

    menu:
        "Нести сміх і світло в наші води":
            v "Ти була повна світла і сміху, поки вони не прийшли. Ти наповнювала наші води життям."
            # hide vila with dissolve
            r "Сміх?"
            r "Я не сміялася вже цілу вічність!"
            # show hopefull rusalka's face
            "Русалка підіймає на тебе очі - раптовий, але короткий, момент світла і надії. Потім швидко опускає очі і замовкає."
            v "Так, сміх. Насправді, твоє лоскотання навіть могло бути зброєю."
            r "Гм, я пам'ятаю лоскотання у воді... Ах, плавання і веселощі в воді - найкраще, що є у цьому житті! Найкраше, що було..."# show back the sad rusalka
            $ rusalka_attitude += 10
            jump make_rusalka_feel_better

        "Зрошувати наші ґрунти дощем і допомагати врожаям":
            v "Ти спускалася на землю разом із краплями дощу. Ти збагачувала наші ґрунти, приносила життя."
            # hide vila with dissolve
            r "Ти, мабуть, плутаєш мене з кимось іншим."
            r "Мені дійно подобається вода..."
            r "... але не та, що на небесах."
            $ rusalka_attitude-=5
            $ darkness_value+=5
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump make_rusalka_feel_better 

        "Красти молодих хлопців і дівчат":
            v "Ти бродила нашими полями і викрадала молодих дівчат і хлопців, як відьма."
            v "Це завдавало багато шкоди."
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
            r "Люди завжди бояться того, чого не знають, і помилково вважають нас злими."
            r "Ми виходимо з води лише навесні, щоб допомагати доглядати за врожаєм."
            r "Наскільки це погано?"
            v "Гадаю, це були чутки, вибач..."
            $ rusalka_attitude-=10
            $ darkness_value+=10
            if darkness_value>=100:
                jump game_over_darkness
            # jump dim_screen
            jump make_rusalka_feel_better

label make_rusalka_feel_better:
    # show vila with dissolve
    r "Згадувати минуле буває боляче..."
    v "Але я тут, з тобою, Русалко!"

    menu:
        "Нагадати про її минуле":
            #ref: https://uk.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%96_%D1%81%D0%B2%D1%8F%D1%82%D0%B0
            #ref: https://uk.wikipedia.org/wiki/%D0%A0%D1%83%D1%81%D0%B0%D0%BB%D0%BA%D0%B0
            # ENG: https://en.wikipedia.org/wiki/Green_week
            v "Насправді, твоє ім'я асоціюється із Зеленими святами, або святом Русалій (Розалій)..."
            v "Ці весняні святкування зазвичай повні обрядових дійств на родючість і навіть похоронних ритуалів!"
            # hide vila with dissolve
            r "Я пам'ятаю молодих дівчат у вінках із квітів."
            r "Вони закликали нас під час Русалій, щоб ми принесли вологість і життєву силу у поля."
            $ rusalka_attitude += 10
            jump rusalka_invite
        
        "Дати надію на майбутнє":
            v "Насправді, шкода, завдана тобі, не залишиться назавжди..."
            v "Поля, які ти доглядала, відроджуються."
            r "Поля були затоплені..."
            r "Не можна недооцінювати силу води. Вона приносить як руйнування, так і відродження."
            r "Останнє я постійно забуваю."
        
            $ rusalka_attitude += 5
            jump rusalka_invite

        "Будь реалістом/песимістом": #not sure how to call this option
            # idk, I wanna add a 'wrong answer' but not sure what fits, and if should be here
            v "Насправді, все могло бути набагато гірше, принаймні ти жива і все ще тут."
            v "Це єдине, що ми знаємо напевно."
            # hide vila with dissolve
            r "Мені не вдалося нікого врятувати..."
            r "...тож я залишусь тут, можливо, назавжди."
            r "Я думала... Я думала, ти допоможеш..."
            "Русалка починає співати сумну пісню і відвертається."
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
        v "Русалко, надія ще не втрачена! Якщо ти приєднаєшся до мене, ми зможемо разом знайти шлях додому. Що скажеш?"
        r "Я відчуваю тепло твого доброго серця. Дякую за це."
        r "Я дійсно хочу приєднатися до тебе... Що далі?"

        "TODO: show Rusalka radiant, turns into magic, dissolves"
        "TODO: show vila's wings getting stronger?"
        $ wing_strength+=1

        jump map
    else:
        v "Русалко, надія ще не втрачена! Якщо ти приєднаєшся до мене, ми зможемо разом знайти шлях додому. Що скажеш?"
        
        r "Я не впевнена... Темрява дуже тисне на мене."
        r "Ти надала мені надію, але це ні до чого не призвело..."

        $ increase_darkness()

    $ rusalka_attitude = 0
    $ rusalka_visited = True 

    call screen backButton
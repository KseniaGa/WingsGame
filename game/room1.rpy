default kikimora_attitude = 0  # Відстеження ставлення Кікімори до Віли


label room1:
    # scene room hell bg
    # scene bg_kiki with dissolve

    hide all
    scene kikimorabg

    if kiki_joined:
        jump kiki_already_joined  
    elif kiki_visited:
        jump kiki_already_visited  
    else: 
        jump kiki_intro
        

label kiki_already_joined:
    show berehynia at right with dissolve
    b "Кікімната-"
    b "Перепрошую! Кімната Кікімори наразі пустує. "
    call screen backButton
    

label kiki_already_visited:
    show berehynia at right with dissolve
    b "Спробуй знову, люба! Я знаю, що в тебе вийде!"
    jump kiki_first

label kiki_intro:
    show vila at left with dissolve
    pause 0.1
    show kikimora at center with dissolve
    pause 0.1
    show berehynia at right with dissolve 

    b "Кікімора – це дух дому, що піклується про порядок та чистоту. Вона живе в кожному закутку, стежачи, щоб усе було на своїх місцях."
    b "Коли вона щаслива, дім наповнюється затишком і спокоєм. Але коли її тривожать чи забувають, її сум і тривога можуть стати нестерпними."
    b "Вона була однією з перших, хто загубився в цій темряві, втративши свою сутність та надію."
    b "Допоможи їй згадати, хто вона є, Віло. Її магія може допомогти тобі на твоєму шляху."

    hide berehynia at right with dissolve

label kiki_first: 
    ki "Треба прибирати, треба прибирати..."
    ki "Ніколи не чисто, ніколи не достатньо чисто..."
    ki "Всі пішли, всі залишили..."

    menu:
        "Представити себе":
            v "Вітаю, Кікімора, так? Я Віла."
            $ kikimora_attitude += 5
            ki "Віла? Метелик?"
            ki "Віла? Фея?"
            ki "Вілла? Будинок?"
            ki "Віла такий маленький будинок..."

            v "Ха-ха. Не будинок, Кікі. Щось поміж феєю та метеликом більш."
            ki "Кікі? Ха-ха Кікі..."
            ki "Кікі любить доглядати за будинками..."   
            ki "Кікі любить метеликів..."

            v "Давай тоді знайдемо тобі будинок та метелеків, Кікі."
            ki "Будинок та метеликів..."

            jump remind_her

        "Попросити поради щодо домашніх справ":
            v "Привіт, ти знаєш когось, хто може допомогти мені з домашньою проблемою, я не знаю як..."
            v "Ее... Я не знаю, як користуватися віником."
            ki "Треба прибирати, треба прибирати..."
            ki "Треба допомогти Вілі з віником..."
            ki "Віли не дуже розумні істоти все-таки..."
            ki "Ось, дивись, Віла"
            # SOUND OF SPWEEPING 
            play sound broom1
            "Кікімора починає підмитати та показувати її улюблені підметальні рухи Вілі."
            "Вона виглядає задоволеною собою."
            $ kikimora_attitude += 10
            ki "Дякую, Кікі!"
            ki "Кікі? Ха-ха Кікі..."
            ki "Кікі любить наводити чистоту..."

            б "Чудово, Віла! Продовжуй в цьому ж ритмі!"
            jump remind_her

        "Підкреслити терміновість":
            v "Кікімора, ти повинна негайно піти зі мною."
            $ kikimora_attitude -= 10
            "Кікімора виглядає засмученою та стурбованою."
            #$ darkness_value += 10
            $ increase_darkness()

            if darkness_value >= 100:
                jump game_over_darkness
            # jump dim_screen
            
            ki "Залишити дім... Ні, я не можу, я не можу залишити..."
            ki "Ні, я не можу... А якщо вони повернуться?"

            v "Хто 'вони', Кікі?"
            ki "Кікі? Ха-ха Кікі..."
            ki "Кікі була з сімєю..."
            ki "Кікі доглядала за сімєю..."
            ki "Кікі нема кого доглядати..."
            ki "Всі пішли, всі залишили..."

            v "Я тобі допоможу! Не знаю як, але ми щось придумаємо разом"
            ki "Разом..."


            jump remind_her

label remind_her:
    menu:
        "Показати їй, хто вона":
            "Віла починає наводити лад у кімнаті та прибирати."
            play sound broom2
            "Кікімора дивиться на Вілу, спочатку з непорозумінням, а потім з зацікавленістю."
            $ kikimora_attitude += 10
            ki "Метелик не правильно робить."
            ki "Дивись, метелик..."
            "Віла починає наводити лад у кімнаті та прибирати."
            v "О! Дякую, Кікі, ти справжній експерт у цьому!"
            ki "Кікі експерт?"
            ki "Кікі експерт... Так, експерт..."
            jump reassure_her

        "Сказати їй, хто вона":
            v "Кікімора, ти дух дому, щось жахливе трапилося з тобою, і ти забула, хто ти є, але я тут, щоб нагадати тобі."
            $ kikimora_attitude += 5
            ki "Дух дому..."
            ki "Дух метеликів нагадає мені..."

            в "Не дух метеликів, Кікі. Просто метелик."
            в "Ее, тобто Віла! Просто Віла."
            в "Дух дому - Кікі, Віла - метелик, тобто, я."
            ki "Кікі - дух дому..."

            jump reassure_her

label reassure_her:
    menu:
        "Шукати надію в майбутньому":
            v "Буде багато нових місць, про які потрібно піклуватися, нових сімей, за якими потрібно дивитися."
            $ kikimora_attitude += 5
            ki "Нові місця... Нові сім'ї..."
            ki "Але як довго Кікі ще чекати?"
            ki "Як довго чекати..."
            jump invite_kikimora

        "Шукати надію в минулому":
            v "Я тут, і я допоможу тобі знайти тих, кого ти втратила."
            $ kikimora_attitude += 5
            ki "Метелик допоможе мені..."
            ki "Але хто допоможе метелику?"

            jump invite_kikimora
            
        "Шукати надію в теперішньому":
            v "Є ті, хто потребує твоєї допомоги зараз. Як я."
            $ kikimora_attitude += 10
            ki "Кікі... потрібна?"
            ki "Кікі потрібна метелику?"
            v "Так, звичайно потрібна."
            "Кікі посміхається кріз сльози."
            jump invite_kikimora

label invite_kikimora:

# Add a sentence here? 

    if kikimora_attitude >= 20:
        v "Кікі, я планую знайти новий дім, і мені знадобиться хтось, щоб зробити це місце домівкою... Чи приєднаєшься ти до мене?"
        
        ki "Новий дім... Нова сім'я... Я приєднаюсь до тебе, метелик."
        show kikimora radiant with dissolve
        play sound tone
        $ kiki_joined = True
        $ wing_strength += 1

    else:
        v "Кікі, я планую знайти новий дім, і мені знадобиться хтось, хто може зробити це місце домівкою... Чи приєднаєшься ти до мене?"
        
        ki "Я... Я повинна повернутися до роботи."
        ki "Ніколи не чисто, ніколи не досить чисто..."
        в "Кікі?"
        ki "Всі пішли, всі залишили..."

        
        
        #  $ darkness_value += 20
        $ increase_darkness()
        
    $ kikimora_attitude = 0
    $ kiki_visited = True 

    call screen backButton

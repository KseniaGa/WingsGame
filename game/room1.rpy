default kikimora_attitude = 0  # Відстеження ставлення Кікімори до Віли
default kiki_visited = False
default kiki_joined = False

label room1:
    # scene room hell bg
    # scene bg_kiki with dissolve

    if kiki_joined:
        jump kiki_already_joined  
    elif kiki_visited:
        jump kiki_already_visited  
    else: 
        jump kiki_intro
        

label kiki_already_joined:
    # show berehynia at right with dissolve
    b "Кікімната-"
    b "Перепрошую! Кімната Кікімори наразі пустує. "
    call screen backButton
    

label kiki_already_visited:
    show berehynia at right with dissolve
    b "Спробуй знову, люба! Я знаю, що в тебе вийде!"
    jump kiki_first

label kiki_intro:
    show vila at left with dissolve
    #"Кімната тьмяно освітлена, заповнена старими, сільськими меблями, а тіні танцюють на стінах, коли мерехтливе світло свічок намагається освітити простір."
    
    show kikimora at center with dissolve
    pause 0.1
    show berehynia at right with dissolve

    b "Кікімора, дух дому. Вона була однією з перших, хто загубився в цій темряві."
    b "Але ти можеш їй допомогти, люба, я знаю, що можеш. Удачі."

    hide berehynia at right with dissolve

label kiki_first: 
    ki "Треба прибирати, треба прибирати..."
    ki "Ніколи не чисто, ніколи не достатньо чисто..."
    ki "Всі пішли, всі залишили..."

    menu:
        "Представити себе":
            v "Вітаю, Кікімора, так? Я Віла."
            $ kikimora_attitude += 5
            ki "Віла? Чому ти тут?"
            jump remind_her

        "Попросити поради щодо домашніх справ":
            v "Привіт, ти знаєш когось, хто може допомогти мені з домашньою проблемою, я не можу..."
            $ kikimora_attitude += 10
            ki "..."
            jump remind_her

        "Підкреслити терміновість":
            v "Кікімора, ти повинна негайно піти зі мною."
            $ kikimora_attitude -= 10
            $ darkness_value += 10
            if darkness_value >= 100:
                jump game_over_darkness
            # jump dim_screen
            
            ki "Залишити дім... Ні, я не можу піти... А якщо вони повернуться?"
            v "Хто 'вони', Кіки?"
            jump remind_her

label remind_her:
    menu:
        "Показати їй, ким вона була":
            # v "*Віла починає прибирати*"
            "Віла починає наводити лад у кімнаті."
            $ kikimora_attitude += 10
            ki ""
            v ""
            jump reassure_her

        "Сказати їй, хто вона є":
            v "Кікімора, ти дух дому, щось жахливе трапилося з тобою, і ти забула, хто ти є, але я тут, щоб нагадати тобі."
            $ kikimora_attitude += 5
            ki "Дух дому..."
            jump reassure_her

label reassure_her:
    menu:
        "Шукати надію в майбутньому":
            v "Буде багато нових місць, про які потрібно піклуватися, нових сімей, за якими потрібно дивитися."
            $ kikimora_attitude += 5
            ki "Нові місця... Нові сім'ї..."
            jump invite_kikimora

        "Шукати надію в минулому":
            v "Я тут, і я допоможу тобі знайти тих, кого ти втратила."
            $ kikimora_attitude += 5
            ki "Ти допоможеш мені знайти їх..."
            jump invite_kikimora
            
        "Шукати надію в теперішньому":
            v "Є ті, хто потребує твоєї допомоги зараз. Як я."
            $ kikimora_attitude += 10
            ki "..."
            jump invite_kikimora

label invite_kikimora:

    if kikimora_attitude >= 15:
        v "Кікі, я планую знайти нове місце з друзями, і я думаю, нам знадобиться хтось, щоб зробити це місце домом... Чи зацікавлена ти до нас приєднатися?"
        
        ki "Новий дім... Нова сім'я... Я приєднаюсь до вас."
        "Кікімора починає світитися, її форма стає яскравішою, коли вона знаходить надію і згадує, хто вона є."
        $ kiki_joined = True
        $ wing_strength += 1
        # $ darkness_value -= 20
    else:
        v "Кікі, я планую знайти нове місце з друзями, і я думаю, нам знадобиться хтось, щоб зробити це місце домом... Чи зацікавлена ти до нас приєднатися?"
        
        ki "Я... Я повинна повернутися до роботи."
        "Кікімора виглядає невпевненою, все ще бореться зі своїми спогадами та темрявою."
        ki "Ніколи не чисто, ніколи не досить чисто..."
        ki "Всі пішли, всі залишили..."
        
<<<<<<< HEAD
        #  $ darkness_value += 20
=======
       #  $ darkness_value += 20
>>>>>>> room/lisovyk
        $ increase_darkness()
        
    $ kikimora_attitude = 0
    $ kiki_visited = True 

    call screen backButton

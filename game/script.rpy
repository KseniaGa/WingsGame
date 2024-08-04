# Define characters
define v = Character("Віла", color="#7ec8e3")       # Player Character
define в = Character("Віла", color="#7ec8e3")       

define b = Character("Берегиня", color="#ffcc00")  #  Guide
define б = Character("Берегиня", color="#ffcc00")  

define m = Character("Мара", color="#9932CC")       # Tutorial 
define м = Character("Мара", color="#9932CC")         

define p = Character("Полудниця")                    # Level 2
define ki = Character("Кікімора")                     # Level 2
define l = Character("Лісовик")                       # Level 3
define r = Character("Русалка")                       # Level 3
define a = Character("Алконост")                      # Final Boss

define t1 = "audio/thump1.ogg"
define t2 = "audio/thump2.ogg"
define t3 = "audio/thump3.ogg"
define t4 = "audio/thump4.ogg"
define t5 = "audio/thump5.ogg"
define t6 = "audio/thump6.ogg"

# wings variables
default wing_strength = 0
default wing_strength_threshold = 3

# Define character images
image vila:
    "character_sprites/vila_wings_[wing_strength].PNG"
    #xzoom(0.5)
    #yzoom(0.5)

image berehynia = "character_sprites/berehynia_neutral.png"
image mara = "character_sprites/mara_neutral.png"
image mara radiant = "character_sprites/mara_radiant.png"
image poludnicia = "character_sprites/poludnicia_neutral.png"
image poludnicia radiant = "character_sprites/poludnicia_radiant.png"
image kikimora = "character_sprites/kikimora_neutral.png"
image kikimora radiant = "character_sprites/kikimora_radiant.png"
image lisovyk = "character_sprites/lisovyk_neutral_flipped.png"
image lisovyk radiant:
    "character_sprites/lisovyk_neutral_flipped.png"
    xzoom(-1) #this will flip it horizontally

image rusalka = "character_sprites/rusalka_neutral.png"
image rusalka radiant = "character_sprites/rusalka_radiant.png"
image alkonost = "character_sprites/alkonost_neutral.png"

# Define the dim overlay image
image dim_overlay = Solid((0, 0, 0, 128))  # A simple semi-transparent black overlay

# darkness bar variables
default show_countdown = False       # Bar starts hidden
default darkness_value = 0.0         # Should go from 0 to 100
default darkness_increase_rate = 10  # Amount by which darkness bar increases on failure or time taken

#bar drawing function
label update_countdown(new_value):
    while darkness_value < new_value:
        $ darkness_value += 1
        $ renpy.pause(0.01)
        $ renpy.redraw(None, 0)
    if darkness_value >= 100:
        jump game_over_darkness
    return

# bar functions to show, hide and update
define show_progress_bar = lambda: (renpy.show_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', True))
# Usage: $ show_progress_bar() - Shows the bar on the side of the screen (and it stays there until hidden or scene is changed)
define hide_progress_bar = lambda: (renpy.hide_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', False))
# Usage: $ hide_progress_bar() - Hides the bar on the side of the screen 
define update_darkness = lambda new_value: renpy.call("update_countdown", new_value)            
# Usage: $ update_darkness(15) - Sets the darkness value to 15 and plays a short animation if it is more than before
# Usage: $ update_darkness(darkness_value + darkness_increase_rate) - Increases darkness value by a set amount and plays a short animation
# It also checks whether darkness is at 100 or more and goes to the game over screen if so
define increase_darkness = lambda: renpy.call("update_countdown", darkness_value + darkness_increase_rate)
# Usage: $ increase_darkness() does the same as the second usage of update_darkness above but without needing parameters


init python:
    import random
    def play_random_thump():
        # List of sound effects
        sfx_list = [t1, t2, t3, t4, t5, t6]
        
        # Select a random sound effect
        selected_sfx = random.choice(sfx_list)
        
        # Play the selected sound effect
        renpy.sound.play(selected_sfx)

init python:
    # Define a new position that shifts characters a bit to the left from the far right edge
    rightly = Position(xalign=0.85)  
    renpy.music.register_channel("ambience", "music", True)

# Гра починається тут.
label start:
    

    # show berehynia at center with move 

    # rightly instead of right, because the progress bar is at the right edge
    # show mara at rightly with dissolve  

    # $ show_progress_bar()
    # hide berehynia with dissolve

    play music bgm loop
    play ambience ambience_cry loop volume 0.25

    scene marabg

    b "Віла, люба"
    b "Будь ласка, прокинься" 
    b "Прокинься!"

    #show rusalka radiant at left
    #show lisovyk radiant at right

    show vila at left with dissolve

    b "Знайомий голос..."
    b "Але так холодно... так важко відкрити очі"
    b "Хочу спати далі, так буде легше, так буде менш болісно"

    b "Віла, люба, я знаю тебе. Я знаю, що ти можеш побороти цю темряву."
    b "Ти маєш велику силу!"
    b "Я допоможу тобі згадати."
    b "Тільки не здавайся, люба, не здавайся!"

    menu:
        "Прокинутися":
            v "Так. Я мушу боротися. За себе та за своїх друзів. Боротися проти темряви. Я знаю, що зможу."
            
            b "Чудово, я знала, що ти зробиш правильний вибір!"
            show berehynia at right with dissolve
            b "Віло, я - Берегиня, твій дух-охоронець. Моя задача обороняти тебе та інших, кого спіткала ця темрява."
            
            
            jump villa_remember
            
        "Спати далі":
            v "Спати. Я хочу спати. Залиш мене, голос."
            b "Ох..."
            b "Спи поки, люба, але я мушу спробувати знову."
            b "До зустрічі."
            
            #jump start
            return

label villa_remember: 

    в "Берегиня..."
    в "Берегиня, так, так, я памятаю. Мені здається, що я чула це ім'я раніше."
    v "Чому я тут? Що це за місце?"
    b "Це місце - темний вимір, царство втрачених спогадів і забутих надій. Ти та багато інших були тут ув'язнені, ваші спогади забрані."
    
    v "Мої спогади... Я відчуваю себе такою загубленою. Як мені вибратися звідси?"
    b "Не втрачай надію, Віло. Твоя магія, магія твоїх крил, може розсіяти цю темряву. Але тобі потрібно знайти інших і допомогти їм, адже їхня магія зробить тебе сильнішою."

    в "Я хочу допомогти іншим як ти допомогла мені!"
    v "Але з чого почати? Як мені їх знайти?"

    б "Мій час майже вийшов, люба. Моя сила дозволяє мені з тобою спілкуватися на великих відстанях, навіть дістатися тебе тут, у потойбіччі, але це потребує багато енергії тому, нажаль, мені інколи потрібно буде тебе залишити."

    б "Знайди мою сестру, Мару. Вона тобі допоможе. "
    б "(Шепотом)напевно~"
    б "Вона завжди була трохи... непередбачувана"

    в "Чекай, Берегиня, не йди..."
    б "Будь обережна, Віло. Не загуби себе в темряві..."
    б "Я повернусь як тільки зможу, люба."
    
    hide berehynia with dissolve

    в "Берегиня! Ти мене чуєш? Як я знайду твою сестру?"
    в "Берегиня?"
    $ increase_darkness()
    $ play_random_thump()

    show dim_overlay with dissolve
    # hide vila at left with dissolve
    pause 0.1
    hide dim_overlay with dissolve

    #jump dim_screen
    в "Що тільки що трапилось? На секунду мені здалося ніби темрява знову поглинула мене."
    в "Ох, де ж мені її шукати?"

    

    
label meet_mara: 

    show mara at right with dissolve  
    
    м "Ха ха ха."
    м "Заблукала в потойбіччі, Віла?"
    
    в "Мара?"
    м "Не мааєш цигарки часом? "
    м "Ха ха ха. Жартую. Жартую "
    
    в "Eee..Мара, твоя сестра поручила мені тебе знайти. Вона сказала,що ти можеш мені допомогти. Допомогти врятувати інших від темряви та повернутися додому."
    
    м "Бережка, ха? "
    м "Ех, вона любить обіцянки давати "
    м "Чому б я тобі допомогала, Віла, я люблю темряву. Темрява - це мій дім. "
    
    "Берегиня шепче Вілі: Щось не так, їй тут не місце, вона ховається від чогось. Або від когось..."
    "Хм..."
    в "Якщо це твій дім, Маро, тоді чому ти тут?"
    в "Я знаю, що богиня темряви зазвичай не ховається бо-зна-де в потойбіччі..."
    в "Можливо ти і не страждаєш від темряви, але тобі теж потрібна допомога."

    м "Ха! Страждаю від темряви? Дівчинко, я і є темрява."
    в " Так, але... "
    
    menu:
        "Благати Мару":
            
            в "Будь ласка? "
            м " Ха-ха-ха "
            jump mara_joins
            
        "Цигарки!":
            в "Я обіцяю, що достану тобі цигарки за першої можливості!"
            м "Ха ха ха, Віла, ти мені подобаєшся."
            м "В тебе є почуття гумору."
            
            jump mara_joins
            
        "Блефувати.":
            v "Добре, я і без тебе справлюся."
            м "Гей, гей, чекай, Віла"
            м " Ох, яка ти серйозна, нагадуєш мені мою сестру"

            jump mara_joins
    

label mara_joins: 

    м "Добре, добре. Мені тут все одно зараз робити нема чого."
    м "Так і бути, Віла, я піду з тобою. "
    м "Але передай моїй сестрі, що вона у мене в боргу (знову.)"
    м "Ех, бачу, що твої крила зовсім позбулися магічного сяєва... "
    в "О, ні... Час в потойбіччі погасив їх магію, як же мені тоді повернутися додому з цього підземелля?"
    м "Хех, я тобі покажу"

    show mara radiant at right with dissolve:
        xzoom 0.5
        yzoom 0.5
    #hide mara radiant at right with dissolve 
    # Mara is turning into magic and joins ! 
    
    $ wing_strength += 1
    play sound tone
    
    в "Мої крила!  Я знову відчуваю магію. "
    
    м "Так, так ... "
    м "Слухай, можливо ти маєш рацію, а можливо моя сестра тебе нагодувала пустими обіцянками, час покаже." 
    m "Але якщо ти хочеш  вибратися звідси, тобі знадобиться допомога, і моєї допомоги недостатьно. -незважаючи на те, що я всемогутня і неймовірна Мара, до речі набагато могутніша від Бережки, щоб ти знала-"
    в "Еее, Мара? "
    м "Кхм кхм, так що я хотіла сказати.. А!"
    м "Це мій дім, тому я можу тобі допомогти орієнтуватися тут"
    # show map image 
    
    м " Якщо хочеш вернутися додому, тобі потрібно якось дістатися верхівки підземелля, а щоб дістатися верхівки, магія твоїх крил повинна бути відновлена "
    м "Моя магія дозволить тобі піднятися на наступний рівень, але для того щоб піднятися вище тобі буде потрібно більше магії"
    м "Але знай, чим довше ти залишаєшся, тим більша вирогідність повернення темряви і тих хто під ЇЇ впливом буде не так просто залучити як мене, Віла."
    # м "Чим більше спроб ти робиш, тим більше це на тобі сказується "
    м "До речі ! Час рушати, красуня!  "
    м "Ви вілли, начебто соціальні метелики, так?"
    м "То йди вже чаруй та вербуй інших, чи що ви там вілли робите. Час мені повернути моє потойбіччя, деякі створіння тут OVERSTAYED THEIR WELCOME. Враховуючи тебе, Віла"
    
    в "Е, вау, дуже мотивує, Мара... Дякую. "
    б "Ха-ха я бачу ви подружилися. Хай щастить, люба. Я завжди поруч."



    jump map


label game_over_darkness:
    scene black
    hide all
    
    $ play_random_thump()
    "The darkness has consumed you. You must start over."
    # Reset variables or provide options to restart the game
    $ wing_strength = 0
    $ darkness_value = 0

    #$ poludnicia_joined = False 
    #$ poludnicia_visited = False 

    #$ kiki_joined = False 
    #$ kiki_visited = False 

    #$ lisovyk_joined = False 
    #$ lisovyk_visited = False 

    #$ rusalka_joined = False 
    #$ rusalka_visited = False 


    jump start

label game_over_light: 
    scene happy_ending
    "Congrats! You win!"
    # На цьому гра закінчується.
    return

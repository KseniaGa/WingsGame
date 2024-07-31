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
    jump lisovyk_guess

label lisovyk_intro:
    show lisovyk at center with dissolve
    show vila at left with dissolve
    pause 0.1
    show berehynia at rightly with dissolve

    b "Lisovyk is a fighter at heart. Till the very end was he defending the nature and all that lives in the shadows of the woods."
    b "Now he himself is in the deep shadows where no sun ray reaches. However, I am sure you can help him too, Vila.."
    b "And yes, beware of something... "
    b "Sometimes his memory fails due to his age, but he does not like when people remind him that!"

    # flashback scene about Lisovyk?

    hide berehynia at rightly with dissolve

    $ show_progress_bar()

    l "This is not looking good, not looking good, I'm telling ya."

    show lisovyk at rightly with move 

    v "Lisovyk? Lisovyk, I am Vila."


label lisovyk_guess:
    v "Lisovyk..?"
    # l "Liso-what? Speak louder, child. The voices of leaves keep whispering into my ears, I forget myself."
    l "Lyso-what? Speak louder, child. The voices around keep whispering into my ears, I forget myself."
    
    menu:
        "Comment on his hearing":
            v "Do you have bananas in your ears?"
            "Presence of Lisovyk makes Vila feel like an actual child, even though she is hundreds years old, maybe older than him!"
            l "Excuse me?"
            l "Bananas?"
            l "Bananas don't grow where I come from. The father of jungles takes care of them. "
            l "Hmm. I haven't spoken to him in ages..."

        "Remind who he is":
            jump lisovyk_remind_who_he_is

        "Ask about your friends":
            pass

        "Ask how old he is"


    call screen backButton


label lisovyk_remind_who_he_is:
    menu:
        "Lee-sooh-vyyyk, you are the father of the foxes. ": #Cause 'FOX' is LYS
            l "Foxes sure.. But not only. I like all the animals."
            $ increase_darkness() #make it harder by punishing wrong answers right away?
            jump lisovyk_guess

        "Lee-sooh-vyyyk, you are the master of the forests.":
            l "Forests have trees. Trees have leaves. Leaves rustle..."
            l "Those are not voices, but the leaves."
            pause 1.0
            "Lisovyk turns his head left and right, a sound of sqeeky wood follows..."
            jump lisovyk_remind_who_he_is

        "Lee-sooh-vyyyk, you are the patron of the bolds.": #Cause BOLD is LYSYY
            l "Khe-khe. My dress might be getting drier every season, yes..." 
            l "...but this is nothing but a natural process."
            $ increase_darkness()
            jump lisovyk_remind_who_he_is

        "Lee-sooh-vyyyk, you are the friend of the frogs. ": # Cause he sits like a frog, and there's a small frog 
            l "Frogs sure.. But not only. I like all the animals."
            $ increase_darkness() #make it harder by punishing wrong answers right away?
            l "I do sit like a frog on Wednesdays occasionally, spent a lot of time with 'em. "
            jump lisovyk_remind_who_he_is
    
label lisovuk_remember:
    l "What are the leaves whispering about, Vila?"

    v "TODO"

    
    
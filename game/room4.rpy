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


label room4:
    scene room hell bg
    
    show vila at left with dissolve
    pause 0.1
    show lisovyk at rightly with dissolve

    l "This is not looking good, not looking good, I'm telling ya."

    # flashback scene about Lisovyk?

    $ show_progress_bar()

    v "Lisovyk? Lisovyk, I am Vila."

    jump lisovyk_remember


label lisovyk_guess:
    # l "Liso-what? Speak louder, child. The voices of leaves keep whispering into my ears, I forget myself."
    l "Lyso-what? Speak louder, child. The voices around keep whispering into my ears, I forget myself."

    menu:

        "Lee-sooh-vyyyk, you are the father of the foxes. ": #Cause 'FOX' is LYS
            l "Foxes sure.. But not only. I like all the animals."
            $ increase_darkness() #make it harder by punishing wrong answers right away?
            jump lisovyk_guess

        "Lee-sooh-vyyyk, you are the master of the forests.":
            l "Forests have trees. Trees have leaves. Leaves rustle..."
            l "Those are not voices, but the leaves."
            pause 1.0
            l "Hmmkhhmmm. Lisovyk turns his head left and right, a sound of sqeeky wood follows..."
            jump lisovyk_remember

        "Lee-sooh-vyyyk, you are the patron of the bolds.": #Cause BOLD is LYSYY
            l "Khe-khe. My dress might be getting drier every season, yes..." 
            l "...but this is nothing but a natural process."
            $ increase_darkness()
            jump lisovyk_guess

        "Lee-sooh-vyyyk, you are the friend of the frogs. ": # Cause he sits like a frog, and there's a small frog 
            l "Frogs sure.. But not only. I like all the animals."
            $ increase_darkness() #make it harder by punishing wrong answers right away?
            l "I do sit like a frog on Wednesdays, spent a lot of time with 'em. "
            jump lisovyk_guess

    call screen backButton
    

label lisovyk_remember:
    
    l "What are the leaves whispering about, Vila?"

    v "TODO"

    
    
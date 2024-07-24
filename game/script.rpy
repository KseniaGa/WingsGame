# Define characters
define v = Character("Vila", color="#7ec8e3")       # Player Character
define b = Character("Berehynia", color="#ffcc00")  # Benevolent Guide
define m = Character("Mara", color="#9932CC")       # Tutorial Boss
define p = Character("Poludnicia")                    # Level 2
define k = Character("Kikimora")                      # Level 2
define l = Character("Lisovyk")                       # Level 3
define r = Character("Rusalka")                       # Level 3
define a = Character("Alkonost")                      # Final Boss

# Define character images
image vila = "character_sprites/vila_neutral.png"
image berehynia = "character_sprites/berehynia_neutral.png"
image mara = "character_sprites/mara_neutral.png"
image mara radiant = "character_sprites/mara_radiant.png"
image poludnicia = "character_sprites/poludnicia_neutral.png"
image kikimora = "character_sprites/kikimora_neutral.png"
image lisovyk = "character_sprites/lisovyk_neutral.png"
image rusalka = "character_sprites/rusalka_neutral.png"
image alkonost = "character_sprites/alkonost_neutral.png"

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

# wings variables
default wing_strength = 0
default wing_strength_threshold = 3

init python:
    # Define a new position that shifts characters a bit to the left from the far right edge
    rightly = Position(xalign=0.85)  


# Гра починається тут.
label start:

    "Посеред темряви прокидається свідомість."
    show vila at left with dissolve
    v "Where am I? It's is so dark..."

    show berehynia at right with dissolve
    b "Do not be afraid, dear Vila. I am Berehynia, your guide and protector."
    b "I will help you down here."

    show berehynia at center with move 

    # rightly instead of right, because the progress bar is at the right edge
    show mara at rightly with dissolve  
    m "Hallowm..."
    $ show_progress_bar()
    m "Who are you? Why have you come?"
    hide berehynia with dissolve
    
    menu:
        "I am here to help you remember who you are.":
            jump mara_remember
        "I am lost and need your guidance.":
            m "I cannot help you if you do not remember who I am. Try to focus on my essence."
            $ increase_darkness()
            jump mara_remember

label mara_remember:
    m "Remember... I used to guide souls and bring peace to the restless."
    
    menu:
        "Yes, you ensured peace in the transition.":
            $ wing_strength += 1
            m "Thank you for reminding me. I can feel my strength returning."
            show mara radiant at rightly with dissolve
            "Mara transforms into a radiant form, and a part of her essence is absorbed into Vila's wings."
            hide mara with dissolve
            show berehynia at rightly with dissolve
            b "Well done. Your wings have grown stronger."
            b "Now you need to rescue more of us, so we can all escape together."
            jump map
        
        "You protected the souls from harm.":
            m "No, that is not quite right. I brought peace, not protection from harm."
            $ increase_darkness()
            jump mara_remember
        
        "You brought fear to the living.":
            m "No, that is not who I am. Try to remember more clearly."
            $ increase_darkness()
            jump mara_remember

label game_over_darkness:
    scene black
    hide all
    $ hide_progress_bar()
    "The darkness has consumed you. You must start over."
    # Reset variables or provide options to restart the game
    $ wing_strength = 0
    $ darkness_value = 0
    jump start

label game_over_light: 
    scene happy_ending
    "Congrats! You win!"
    # На цьому гра закінчується.
    return

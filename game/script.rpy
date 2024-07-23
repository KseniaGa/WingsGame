# Define characters
define v = Character("Vila", color="#7ec8e3")
define b = Character("Berehynia", color="#ffcc00")
define m = Character("Mara", color="#9932CC")
define d = Character("Domovyk")
define p = Character("Poludnicia")

# bar variables
default show_countdown = False
default countdown_value = 0.0

default darkness_value = countdown_value

default darkness_increase_rate = 10  # Amount by which darkness bar increases on failure or time taken
default darkness_decrease_rate = 20  # Amount by which darkness bar decreases on success

#bar drawing function
label update_countdown(new_value):
    while countdown_value < new_value:
        $ countdown_value += 1
        $ renpy.pause(0.01)
        $ renpy.redraw(None, 0)
    return

# bar functions to show, hide and update
define show_progress_bar = lambda: (renpy.show_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', True))
define hide_progress_bar = lambda: (renpy.hide_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', False))
define update_progress_bar = lambda new_value: renpy.call("update_countdown", new_value)



# wings variables
default wing_strength = 0
default wing_strength_threshold = 3

# Гра починається тут.
label start:

    v "Where am I? It's is so dark..."
    b "Do not be afraid, dear Vila. I am Berehynia, your guide and protector."

    m "Hallowm I am Mara"

    m "Who are you? Why have you come?"
    
    menu:
        "I am here to help you remember who you are.":
            jump mara_remember
        "I am lost and need your guidance.":
            m "I cannot help you if you do not remember who I am. Try to focus on my essence."
            $ darkness_value += darkness_increase_rate
            if darkness_value >= 100:
                jump game_over_darkness
            jump mara_remember

label mara_remember:
    m "Remember... I used to guide souls and bring peace to the restless."
    
    menu:
        "Yes, you ensured peace in the transition.":
            $ wing_strength += 1
            $ darkness_value -= darkness_decrease_rate

            show mara_radiant at center with dissolve
            m "Thank you for reminding me. I can feel my strength returning."
            "Mara transforms into a radiant form, and a part of her essence is absorbed into Vila’s wings."
            b "Well done. Your wings have grown stronger."
            jump map
        
        "You protected the souls from harm.":
            m "No, that is not quite right. I brought peace, not protection from harm."
            $ darkness_value += darkness_increase_rate
            if darkness_value >= 100:
                jump game_over_darkness
            jump mara_remember
        
        "You brought fear to the living.":
            m "No, that is not who I am. Try to remember more clearly."
            $ darkness_value += darkness_increase_rate
            if darkness_value >= 100:
                jump game_over_darkness
            jump mara_remember



    call screen mapScreen

label game_over_darkness:
    scene bg_dark_dimension
    "The darkness has consumed you. You must start over."
    # Reset variables or provide options to restart the game
    $ wing_strength = 0
    $ darkness_value = 100

    jump start

label game_over_light: 
    scene happy_ending
    "Congrats! You win!"


    # На цьому гра закінчується.
    return

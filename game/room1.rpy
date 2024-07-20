label room1:
    scene room hell bg
    
    "gonna show bar"

    $ countdown_value = 0  # Initial value
    $ show_progress_bar()
    $ update_progress_bar(5)

    
    "Hello this is room 1"
    $ update_progress_bar(60)

    "increased bar"

    $ hide_progress_bar()

    "hid bar again"

    call screen backButton
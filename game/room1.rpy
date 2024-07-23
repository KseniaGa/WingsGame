label room1:
    scene room hell bg

    d "Hallowm I am Domovyk"
    
    "gonna show bar"

    $ darkness_value = 0  # Initial value
    $ show_progress_bar()
    $ update_darkness(5)

    "Hello this is room 1"
    $ update_darkness(60)

    "increased bar"

    $ update_darkness(darkness_value + 20)

    "increased bar again"

    $ hide_progress_bar()

    "hid bar again"

    call screen backButton
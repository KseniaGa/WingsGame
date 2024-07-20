# У цьому файлі міститься скрипт гри.

# Оголошення персонажів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім’я персонажа.

define e = Character("Ейлін")

default show_countdown = False
default countdown_value = 0.0

label update_countdown(new_value):
    while countdown_value < new_value:
        $ countdown_value += 1
        $ renpy.pause(0.01)
        $ renpy.redraw(None, 0)
    return

define show_progress_bar = lambda: (renpy.show_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', True))
define hide_progress_bar = lambda: (renpy.hide_screen("countdown_bar"), setattr(renpy.store, 'show_countdown', False))
define update_progress_bar = lambda new_value: renpy.call("update_countdown", new_value)

# Гра починається тут.

label start:

    # Це показує тло. За стандратом використовується заповнювач, але ви можете
    # додати файл (з назвою «bg room.png» або «bg room.jpg») до
    # теки images, щоб показати його.

    call screen mapScreen

    scene bg room

    # Це показує спрайт персонажа. Використовується заповнювач, але ви можете
    # замінити його, додавши до зображень файл із назвою «eileen happy.png».
    # до теки.

    show eileen happy

    # Це репліки діалогу.

    e "Ви створили нову гру Ren'Py."

    e "Додавши історію, зображення та музику, ви можете оприлюднити це світові!"

    # На цьому гра закінчується.

    return

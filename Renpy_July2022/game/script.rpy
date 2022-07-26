﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg void

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "In a City Square"

    "A body hangs on the spire."

    "Jihad is a gay person. Lol."

    menu:

        "Choose scene"

        "Scene 1":
            call scene_1
        
        "Scene 2":
            call scene_2

    "Thank you for playing"

    # This ends the game.

    return

define b = Character("Boss")
define k = Character("Keiran")
define p = Character("Parker")

label scene_2:

    scene street overpass
    with fade

    show Boss smirk
    
    b "Took you long enough."
    k "Sorry it was just so early!"
    k "So.. you said it was urgent?"
    b "Just come with me."

    scene overpass murder as om
    with fade 

    k "Wh..."
    k "Wh..."
    k "What the hell??!!"

    scene overpass murder close-up
    with fade

    pause 3.0

    scene om
    with fade

    show Boss neutral

    k "That's horrible... Who would do something like this?"
    b "That's why we are here, son."
    b "You're an investigator for god's sake."
    k "..."

    pause 1.0

    b "In any case, we got a call from an early bird. She heard a loud bang and saw sombebody putting up the body, but couldn't make out any details."
    b "You should talk to her later."
    k "Right."
    b "You there, give us a report."

    show Parker neutral

    p @ neutral """
    Yes sir!

    The time of death is approximately somewhere between 6 PM and 11 PM yesterday.

    Also, the rope was not simply tied to his hands. It went {i}through{/i} the hands and wrist.
    He was still alive when the holes were made.
    """

    b @ thought "..."

    "Kieran?"

    k "!"

    "Kieran, can you hear me?"

    k "Ah! Yes..."
    k "Sorry Lizzie, still not used to this"

    l "It's okay. It's your first time"

    return
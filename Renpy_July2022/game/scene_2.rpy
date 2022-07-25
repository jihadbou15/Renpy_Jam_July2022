define b = Character("Boss")
define k = Character("Kieran")
define p = Character("Parker")
define l = Character("Lizzy")
define w = Character("Older Lady")

label scene_2:

    scene street overpass
    with fade

    show Boss neutral
    
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
    k "Sorry Lizzy, still not used to this"

    l happy "It's okay. It's your first time in the HCS after all."
    l "Anyways, Boss already knows this but the victim is Gant Baddoer."

    k "Wait I know that name."
    l "That's because he was an old investigator at the precinct"
    l "Interestingly, he did not exactly have a smooth career..."
    k "What do you mean by that?"
    l """
    Rumors are, he would sometimes plant evidence.
    
    They were simply rumors of course. He aways denied them.

    Unfortunately for him, one of his victims's relatives was well known and lodged a complaint with the precinct.

    That made the newspapers. And while it didn't stick, the bad press that generated was enough to keep him off the HCS.
    """

    k "I see..."
    b "Kieran, as much as I love watching you have a conversation that has nothing to do with this case, we have more pressing matters to attend to. "
    b "Like interviewing the witness. It's just a suggestion of course"
    k "Right, sorry"
    l "Yeah Keiran, chop chop!"
    k "Shut up!"
    menu:
        "What should we do"

        "Interview the witness":
            call scene_2_1

    return

label scene_2_1:
    scene street overpass
    with fade

    k "Excuse me, I am with the HCS. I have a few questions."

    show older lady smiling
    with dissolve

    w "Oh hello there young man, I'm sorry, but I already told the officers everything I know!"
    k "I understand, but I would like to confirm everything for myself."
    k "Please."
    w "You seem like a nice young man, so I will tell you."
    k "Thank you very much madam."

    show blurry pickup truck
    with fade

    hide older lady

    w """
    It was around 5 AM, I couldn't really sleep.

    Suddenly, I heard a loud bang outside!

    I was curious so I looked out my windoow to see what was going on.
    
    There I saw it...

    A tall woman, hangning the body from the overpass!

    I called the police but she already drove off before they could arrive
    """
    k "Did you see what the woman looked like?"
    w "She was wearing a long black trench coat and a hat. That was all I could make out from my window."
    k "Then how did you know it was a woman?"
    w "Young man, I shouldn't have to explain secondary sexual characteristics to a 23 year old."
    l "Kieran Kieran, i expect more from you."
    k "ALRIGHT SO SHE HAD MASSIVE TITS."
    w "Young man, language. Please."
    
    show blurry pickup truck 
    with vpunch

    k "..."
    k "You said you saw a pickup truck?"
    w "Yes, it was dark gray. That was all I could see"
    k "//This is probably all the information i will be able to get from her."
    k "Thank you for your time."
    w "You're welcome."


    l "Keiran, I checked the cameras of the sorrounding area."
    k "?"
    l "Unfortunately, there are no cameras observing this particular overpass so I can't exactly confirm her story."
    k "What about the pick-up?"
    l "I found camera footage of a dark gray WolkVagen pick-up going to and away from the overpass."
    l "Judging from the footage, it went to an abandoned parking lot nearby."
    k "And the perp?"
    l "They somehow managed to avoid camera detection after leaving the pick-up truck there."
    l "Like she knew where they were..."
    k "What about the owner of the pick-up?"
    l "The license plate is registered to a Mr. Terry Pidus. He is a mechanic."
    k "We should visit him later..."

    return
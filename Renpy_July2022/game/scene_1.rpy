define c = Character("Crystal")
define p = Character("Parker")

label scene_1:

    $ crystal_y = 0.22

    scene bg city square
    with fade

    show crystal shocked at left:
        yalign crystal_y

    c "I came as fast as i could, Is it true? Is he really…?"

    show Parker disturbed at right

    p "See for yourself."

    scene first body
    with fade

    pause 2.0

    scene bg city square
    show crystal distressed at left:
        yalign crystal_y
    with fade

    c "{cps=*.1}Boss…. Why….What happened?{/cps}"

    show Parker distressed at right

    p "We have already called Kieran to the scene"

    show crystal angry at left:
        yalign crystal_y

    c "Why??"

    show Parker explaining at right

    p "This is being treated as part of the Coded Killings"
    p "Whether we like it or not, Kieran has the most experience with it."
    p "He should have a better view on it than us."

    show crystal annoyed at left:
        yalign crystal_y

    c "Fiiiine, just give me a rundown of the evidence you already got."
    p "Sure thing."

    show crystal thinking at left:
        yalign crystal_y

    p "Preliminary autopsy puts the time of death between 6 PM yesterday and 12 AM today."
    p "Cause of death is currently unknown, but we have ruled out the hook."
    p "Based on the lack of blood near the body, it seems that the hook was attached post mortem, some time after the murder."
    p "The blood here is not blood. It is actually just red paint."
    p "The murderer painted it with a wide brush that we found in a trash can nearby. Of course, no fingerprints were found on the brush nor the hook."
    p "The murderer seems to have been wearing gloves during the entire setup."
    c "No sign of a murder weapon?"
    p "Not that we could find, no. We don't even know what we are looking for to be honest with you."
    p "We did notice that there were no signs of a struggle, which seems to point to the possibility that he was unconscious as he was murdered."
    p "We do not know how yet, but a definitive autopsy should clear that up."

    show crystal confused at left:
        yalign crystal_y

    c "Thanks... What's your name again?"

    show Parker angry at right

    p "It's Parker!"
    c "Riiight, I'll have a look around."

    show Parker explaining at right

    p "Please don't disturb the scene. Kieran will eat my heart otherwise."

    # c "Yeah, yeah. We both know Kieran is a big baby."

    return



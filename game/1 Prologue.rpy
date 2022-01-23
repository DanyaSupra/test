label start:
    if persistent.trueendstage2 == True:
        jump tenew
    label prologue2:
        pass
    scene bg college with d
    play music intro fadein 3.0
    call clothesformal from _call_clothesformal_27
    show mce happy2
    with d
    "Hello!"
    "I'm an eighteen year old girl!"
    "You can call me..."
    python:
        mc = renpy.input("Name your character.")
        mc = mc.strip()
        if not mc:
            mc = "Taco"
    show mce happy
    with d
    "That's right, my name is [mc]!"
    "If I were to describe myself as honestly as possible..."
    menu personalitymenu:
        "(Select your personality type. Select the option for more information.)"
        "An Innocent Girl" if True:
            "+1 Crush Affection. -20%% Sexual Desire and Shame, but +20%% Money, Followers and Smarts from all sources."
            "It's possible to transform this personality later on into something special."
            menu:
                "That's me!" if True:
                    $ ca += 1
                    $ sdmult = 0.8
                    $ shamemult = 0.8
                    $ smartsmult = 1.2
                    $ folmult = 1.2
                    $ moneymult = 1.2
                    $ personality = 1
                    $ personalityname = "An Innocent Girl"
                "Let me think again..." if True:
                    jump personalitymenu
        "Always Horny" if True:
            "+10 Sexual Desire. +20%% Sexual Desire from all sources."
            "Due to an overwhelming libido, it will be impossible to say no to a sexual encounter you can do."
            menu:
                "That's me!" if True:
                    $ sd += 10
                    $ sdmult = 1.2
                    $ personality = 2
                    $ personalityname = "Always Horny"
                "Let me think again..." if True:
                    jump personalitymenu
        "A Smooth Operator" if True:
            "+$50, -5 Shame. +20%% Money from all sources"
            "Gives you the ability to steal in certain situations."
            menu:
                "That's me!" if True:
                    $ money += 50
                    $ shame -= 5
                    $ shamemult = 1.1
                    $ moneymult = 1.2
                    $ personality = 3
                    $ personalityname = "A Smooth Operator"
                "Let me think again..." if True:
                    jump personalitymenu
        "Overly Confident" if True:
            "-10 Shame. +20%% Shame Loss from all sources."
            "Gains +20%% Sexual Desire once you reach 0 Shame."
            menu:
                "That's me!" if True:
                    $ shame -= 10
                    $ shamemult = 1.2
                    $ personality = 4
                    $ personalityname = "Overly Confident"
                "Let me think again..." if True:
                    jump personalitymenu
        "Thrill Junkie" if True:
            "+5 Sexual Desire, -5 Shame. +10%% Sexual Desire and Shame, but -10%% Smarts from all sources."
            "Doing something for the first time gives twice the stats and a small stat boost for 24 hours."
            menu:
                "That's me!" if True:
                    $ sd += 5
                    $ shame -= 5
                    $ sdmult = 1.10
                    $ shamemult = 1.10
                    $ smartsmult = 0.9
                    $ personality = 5
                    $ personalityname = "Thrill Junkie"
                "Let me think again..." if True:
                    jump personalitymenu
    play sound success
    "Yep! I'm [personalityname]!"
    "But that's not all, I have a few quirks that make me special too!"
    label quirkmenu:
        if quirks == 2:
            jump postquirkmenu
    menu:
        "(Select at least one quirk, or a maximum of two. Select the option for more information.)"
        "Selfie Star" if qselfiestar == 0:
            "You already have quite the online presence. Start with 100 followers, and gain them 10%% faster!"
            menu:
                "That's me!" if True:
                    $ qselfiestar = 1
                    $ quirks += 1
                    $ fol += 100
                    $ folmult = 1.10
                    play sound success
                    "Yup! My pics get tons of likes, and I have a ton of friends. I don't even know them all, hehe."
                    jump quirkmenu
                "Let me think again..." if True:
                    jump quirkmenu
        "Rich Parents" if qrichkid == 0:
            "Your parents send you $30 a week, and you start with +$30 extra. Not bad! Unfortunately, your parents aren't so rich that they can pay for your tuition."
            menu:
                "That's me!" if True:
                    $ qrichkid = 1
                    $ quirks += 1
                    $ money += 30
                    play sound success
                    "Yup! You could say I'm fairly well off! It could always be better, though..."
                    jump quirkmenu
                "Let me think again..." if True:
                    jump quirkmenu
        "Sexually Experienced" if qsexuallyexperienced == 0:
            "You've already been round the block. +5 Sexual Desire, and you start as a sexual novice."
            menu:
                "That's me!" if True:
                    $ qsexuallyexperienced = 1
                    $ quirks += 1
                    $ sd += 5
                    $ status += 6
                    $ virgin = 1
                    play sound success
                    "I have a bit of experience! But it doesn't mean much."
                "Let me think again..." if True:
                    jump quirkmenu
        "Anal Queen" if qanalqueen == 0:
            "All anal options have their requirements dropped to that of vaginal sex. +5 Sexual Desire."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qanalqueen = 1
                    $ sd += 5
                    play sound success
                    "It just feels good, alright?"
                "Let me think again..." if True:
                    jump quirkmenu
        "Woops! Already pregnant!" if qpregnant == 0:
            "Yikes! You don't start a virgin, and you start with your pregnancy showing."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qpregnant = 1
                    $ pregnant = 1
                    $ pregnancyshowing = 1
                    $ pregnancyterm = 11
                    $ pregnancies += 1
                    $ vaginalsexes += 1
                    $ virgin = 1
                    $ status += 1
                    play sound success
                    call clothesformal from _call_clothesformal_28
                    show mce neutral
                    with d
                    "Ahh, woops! It was only one time, I swear!"
                    show mce happy with d
                "Let me think again..." if True:
                    jump quirkmenu
        "Heavy Sleeper" if qheavysleeper == 0:
            "You gain x2 stats when dreaming."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qheavysleeper = 1
                    play sound success
                    "It'd take a hurricane to wake me up!"
                "Let me think again..." if True:
                    jump quirkmenu
        "Lightweight" if qlightweight == 0:
            "All effects of alcohol and drugs are doubled. Including negative effects."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qlightweight = 1
                    play sound success
                    "Yeaaahh, I'm totally knocked out after only 2-3 drinks!"
                "Let me think again..." if True:
                    jump quirkmenu
        "Introvert" if qintrovert == 0:
            "You like things behind doors and alone more than with people. You gain +10%% to everything while alone."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qintrovert = 1
                    $ alonemult = 1.1
                    play sound success
                    "Things are just easier to deal with than people!"
                "Let me think again..." if True:
                    jump quirkmenu
        "Secretly Depraved" if qsecretlydepraved == 0:
            "You're actually into this shit! Double sexual desire gains from depraved actions. -2 Shame."
            menu:
                "That's me!" if True:
                    $ quirks += 1
                    $ qsecretlydepraved = 1
                    $ shame -= 2
                    play sound success
                    "Whaaat? Don't judge me!"
                "Let me think again..." if True:
                    jump quirkmenu
        "Done" if quirks == 1:
            "Are you sure you only want to select one quirk?"
            menu:
                "Yeah, I'll be fine" if True:
                    jump postquirkmenu
                "Wait, I can select two?" if True:
                    jump quirkmenu
    jump quirkmenu
    label postquirkmenu:
        pass
    "I'm quite the character, huh? Even so, I managed to get into my dream college! Hero Academy!"
    "Hero Academy is renowned for being the absolute best education for upcoming heroes in the country."
    "It was always the college of my dreams..."
    "Well, I don’t have to dream any longer! Because I’m right here!"
    show bg bedroomday
    show mce laughing
    with d
    "The accommodation is incredible, it’s like living in a luxury hotel suite!"
    "The facilities are breath-taking, everything you could possibly dream of!"
    "A free gym, pools, a sauna, bars, athletics tracks and so much more."
    "It’s all so overwhelming…"
    "I spent my entire first day meeting new people, and becoming familiar with the campus."
    stop music fadeout 3.0
    scene bg bedroomnight with dissolve
    "However, all was not as I had imagined…"
    "As the sun drowned, and darkness rose up to consume the land... I discovered I was in grave danger."
    "…"
    call clothespjs from _call_clothespjs_3
    show mce sad
    with d
    "$9000 a year for tuition. $9000 a year for rent."
    "$18,000 a year, for four years, that’s…"
    "$72,000?! And that’s not even including food, entertainment and important study materials."
    "This isn’t a dream, it’s an absolute nightmare!"
    "For many, this'll be their Hero Academia, but for me... It'll probably be my Tuition Academia... Time to make some money…"
    "But… how?"
    "I sit here in my ‘luxury suite’ of a room and contemplate my next step."
    "I can't just sit around and wait for money to come to me!"
    play sound equip
    call clothescasual from _call_clothescasual
    show mce angry
    with d
    "Getting dressed again, I sit down at my laptop and research quick ways to earn money..."
    mc "Modelling... Nude modelling? Escorting?! I... don't know about that..."
    play sound success
    $ sdgain = 2
    call sdgain from _call_sdgain_87
    "(+[fsd] Sexual Desire!)"
    "(Encountering lewd ongoings in the world can increase your receptivity to sex.)"
    show mce happy
    with d
    mc "There are lots of models online that sell photos of themselves..."
    mc "I don’t think I could ever show my nude body..."
    mc "But if I don't show my face, maybe I could pose in my underwear to earn some cash."
    play sound success
    $ shameloss = 1
    call shameloss from _call_shameloss_61
    "(-[fshame] Shame!)"
    "(Depraving yourself will lower your pride and can increase what you're willing to do for money.)"
    mc "Ohhh, and I remember the university had a bar, it said it was looking for a part-time worker."
    mc "It’s settled. Every evening I’m going to do something to earn money. No matter the cost."

    play music rest
    scene bg bedroomnight
    show blankbedroom
    show mc:
        xpos 850
    show mco:
        xpos 850
    call clothes from _call_clothes_111
    show mce happy:
        xpos 850
    with d
    "(From now on, I’ll have the ability to take two actions a day, with the ultimate goal of earning $72,000.)"
    "(Have a look around the bedroom now to explore your options.)"
    menu:
        "Do you want to take a sixty second tutorial for the bedroom menu?"
        "Yes" if True:
            pass
        "Skip" if True:
            jump prologueposttut
    show circle:
        xpos 0 ypos 350
    with d
    "(From the Computer, you can visit various websites, to study, upload content, or view content.)"
    show circle:
        linear 0.5 xpos 300 ypos 70
    "(Your Wardrobe will let you swap between many outfits, you already have a selection to choose from.)"
    show circle:
        linear 0.5 xpos 620 ypos 70
    "(Your Inventory will allow you to use consumable items you purchase from the shops.)"
    show circle:
        linear 0.5 xpos 1430 ypos 380
    "(Your Bed can let you skip half a day by sleeping, or masturbating.)"
    show circle:
        linear 0.5 xpos 475 ypos 475
    "(Clicking the 'Status' button, opens a record of your experiences.)"
    show circle:
        linear 0.5 xpos 750 ypos 680
    "(The Outside button will send you to the world map. There are a lot of places to visit and discover.)"
    show circle:
        linear 0.5 xpos 1425 ypos 50
    "(Finally, if you're ever unsure of what to do next, the tips button tells you what [mc] is thinking.)"
    show circle:
        linear 0.5 xpos 475 ypos 475
    "(Your stats will dictate what you’ll be willing to do, keep an eye on your pregnancy chance too.)"
    hide circle with d
    "(Your main stats are 'Sexual Desire' and 'Shame', these are the two main things that'll hold your character back from performing actions in the world.)"
    "(Minor stats include 'Followers', how many people watch and experience content you upload online, the more you have, the more money you'll get. 'Smarts' allows you to earn more money completing jobs, at a rate of 0.5%% per point, and it will allow you to pass college tests every Friday.)"
    label prologueposttut:
        pass
    "(What you decide to do next is up to you. Good luck!)"
    jump postbedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

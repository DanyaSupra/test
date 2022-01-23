
init:
    $ tsd = 0
label sdgain:
    $ tsd = sdgain * sdmult * alonemult * llthf
    python:
        fsd = round(tsd, 1)
        sd = round(sd, 1)
    $ sd += fsd
    $ dsd = int(sd)
    return

label shameloss:
    $ tshame = shameloss * shamemult * alonemult * unwavering * llthf
    python:
        fshame = round(tshame, 1)
        shame = round(shame, 1)
    $ shame -= fshame
    $ dshame = int(shame)+1
    return

label moneygain:
    if smarts > 200:
        $ tmoney = moneygain * moneymult * alonemult * seriouslyfocused * 2
    elif True:
        $ tmoney = moneygain * moneymult * alonemult * seriouslyfocused * (smarts/200 + 1)
    python:
        fmoney = round(tmoney, 2)
    $ money += fmoney
    return

label moneycalculate:
    if smarts > 200:
        $ tmoney = moneygain * moneymult * alonemult * seriouslyfocused * 2
    elif True:
        $ tmoney = moneygain * moneymult * alonemult * seriouslyfocused * (smarts/200 + 1)
    if smarts > 200:
        $ fmoney1 = money1 * moneymult * alonemult * seriouslyfocused * 2
    elif True:
        $ fmoney1 = money1 * moneymult * alonemult * seriouslyfocused * (smarts/200 + 1)
    if smarts > 200:
        $ fmoney2 = money2 * moneymult * alonemult * seriouslyfocused * 2
    elif True:
        $ fmoney2 = money2 * moneymult * alonemult * seriouslyfocused * (smarts/200 + 1)
    if smarts > 200:
        $ fmoney3 = money3 * moneymult * alonemult * seriouslyfocused * 2
    elif True:
        $ fmoney3 = money3 * moneymult * alonemult * seriouslyfocused * (smarts/200 + 1)
    python:
        fmoney = round(tmoney, 2)
        fmoney1 = round(fmoney1, 2)
        fmoney2 = round(fmoney2, 2)
        fmoney3 = round(fmoney3, 2)


    return

label folgain:
    $ ffol = folgain * folmult * alonemult * determination
    $ ffol = int(ffol)
    $ fol += int(ffol)
    return

label smartsgain:
    $ tsmarts = smartsgain * smartsmult * alonemult * stressfree
    python:
        fsmarts = round(tsmarts, 1)
    $ smarts += fsmarts
    $ dsmarts = int(smarts)
    return


label clothingedits:
    if tan == 0:
        show mc nude
        if pregnancyshowing == 1:
            show mc pregnant
    elif True:
        show mc tan
        if pregnancyshowing == 1:
            show mc tanpregnant
    if catearson == 1:
        show mccatears
    if piercingson == 1:
        show mcpiercings
    show mch
    if hair == 1:
        show mch black
    if hair == 2:
        show mch blonde
    if pinkhair == 1:
        show mch pink
    if slimebody == 1:
        show pinkbody
        if pregnancyshowing == 1:
            show pinkbody p
    if slimehair == 1:
        show pinkhair
    return

label currentoutfit:
    label clothes:
        call clothingedits from _call_clothingedits
        if clothes == 0:
            pass
        if clothes == 1:
            if pregnancyshowing == 1:
                show mco uniformp
            elif True:
                show mco uniform
        if clothes == 2:
            if pregnancyshowing == 1:
                show mco casualp
            elif True:
                show mco casual
        if clothes == 3:
            if pregnancyshowing == 1:
                show mco pjsp
            elif True:
                show mco pjs
        if clothes == 4:
            show mco catlingerie
        if clothes == 5:
            if pregnancyshowing == 1:
                show mco bunnysuitp
            elif True:
                show mco bunnysuit
        if clothes == 6:
            show mco camisole
        if clothes == 7:
            show mco underwear
        if clothes == 9:
            if pregnancyshowing == 1:
                show mco clubp
            elif True:
                show mco club
        if clothes == 10:
            show mco bar
        if clothes == 11:
            show mco swimsuit
        if clothes == 12:
            show mco uniform2
            if pregnancyshowing == 1:
                show mco uniform2p
        if clothes == 13:
            show mco hero
            if pregnancyshowing == 1:
                show mco herop
        if clothes == 14:
            show mco slimehero
            if pregnancyshowing == 1:
                show mco slimeherop
        if clothes == 15:
            show mco dom
            if pregnancyshowing == 1:
                show mco domp
        return
    label clothesnude:
        call clothingedits from _call_clothingedits_1
        return
    label clothesdom:
        call clothingedits from _call_clothingedits_16
        show mco dom
        if pregnancyshowing == 1:
            show mco domp
        return
    label clothesunderwear:
        call clothingedits from _call_clothingedits_2
        show mco underwear
        return
    label clothespanties:
        call clothingedits from _call_clothingedits_3
        show mco panties
        return
    label clothesbunnysuit:
        if tan == 0:
            show mc nude
            if pregnancyshowing == 1:
                show mc pregnant
        elif True:
            show mc tan
            if pregnancyshowing == 1:
                show mc tanpregnant
        if piercingson == 1:
            show mcpiercings
        show mch
        if hair == 1:
            show mch black
        if hair == 2:
            show mch blonde
        show mco bunnysuit
        if pregnancyshowing == 1:
            show mco bunnysuitp
        return
    label clothesbar:
        call clothingedits from _call_clothingedits_4
        show mco bar
        return
    label clothesbar2:
        call clothingedits from _call_clothingedits_5
        show mco bar2
        return
    label clothesbar3:
        call clothingedits from _call_clothingedits_6
        show mco bar3
        return
    label clothesbeach:
        call clothingedits from _call_clothingedits_7
        show mco swimsuit
        return
    label clothesformal:
        call clothingedits from _call_clothingedits_8
        show mco uniform
        if pregnancyshowing == 1:
            show mco uniformp
        return
    label clothescasual:
        call clothingedits from _call_clothingedits_9
        show mco casual
        if pregnancyshowing == 1:
            show mco casualp
        return
    label clothesclub:
        call clothingedits from _call_clothingedits_10
        show mco club
        if pregnancyshowing == 1:
            show mco clubp
        return
    label clothespjs:
        call clothingedits from _call_clothingedits_11
        show mco pjs
        if pregnancyshowing == 1:
            show mco pjsp
        return
    label clothescatlingerie:
        call clothingedits from _call_clothingedits_12
        show mco catlingerie
        return
    label clothescamisole:
        call clothingedits from _call_clothingedits_13
        show mco camisole
        return
    label clothesuniform:
        call clothingedits from _call_clothingedits_14
        show mco uniform2
        if pregnancyshowing == 1:
            show mco uniform2p
        return
    label clotheshero:
        call clothingedits from _call_clothingedits_15
        show mco hero
        if pregnancyshowing == 1:
            show mco herop
        return

label dream:
    $ rand = renpy.random.randint(1,10)
    if dream == 0:
        if rand == 1 and sd > 150:
            "Dream: You wake up incredibly horny, so you rub your dripping wet pussy at the thought of being gangbanged."
            $ sdgain = 1
            if qheavysleeper == 1:
                $ sdgain = 2
            call sdgain from _call_sdgain_75
            play sound success
            "(+[fsd] Sexual Desire!)"
        elif rand == 1 and sd > 50:
            "Dream: You have a wet dream where you're bent over and pounded. You masturbate in the morning at the thought of it."
            $ sdgain = 1
            if qheavysleeper == 1:
                $ sdgain = 2
            call sdgain from _call_sdgain_76
            play sound success
            "(+[fsd] Sexual Desire!)"
        elif rand == 1:
            "Dream: You have a lewd dream that causes you to wake up hot and bothered."
            $ sdgain = 1
            if qheavysleeper == 1:
                $ sdgain = 2
            call sdgain from _call_sdgain_77
            play sound success
            "(+[fsd] Sexual Desire!)"
        if rand == 2:
            "Dream: You sleep really well, causing you to retain information better today."
            $ smartsgain = 1
            if qheavysleeper == 1:
                $ smartsgain = 2
            call smartsgain from _call_smartsgain_5
            play sound success
            "(+[fsmarts] Smarts!)"
        if rand == 3 and shame < 10:
            "Dream: With no sense of shame, you wonder if it'd be easier to offer sex to people on the street for cash."
            $ shameloss = 1
            if qheavysleeper == 1:
                $ shameloss = 2
            call shameloss from _call_shameloss_53
            play sound success
            "(-[fshame] Shame!)"
        elif rand == 3 and shame < 50:
            "Dream: You think of increasingly depraved ways to earn money."
            $ shameloss = 1
            if qheavysleeper == 1:
                $ shameloss = 2
            call shameloss from _call_shameloss_54
            "(-[fshame] Shame!)"
        elif rand == 3:
            "Dream: You were kept up thinking about money problems. You're a little more desperate now than you were before."
            $ shameloss = 1
            if qheavysleeper == 1:
                $ shameloss = 2
            call shameloss from _call_shameloss_55
            "(-[fshame] Shame!)"
    elif True:
        $ dream = 0
    return


label morningeffects:
    $ morning = 1
    $ weekend = 0
    $ days += 1
    $ clubpp = 0
    $ bloated = 0
    $ rand = renpy.random.randint(1,100)
    $ rand2 = renpy.random.randint(1,100)
    $ rand3 = renpy.random.randint(1,100)
    if pregnancyshowing == 1 and pregnant == 0:
        $ pregnancyshowing = 0
        "My bloated belly returned to its normal size in my sleep."
    if pregnancyterm > 0 and pregnant == 0:
        $ pregnancyterm = 0
    if dailygrope == 1:
        $ sd -= 5
        $ dailygrope = 0
    if tantime > 0:
        $ tantime -= 1
        if tantime == 0:
            $ tan = 0
    if droppedout == 0:
        $ potencollegemissed += 1
    $ gssa = 0
    if qintrovert == 1:
        $ alonemult == 1.1
    call thrillseekercheck from _call_thrillseekercheck
    if pregnant == 1:
        $ pregnancyterm += 1
        if pregnancyspeed == 2:
            $ pregnancyterm += 1
        elif pregnancyspeed == 4:
            $ pregnancyterm += 3
        elif pregnancyspeed == 6:
            $ pregnancyterm += 5
    if event == 7:
        $ event = 0
        if qrichkid == 1:
            $ moneygain = 30
            call moneygain from _call_moneygain_50
            play sound success
            "The money from my parents comes in! (+$[fmoney])!"
    $ event += 1
    $ pregchan = renpy.random.randint(0,2)
    if pregchan == 2:
        $ fertilityrate = "Safe Day"
    elif pregchan == 1:
        $ fertilityrate = "Risky Day"
    elif pregchan == 0:
        $ fertilityrate = "Dangerous Day"

    if aphrodisiacdrank == 1:
        $ aphrodisiacdrank = 0
        if qlightweight == 1:
            $ sd -= 20
            $ shame += 10
        $ sd -= 20
        $ shame += 10
        "The aphrodsiac wore off in my sleep, returning my thoughts and desires back to normal."
    if fertile == 1:
        $ fertile = 0
    if drunk >= 5:
        if drunk == 10:
            if qlightweight == 1:
                $ sd -= 50
                $ shame += 50
            $ sd -= 50
            $ shame += 50
        if drunk == 9:
            if qlightweight == 1:
                $ sd -= 45
                $ shame += 45
            $ sd -= 45
            $ shame += 45
        if drunk == 8:
            if qlightweight == 1:
                $ sd -= 40
                $ shame += 40
            $ sd -= 40
            $ shame += 40
        if drunk == 7:
            if qlightweight == 1:
                $ sd -= 35
                $ shame += 35
            $ sd -= 35
            $ shame += 35
        if drunk == 6:
            if qlightweight == 1:
                $ sd -= 30
                $ shame += 30
            $ sd -= 30
            $ shame += 30
        if drunk == 5:
            if qlightweight == 1:
                $ sd -= 25
                $ shame += 25
            $ sd -= 25
            $ shame += 25
        show mc:
            xpos 850
        show mcpiercings blank:
            xpos 850
        show mccatears blank:
            xpos 850
        show mch:
            xpos 850
        show mco:
            xpos 850
        call clothesnude from _call_clothesnude_47
        show mce neutral:
            xpos 850
        with d
        "Mmphh... Mmm... What happened? I'm at home? I'm completely naked..."
        "Urgh... My head hurts so much... Just how much did I drink last night?"
        "What the hell... I don't remember anything, it's like I lost an entire day."
        "I'm glad I got home safe, though..."
        "Although... There is a white, sticky substance between my thighs... I think it'd be better for my sanity if I just had a shower and forgot about that."
        $ drunk = 0
    elif drunk > 0:
        if drunk == 4:
            if qlightweight == 1:
                $ sd -= 20
                $ shame += 20
            $ sd -= 20
            $ shame += 20
        elif drunk == 3:
            if qlightweight == 1:
                $ sd -= 15
                $ shame += 15
            $ sd -= 15
            $ shame += 15
        elif drunk == 2:
            if qlightweight == 1:
                $ sd -= 10
                $ shame += 10
            $ sd -= 10
            $ shame += 10
        elif drunk == 1:
            if qlightweight == 1:
                $ sd -= 5
                $ shame += 5
            $ sd -= 5
            $ shame += 5
        "As you sobered up, your stats return to normal."
    if drunk >= 5:
        "You were drunk beyond comprehension last night. You don't even remember what you did or where you were..."
        "Oh, and you almost missed the entire morning..."
        if event < 6:
            if droppedout == 0:
                "And college! Oh shit!"
        play sound success2
        if qlightweight == 1:
            $ smarts -= 2
            "(-2 Smarts!)"
        elif True:
            $ smarts -= 1
            "(-1 Smarts!)"
        $ drunk = 0
        jump postworktrans
    elif drunk >= 3:
        show mc:
            xpos 850
        show mcpiercings blank:
            xpos 850
        show mccatears blank:
            xpos 850
        show mch:
            xpos 850
        show mco:
            xpos 850
        call clothespjs from _call_clothespjs_9
        show mce neutral:
            xpos 850
        with d
        "Ahh... I got way too drunk, and I wake up with a remarkable hangover..."
        if event < 6:
            if droppedout == 0:
                "And I miss my first few classes."
        play sound success2
        if qlightweight == 1:
            $ smarts -= 2
            "(-2 Smarts!)"
        elif True:
            $ smarts -= 1
            "(-1 Smarts!)"
    elif True:
        show mc:
            xpos 850
        show pinkbody 0:
            xpos 850
        show mcpiercings blank:
            xpos 850
        show mccatears blank:
            xpos 850
        show mch:
            xpos 850
        show mco:
            xpos 850
        show pinkhair 0:
            xpos 850
        call clothes from _call_clothes_81
        show mce neutral:
            xpos 850
        with d
        if pregnancyterm > 280:
            "Uh oh, I think my water just broke!"
            scene bg black with d
            jump naturalbirth
        "Getting up promptly at 8:00am, I shower, then prepare to face the day!"
    $ drunk = 0
    $ interestpercentage = interest/100.00
    $ interestpercentage += 1.00
    $ fbanked = int(interestpercentage*banked)
    $ nbanked += fbanked - banked
    $ banked = fbanked
return



label studyquiz:
    "(Answer the following question correctly, and you will recieve double smarts!)"
    if tq == 11:
        pass
    elif True:
        $ tq += 1
    if tq == 1:
        menu:
            "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, is the start of which famous sequence of numbers?"
            "Fibonnaci's Sequence" if True:
                call tqc from _call_tqc
            "Prime Numbers" if True:
                call tqi from _call_tqi
            "Geometric Sequence" if True:
                call tqi from _call_tqi_1
            "The Smooth Criminal" if True:
                call tqi from _call_tqi_2
    elif tq == 2:
        menu:
            "In terms of fireworks, what colour would you expect to be produced by a firework containing copper chloride?"
            "Brown" if True:
                call tqi from _call_tqi_3
            "Blue" if True:
                call tqc from _call_tqc_1
            "Rainbow" if True:
                call tqi from _call_tqi_4
            "Red" if True:
                call tqi from _call_tqi_5
    elif tq == 3:
        menu:
            "What term is used to describe the frequency of a sound when it is more than 20,000 Hz?"
            "Supersonic" if True:
                call tqi from _call_tqi_9
            "Hypersonic" if True:
                call tqi from _call_tqi_10
            "Ultrasonic" if True:
                call tqc from _call_tqc_2
            "Speed of Sound Sonic" if True:
                call tqi from _call_tqi_11
    elif tq == 4:
        menu:
            "An astronomical unit is the standard measurement taken from the earth to where?"
            "The Sun" if True:
                call tqc from _call_tqc_3
            "Pluto" if True:
                call tqi from _call_tqi_7
            "Your Mom" if True:
                "Hey! What's this one doing here?!"
                call tqi from _call_tqi_8
            "The Moon" if True:
                call tqi from _call_tqi_6
    elif tq == 5:
        menu:
            "What type of involuntary action in humans is known as a 'singultus' in medicine?"
            "Hiccups" if True:
                call tqc from _call_tqc_4
            "Sneezes" if True:
                call tqi from _call_tqi_12
            "Yawns" if True:
                call tqi from _call_tqi_13
            "Orgasm" if True:
                call tqi from _call_tqi_14
    elif tq == 6:
        menu:
            "What is the hottest planet in the solar system?"
            "Mercury" if True:
                call tqi from _call_tqi_15
            "Venus" if True:
                "Venus, with a temperature of 460°C, approximately 30°C higher than Mercury."
                call tqc from _call_tqc_5
            "Mars" if True:
                call tqi from _call_tqi_16
            "Sun" if True:
                call tqi from _call_tqi_17
    elif tq == 7:
        menu:
            "What color is your blood when it’s inside your body?"
            "Blue" if True:
                call tqi from _call_tqi_18
            "Purple" if True:
                call tqi from _call_tqi_19
            "Red" if True:
                "Blood contains hemoglobin, which is a red protein. Blue blood is merely a myth."
                call tqc from _call_tqc_6
            "Rainbow" if True:
                call tqi from _call_tqi_20
    elif tq == 8:
        menu:
            "What is a duel between three people called?"
            "A Three-Way" if True:
                call tqi from _call_tqi_21
            "A Truel" if True:
                call tqc from _call_tqc_7
            "A Triduel" if True:
                call tqi from _call_tqi_22
            "A Triage" if True:
                call tqi from _call_tqi_23
    elif tq == 9:
        menu:
            "Which of the following is a mammals that lays eggs?"
            "Pangolins" if True:
                call tqi from _call_tqi_24
            "Kangaroos" if True:
                call tqc from _call_tqc_8
            "Bats" if True:
                call tqi from _call_tqi_25
            "Echidnas" if True:
                call tqc from _call_tqc_9
    elif tq == 10:
        menu:
            "The name of which African animal means 'river horse'?"
            "Crocodile" if True:
                call tqi from _call_tqi_26
            "Zebra" if True:
                call tqi from _call_tqi_27
            "Hippopotamus" if True:
                call tqc from _call_tqc_10
            "Elephant" if True:
                call tqi from _call_tqi_28
    elif True:
        "(Looks like you've answered every single question. For that, you'll get the bonus smarts anyway!)"
        jump tqc
    return

label tqc:
    play sound success
    $ smartsgain = 1
    call smartsgain from _call_smartsgain
    "(Correct! +[fsmarts] Bonus Smarts!)"
    return

label tqi:
    "(Incorrect! Better luck next time.)"
    return


label thrillseekercheck:
    if personality == 5:
        if masturbations >= 1 and tsm == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_15
            call shameloss from _call_shameloss_3
            play sound success
            "(Thrill Seeker) You remember the thrill of masturbating yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsm = 1
        elif tsm == 1:
            "You come down from the thrill of masturbating. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsm = 2
        if groped >= 1 and tsg == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_16
            call shameloss from _call_shameloss_4
            play sound success
            "(Thrill Seeker) You remember the thrill of getting groped yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsg = 1
        elif tsg == 1:
            "You come down from the thrill of getting groped. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsg = 2
        if blowjobs >= 1 and tsbj == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_17
            call shameloss from _call_shameloss_5
            play sound success
            "(Thrill Seeker) You remember the thrill of giving a blowjob yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsbj = 1
        elif tsbj == 1:
            "You come down from the thrill of giving a blowjob. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsbj = 2
        if vaginalsexes >= 1 and tsv == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_18
            call shameloss from _call_shameloss_6
            play sound success
            "(Thrill Seeker) You remember the thrill of having vaginal sex yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsv = 1
        elif tsv == 1:
            "You come down from the thrill of having vaginal sex. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsv = 2
        if riskycreampies >= 1 and tsrc == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_19
            call shameloss from _call_shameloss_7
            play sound success
            "(Thrill Seeker) You remember the thrill of having a risky creampie yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsrc = 1
        elif tsrc == 1:
            "You come down from the thrill of having a risky creampie. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsrc = 2
        if analsexes >= 1 and tsas == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_20
            call shameloss from _call_shameloss_8
            play sound success
            "(Thrill Seeker) You remember the thrill of having anal sex yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsas = 1
        elif tsas == 1:
            "You come down from the thrill of having a anal sex. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsas = 2
        if groupsexes >= 1 and tsgs == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_21
            call shameloss from _call_shameloss_9
            play sound success
            "(Thrill Seeker) You remember the thrill of having group sex yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsgs = 1
        elif tsgs == 1:
            "You come down from the thrill of having group sex, somehow... (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsgs = 2
        if pregnancies >= 1 and tsp == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_22
            call shameloss from _call_shameloss_10
            play sound success
            "(Thrill Seeker) You remember the thrill of discovering you were pregnant yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsp = 1
        elif tsp == 1:
            "You come down from the thrill of becoming pregnant. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsp = 2
        if kisses >= 1 and tsk == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_118
            call shameloss from _call_shameloss_81
            play sound success
            "(Thrill Seeker) You remember the thrill of having your first kiss yesterday. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsk = 1
        elif tsk == 1:
            "You come down from the thrill of your first kiss. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsk = 2
        if voyeurisms >= 1 and tsv == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_119
            call shameloss from _call_shameloss_82
            play sound success
            "(Thrill Seeker) You remember the thrill of watching someone else have sex. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsv = 1
        elif tsv == 1:
            "You come down from the thrill of watching someone have sex. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsv = 2
        if publicdisplays >= 1 and tspd == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_120
            call shameloss from _call_shameloss_83
            play sound success
            "(Thrill Seeker) You remember the thrill of doing something naughty in public. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tspd = 1
        elif tspd == 1:
            "You come down from the thrill of being lewd in public.. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tspd = 2
        if photosets >= 1 and tsphs == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_121
            call shameloss from _call_shameloss_84
            play sound success
            "(Thrill Seeker) You remember the thrill of uploading a photo set of yourself online. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsphs = 1
        elif tsphs == 1:
            "You come down from the thrill of uploading a photo set of yourself online. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsphs = 2
        if pornshoots >= 1 and tspos == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_122
            call shameloss from _call_shameloss_85
            play sound success
            "(Thrill Seeker) You remember the thrill of having your first porn shoot. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tspos = 1
        elif tspos == 1:
            "You come down from the thrill of your porn shoot. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tspos = 2
        if camshows >= 1 and tscs == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_123
            call shameloss from _call_shameloss_86
            play sound success
            "(Thrill Seeker) You remember the thrill of having your first cam show. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tscs = 1
        elif tscs == 1:
            "You come down from the thrill of your cam show. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tscs = 2
        if lesbian >= 1 and tsls == 0:
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_124
            call shameloss from _call_shameloss_87
            play sound success
            "(Thrill Seeker) You remember the thrill of having your first sexual lesbian interaction. (+[fsd] Sexual Desire, -[fshame] Shame)"
            $ sd += 5
            $ shame -= 5
            "And it has given you a small stat boost today as you seek your next high! (+5 Sexual Desire, and -5 Shame for today)"
            $ tsls = 1
        elif tsls == 1:
            "You come down from the thrill of your first lesbian interaction. (-5 Sexual Desire, +5 Shame)"
            $ sd -= 5
            $ shame += 5
            $ tsls = 2
return

init:
    $ tsk = 0
    $ tsv = 0
    $ tspd = 0
    $ tsphs = 0
    $ tspos = 0
    $ tscs = 0
    $ tsls = 0
    $ tsm = 0
    $ tsg = 0
    $ tsbj = 0
    $ tsv = 0
    $ tsrc = 0
    $ tsas = 0
    $ tsgs = 0
    $ tsp = 0

label virgin:
    if virgin == 0:
        $ virgin = 1
        "Taking my virginity in the process!"
    return

label pregnancyroll:
    if pregnancyshowing == 1 or condomon == 1:
        return
    $ rand2 = renpy.random.randint(1,1000)
    if fertile == 1:
        if rand2 >= 10:
            $ riskycreampies += 1
            $ pregnant = 1
    elif onpill == 1 or pregchan == 2:
        return
    elif pregchan == 1:
        $ riskycreampies += 1
        if rand2 <= 125:
            $ pregnant = 1
    elif pregchan == 0:
        $ riskycreampies += 1
        if rand2 <= 250:
            $ pregnant = 1
    return

label postworktrans:
    stop ambience fadeout 1.0
    stop sound2 fadeout 1.0
    if qintrovert == 1:
        $ alonemult = 1.1
    if drunk >= 5:
        jump blackout
    if morning == 1:
        $ morning = 0
        $ rand = renpy.random.randint(1,100)
        if event == 5:
            jump postday
        elif rand >= 33:
            jump event
        elif True:
            jump postday
    jump genericsleep

label status:
    if morning == 1:
        scene bg bedroomday
    elif True:
        scene bg bedroomnight
    show mc:
        xpos 850
    show pinkbody 0:
        xpos 850
    show mcpiercings blank:
        xpos 850
    show mccatears blank:
        xpos 850
    show mch:
        xpos 850
    show mco:
        xpos 850
    show pinkhair 0:
        xpos 850
    call clothesnude from _call_clothesnude_48
    show mce horny:
        xpos 850
    with d
    show statusmenuborder
    call screen status with d


screen status():
    imagemap:
        ground "statusmenu"
        hover "statusmenu hover"
        hotspot (700, 680, 700, 500) clicked Jump ("statusbacktransition")
    text "{b}Personality:{/b}":
        xpos 50
        ypos 50
    text "[personalityname]":
        xpos 50
        ypos 100
    text "{b}Quirks:{/b}":
        xpos 50
        ypos 150
    if qrichkid == 1:
        text "Rich Kid":
            xpos 50
            ypos 200
    if qsexuallyexperienced == 1:
        text "Sexually Experienced":
            xpos 50
            ypos 250
    if qanalqueen == 1:
        text "Anal Queen":
            xpos 50
            ypos 300
    if qpregnant == 1:
        text "Woops! Already Pregnant!":
            xpos 50
            ypos 350
    if qheavysleeper == 1:
        text "Heavy Sleeper":
            xpos 50
            ypos 400
    if qlightweight == 1:
        text "Lightweight":
            xpos 50
            ypos 450
    if qintrovert == 1:
        text "Introvert":
            xpos 50
            ypos 500
    if qsecretlydepraved == 1:
        text "Secretly Depraved":
            xpos 50
            ypos 550
    if qseriouslyfocused == 1:
        text "Serious Grafter":
            xpos 50
            ypos 600
    if qunwavering == 1:
        text "Unwavering Will":
            xpos 50
            ypos 650
    if qstressfree == 1:
        text "Stress Free":
            xpos 50
            ypos 700
    if qdetermination == 1:
        text "Determination":
            xpos 50
            ypos 750
    if qllthf == 1:
        text "Living Life to the Full!":
            xpos 50
            ypos 800
    if qselfiestar == 1:
        text "Selfie Star":
            xpos 50
            ypos 850

    text "{b}Sexual Experiences:{/b}":
        xpos 500
        ypos 50
    text "[kisses]":
        xpos 810
        ypos 117
    text "[voyeurisms]":
        xpos 810
        ypos 167
    text "[publicdisplays]":
        xpos 810
        ypos 217
    text "[photosets]":
        xpos 810
        ypos 267
    text "[pornshoots]":
        xpos 810
        ypos 317
    text "[camshows]":
        xpos 810
        ypos 367
    text "[lesbian]":
        xpos 810
        ypos 417
    text "[masturbations]":
        xpos 810
        ypos 467
    text "[groped]":
        xpos 810
        ypos 517
    text "[blowjobs]":
        xpos 810
        ypos 568
    text "[vaginalsexes]":
        xpos 810
        ypos 615
    text "[riskycreampies]":
        xpos 810
        ypos 665
    text "[analsexes]":
        xpos 810
        ypos 715
    text "[groupsexes]":
        xpos 810
        ypos 765
    text "[pregnancies]":
        xpos 810
        ypos 815
label statusbacktransition:
    hide statusmenuborder
    if morning == 0:
        jump bedroom
    elif True:
        jump bedroommorning

label blackout:
    play sound success2
    stop music
    stop ambience
    scene bg black with d
    $ blackoutsex = 1
    "While excessively drunk, you completely black out!"
    "While you were out..."
    play ambience sex fadein 5.0
    play sound2 foreplay1 fadein 5.0
    show missionarysexb
    if pregnancyshowing == 1:
        show missionarysexa pregnant1
    if tan == 1:
        show missionarysexbtan
        if pregnancyshowing == 1:
            show missionarysexbtanp
    if hair == 1:
        show missionarysexh black
    if hair == 2:
        show missionarysexh blonde
    if piercingson == 1:
        show missionarysexpiercings
    show missionarysex 2b
    show blackring:
        xalign 0.5 ypos -100
        linear 8.0 ypos -850
        linear 8.0 ypos -100
        repeat
    show black border
    show black:
        linear 2 alpha 0.5
        linear 2 alpha 0.1
        repeat
    with d
    "Briefly fading in and out of consiousness... I don't really know how I got here, or what's happening..."
    "Am I home? I don't think so..."
    "Something feels uncomfortable... But still kind of pleasant..."
    play sound cum
    show missionarysex 3b with cum
    play sound cum
    show missionarysex 3b with cum
    "Something hot, and warm emanates from within me, splattering on my thighs and pelvis..."
    "My body shivers, and before I can think of anything else..."
    stop ambience fadeout 3.0
    stop sound2 fadeout 3.0
    if virgin == 0:
        $ virgin = 1
    $ status += 1
    $ vaginalsexes += 1
    call pregnancyroll from _call_pregnancyroll_20
    jump morning

label trueendbg:
    scene black
    show trueendingbgwindow1:
    show trueendingbgwindow2:
        alpha 0
        linear 3.0 alpha 1.0
        linear 3.0 alpha 0
        repeat
    show trueendingbg4
    show trueendingbg3:
        alpha 0
        linear 6.0 alpha 1.0
        linear 6.0 alpha 0
        repeat
    show trueendingbg1:
        alpha 1.0
        linear 4.0 alpha 0
        linear 4.0 alpha 1.0
        repeat
    show trueendingbg2:
        alpha 0
        linear 5.0 alpha 1.0
        linear 5.0 alpha 0
        repeat
    return

label trueendtacotable:
    show trueendingtacob table
    if persistent.tetan == 1:
        show trueendingtacob tabletan
    if persistent.tehair == 1:
        show trueendingtacoh black
    elif persistent.tehair == 2:
        show trueendingtacoh blonde
    if persistent.tepiercings == 1:
        show trueendingtacoepiercings

    if persistent.tewet == 1:
        show trueendingtacoewet

    if persistent.tebra == 1:
        show trueendingtacoobra
    if persistent.teclothes == 1:
        show trueendingtacoo formaltable
    elif persistent.teclothes == 2:
        show trueendingtacoo formallewdtable
    elif persistent.teclothes == 3:
        show trueendingtacoo camisole
        show trueendingtacotableoutfitclip
        if persistent.tetan == 1:
            show trueendingtacotableoutfitcliptan
    elif persistent.teclothes == 4:
        show trueendingtacoo cat
        show trueendingtacotableoutfitclip
        if persistent.tetan == 1:
            show trueendingtacotableoutfitcliptan
    if persistent.cum1 == 1:
        show trueendingtacoe cum1t
    if persistent.cum2 == 1:
        show trueendingtacoe cum2t
    if persistent.cum3 == 1:
        show trueendingtacoe cum3t
    return

label trueendtaco:
    show trueendingtacob notable
    if persistent.tetan == 1:
        show trueendingtacob notabletan
    if persistent.tehair == 1:
        show trueendingtacoh black
    elif persistent.tehair == 2:
        show trueendingtacoh blonde
    if persistent.tepiercings == 1:
        show trueendingtacoepiercings
    if persistent.tewet == 1:
        show trueendingtacoewet

    if persistent.tebra == 1:
        show trueendingtacoobra
    if persistent.tepanties == 1:
        show trueendingtacoopanties
    if persistent.teclothes == 1:
        show trueendingtacoo formal
    elif persistent.teclothes == 2:
        show trueendingtacoo formallewd
    elif persistent.teclothes == 3:
        show trueendingtacoo camisole
    elif persistent.teclothes == 4:
        show trueendingtacoo cat
    if persistent.cum1 == 1:
        show trueendingtacoe cum1
    if persistent.cum2 == 1:
        show trueendingtacoe cum2
    if persistent.cum3 == 1:
        show trueendingtacoe cum3
    return

label trueendtacodate:
    show mc nude
    if persistent.tetan == 1:
        show mc tan
    if persistent.tehair == 1:
        show mch black
    elif persistent.tehair == 2:
        show mch blonde
    if persistent.tepiercings == 1:
        show mcpiercings

    if persistent.tepanties == 1:
        show mco panties
    if persistent.tebra == 1:
        show mco bra
    if persistent.teclothes == 1:
        show mco uniform
    elif persistent.teclothes == 2:
        show mco uniform2
    elif persistent.teclothes == 3:
        show mco camisole
    elif persistent.teclothes == 4:
        show mco catlingerie
    return

label tebt:
    if persistent.trueendstage2 == False:
        mc "*Yawn* Wonder what we'll do today?"
        jump maptobedroom
    if morning == 1:
        hide bedroom screen border
        with d
    menu tebtm:
        "Are you sure you want to return to the Astral Bedroom? This will lose unsaved progress."
        "Save" if True:
            call screen save
            jump tebtm
        "Return to Astral Bedroom" if True:
            jump trueendscreen
        "Back" if True:
            jump maptobedroom

label temusic:
    if persistent.temusicrandom == 1:
        $ persistent.temusic = renpy.random.randint(2,14)
    if persistent.temusic == 0:
        play music ending
    elif persistent.temusic == 1:
        stop music fadeout 1.0
    elif persistent.temusic == 2:
        play music ending
    elif persistent.temusic == 3:
        play music intro
    elif persistent.temusic == 4:
        play music daytime
    elif persistent.temusic == 5:
        play music rest
    elif persistent.temusic == 6:
        play music lonelyfans
    elif persistent.temusic == 7:
        play music club
    elif persistent.temusic == 8:
        play music toko
    elif persistent.temusic == 9:
        play music dungeon
    elif persistent.temusic == 10:
        play music massage
    elif persistent.temusic == 11:
        play music girls
    elif persistent.temusic == 12:
        play music studio
    elif persistent.temusic == 13:
        play music te
    elif persistent.temusic == 14:
        play music action
    return

label spacebg:
    scene space3:
        alpha 0
        linear 20.0 alpha 1.0
    show space1:
        alpha 0.0
        linear 20.0 alpha 1.0
        linear 8.0 alpha 0
        block:
            alpha 0
            linear 8.0 alpha 1.0
            linear 8.0 alpha 0
            repeat
    show space2:
        alpha 0.0
        linear 20.0 alpha 0
        linear 8.0 alpha 1.0
        block:
            alpha 1.0
            linear 8.0 alpha 0
            linear 8.0 alpha 1.0
            repeat
    call trueendtacodate from _call_trueendtacodate_9
    show mce angry
    with d
    return

init:
    $ tq = 0
    $ rand2 = 0
    $ kisses = 0
    $ masturbations = 0
    $ groped = 0
    $ blowjobs = 0
    $ vaginalsexes = 0
    $ riskycreampies = 0
    $ analsexes = 0
    $ groupsexes = 0
    $ pregnancies = 0
    $ camshows = 0
    $ lesbian = 0
    $ pornshoots = 0
    $ photosets = 0
    $ voyeurisms = 0
    $ publicdisplays = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label bank:
    if bankunlocked == 0:
        "Unlock this location by having over $500."
        if money >= 500:
            "Unlock?"
            menu:
                "Unlock" if True:
                    $ bankunlocked = 1
                    play sound success
                    jump postworldmap
                "Back" if True:
                    pass
        jump postworldmap
    elif True:
        play music studio
        scene bg bank
        call clothes from _call_clothes_28
        show mce happy
        with d
        if lewdoutfit or nude == 1:
            show mce horny
            with d
            "I can't believe I'm wearing this at the bank. Everyone keeps staring at me!"
        if bankaccount == 0:
            $ bankaccount = 1
            "Walking up to the counter, I wait in line to open an account."
            mc "Hello, I'd like to make an account? I'm a student, and I'm interested in the account type that helps pay off my student loan."
            receptionist "Alright, please go through the hall and enter the first door on the left."
            mc "Thank you."
            "An interview for my bank account? Seems a bit over the top, but this bank does give exceptional deals for hero students."
            scene bg bank2
            show stranger2:
                xpos 1200
            with d
            boss "Welcome! [mc], right?"
            call clothes from _call_clothes_103
            show mce laughing
            with d
            mc "Ah, yes. Thank you."
            if lewdoutfit or nude == 1:
                "He looks up from his desk, eyes widening as he sees what I'm wearing."
                boss "Eh-hem, well, uhm..."
            boss "Whatcha looking to open this account for?"
            show mce happy with d
            mc "I just want to save money to pay off my student debt."
            boss "And how much would that be?"
            mc "$72,000."
            boss "Hmm… That’s on the high end, and we don’t usually accept applicants long term on such short notice."
            show mce neutral with d
            mc "Aahh, but…"
            boss "Normal accounts have a 0.5%% interest, but since you’re so damn gorgeous, I think we could look at some higher accounts. Maybe you should tell me what you’re interested in."
            mc "H-Huh?"
            "Catching me in momentarily disbelief, he pushes forward a couple of account options. There I see a 1%% interest, 2%% and 4%% interest accounts."
            "I can just… pick one of these? What’s the catch?"
            show mce horny with d
            mc "Let’s say I hypothetically wanted the highest?"
            boss "I can’t let you have that, unless… I suppose I’d want to know how badly you wanted it."
            "He nonchalantly pats his thigh in a manner conspicuous enough to avoid getting in trouble."
            show mce neutral with d
            mc "*Gulp* Uhm, and 2%%?"
            boss "Again, not something I could really do off the bat. I’d need some convincing…"
            show mce happy with d
            mc "Aahh… 1%%?"
            boss "1%%? It’s a bit shit, isn’t it? You’ll never pay your debt off with that."
            show mce sad with d
            mc "You’re not wrong there…"
            "If it wasn’t already obvious what he was implying, the big suit unbuckles his belt, and weaves it away from his pants."
            boss "Pardon me, I had quite a large brunch."
            boss "Are you going for the 2%%? Surely that’d be more suitable than 0.5%% for a lady such as yourself."
            show mce angry with d
            play music dungeon
            "He’s put me in a difficult situation here."
            "I guess I could probably…"
            menu:
                "Sexual Desire: [sd], Shame: [shame], Smarts: [smarts]."
                "Persuade (Smooth Operator)" if personality == 3:
                    show mce horny with d
                    mc "While I say I'm looking to pay off debts, I'm not just 'any' student."
                    mc "I have big plans, and I need a great, reliable bank to hold onto my money as it racks up."
                    boss "Aahh, you're planning to go big?"
                    mc "I'm not a NeoHero Student for nothing. Top college in the country, and the last two top heroes in the country graduated from there. You know exactly what I can offer."
                    boss "Quite right, quite right... Fine, in that case... I can write you a 2%% account, 4%% is pushing it, but 2%% will be just fine."
                    "He turns to his PC and opens up my account."
                    boss "There, your account is upgraded."
                    mc "Perfect, thank you very much!"
                    play sound success
                    $ shameloss = 0.5
                    call shameloss from _call_shameloss_130
                    "(-[fshame] Shame!)"
                    "(Your bank account now earns 2%% interest a day.)"
                    $ interest = 2
                    jump bank
                "Threaten to Report him for 2%% (25 Smarts)" if True:
                    if smarts <= 25:
                        "Report him? I'm not sure how I'd do that."
                        jump banksfm
                    mc "This is remarkably illegal, and don't think subtle language will stop me from reporting this to your superiors immediately."
                    "To bolster my threat, I prepare to leave the room immediately."
                    boss "Woah, woah, woah! Calm down! I don't know what gave you that idea."
                    boss "Come on, I'm on your side, how about a 2%% account?"
                    mc "You can't do 4%%?"
                    boss "Eeehhh... Those are for special customers..."
                    mc "Fine, 2%% and I'll keep quiet about what you do."
                    "He turns to his PC and opens up my account."
                    boss "There, your account is upgraded."
                    mc "Perfect, thank you very much!"
                    play sound success
                    $ shameloss = 0.5
                    call shameloss from _call_shameloss_131
                    "(-[fshame] Shame!)"
                    "(Your bank account now earns 2%% interest a day.)"
                    $ interest = 2
                    jump bank
                "Handjob for 2%%. (30 Sexual Desire, <70 Shame)" if True:
                    if sd < 30 or shame > 70:
                        "Touching his cock? Ew, no way!"
                        jump banksfm
                    show mce happy with d
                    "This is a big deal, and making a few sacrifices to pull a few strings might be worth it."
                    "I can probably get away with doing something fairly light too."
                    "I don’t know if I should scold this man for taking advantage of me, or praise him for breaking the rules for me in exchange for something I can give him."
                    "It almost seems like a fair trade…"
                    mc "Okay, let’s try for 2%%... Is the door locked?"
                    boss "Oh, it always is."
                    $ interest = 2
                    jump bankhj
                "Take 0.5%%." if True:
                    show mce neutral with d
                    mc "No, no, 0.5%% will be fine…"
                    "I could probably just… swap banks, right?"
                    "Even though this bank gives great bonuses and rates for hero students… Eugh, what a dilemma."
                    $ interest = 0.5
                    play sound success2
                    "(Your bank account now earns 0.5%% interest a day.)"
                    jump bank
        elif True:
            if bankintro == 0:
                $ bankintro = 1
                receptionist "Hello, [mc]. Your account is open, and has come with a free $10 as a reward for opening an account with us."
                mc "Oohh, excellent!"
                receptionist "You may withdraw and deposit money at any time, and it'll earn an interest rate of [interest] per day."
                receptionist "Now, how can I help you?"
            if nbanked > 0:
                play sound success
                "You've made $[nbanked] in interest since your last visit."
                $ nbanked = 0
            "What would you like to do?"
            menu bankmenu:
                "You have $[money]. In your bank you have $[banked] deposited at an interest rate of [interest]%% per day."
                "Deposit" if True:
                    menu bankmenud:
                        "You have $[money]. In your bank you have $[banked] deposited at an interest rate of [interest]%% per day."
                        "$100" if True:
                            if money < 100:
                                "I don't have enough."
                                jump bankmenud
                            $ banked += 100
                            $ money -= 100
                        "$500" if True:
                            if money < 500:
                                "I don't have enough."
                                jump bankmenud
                            $ banked += 500
                            $ money -= 500
                        "$1000" if True:
                            if money < 1000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked += 1000
                            $ money -= 1000
                        "$5000" if True:
                            if money < 5000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked += 5000
                            $ money -= 5000
                        "$10,000" if True:
                            if money < 10000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked += 10000
                            $ money -= 10000
                        "Back" if True:
                            jump bankmenu
                    play sound success
                    jump bankmenud
                "Withdraw" if True:
                    menu bankmenuw:
                        "You have $[money]. In your bank you have $[banked] deposited at an interest rate of [interest]%% per day."
                        "$100" if True:
                            if banked < 100:
                                "I don't have enough."
                                jump bankmenud
                            $ banked -= 100
                            $ money += 100
                        "$500" if True:
                            if banked < 500:
                                "I don't have enough."
                                jump bankmenud
                            $ banked -= 500
                            $ money += 500
                        "$1000" if True:
                            if banked < 1000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked -= 1000
                            $ money += 1000
                        "$5000" if True:
                            if banked < 5000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked -= 5000
                            $ money += 5000
                        "$10,000" if True:
                            if banked < 10000:
                                "I don't have enough."
                                jump bankmenud
                            $ banked -= 10000
                            $ money += 10000
                        "Back" if True:
                            jump bankmenu
                    play sound success
                    jump bankmenuw
                "Sexual Favors" if True:
                    "I could visit the manager and trade sexual favours in exchange for a higher rate… What am I willing to do?"
                    menu banksfm:
                        "Sexual Desire: [sd], Shame: [shame]."
                        "Sex for 4%% (70 Sexual Desire, <30 Shame)" if True:
                            if sd < 70 or shame > 30:
                                "I don't think so... I'm not so desperate that I'd sell myself."
                                jump banksfm
                            if interest < 4:
                                pass
                            elif True:
                                "I won’t be able to increase my accounts standing by having sex with him again."
                                "Am I sure I want to do it?"
                                menu:
                                    "Yeah" if True:
                                        pass
                                    "Nevermind" if True:
                                        jump banksfm
                            scene bg bank2
                            show stranger2:
                                xpos 1200
                            call clothes from _call_clothes_106
                            show mce horny
                            with d
                            play music action
                            mc "Hey, babe… I really wanted to try for that 4%% account."
                            bank "Sweet words won’t be enough for me to put my job on the line. These accounts are only for our best customers."
                            mc "Oh I’ll be your best customer, alright. You might want to unzip pre-emptively for this one."
                            play sound equip
                            if nude == 0:
                                scene bg bank2
                                show stranger2:
                                    xpos 1200
                                call clothesnude from _call_clothesnude_76
                                show mce horny
                                with d
                                "I remove my clothing one by one, allowing each article to drop onto the floor as I seductively cat walk around the banker’s chair."
                            elif True:
                                mc "I came in the nude for a reason, hehe..."
                                bank "What are you? Some kind of damn nymph?"
                            "I turn his chair around to face a wall, just as I get into position to show off my ass."
                            show bankersexb
                            if pregnancyshowing == 1:
                                show bankersexbp
                            if tan == 1:
                                show bankersexbtan
                                if pregnancyshowing == 1:
                                    show bankersexbtanp
                            if hair == 1:
                                show bankersexh black
                            if hair == 2:
                                show bankersexh blonde
                            if piercingson == 1:
                                show bankersexpiercings
                            show bankersex 1
                            with d
                            mc "This can be all yours for 4%%. I’ll just need to confirm you make the change before I let you fuck me."
                            bank "Y-You do know that I have a wife? Right? A hand job is one thing, but…"
                            mc "This is the easiest affair in the world to hide. Why draw the line at penetration over a handie?"
                            bank "R-Right! By all means, I’ll upgrade your account right now."
                            "Quickly clicking away at his keyboard, he brings up my account and upgrades it to the highest tier."
                            play sound success
                            "(You now earn 4%% interest a day.)"
                            $ interest = 4
                            "Heh, his cock is already rock hard. Then again, my pussy is already soaking wet."
                            "Using my sexuality like this is almost enough to get me off on its own."
                            mc "Perfect. Now I want you to fuck me hard."
                            "Impatiently he unbuckles his belt, unzips his pants and pops his cock out of his underwear as he scurries into position behind me."
                            $ condomon = 0
                            if condoms > 0 and pregnancyshowing == 0:
                                menu:
                                    "Use a condom? Condoms: [condoms]. [fertilityrate]."
                                    "Yeah." if True:
                                        $ condomon = 1
                                        $ condoms -= 1
                                    "Fuck the rules! (Without protection!)" if True:
                                        $ condomon = 0
                            "I’m so wet and ready that when he thrusts it in immediately, I take it with ease."
                            play sound cum
                            show bankersex 2 with d
                            if virgin == 0:
                                $ virgin = 1
                                "I know I'm giving him my virginity, but this is an excellent investment."
                                "An account like this will set me for life. It's almost poetic in a way."
                            play sound2 foreplay1
                            play ambience sex
                            "He starts humping like a desperate dog, slamming his cock back and forth. He roughly pounds my pussy, while maintaining a firm grip on my hips."
                            "The sounds of our sexes slapping against each other mix and echo through the office, combined with my moans of pleasure, it truly is an erotic symphony to the ears."
                            "We’re not exactly being subtle. I’m sure anyone that walks past this room can hear us rutting like animals."
                            mc "Mpphh, mmm… Keep going, I’m gonna need a thick deposit of cum, Mr. Banker!"
                            bank "Yeah, yeah! Your ass is amazing!"
                            "Almost beguiled, he continues to pound my bouncy butt as aggressively as he can. His cock twitching and swelling as his orgasm builds."
                            "My orgasm isn’t far off either, and as we keep up for another minute, I can feel myself on the very edge of climax."
                            mc "Aaahhh, t-that’s it! I’m going to come! Aaahhh, aahhh…"
                            "I climax, my pussy clenching tightly as I squeal with pleasure."
                            "My partner grits his teeth, driving his cock deeper and faster than before, really pushing me to the heights of euphoria."
                            mc "Mphh mmphhh! Yesss, this is exactly what I need! *Squish, squelch*!"
                            "My orgasmic daze leaves me with jelly legs, and I struggle to remain upright. Fortunately, he’s not far off coming too."
                            play sound cum
                            show bankersex 3 with cum
                            play sound cum
                            show bankersex 3 with cum
                            "A sudden torrent of thick, jism spews deep into my pussy and womb."
                            play sound cum
                            show bankersex 3 with cum
                            play sound cum
                            show bankersex 3 with cum
                            "Three loads, six, then nine. My pussy is filled to the brim, so much that it readily oozes and spills out."
                            stop ambience fadeout 2.0
                            stop sound2 fadeout 2.0
                            "I barely have the energy to stay standing after that. I’m tremendously satisfied."
                            play sound cum
                            show bankersex 4 with d
                            "He pulls out and I fall forward, leaning heavily on the wall so stay upright."
                            mc "Phew… Wife not putting out in bed?"
                            bank "How could you tell?"
                            mc "Hehehe… Thanks for the 4%%, boss."
                            stop music fadeout 3.0
                            scene bg black with d
                            "I’m quick to clean up, redress and slip out of the office."
                            scene bg street2
                            call clothes from _call_clothes_107
                            show mce horny
                            with d
                            "I wonder how I should feel about that."
                            "Getting what I want with sex is fun, but it’s not exactly moral."
                            "I guess it's taboo. But do I really care about what others think about me?"
                            call pregnancyroll from _call_pregnancyroll_28
                            play sound success
                            $ banksex = 1
                            $ vaginalsexes += 1
                            $ status += 1
                            call sdgain from _call_sdgain_49
                            call shameloss from _call_shameloss_132
                            "(+[fsd] Sexual Desire, -[fshame] Shame)"
                            jump postworktrans
                        "Handjob for 2%%. (30 Sexual Desire, <70 Shame)" if True:
                            if sd < 30 or shame > 70:
                                "I don't think so... I'm not so desperate that I'd sell myself."
                                jump banksfm
                            if interest < 2:
                                pass
                            elif True:
                                "I won’t be able to increase my accounts standing by just giving him another handjob."
                                "Am I sure I want to do it?"
                                menu:
                                    "Yeah" if True:
                                        pass
                                    "Nevermind" if True:
                                        jump banksfm
                            scene bg bank2
                            show stranger2:
                                xpos 1200
                            call clothes from _call_clothes_108
                            show mce happy
                            with d
                            "I enter his office, and make my desires clear."
                            jump bankhj
                        "Back" if True:
                            jump bankmenu
                "Back" if True:
                    jump worldmap
jump bankmenu



label bankhj:
    play music action
    mc "I think I can lend you a hand in giving me 2%% interest, what do you think?"
    if nude == 0:
        "I start to undress my top, taking out my bountiful bosom to the banker’s delight."
        play sound equip
        scene bg bank2
        show stranger2:
            xpos 1200
        with d
    boss "Aahh, now that’s a convincing argument!"
    scene bankerhjb
    if pregnancyshowing == 1:
        show bankerhjbp
    if tan == 1:
        show bankerhjbtan
        if pregnancyshowing == 1:
            show bankerhjbtanp
    if piercingson == 1:
        show bankerhjpiercings
    if hair == 1:
        show bankerhjh black
    if hair == 2:
        show bankerhjh blonde
    show bankerhj 1
    with d
    "He unzips his pants and soon his half-chub pops out of his underwear. It’s underwhelming at first, but as I wrap my hand around it is soon balloons to a size, I can’t help but be impressed by."
    "As sleazy as this may be, that doesn’t mean it can’t be fun, or even hot."
    play ambience sex fadein 5.0
    "I gently jack his cock back and forth, getting a feel for it as it throbs in my grip."
    mc "You should have told me you had this monster, maybe you could have convinced me without raising my interest, hehehe."
    boss "Think nothing of it. We can both get something we want this way."
    mc "Ohh, you want me, do you? I bet you say that to all the girls that walk in here."
    boss "Only the drop-dead gorgeous ones such as yourself, babe."
    mc "Enough of the sweet sentiments, all I want to hear from you are moans."
    "Speeding up my hand, I quickly raise the tempo to one that could get him off."
    "It’s only a hand job, so there’s little room for exciting foreplay, and I’m sure I could get him off in only one or two minutes in this erotic situation."
    "I put on my best face, allow my breasts to sway back and forth, and waggle my tongue. All towards trying to make him blow his load in my face."
    "Thoughts of earning double interest swirl in my mind, almost overtaking the excitement of the sexual act."
    mc "Ohh, yeaahhh… I want you to cum all over my face."
    "He grits his teeth, and his cock swells up, signalling to me that he’s close. I put all my effort into jacking him off, and redouble my efforts with my tongue."
    play sound cum
    show bankerhj 2 with cum
    play sound cum
    show bankerhj 2 with cum
    "It doesn’t take much longer for him to finally cum, dousing me in a generous load of his jism."
    play sound cum
    show bankerhj 2 with cum
    play sound cum
    show bankerhj 2 with cum
    stop ambience fadeout 4.0
    "No wonder this guy came so fast, he’s been saving up, and I’m entirely on the receieving end of this excessive amount of cum."
    "I feel a little gross doing that with a stranger for money. It was kinda hot, though, maybe I let my libido go too far."
    "Regardless, it was only a handjob. Who knows if I’ll ever be able to use a modicum of my sexuality to such a great benefit again. It’s just one of the many advantages of being a woman, right?"
    play sound equip
    scene bg bank2
    show stranger2:
        xpos 1200
    call clothes from _call_clothes_109
    show mce horny
    with d
    mc "So… About that bank account?"
    bank "2%%! Consider it done!"
    mc "Uhhmm, what about 4%%?"
    bank "Hmph… Maybe… That’s hard to just make ‘happen’…"
    bank "Come back another time and I’ll see if I can pull a few strings, but it wouldn’t be something I’d do for just anyone."
    mc "Riiight, riiight. You need to get your kicks somehow."
    bank "It’s not just about that, I am breaking the rules here."
    mc "The end result is all I’m interested in. Maybe we’ll see each other again, maybe not."
    bank "It’s up to you, pretty lady. But for now? You have 2%% interest."
    play sound success
    "(Your bank account now gains 2%% interest per day.)"
    $ interest = 2
    $ bankhj = 1
    call sdgain from _call_sdgain_184
    call shameloss from _call_shameloss_133
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans


init:
    $ bankintro = 0
    $ bankunlocked = 0
    $ banksex = 0
    $ bankaccount = 0
    $ interest = 1
    $ interestpercentage = 0
    $ banked = 10
    $ nbanked = 0
    $ fbanked = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

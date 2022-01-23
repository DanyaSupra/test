label massage:
    if massageparlourunlocked == 0:
        "Unlock this location by having >20 Sexual Desire."
        if sd >= 20:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump massageunlock
                "Back" if True:
                    pass
        jump postworldmap
    play music massage
    scene bg massage
    call clothes from _call_clothes_9
    show mce happy
    if nude == 1 or lewdoutfit == 1:
        show mce horny
    if massage >= 1:
        show bunny with d:
            xpos 1200
        if nude == 1:
            bun "Wow, you're really bearing all, huh? Even I'm not quite that brave, hah!"
        elif lewdoutfit == 1:
            bun "You look super cute and sexy! I'd love to unwrap you myself if I could."

    if massage == 0:
        $ massage = 1
        show mce neutral with d
        "So, uhmm... Therif mase was this massage parlour hiring down the street, so I decided to go and check it out."
        "But as I step inside, I quickly realize that 'massage parlour' was just a front..."
        "The walls are lined with sexy pictures of women, and the waiting room has dirty magazines."
        "Yup, this is a brothel in disguise!"
        "A literal bunny girl is at the reception looking bored, although her expression shifts to bemusement when she notices me."
        show bunny with d:
            xpos 1200
        "H-Hang on! I recognize that girl, she's a professional hero. What's she doing in an establishment like this?"
        bun "We do serve women, although judging by your expression this wasn't quite what you expected."
        mc "Uhm, actually I saw that you were hiring..."
        bun "Ahh, and are you still interested?"
        if sd >= 60:
            show mce horny
            mc "Yeah, definitely."
            bun "Perfect! Well, don't sit around, I'll interview you."
        elif sd >= 30:
            show mce happy
            mc "That depends on what I'll have to do."
            bun "Well, I suppose that depends on how far you want to go. Customers usually pay for what they want before they begin, and we can assign them a girl that's willing to go that far."
            mc "That seems reasonable."
        elif True:
            show mce neutral
            mc "No, I don't think so."
            bun "Awhh, shame... You look like such a scumptious morsel."
        show mce happy with d
        mc "Uhmm... are you really 'that' pro hero?"
        bun "Sure am! My power is 'bunny', sooo, I'm always extremely horny."
        bun "When I decided to kick start a business to pay less tax, this was a natural extention of my abilities! Eh?"
        show mce laughing with d
        mc "I thought something like that would be more controversial!"
        bun "Huh? No way!"
        bun "Most of my fans were male anyway, and now they have the opportunity to fuck me! My ratings have been through the roof!"
        show mce happy with d
        "Wow... So this girl is not only selling herself for sex, but does so with complete pride and confidence."
        "She turned it into a business, so she could not only fuck for fun, but get paid doing it, and then pay less tax on what she earns!"
        "Is she someone to look up to?"
        "Or is that a fate I want to avoid?"
        play sound success
        $ sdgain = 1
        call sdgain from _call_sdgain_37
        "+[fsd] Sexual Desire"
    elif massage == 1:
        if massageroute1 == 0:
            jump massageroute1
        elif massageroute2 == 0:
            jump massageroute2
        elif massageroute3 == 0:
            jump massageroute3
        elif massageroute4 == 0:
            jump massageroute4
        elif massageroute5 == 0:
            jump massageroute5
        elif massageroute6 == 0:
            jump massageroute5

label massageroute6:
    pass

label massageroute1:
    bun "Have you finally decided to take my offer?"
    menu massagemenu1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Take interview (30 Sexual Desire, <70 Shame)" if True:
            if sd < 30 or shame > 70:
                "An interview to be a sex worker? I think that's going a little too far."
                jump massagemenu1
        "Leave" if True:
            if personality == 2 and sd > 30 and shame < 70:
                "(Always Horny) Leave? But this could be a great opportunity for me to get easy sex!"
                jump massagemenu1
            jump worldmap
    $ massageroute1 = 1
    bun "Perfect! I'm so excited to have a student sign up, you'll definitely attract some customers."
    mc "Uhhh, right!"
    if pregnancyshowing == 1:
        bun "Pregnant too, eh? Now that's going to be popular."
    "Another customer enters interrupting our 'interview'."
    show student4:
        xpos 200
    customer "Hey, just you two today?"
    bun "No actu-"
    customer "I'll have the bunny girl, full service."
    bun "Ah, can do!"
    customer "Here's the payment. I'll take a full hour slot, skip the massage."
    "$200?! That's quite a lot! Isn't it?"
    mc "S-Should I come back later?"
    bun "Naaahhh, don't worry about it! Call it 'on-the-job' training?"
    "Undressing, the bunny hero quickly gets into position for the customer."
    show bunnyspreadingassb
    show bunnyspreadingass 1
    with d
    mc "Huh? No massage at all?"
    bun "Oh please! You're so naive, darling."
    "The customer seems happy as he undoes his belt and gets into positon behind the incredibly sexy bunny girl."
    bun "Go as hard as you want, big boy, I'm all yours."
    "Mildly mortified, albeit curious, I take a seat adjacent to the act and watch as the customer slides his cock inside."
    play sound cum
    show bunnyspreadingass 2
    with d
    play ambience sex fadein 1.0
    mc "So... This isn't a massage parlour, just a brothel?"
    bun "Haaahh, fuck yeaahh... Wait, I mean, no! We do massages too, but the customer asked for the 'full service', which is specifically sex."
    mc "Ohh, so the customer comes in, says what he wants, and then he gets to choose a girl willing to do it?"
    bun "Yup! Oohhh, fuck... Y-You've got it, cutie!"
    mc "That means I'll be able to work here whenever, and I'll still get paid if no customer chooses me."
    bun "Ohh, god yes!"
    "Was she even responding to me? I'll take it as a yes. I awkwardly scratch my head as I watch her get pounded from a surprisingly good angle."
    "Is this actually turning me on? Oh my god, it is!"
    "Well, how could it not? The sex is so raw, so wet, and they're both really enjoying it."
    "Could I picture myself in that position? Maybe I could start with something a little slower and gradually build my way up."
    "I can tell the bunny girl is experienced, maybe a little too experienced. The way she rolls her hips, and tenses her muscles, she's getting 110%% out of both her and the customer."
    "And it doesn't take long for the bunny to start climaxing, I guess it doesn't take as long for her."
    play sound cum
    show bunnyspreadingass 3 with cum
    play sound cum
    show bunnyspreadingass 3 with cum
    "As her pussy squeezes and sucks the customer's throbbing cock, it soon coaxes an intense orgasm."
    play sound cum
    show bunnyspreadingass 3 with cum
    play sound cum
    show bunnyspreadingass 3 with cum
    "Copious amounts of cum shoot deep into her pussy and womb, filling her up to such a degree that some of it shoots out the sides as they continue to fuck at a reckless pace."
    stop ambience fadeout 1.0
    "They genuinely keep going until the man is almost entirely flacid and sensitive. The bunny hero squeezed every drop of pleasure out of that as possible, it's a wonder she's not paying him."
    play sound cum
    show bunnyspreadingass 4 with d
    bun "H-Hey, wait a second... Did you not wear a condom?"
    bun "Damnit... I was so focused on the interview that I totally forgot."
    show bunnyspreadingass 5 with d
    bun "*Siiighh* Oh well, there's probably no risk with just one creampie."
    customer "Sorry about that. Shall we go again in a few minutes?"
    bun "Absolutely! I'm already ready to go again."
    scene bg massage
    call clothes from _call_clothes_10
    show mce neutral
    with d
    mc "I feel like I've been forgotten about."
    show bunny with d:
        xpos 1200
    bun "Ah, sorry about that. I think you've had a pretty good introduction as to what you can expect here."
    show mce happy with d
    "But I have no idea how to massage... Oh well, I can probably still jack someone off."
    if sd < 60:
        mc "I'd like to 'start' slow if possible. No more than a massage with a happy ending."
    elif True:
        mc "I'm up for anything, even what you just did."
    bun "*Winks* I believe I can accomodate!"
    bun "With that being said, you handled the interview well, you've got the job!"
    show mce neutral with d
    "I did...?"
    show mce happy with d
    mc "Thank you!"
    bun "Next time you come here, I'll let you join the selection process for customers, and you can do whatever you feel comfortable with."
    mc "Okay, see you later, Bunny!"
    pause 0.5
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_38
    $ shameloss = 1
    call shameloss from _call_shameloss_46
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    $ massageroute1 = 1
    show bunnyspreadingassb
    show bunnyspreadingass 4
    with d
    bun "Now... Where were we? Ohh, customer!"
    scene bg black with d
    jump postworktrans


label massageroute2:
    bun "You're just in time!"
    mc "Well, this is the opening time, right?"
    bun "Yup, and we just got our first customer. All they want is a massage with an oral happy ending."
    bun "Wanna take it?"
    show mce neutral with d
    "Just like that? Don't I need training, or something?"
    menu mr2m:
        "Sexual Desire: [sd], Shame: [shame]."
        "Massage with Blowjob (40 Sexual Desire, <65 Shame)" if True:
            if sd < 40 or shame > 65:
                "Nah, let's go for an easier customer."
                jump mr2m
            scene bg black with d
            "I accept bunny's proposition and escort the customer to a private room where I can focus on them one on one."
            label massageoralservice:
                pass
            scene bg massage with d
            "It begins with a simple massage, but that's clearly not the focus as the nude customer is soon at full-mast."
            "Time to service him to the best of my ability."
            play music action
            play ambience blowjob
            show lyingblowjobb
            if tan == 1:
                show lyingblowjobb tan
            if piercingson == 1:
                show lyingblowjobpiercings
            if hair == 1:
                show lyingblowjobh black
            if hair == 2:
                show lyingblowjobh blonde
            show lyingblowjob 1
            if pregnancyshowing == 1:
                show lyingblowjobe milk
            with d
            "The customer lays back and I soon have his erection in my hands. Curiously, I wrap my lips around the tip and swirl my toungue around the glans."
            mc "Mmphh... Ish this good? You're so big... *Giggle*"
            "I take a hand and begin to jerk it up and down, mixing that with my tongue is sure to make him feel good."
            "Keeping an eye on his reactions, I focus on the aspects of the blowjob he enjoys most and it doesn't take long for him to really melt with the pleasure."
            mc "Ooohhh... Are you getting close for me? *Slurp, lick*"
            "Speeding up, I keep up my handjob and tongue motions until I can feel his cock swell up."
            mc "Mmm, cum for me! *Lick, suck*"
            play sound cum
            show lyingblowjob 2 with cum
            play sound cum
            show lyingblowjob 2 with cum
            "His entire body visibly tenses for a moment before a surge of hot cum erupts into my mouth."
            play sound cum
            show lyingblowjob 2 with cum
            play sound cum
            show lyingblowjob 2 with cum
            stop ambience fadeout 3.0
            "Several loads hit the back of my throat which I graciously swallow."
            "It didn't taste great, but damn was it arousing; my pussy is soaked."
            "I spend the next few moments lazily cleaning his cock with my tongue before it becomes fully unerect."
            scene bg massage with d
            call clothes from _call_clothes_11
            show mce happy
            if nude == 1 or lewdoutfit == 1:
                show mce horny
            show mce laughing
            with d
            if massageroute2 == 0:
                "It feels empowering pleasuring a man like this, I have all the control in the world. But I must admit, it does feel different servicing a customer and getting paid for it."
                show mce happy
                with d
                "In any other situation I'd perhaps have my fingers betweem my legs, rubbing lustfully, but it'd feel wrong to derive too much sexual satisfaction from this."
                "Then again, doesn't Bunny enjoy her work? Maybe I'm just not being open minded enough."
            play sound success
            $ blowjobs += 1
            $ sdgain = 1
            call sdgain from _call_sdgain_69
            $ shameloss = 1
            call shameloss from _call_shameloss_47
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            scene bg massage with d
            call clothes from _call_clothes_12
            show mce happy
            if nude == 1 or lewdoutfit == 1:
                show mce horny
            show mce happy
            with d
            show bunny with d:
                xpos 1200
            "With the customer serviced, I return to the main room and get my pay."
            play sound success
            $ moneygain = 50
            call moneygain from _call_moneygain_40
            "(+$[fmoney])"
            if massageroute2 == 0:
                $ massageroute2 = 1
                mc "Niiice!"
                bun "Good pay for a good job! This place isn't really for profit, so I only take a 30%% cut from you."
                mc "Thank you, Bunny! Money is my goal, so that means a lot."
                bun "Hey, if you're brave, you could earn some big bucks by offering some of the most 'advanced' services here. Think it through!"
                show mce horny with d
                "I just might..."
            jump postworktrans
        "Service an easier customer" if True:
            if personality == 2 and sd > 40 and shame < 65:
                "(Always Horny) I should really take that customer... I'll regret it later if I don't."
                jump mr2m
            show mce happy with d
            mc "Got anything lighter?"
            bun "Hmm... Are you okay with a customer that just wants a massage?"
            mc "Yeah, I can do that."
            scene bg black with d
            "I wait for a customer, and end up servicing another girl, and a guy a little later."
            play sound success
            $ moneygain = 50
            call moneygain from _call_moneygain_41
            "I get paid $[fmoney] for my work."
            jump postworktrans
        "Completely back out and leave" if True:
            if personality == 2 and sd > 40 and shame < 65:
                "(Always Horny) I should really take that customer... I'll regret it later if I don't."
                jump mr2m
            show mce neutral with d
            mc "Ahhhaah, you're gonna hate me but, I think I'm just gonna chicken out."
            bun "Pfft, that's alright. That's just more fun for me, I guess!"
            bun "Do come back sometime though, having you here will draw customers in."
            mc "I'll try, Bunny."
            jump worldmap


label massageroute3:
    bun "Okay, so you know what I said last time about offering a pricier service, have you thought much about it?"
    "Hmm... The next option above blowjob is straight up vaginal..."
    "That's a big jump."
    "I can't pretend I'm just a fancy massage therapist if I start fucking customers..."
    if virgin == 0:
        mc "But I'm a virgin."
        bun "Eh?! You're a virgin sex worker?"
        bun "Hmm... Have you considered selling your virginity?"
        menu mr3mm:
            "Sure..? (70 Sexual Desire, <50 Shame)" if True:
                if sd < 50 or shame > 60:
                    "Nooo, no no no no..."
                    jump mr3mm
                bun "Ohoho, hold on then, let me see if I can find the right customer for you..."
                bun "Trust me, this is going to pay a lot."
                mc "Huh?"
                "Just what did I sign myself up to?"
            "I prefer anal. (Anal Queen)" if qanalqueen == 1:
                bun "Ahaha! We actually charge even more for that, and not a lot of our girls are comfortable doing that."
                bun "Perfect!"
                "Woops, by admitting that, just what did I get myself into?"
            "No way!" if True:
                bun "Awhh, that's fine too. You can just do what you're comfortable with."
    menu mr3m:
        "Sexual Desire: [sd], Shame: [shame]."
        "Can I do anal?" if qanalqueen == 1:
            $ massageroute3 = 1
            bun "Hmm, let me check if we have any customers for you... Ah-ha!"
            jump massageroute4aq
        "Vaginal Service (70 Sexual Desire, <50 Shame)" if True:
            if sd < 70 or shame > 60:
                "I'm not ready for that kind of leap quite yet."
                jump mr3m
            bun "Perfect, perfect..."
            if virgin == 0:
                bun "And since you're a virgin, I managed to convince the client to pay double!"
                mc "And how much is that?"
                $ moneygain = 150
                call moneycalculate from _call_moneycalculate_13
                bun "An additional $[fmoney] to your $[fmoney]!"
                "I'm initially bewildered at a large, promising sum of money."
                "But then, I feel this unease in my gut. Is $[fmoney] really the price of my virginity?"
                "That's a piece of myself I'll never get back, and... I suppose it's already too late."
            label mvaginalservice:
                pass
            scene bg black with d
            "The client walks up and I escort him to a private massage room."
            scene bg massage with d
            play music action
            scene missionarysexb
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
            show missionarysex 1
            with d
            $ condomon = 1
            "We don't even pretend to have the pretense of a massage, as the customer suggests I immediately take off my clothing and lay on the table instead."
            "I use a female condom, as per the parlour's rules, then sit comfortably on the massage 'bed' with my head rested in the pillow."
            "Seems like a good course of action, the faster I get this over with, the less time I have to work for the pay! Now that's efficient."
            "And I know he probably only had one load in the tank."
            "On my back, I spread my legs out and beckon for him to take me. My lustful pussy is on full display, sheening slightly from a wetness."
            "As he pushes the tip inside me, he pushes forward and slides deeper into my soaking wet insides."
            play sound cum
            show missionarysex 2
            with d
            if virgin == 0:
                "And just like that, the customer gets what he paid for as he takes my virginity."
            mc "Ahhh, you're quite big! Go steady at first."
            play ambience sex fadein 3.0
            "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
            "These deep thrusts drive me wild as they grind against sensitive erogenous zones deep inside of me."
            "Making me feel even better, he starts to thrust faster while reaching down to rub my clit."
            "Even as the customer, he generously treats me as a lover, giving me as much pleasure as possible."
            "The pleasure overwhelmed me, turning my mind blank as my body trembled towards a potent orgasm."
            mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
            play sound cum
            show missionarysex 3
            if pregnancyshowing == 1 and tan == 0:
                show missionarysexa pregnant2
            with cum
            "I tightly grip the bedsheets as I climax, my pussy tightening around the customer's throbbing cock."
            "And he only speeds up, motivated by my climax, he pushes towards his own."
            play sound cum
            show missionarysex 4 with cum
            play sound cum
            show missionarysex 4 with cum
            "His tight cock explodes a hot load deep into my pussy as he ravishes me"
            play sound cum
            show missionarysex 4 with cum
            play sound cum
            show missionarysex 4 with cum
            "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
            play sound cum
            show missionarysex 5 with d
            stop ambience fadeout 3.0
            "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my pelvis and thighs."
            if condomon == 1 and pregnancyshowing == 0:
                "But thanks to the condom, I don't need to worry about getting pregnant."
            elif True:
                call pregnancyroll from _call_pregnancyroll_6
            if virgin == 0:
                "For my first time, that wasn't bad at all! The customer seemed to appreciate my situation and he put a lot of effort into pleasing me."
            scene bg black with d
            "Afterwards, we clean up and I return to the foyer."
            scene bg massage
            call clothes from _call_clothes_13
            show mce happy
            if nude == 1 or lewdoutfit == 1:
                show mce horny
            show mce happy
            show bunny:
                xpos 1200
            with d
            if massageroute3 == 1:
                return
            elif True:
                $ massageroute3 = 1
            bun "Excellent work! He was really impressed with you."
            show mce laughing with d
            mc "Eheh, I barely did anything..."
            bun "It's how you carry yourself, it's almost entirely attitude, and I know you've got potential."
            show mce neutral with d
            mc "I-I do?"
            bun "Mhm, I see it in your eyes. You're a natural!"
            show mce happy2 with d
            "I don't really know what I did. I honestly don't even know the difference between being a good sex worker or not, but I guess I'll listen to Bunny."
            if virgin == 0:
                $ virgin = 1
                $ moneygain = 300
                call moneygain from _call_moneygain_42
                bun "And since it was your first time, here's the full $f[money]! Congratulations!"
                mc "Phew, that's a lot of money!"
                play sound success
                "(+$[fmoney])"
            elif True:
                $ moneygain = 150
                call moneygain from _call_moneygain_43
                bun "Congratulations on your first sexy service! Here's the full $[fmoney]!"
                mc "Phew, that's a lot of money!"
                play sound success
                "(+$[fmoney])"
            bun "Hehe, do come back!"
            label massageparlourscare:
                pass
            scene bg black with d
            stop music fadeout 3.0
            scene bg bedroomnight with d
            call clothespjs from _call_clothespjs_8
            show mce happy
            if nude == 1 or lewdoutfit == 1:
                show mce horny
            show mce neutral
            with d
            "After servicing that customer I return home. I can't get the images of what happened out of my head."
            "Working there pays really well..."
            "But, god... It didn't even occur to me that I've literally become a prostiute."
            "It happened so fast, and I barely took the time to realize how far I'd gone for money."
            "At first it was just using my sexuality for small sums of cash, but now I'm taking $100s for sex."
            "And the thing worrying me most is that... I really enjoyed it."
            "Bunny was right, I enjoyed fucking that customer. I enjoyed the thick feeling of his cock."
            "And I came so easily, and so much harder than if I were masturbating alone..."
            "So why am I so conflicted? Am I just suffering from the social stigma of prostitution?"
            "Is my pride as an individual hurt for doing such things for money?"
            "I just don't know anymore."
            "I thought I knew what kind of person I was, a happy-go-lucky, innocent and bubbily girl."
            "But... I'm changing so fast that it's scaring me."
            "It almost feels like today was a crossroad, and I started walking down a scary new path."
            if persistent.massagescare == False:
                $ persistent.massagescare = True
                play sound success2
                show losingit2:
                show losingit:
                    xalign 0.5 ypos 0
                with d
                pause 0.5
                play music losing
                show losingit:
                    linear 12.0 xalign 0.5 ypos 500
                show losingit3 with d7
            elif True:
                mc "What? Did you see something weird?"
            $ status += 1
            $ sdgain = 1
            call sdgain from _call_sdgain_70
            $ shameloss = 1
            call shameloss from _call_shameloss_48
            $ vaginalsexes += 1
            stop music
            $ dream = 1
            jump postworktrans
        "Oral Service (Pays $50)" if True:
            mc "I'll stick with what I know for now."
            bunny "Can't argue with that! I'll let you take the next oral customer."
            scene bg black with d
            "A customer that wants the oral service eventually arrives, and I take him to a private room."
            call massageoralservice from _call_massageoralservice
            mc "Thank you, Bunny"
            bun "Hey, why thank me? You're doing a great job out there. Keep it up!"
            scene bg black with d
            jump postworktrans
        "Massage Service (Pays $30)" if True:
            mc "Let's go for something non-sexual today."
            bun "Be my guest!"
            "Ahh, Bunny is so understanding."
            scene bg black with d
            "I wait for a customer, and end up servicing another girl, and a guy a little later."
            play sound success
            $ moneygain = 30
            call moneygain from _call_moneygain_44
            "I get paid $[fmoney] for my work."
            jump postworktrans
        "Go Home" if True:
            jump worldmap
label massageroute4:
    bun "You're just the girl I was hoping to see!"
    mc "Hello, Bunny!"
    label massageroute4aq:
        pass
    bun "I have a customer coming in later that wants an anal service. After your fantastic job last time, I was wondering if you wanted to take this one?"
    show mce neutral with d
    if event2complete == 1:
        mc "Hmm... I have had anal sex before, but..."
    elif True:
        mc "I don't have much experience with my uhm, butt..."
    bun "I see, so you're not quite confident you'll be able to service the customer?"
    show mce laughing with d
    mc "Well, it's kind of a scary thing!"
    bun "Okay, then... How about you watch me service this customer, and I'll show you how easy it can be!"
    show mce happy with d
    mc "Uuuhhhmmmm... Sure?"
    "Bunny and I wait for the customer and we all move into a private room when he arrives."
    play music action fadein 3.0
    scene bg massage with d
    show bunnystandingbendingb
    show bunnystandingbending 1
    with d
    "Turning her head upsidedown, she makes eye contract as she exposes her rear to the customer."
    bun "Alright, lad! Condom on, lube up, and ravish me!"
    "This is totally lewd! I hope I don't develop any voyeuristic tendencies watching Bunny fuck customers."
    play sound cum
    show bunnystandingbending a2
    with d
    play ambience sex fadein 3.0
    "The lubrication helps a lot as the customer presses the tip of their cock against Bunny's pucker. It slowly loosens and he edges himself inside."
    bun "Mmpphhh, mmmm... I'm a complete butt slut, always ready for a good pounding thanks to my high fibre diet and a lot of water!"
    "Fiber hm? Is that the secret to being ready? I best take some mental notes."
    "Bunny's ass is clearly very tight around the customer's shaft. He can only fuck her gently as she gradually loosens and adjusts to the throbbing cock."
    bun "At first it's all about relaxing your muscles while maintaining stable breathing."
    "It's quite an intoxicating watch. I'd be lying if I said I wasn't getting slightly aroused."
    "Her ass finally starts to loosen up, and the customer begins to fuck her at a good pace. The body language from Bunny exudes pleasure."
    bun "If you get it right, it shouldn't hurt at all. Mmmm..."
    "She makes it look amazing. Her ass definitely seems tighter than her pussy too, with a lot of the tightness concentrated at the sphincter."
    "Bunny isn't one to just take it however, as she begins to rock her hips back and forth. Her strength and form soon overpowering even the customer that you'd otherwise assume is at an advantageous position."
    "Her ass slides up and down the cock, going as hard and fast as she can take it."
    "At this rate, they'll both come in no time at all."
    "She bounces on the cock as the customer merely stands in place at awe. He even gives me a knowing wink."
    customer "This is why I love it 'ere!"
    "The customer can't hold back much longer, his cock swells up as he reaches his limit."
    play sound cum
    show bunnystandingbending a3 with cum
    play sound cum
    show bunnystandingbending a3 with cum
    "Both of them experience powerful orgasms, as evident by their body language. Multiple loads are blown into Bunny's ass, all being caught in the condom, but some of it splashing out wildly."
    play sound cum
    show bunnystandingbending a3 with cum
    play sound cum
    show bunnystandingbending a3 with cum
    "They both go out at, Bunny in typical fashion milks as much as she can out of the customer while remaining in total control."
    stop ambience fadeout 3.0
    "Eventually as the intensity of the rutting wears down, the guy pulls out."
    play sound cum
    show bunnystandingbending 4 with d
    bun "Aaahhh, anal feels amazing. Why constrain your sexlife to just one hole? Hehe."
    bun "You should practice, [mc]!"
    mc "I-I might!"
    $ massageroute4 = 1
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_71
    $ shameloss = 1
    call shameloss from _call_shameloss_49
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    scene bg black with d
    pause 0.3
    scene bg massage with d
    show lyingblowjobb
    show lyingblowjob 1
    if pregnancyshowing == 1:
        show lyingblowjobe milk
    with d
    "We only get easy customers today, my shift comprises of a blowjob and a handjob."
    scene bg massage
    call clothes from _call_clothes_14
    show mce happy
    if nude == 1 or lewdoutfit == 1:
        show mce horny
    show mce happy
    with d
    show bunny with d:
        xpos 1200
    play sound success
    $ moneygain = 80
    call moneygain from _call_moneygain_45
    "Afterwards I get paid $[fmoney]."
    jump postworktrans


label massageroute5:
    bun "We got a fair few customers booked in today, take your pick."
    mc "Thanks, Bun!"
    menu mr5m:
        "Anal" if massageroute5 == 1:
            jump massagerouteanal
        "Anal (70 Sexual Desire, <50 Shame)" if qanalqueen == 1 and massageroute5 == 0:
            jump massagerouteanal
        "Anal (80 Sexual Desire, <40 Shame)" if qanalqueen == 0 and massageroute5 == 0:
            label massagerouteanal:
                pass
            $ massageroute5 = 1
            mc "Okay, I'm ready to take an anal customer."
            bun "Excellent! That'll take a load off me having to take all the anal customers."
            scene bg black with d
            scene bg massage2 with d
            "I wait a while for an anal customer, and even end up giving someone else a massage in the meantime. But soon enough, my customer arrives."
            play music action
            show legs-upsexb
            if tan == 1:
                show legs-upsexbtan
            if hair == 1:
                show legs-upsexh black
            if hair == 2:
                show legs-upsexh blonde
            show legs-upsex 1
            with d
            "I lead him into the passage parlour with confidence, and once we're both ready, I left my legs up and present him with my cute butt."
            "As he watches, stroking his cock to erection, I take some lube and gently apply it to my pucker."
            mc "Mmphh, I'm ready for that fat cock now... Do go easy on me, hehe."
            "With my legs held up high, I teasingly wiggle my butt and spread my cheeks."
            play sound cum
            play ambience sex fadein 2.0
            show legs-upsex a2 with d
            "He taps the tip of his cock against my anus a few times before lining it up properly and pushing in deep."
            "It takes a while for my ass to adjust, but the lubrication in combination with Bunny's advice to relax enable me to take it with ease."
            "Not only that, but it starts to feel good!"
            "Once I'm ready, he begins slowly sliding his cock almost all the way out before sinking back in."
            mc "Ohhh, yeaahh... Ahhh, you're really filling me up!"
            "I love the way it grinds against all the sensitive spots deep inside. With my legs held together like this, it feels tighter and totally amazing for me."
            mc "Aahhh, mmmpphhmmm... Your cock feels great!"
            "Even as the customer, he starts to thrust faster while reaching down to rub my clit, giving me as much pleasure as possible."
            "And that pleasure is enough to bring about my orgasm rather quickly, causing my entire body to tremble."
            mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
            play sound cum
            show legs-upsex a2
            with cum
            "I tightly grip my ass, squeezing around my partner's tense cock as I climax."
            "And as my ass squeezees and milks his cock, he only speeds up. Motivated by my climax, he pushes towards his own."
            play sound cum
            show legs-upsex a3 with cum
            play sound cum
            show legs-upsex a3 with cum
            "His tight cock explodes a hot load deep into my ass as he ravishes me"
            play sound cum
            show legs-upsex a3 with cum
            play sound cum
            show legs-upsex a3 with cum
            "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
            play sound cum
            show legs-upsex 4 with d
            stop ambience fadeout 3.0
            "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked butt and drip down."
            scene bg black with d
            "Afterwards, we clean up and my client leaves."
            play sound success
            $ moneygain = 200
            call moneygain from _call_moneygain_46
            $ sdgain = 1
            call sdgain from _call_sdgain_72
            $ shameloss = 1
            call shameloss from _call_shameloss_50
            "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
            "Phew! That's a lot of money! Being a prostitute sure pays well..."
            $ status += 1
            $ analsexes += 1
            scene bg massage
            call clothes from _call_clothes_15
            show mce happy
            if nude == 1 or lewdoutfit == 1:
                show mce horny
            show bunny with d:
                xpos 1200
            mc "All done! Thanks, Bunny"
            bun "Hey, why thank me? You're doing a great job out there. Keep it up!"
            if persistent.massagescare == False:
                jump massageparlourscare
            scene bg black with d
            "I finish up and return home."
            jump postworktrans
        "Vaginal" if True:
            mc "Let's have some fun today!"
            bun "You got it! Your next customer will be here in 20 minutes."
            scene bg black with d
            "The customer eventually arrives."
            call mvaginalservice from _call_mvaginalservice
            mc "All done! Thanks, Bunny"
            bun "Hey, why thank me? You're doing a great job out there. Keep it up!"
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_73
            $ shameloss = 1
            call shameloss from _call_shameloss_51
            $ moneygain = 150
            call moneygain from _call_moneygain_47
            "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
            $ status += 1
            call sdgain from _call_sdgain_42
            $ shame -= 1
            $ vaginalsexes += 1
            $ virgin = 1
            scene bg black with d
            jump postworktrans
        "Oral" if True:
            mc "I'll stick with what I know for now."
            bunny "Can't argue with that! I'll let you take the next oral customer."
            scene bg black with d
            "A customer that wants the oral service eventually arrives, and I take him to a private room."
            call massageoralservice from _call_massageoralservice_1
            mc "All done! Thanks, Bunny"
            bun "Hey, why thank me? You're doing a great job out there. Keep it up!"
            scene bg black with d
            "I finish up and return home."
            jump postworktrans
        "Non-Sexual Massage" if True:
            mc "Let's go for something non-sexual today."
            bun "Someone's gotta do 'em!"
            "Ahh, Bunny is so understanding."
            scene bg black with d
            "I wait for a customer, and end up servicing another girl, and a guy a little later."
            play sound success
            $ moneygain = 30
            call moneygain from _call_moneygain_48
            "I get paid $[fmoney] for my work."
            jump postworktrans
        "Leave" if True:
            jump worldmap

jump prebedroom

init:
    $ massageroute1 = 0
    $ massageroute2 = 0
    $ massageroute3 = 0
    $ massageroute4 = 0
    $ massageroute5 = 0
    $ massageroute6 = 0
    $ massageroute7 = 0
    $ massageroute8 = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

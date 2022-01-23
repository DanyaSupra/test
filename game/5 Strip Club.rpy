label stripclub:
    if stripclubunlocked == 0:
        "Unlock this location by having >30 Sexual Desire."
        if sd >= 30:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump stripclubunlock
                "Back" if True:
                    pass
        jump postworldmap
    if morning == 1:
        "The Strip Club isn't open right now."
        jump postworldmap
    label stripclub2:
        pass
    play music lonelyfans
    scene bg stripclub
    call clothes from _call_clothes_26
    show mce happy
    with d
    if stripclubvisited == 0:
        $ stripclubvisited = 1
        "Yup, I was right, this is definitely a strip club. Despite that, it said 'gentleman's club' on a sign outside."
        show mce laughing with d
        "Well, that's not very fair! What if I wanted to watch cute girls dancing too."
        if sd < 30:
            "Although to be honest, I do think this kind of environment is a little much for me, especially alone."
        show twilight:
            xpos 1200
        with d
        show mce neutral with d
        "Ah!? Why is one of my professors working here?! She's wearing a bunny suit!"
        twilight "My, you truly must be lost to have stumbled here. Be sure to call me by my stripper name, 'Twilight' while you're here, okay?"
        mc "Y-Yes, Miss!"
        twilight "No, not 'Miss', 'Twilight'."
        mc "Right! Twilight!"
        show mce horny with d
        mc "... Can I, like, even get a dance from you?"
        twilight "I'm just another girl working here, and you get a dance from any one of us."
        mc "I seeeee, hehehe."
        hide twilight with d
        "Wooow! I knew teachers didn't get paid enough, but having to work at a place like this too? Hah! It's a little sad, but also a little funny."
        "Hmm, should I work here too? I mean, it must pay well."
        if shame > 70:
            "Meh, what am I thinking? This isn't the kind of environment I could be in. Then again, Twilight is here... How bad could it be?"
        elif True:
            "I think I could do it! I just need a bunny suit, or something."
        play sound success
        $ shameloss = 1
        call shameloss from _call_shameloss_65
        "(-[fshame] Shame)"
    elif True:

        pass
    menu sbm1:
        "Sexual Desire: [sd], Shame: [shame], Money: $[money]."
        "Get a Dance (-$40)" if True:
            if money < 40:
                "I don't have enough money for that."
                jump sbm1
            $ money -= 40
            jump twilightdance
        "Work Here (Bunny Suit, 20 Sexual Desire, <80 Shame)" if True:
            if sd < 20 or shame > 80:
                "Working in a strip club? I don't think so"
                jump sbm1
            elif bs == 0:
                "I don't have the bunny suit everyone is wearing here, I should buy one."
                jump sbm1
            if stripclubwork1intro == 0:
                jump stripclubworkintro
            jump stripclubwork
        "Leave" if True:
            jump worldmap



label stripclubwork:
    play sound equip
    scene bg black with d
    scene bg stripclub
    call clothesbunnysuit from _call_clothesbunnysuit
    show mce happy
    with d
    "How should I spend my shift?"
    menu scw1m2:
        "Customer Service IV (Anal Bukkake Gangbang)" if stripclubwork3 == 1:
            scene bg booth with d
            call clothesbunnysuit from _call_clothesbunnysuit_1
            show mce happy
            with d
            "During my shift, I find myself in a private room with my two favourite regulars."
            "Wait… How did I get here? I don’t… remembering come in…"
            "Oh well, that doesn’t matter."
            scene bg booth
            show student1:
                xpos 0
            show student7:
                xpos 250
            show student3:
                xpos 550
            show student4:
                xpos 800
            show student5:
                xpos 1200
            with d
            mc "There’s a lot of people here today!"
            scene bg booth with d
            call clothesbunnysuit from _call_clothesbunnysuit_2
            show mce happy
            show student5:
                xpos 1200
            with d
            boss "Welcome, [mc]! The whole gang is here today."
            boss "And you will serve and each and everyone one of us, you’re our bitch in heat, don’t forget that."
            mc "Bitch in heat…"
            show mce horny with d
            call hypnosiseffect from _call_hypnosiseffect
            "Suddenly, a strong pang on desire rushes over my body, and my loins start to heat up."
            "That’s right, I’m a horny bitch… I can’t wait to fuck these men."
            if stripclubwork4 == 0:
                "But… something doesn’t quite feel right…"
                "I must be overthinking this, right? I mean… I work here, I get paid, I’m trying to pay off my tuition."
                "Of course, I’m going to service these men for money."
            mc "Mhm… Okay!"
            if stripclubwork4 == 0:
                customer "Hehe, she’s completely hypnotised. I bet we won’t even have to pay her."
                show mce laughing with d
                mc "Nope, each and every one has to pay up!"
                customer "Wah?!"
                boss "Heh, she may be so far hypnotised that she’ll do anything we ask, but her burning desire for money is so strong, not even our advanced techniques could break that."
                boss "This was never about the money, it was about breaking in the new girl and wrapping her around my finger. If it takes a little money to do that, it’s no problem at all. Of course, we’ll pay"
                show mce happy2 with d
                mc "Excellent! Then by all means, I'm yours!"
            play music action fadein 2.0
            show analbukkakeb
            if tan == 1:
                show analbukkakebtan
                if pregnancyshowing == 1:
                    show analbukkakebtanp
            if piercingson == 1:
                show analbukkakepiercings
            if hair == 1:
                show analbukkakeh black
            if hair == 2:
                show analbukkakeh blonde
            if pregnancyshowing == 0:
                show analbukkakee bunny
            elif True:
                show analbukkakee bunnypregnant
            show analbukkake 1
            with d
            "Face up, I lay myself down in front of the group of customers, parting the crotch of my bunny suit and spreading my pussy with two fingers."
            "I thrust my waist forward and flaunt my pussy, playing with myself."
            mc "Who’s first, then? I’m all yours!"
            "Taking my example, the men of the room undress and begin to masturbate in front of me."
            "The lecherous masturbatory sounds of my wet pussy are like a sweet song to the swelling erections of my customers."
            mc "I won’t be satisfied until I’ve emptied every single one of your balls."
            "As the boss approaches first, his giant cock in hand, I eagerly spread my pussy as invitingly as possible."
            play sound cum
            show analbukkake 2 with d
            play sound2 foreplay1 fadein 3.0
            "However, he takes interest in my twitching anus instead. In too much of a hypnotic trance to resist, he plunges his cock straight into my ass."
            mc "Uuoohhhh! S-So thick! Aaahhh…"
            "Thrusting all of the way inside, my pucker constricts around his swelling member like a ring. I shudder with immense pleasure as a result."
            play ambience sex fadein 3.0
            "Wasting no time, he begins thrusting back and forth, and I can’t help but rock my hips back and forth against him too."
            mc "Aaahhh, haaahhh… Come on boys, you’re not just going to watch with your dicks in hand, are you?"
            show analbukkake 3 with d
            "Approaching around me, the men began to jack off over me. Their eyes hungrily scanning my body from pussy to breasts."
            "Although as my gooey pussy is spread open, they gawk in awe, and seemingly get the idea that jerking off into that is what they want to do as their hands accelerate."
            show analbukkake 4 with d
            mc "Hehe, I bet you want to cum inside my pussy, don’t you? Have some patience, boys… But if you’re so desperate, you can cum on me, hehe…"
            "The men were so absorbed in their movements. While pounded in the ass by one, the others were jacking off as if preparing a long-ranged creampie."
            mc "Try and get as much into my pussy as you can, okay?"
            "Not too much longer, the two masturbating men were steadily brought to their limits!"
            play sound cum
            show analbukkake 5 with cum
            play sound cum
            show analbukkake 5 with cum
            "A torrent of hot semen splatters against my pussy and pelvis."
            play sound cum
            show analbukkake 5 with cum
            play sound cum
            show analbukkake 5 with cum
            mc "Aaahh, so much! Mmphhh… Cover me! Ahhh!"
            "A ton of it managed to seep into my spread pussy, I shudder as I feel it drip down and mix with my own juice."
            "And as I indulge in the pleasure, I clamp down around the thrusting cock in my ass, and soon he too is pushed over the edge."
            play sound cum
            show analbukkake 6 with cum
            play sound cum
            show analbukkake 6 with cum
            mc "Mmphh, mooooree, more! Fill me up!"
            play sound cum
            show analbukkake 6 with cum
            play sound cum
            show analbukkake 6 with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 3.0
            "My ass is pounded and pumped with thicker cum, some of it dripping and spurting out."
            mc "Aahh, amazing… I feel like I’m in some kind of cummy heaven."
            play sound cum
            show analbukkake 7 with d
            "The three men pull out and away. panting for air as they catch their breath."
            customer "Jesus, boss, where’d you find a girl like this?"
            customer "I can’t tell who is more hypnotised, me or her. Just look at her!"
            boss "Ayy, she’s the best yet."
            "I lay my head back and just enjoy the feeling of cum trickling down my body, and dripping onto the floor."
            mc "Alright… Who’s next?"
            stop music fadeout 3.0
            scene bg black with d
            "I diligently, and obediently serve every single man for the duration they have the room rented."
            "When all is said and done. I’m so excessively covered and filled with cum that I have to take one of the showers on premise because no amount of tissue could help me."
            "Collecting my money just before I leave, I head out with a spring in my step."
            play sound success
            $ moneygain = 300
            call moneygain from _call_moneygain_55
            "(+$[fmoney])"
            scene bg booth
            call clothesbunnysuit from _call_clothesbunnysuit_3
            show mce laughing
            with d

            call hypnosiseffect from _call_hypnosiseffect_1
            "I love working here."
            call hypnosiseffect from _call_hypnosiseffect_2
            show mce horny with d
            "I should come here to serve these men every day…"
            call hypnosiseffect from _call_hypnosiseffect_3
            "After all, I’m their property. Their bitch."
            "(Perk unlocked! Fully Hypnotised. You can no longer refuse serving customers at the Strip Club.)"
            play sound success
            $ stripclubwork4 = 1
            $ hypnotised += 1000
            $ groupsexes += 1
            $ analsexes += 3
            $ vaginalsexes += 4
            $ blowjobs += 2
            $ sdgain = 1
            $ shameloss = 1
            $ status += 3
            call sdgain from _call_sdgain_103
            call shameloss from _call_shameloss_98
            "(+[fsd] Sexual Desire, -[fshame] Shame! Sex Statistics: +3 Anal Sexes, +4 Vaginal Sexes, +2 Blowjobs)"
            jump postworktrans
        "Customer Service III (Double Penetration)" if stripclubwork2 == 1:
            "While working, a group of people approach me, one of which is the man that has hired my services before."
            show student7:
                xpos 30
            show student5:
                xpos 1200
            with d
            if sc3endured == 0:
                customer "This is the girl, boss."
            elif True:
                customer "There she is again."
            boss "Excellent, bunny. Come with us to a private room."
            show mce neutral with d
            mc "Eh?! O-Okay!"
            "Seemingly unable to refuse, I enter a private booth that has been rented out."
            scene bg stripclub
            if sc3endured == 0:
                show twilight
                with d
                twilight "*Sigh* There she goes… They always try this with the new bunnies."
            stop music fadeout 3.0
            scene bg black with d
            show bg booth
            call clothesbunnysuit from _call_clothesbunnysuit_4
            show mce happy
            show student7:
                xpos 30
            show student5:
                xpos 1200
            with d
            if stripclub2intro == 0:
                boss "Was she susceptible to your power? How deep is she?"
                customer "Could be a little deeper."
                show mce neutral with d
                mc "H-Hey, don’t talk about my pussy like that!"
                customer "Heh, let’s make her ours."
                mc "Uhhmm, what service did you want? I’m allowed to refuse, you know!"
                boss "Bwahaha, what a feisty one, we’ll see how long that lasts with my boosting power and your hypnosis power combined."
                customer "Ready when you are, I brought a pocket watch this time."
                boss "Hey, lady, can you check the time for me?"
                show mce laughing with d
                mc "I don’t have my phone on me, no pockets!"
                boss "Here, check this pocket watch."
                show mce neutral with d
                "In what I assume must be a joking manner, he takes out the watch and sways it back and forth. Forcing me to concentrate to try and catch the time."
                mc "Hey, stop… swinging it… come on… I can’t…"
                boss "I invite you to relax deeply, and as you look deeply into this watch… You’ll feel weary, heavy and tired."
                call hypnosiseffect from _call_hypnosiseffect_4
                mc "W-What are you saying?"
                boss "Learn to let go of all past obstacles, and all subconscious negativity. Drift away into a deep, relaxing sleep."
                call hypnosiseffect from _call_hypnosiseffect_5
                mc "S-Sleepy…"
                boss "And when I snap my fingers, you will become a subservient bunny for us. As intensely horny and open to sex as a bunny, and as subservient and loyal as a bitch in heat."
                mc "A bitch in heat…"
                boss "And… now! *Snap*"
                play music toko
                call hypnosiseffect from _call_hypnosiseffect_6
                show pink:
                    alpha 0.2
                show mce horny with d
                mc "H-Huh! S-Sorry, sir... Mphh... But your pocket watch appears to have broken, aahh, the hands aren’t even moving."
                boss "Heh, I know."
                customer "Hey, bunny. Will you service us?"
                mc "Mhm, of course. That’s my job. I’m happy to do any of the services listed from handjob, to oral to sex."
                boss "Good, she’s ready. Let’s see how you handle some double penetration, then."
                mc "Wait, that’s not one of the listed services."
                customer "Huh?!"
                boss "She’s not fully hypnotised yet?"
                "A little confused, I wait subserviently and patiently for my next order. Although I seem conflicted, somehow."
                mc "Uhm… Hang on, I need to think a second, I might have made a mistake."
            elif True:
                boss "Now, relax, bunny."
                mc "Ohh, okay? Don't you want a dance, or maybe something sexual?"
                boss "Indeed we do, but first, allow me to check the time."
                "Taking out a pocket watch like before, he playfully swings it back and forth causing me to giggle."
                call hypnosiseffect from _call_hypnosiseffect_7
                mc "Hehe, silly, your watch doesn't work, remember?"
                boss "Ohh it works just fine alright."
                customer "Her eyes are glazing over boss. Let's try asking again."
                boss "Indeed, are you ready to try double penetration?"
                show mce horny with d
                mc "Aaahh, I really want to do it, but..."
            $ stripclub2intro = 1
            $ sdreq = 100.0
            $ shamereq = 20.0
            $ hmult3= (hmult + hypnotised)/100
            $ hypnosd = int(sdreq / hmult3)
            $ hypnoshame = int(shamereq * hmult3)
            menu scr2:
                "Sexual Desire: [sd], Shame: [shame], [hypnotised]%% Hypnotised lowering requirement multiplicatively by [hypnotised]%%."
                "Double Penetration ([hypnosd] Sexual Desire, <[hypnoshame] Shame)" if True:
                    if hypnosd > sd or hypnoshame < shame:
                        "I can't do something like that for money..."
                        jump scr2
                    mc "Yeah… I’m wrong. By all means, serving you two for me is far more important than listening to any rules…"
                    mc "As long…"
                    customer "As long as what?"
                    mc "You both have to pay me, okay?"
                    customer "Wha?! I’ve never someone that deep ask to get paid before!"
                    boss "What an impressive desire for money she must have. You have a deal, bunny."
                    mc "*Pant* Excellent, then… Please enjoy me! I’m so horny right now I think I’m going to burst!"
                    mc "Just thinking about you two fucking me hard is driving me crazy."
                    boss "Kehe…"
                    scene bg black with d
                    pause 0.4
                    show standingdpb
                    if tan == 1:
                        show standingdpbtan
                    if pregnancyshowing == 1:
                        show standingdpe pregnant
                        if tan == 1:
                            show standingdpe tanpregnant
                    if hair == 1:
                        show standingdph black
                    if hair == 2:
                        show standingdph blonde
                    if piercingson == 1:
                        show standingdppiercings
                    if pregnancyshowing == 1:
                        show standingdpe bunnypregnant
                    elif True:
                        show standingdpe bunny
                    show standingdp 1
                    with d
                    play ambience doublepenetration fadein 2.0
                    play sound2 foreplay2 fadein 3.0
                    mc "Mphhh, aahh, ahhh! Aaahh! *Pant*"
                    customer "Ohh, her ass is so tight!"
                    boss "Not bad from this side either, her pussy is so wet."
                    mc "Hnngghh, please fuck me faster! Use me however you’d like, I’m just an object for your pleasure!"
                    "The room was filled with sticky, wet sounds as I was fucked deep and hard in both holes at once. The pleasure was euphoric."
                    "Even as a sex object sandwiched between two people, they were still my customers, and I was still a prostitute. With all my vigour and energy, I serviced them to the best ability. I don’t quite know why, but I want to satisfy them as much as I can!"
                    boss "You were right! This girl is perfect!"
                    customer "Haha, she’s so happy getting fucked, she can’t stop rocking her hips."
                    mc "Yesss, I love being filled up by cocks! I can’t get enough!"
                    mc "Oh god…. *Pant, pant* I-I’m gonna come already! S-So hard!"
                    "My entire body shakes and shudders as I’m utterly and endlessly pounded by the two men."
                    customer "Ohhh, yes! I’m gonna fill you right up!"
                    play sound cum
                    show standingdp 2 with cum
                    play sound cum
                    show standingdp 2 with cum
                    mc "Oohh, fuck! Mmmphhhh, mmmgghhh…"
                    play sound cum
                    show standingdp 2 with cum
                    play sound cum
                    show standingdp 2 with cum
                    boss "I’m coming too!"
                    play sound cum
                    show standingdp 2 with cum
                    play sound cum
                    show standingdp 2 with cum
                    stop ambience fadeout 2.0
                    stop sound2 fadeout 2.0
                    stop music fadeout 2.0
                    "Both my holes are pumped full of hot, sticky cum, all whilst I was overwhelmed with a full-body orgasm."
                    "It was so powerful that I almost blacked out, maybe I did."
                    mc "Ahh, haaahhh… *Pant, pant*"
                    "My body shivered as I gradually came down from my high. Cum freely dripping from my ass and pussy."
                    scene bg booth with d
                    call clothesbunnysuit from _call_clothesbunnysuit_5
                    show mce happy
                    show student7:
                        xpos 50
                    show student5:
                        xpos 1200
                    with d
                    mc "That was sooo good! I can’t believe how hard I came… Phew…"
                    customer "Hey, we still have plenty of time left with this room, we’ll fuck you a few more times yet."
                    show mce horny with d
                    mc "Yes! Fuck me as much as you want!"
                    scene bg black with d
                    show standingdpb
                    if tan == 1:
                        show standingdpbtan
                    if pregnancyshowing == 1:
                        show standingdpe pregnant
                        if tan == 1:
                            show standingdpe tanpregnant
                    if hair == 1:
                        show standingdph black
                    if hair == 2:
                        show standingdph blonde
                    if piercingson == 1:
                        show standingdppiercings
                    if pregnancyshowing == 1:
                        show standingdpe bunnypregnant
                    elif True:
                        show standingdpe bunny
                    show standingdp 1
                    with d
                    "After a small break, I was fucked over and over again for the full shift."
                    scene bg black with d
                    "And yet, afterwards, my recollection of the events is incredibly hazy."
                    play music rest
                    scene bg booth
                    call clothesbunnysuit from _call_clothesbunnysuit_6
                    show mce neutral
                    with d
                    mc "I, uhh… I served a customer, right?"
                    "I come to, alone and a little confused in the rented room. The customers just left."
                    "Damn, I feel really filled up with cum!"
                    "I collect the money that was left on the table and return home."
                    $ stripclubwork3 = 1
                    $ sdgain = 1
                    $ shameloss = 1
                    $ groupsexes += 1
                    $ vaginalsexes += 3
                    $ analsexes += 3
                    $ status += 3
                    $ moneygain = 200
                    play sound success
                    call moneygain from _call_moneygain_56
                    call sdgain from _call_sdgain_104
                    call shameloss from _call_shameloss_99
                    "(+$[fmoney])"
                    "(+[fsd] Sexual Desire, -[fshame] Shame!)"
                    "(Sexual Stats: +3 Vaginal Sex, +3 Anal Sex)"
                    jump postworktrans
                "Endure" if stripclubwork4 == 0:
                    if sc3endured == 0:
                        $ sc3endured = 1
                        mc "Yeah, I have it right. This place doesn’t even offer anal."
                        boss "Hmph… Fine, we’ll-"
                        scene bg black
                        scene bg booth
                        call clothesbunnysuit from _call_clothesbunnysuit_7
                        show mce happy
                        show student7:
                            xpos 0
                        show student5:
                            xpos 300
                        show twilight:
                            xpos 1200
                        show mce neutral
                        with d
                        twilight "Hey, pigs. Time’s up, you’re done with this room."
                        customer "That’s a lie! We have another hour!"
                        twilight "Get a refund, then. Out."
                        customer "Grr, you can’t do this."
                        boss "Calm down. You don’t mess with Twilight. Apologies, Madam, we’ll leave immediately."
                        hide student7
                        hide student5
                        with d
                        "What on earth is going on?"
                        twilight "You okay, honey?"
                        mc "Yeah, I feel great. Is something wrong?"
                        twilight "Hm… Are you okay with guys like that using you?"
                        mc "As long as they pay, I guess."
                        twilight "Hmph… I won’t protect you a second time, alright?"
                        mc "Ohh, uhm… Okay."
                        hide twilight with d
                        "Twilight leaves the room, and thus I’m all alone."
                    elif True:
                        mc "S-Sorry... You'll have to find someone else."
                        scene bg stripclub with d
                        "I leave the horny customers to their own devices and return to the main floor."
                    "And, I’m somewhat frustrated too. I am extremely, extremely horny right now! it’s like I’m in heat or something, damn!"
                    show bg stripclub with d
                    "Regardless, I do my best to continue my shift serving drinks. My bunny suit ends up really wet though!"
                    play sound success
                    $ sdgain = 1
                    $ moneygain = 30
                    call moneygain from _call_moneygain_57
                    call sdgain from _call_sdgain_105
                    "(+[fsd] Sexual Desire!)"
                    "I get paid a comfortable $[fmoney] for my work. It feels nice not having to rely on tips."
                    jump postworktrans
        "Customer Service II (Doggystyle)" if stripclubwork1 == 1:
            show student7 with d:
                xpos 50
            if stripclub2intro == 0:
                customer "Ah, hey! It’s me from last time."
                mc "Ohh, hey! What can I get you?"
                customer "I’ve been having a bit of a dilemma, and maybe you could help me. I need to know if you’re a virgin?"
                show mce neutral with d
                mc "Bit of a personal question… I don’t think I’ll answer that, sorry!"
                "The customer nonchalantly flicks a coin."
                call hypnosiseffect from _call_hypnosiseffect_8
                customer "Customer knows best, don’t they?"
                show mce happy with d
                mc "Uhmm… Huh? Of course I'll answer your question, it's no big deal."
                menu:
                    "Yeah (Truth)" if virgin == 0:
                        mc "Mhm, so you probably understand why I don't want to answer that in this kind of establishment."
                        customer "That's quite a valuable asset."
                    "Yeah (Lie)" if virgin == 1:
                        mc "Yep! I'm still as innocent as you implied when we last met."
                        customer "That's quite a valuable asset."
                    "Nope (Truth)" if virgin == 1:
                        mc "I'm not quite as innocent as you probably think."
                        customer "Experience can be invaluable when it comes to this career."
                    "Nope (Lie)" if virgin == 0:
                        mc "I'm working here, what do you think? Of course not."
                        customer "Experience can be invaluable when it comes to this career."
                customer "Dancers here set their own prices for sexual services, so, how much for you? Name a price?"
                "A strange feeling washes over me."
                "What am I worth, exactly?"
                "I can just say... anything? Am I being profiled, or something?"
                menu scw1m:
                    "Sexual Desire: [sd], Shame: [shame]"
                    "$500 (30 Sexual Desire, <70 Shame)" if True:
                        if sd < 30 or shame > 70:
                            "There's no amount that could make me do that!"
                            jump scw1m
                        $ moneygain = 500
                        mc "$500?"
                        customer "Steep... Guess you're just not interested in that kind of thing."
                    "$200 (40 Sexual Desire, <60 Shame)" if True:
                        if sd < 40 or shame > 60:
                            "That's not right..."
                            jump scw1m
                        $ moneygain = 205
                        mc "$200?"
                        customer "A little on the high end, but I can see that making sense."
                    "$150 (50 Sexual Desire, <50 Shame)" if True:
                        if sd < 50 or shame > 50:
                            "That's not right..."
                            jump scw1m
                        $ moneygain = 155
                        mc "$150?"
                        customer "Not bad, that's around the prices some ladies here offer..."
                    "$100 (60 Sexual Desire, <40 Shame)" if True:
                        if sd < 60 or shame > 40:
                            "That's not right..."
                            jump scw1m
                        $ moneygain = 105
                        mc "$100?"
                        customer "That's a good price."
                    "Free? (100 Sexual Desire)" if True:
                        if sd < 100:
                            "That's not right..."
                            jump scw1m
                        $ moneygain = 105
                        mc "Free?"
                        customer "You're that kind of person, huh?"
                    "Refuse to answer." if True:
                        show mce laughing with d
                        mc "Top secret!"
                        customer "Huh, really?"
                        $ moneygain = 205
                if moneygain < 500:
                    "The customer shows off a wad of cash from his wallet, counting it out to be around $[moneygain]."
                customer "Take me into a booth, let me fuck you, and this can be yours."
                show mce neutral with d
                "*Gulp*... Would Twilight get mad at me?"
                "Would {i}I{/i} be mad at me?"
                "I've already done the titjob, this isn't that much worse, is it?"
            elif True:
                customer "Ah, hey! It’s me from last time."
                mc "Ohh, hey! What can I get you?"
                customer "You've changed your mind on my offer?"
                show mce neutral with d
                mc "Uhh, nope, I don't think I have?"
                customer "No, I'm telling you that you have."
                call hypnosiseffect from _call_hypnosiseffect_9
                show mce happy with d
                mc "Oohhh, riiight... ... I have?"
                "Now I'm really confused... I'm pretty sure I changed my mind, but wasn't the offer to have sex with him?"
                $ moneygain = 100
            $ stripclub2intro = 1
            $ sdreq = 70.0
            $ shamereq = 30.0
            $ hmult3= (hmult + hypnotised)/100
            $ hypnosd = int(sdreq / hmult3)
            $ hypnoshame = int(shamereq * hmult3)
            menu scr1:
                "Sexual Desire: [sd], Shame: [shame], [hypnotised]%% Hypnotised lowering requirement multiplicatively by [hypnotised]%%"
                "Agree ([hypnosd] Sexual Desire, <[hypnoshame] Shame)" if True:
                    if hypnosd > sd or hypnoshame < shame:
                        "I can't do it..."
                        jump scr1
                    label privatedance1:
                        pass
                    play music action
                    scene bg black with d
                    "I slip away from the main floor, and into one of the booths at the back."
                    play sound equip
                    scene bg booth
                    show doggy2b
                    if tan == 1:
                        show doggy2tan
                        if pregnancyshowing == 1:
                            show doggy2tanp
                    if hair == 1:
                        show doggy2h black
                    if hair == 2:
                        show doggy2h blonde
                    show doggy2bunny
                    if pregnancyshowing == 1:
                        show doggy2e bunnypregnant
                    if piercingson == 1:
                        show doggy2piercings
                    show doggy2 1
                    with d
                    "Panting slightly, I wiggle my butt infront of the customer. I know I'm being used, but isn't getting paid what I came here for?"
                    $ condomon = 0
                    if condoms > 0 and pregnancyshowing == 0:
                        menu:
                            "Use a condom? Condoms: [condoms]. [fertilityrate]."
                            "Yeah." if True:
                                $ condomon = 1
                                $ condoms -= 1
                            "Fuck the rules! (Without protection!)" if True:
                                $ condomon = 0
                    if sd < 40:
                        "I know this is an extreme action, but... It's hard to turn away such a large sum of money. He's basically already paying off that bunny suit."
                    customer "Ahh, the new ones are always the best."
                    mc "What's that supposed to mean?!"
                    customer "You're cute and innocent, that's what I mean."
                    mc "This again? Oh well, it's a good thing, right?"
                    "He presses the tip of his cock against my wet labia, and it slowly stretches around him, accomodating his large cock as he slides it inside."
                    play sound cum
                    show doggy2 2
                    "My pussy is actually so wet it squelches as he pushes deep inside."
                    if virgin == 0:
                        "Taking my virginity, just like that!"
                        $ virgin = 1
                    play ambience sex
                    play sound2 foreplay1 fadein 2.0
                    mc "Aahhh you're so thick, and long too! I can barely take you all the way!"
                    "I don't know why I'm so horny. I suppose fucking a customer on one of my first shifts is the exact depraved thrill required to get me going."
                    "Sweat drips from my body as we begin to both rock our hips faster, even if the situation is weird, I can't help but smile with satisfaction as the immense amount of pleasure keeps me feeling good.."
                    play sound spank
                    "Oof! He spanked me! Ahh, and it actually felt really good! My pussy clenched tightly at the impact, and I could feel his cock throb within me."
                    customer "Did you like that, you little slut?"
                    mc "Mmphh, yess! Again!"
                    play sound spank
                    mc "Aaahhh, aaahh!"
                    "He begins to pound my pussy, slapping noises from our bodies connecting mix with my ragged pants and moans."
                    "His hands clamp aggressively around my hips, fingers sinking deeply into the flesh as he grabs me tightly."
                    "He's not just pumping me with his waist, he's holding my hips and pushing my ass back and forth, almost as if he's using my body to jerk himself off."
                    "My pussy is absolutely dripping, and the lewd wet noises don't stop as my body prepares itself to accept a thick load."
                    "*Slap, smack, slap* It doesn't seem like it'll take much longer, I can feel his cock swelling up inside of me!"
                    mc "Aaahhh, so good! -I'm going to cum!"
                    play sound cum
                    show doggy2 3 with cum
                    mc "Oohhhh, yesssss!!!"
                    play sound cum
                    show doggy2 3 with cum
                    stop ambience fadeout 1.0
                    stop sound2 fadeout 1.0
                    "My entire body spasms with orgasmic pleasure as a hot explosion of cum fills up my pussy, painting my insides white."
                    if condomon == 1 and pregnancyshowing == 0:
                        "But thanks to the condom, I don't need to worry about getting pregnant."
                    elif True:
                        call pregnancyroll from _call_pregnancyroll_9
                    show doggy2 4 with d
                    "Pulling out, an excessive amount drops out of my pussy, it's so messy!"
                    mc "*Pant, pant* That was really good, haaahh..."
                    customer "Here's what I owe you."
                    play sound success
                    $ moneygain += 10
                    call moneygain from _call_moneygain_36
                    "The customer leaves just as I count my money."
                    scene bg booth with d
                    call clothesbunnysuit from _call_clothesbunnysuit_8
                    show mce neutral
                    with d
                    "This initially gives me a fright, because I wanted to check if he had shorted me."
                    "Although to my surprise, the man had actually paid me extra than what we agreed on."
                    show mce happy2 with d
                    play sound success
                    "(+$[fmoney])"
                    show mce horny with d
                    if stripclubwork1 == 0:
                        $ stripclubwork1 = 1
                        "Siigghhh.... As I clean myself up with a tissue, I really don't know how to feel about today's shift..."
                        "If I can get that much money every day for the rest of my life, that'd be the dream."
                        "But do I really need to subject myself to these kinds of conditions?"
                        "My mind flashes to Twilight. Maybe, just maybe... I'm looking at it the wrong way. She's both a professional hero, and working here."
                        "What if there's a way to truly enjoy this lifestyle? That'd surely make this the dream job."
                        "But... Is it my dream job?"
                        "Hmm..."
                    scene bg black with d
                    play sound success
                    $ stripclubwork2 = 1
                    $ vaginalsexes += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    $ status += 1
                    call sdgain from _call_sdgain_96
                    call shameloss from _call_shameloss_66
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    jump postworktrans
                "Decline" if stripclubwork4 == 0:
                    hide student7 with d
                    "I end up leaving the horny customer to his own devices and continuing my shift on my own."
                    $ moneygain = 30
                    call moneygain from _call_moneygain_68
                    "I get paid a comfortable $[fmoney] for my work. It feels nice not having to rely on tips."
                    jump postworktrans
        "Customer Service I (Paizuri)" if True:
            if stripclubwork2 == 0:
                if stripclub1intro == 0:
                    "I’m still a little nervous. This is my first time actively offering services to customers instead of just working at the bar."
                    "But I’ll do my best anyway!"
                "The bunny suit obviously accentuates my bosom and ass, so I can’t escape the subtle gaze of customers as I pass by."
                "Although noticeably one customer does seem to take a particular interest with me and flags me down so I can serve him."
                "He sparks a conversation too."
                show student7 with d:
                    xpos 50
                if stripclub1intro == 0:
                    customer "Hey, newbie, fancy a fun game?"
                    show mce happy2 with d
                    mc "Hm? What’s the game?"
                    customer "Just a small game of guessing heads and tails. How about it?"
                    show mce happy with d
                    mc "Ah? What’s the catch? That’s not really a game."
                    customer "It’s more of a magic trick, you’ll have to watch really closely to catch it though!"
                    show mce laughing with d
                    mc "Ohhh, show me!"
                    "The customer playfully twiddles a coin around their knuckles with obvious skill."
                    "I watch him closely with glee as he shows me the front and back of the coin, an obvious heads and tails."
                    customer "Choose a side!"
                    show mce happy with d
                elif True:
                    mc "Ohh, yeahh! I recognize you."
                    customer "Fancy another game? Heads or tails?"
                mc "Uhhmm…"
                menu:
                    "Heads" if True:
                        $ sc1c = "heads"
                        mc "Heads!"
                    "Tails" if True:
                        $ sc1c = "tails"
                        mc "Tails!"
                customer "Okay now, when I flip the coin and catch it, you will fall under just a little more."
                show mce neutral with d
                "Eh? Fall under what?"
                call hypnosiseffect from _call_hypnosiseffect_10
                "Paying too close attention to the coin to question his wording, he flips the coin and catches it."
                "And then revealing the result, it was obviously a [sc1c]."
                mc "Ah, I got it right! It’s a [sc1c]!"
                customer "Are you sure about that? Look again."
                show mce neutral with d
                mc "Hm…? Really?"
                "Looking back at the coin, it’s unchanging. It’s still a [sc1c]… But for some reason, I have an overwhelming urge to…"
                "An overwhelming urge to…"
                call hypnosiseffect from _call_hypnosiseffect_11
                show mce laughing with d
                mc "You’re right, it’s not a [sc1c]… I guess I was wrong."
                "Was I wrong? I don’t know, something compels me to believe it so."
                customer "Hehe, excellent. How was that?"
                show mce neutral with d
                mc "I don’t really get it…"
                customer "Ohh, you didn’t?"
                customer "How about I show you again, after a private session? Maybe something oral, or with your breasts?"
                mc "A private session? I haven’t done one of those before… It’s my first time serving on the floor!"
                customer "You really want to do it though, don’t you?"
                call hypnosiseffect from _call_hypnosiseffect_12
                show mce happy with d
                mc "Yeah, I do! It’s a good idea."
                show mce neutral with d
                mc "Oh, but… I-I don’t really know, uhmm…"
                "The customer raises an eyebrow as he flicks his coin once more."
                customer "You sure have a strong will."
            elif True:
                "A certain customer beckons me on the floor, and asks for a private session."
                "Ah, I recognize this man. He's the one with the coin trick."
                show student7 with d:
                    xpos 50
                call hypnosiseffect from _call_hypnosiseffect_13
                "He grins as I approach and flicks his coin, the sound of metal clinking sends shivers down my spine."
                "Just looking at him and..."
            $ sdreq = 45.0
            $ shamereq = 55.0
            $ hmult3= (hmult + hypnotised)/100
            $ hypnosd = int(sdreq / hmult3)
            $ hypnoshame = int(shamereq * hmult3)
            "For some reason, I really want to service him."
            $ stripclub1intro = 1
            menu scm1:
                "Sexual Desire: [sd], Shame: [shame].{p}[hypnotised]%% Hypnotised lowering requirement multiplicatively by [hypnotised]%%."
                "Paizuri Service ([hypnosd] Sexual Desire, <[hypnoshame] Shame)" if True:
                    if hypnosd > sd or hypnoshame < shame:
                        "I really shouldn't do these kinds of things for money."
                        jump scm1
                    play music action
                    $ stripclubwork1 = 1
                    scene bg black with d
                    "All alone with the customer in a private, rented room…."
                    play sound equip
                    scene bg booth
                    show paizurib
                    if tan == 1:
                        show paizuribtan
                    if hair == 1:
                        show paizurih black
                    if hair == 2:
                        show paizurih blonde
                    if piercingson == 1:
                        show paizuripiercings
                    show paizurie bunny
                    show paizuri 1
                    with d
                    customer "You still seem innocent and naïve, that’s quite unlike a lot of the other customers."
                    show paizuri 1b with d
                    mc "Heyy, what’s that supposed to mean? I’ve been around the block!"
                    mc "Haha, anyway, I can hardly be innocent if I’m in a position like this, can I?"
                    customer "True enough, just try to have some fun!"
                    show paizuri 1
                    call hypnosiseffect from _call_hypnosiseffect_14
                    with d
                    mc "Ahh, yes…"
                    mc "Wow, you’re so hard… Alright, I’ll begin… Mmphhh…"
                    play sound2 oral1 fadein 3.0
                    "The man had requested an oral service, but after seeing my breasts he couldn’t resist asking to be serviced by them. I can still kiss and play with the tip though."
                    "I squeeze his cock between my pillowy breasts, and drool on the tip to get it nice and lubricated."
                    customer "Uuhh, how exquisite! You truly are a promising girl!"
                    show paizuri 2 with d
                    "I’m pretty inexperienced, but since I treat this like a job, and I’m a hard worker, I focus myself on pleasuring the man as much as I can."
                    mc "*Lick, chuu* Do my breasts feel that good? Mmphhh, mmm…. *Pant, pant* Your cock feels excellent, hehe…"
                    "My movements grow more passionate, as I find a suitable rhythm, and gradually get more aroused."
                    customer "Huff, *pant*. Yes! You’re perfect!"
                    "I could feel a dampness in-between my legs. I wanted to feel good too, but… I suppose I’ll focus on the man for now. I’m surprised by just how much I’m enjoying this, it’s like it’s something I was always meant to do."
                    "Feeling the customer begin to throb and grow tense between my breasts, I more often introduced my tongue against his sensitive tip. Kissing and licking at the peak of each thrust."
                    "His cock trembles, and precum drips out which I dutifully collect. Juices won’t stop dripping from my pussy either."
                    "Everything is just making my head go blank, I can think of and do nothing but service this man… I want to make him cum so badly."
                    customer "I’m almost there, oohh, keep going!"
                    mc "Mmphh.. *Chuu* Yesshh, please cover me with your cum!"
                    play sound cum
                    show paizuri 3 with cum
                    play sound cum
                    show paizuri 3 with cum
                    mc "Mmphhh, aaahhh! S-So much!"
                    play sound cum
                    show paizuri 3 with cum
                    play sound cum
                    show paizuri 3 with cum
                    stop sound2 fadeout 3.0
                    "Several sprays of hot cum land on my face, head, and drip down my breasts. It’s a complete mess and I love every second of it."
                    stop ambience fadeout 1.0
                    stop sound2 fadeout 1.0
                    "For a while, our panting echoes through the room as we enjoy the afterglow."
                    mc "Haaahhh, was my service satisfactory, master? *Pant, pant*"
                    scene bg booth
                    show student7:
                        xpos 50
                    call clothesbunnysuit from _call_clothesbunnysuit_9
                    show mce happy2
                    with d
                    customer "Yep! Excellent for your first time, you’re a perfect candidate for this kind of job."
                    show mce laughing with d
                    mc "Fuhu… You shouldn’t say that about a girl, saying they’re a perfect whore…"
                    customer "Keheh… Here’s your pay."
                    scene bg black with d
                    stop music fadeout 3.0
                    $ moneygain = 60
                    call moneygain from _call_moneygain_69
                    play sound success
                    "(+$[fmoney])"
                    scene bg black with d
                    if stripclubwork1 == 0:
                        show bg street
                        call clothes from _call_clothes_1
                        show mce neutral
                        with d
                        "Really… I’m the perfect whore? I feel a little disgusted just thinking about it."
                        "Those words stayed with me long into the day, leaving me feeling restless."
                    play sound success
                    $ blowjobs += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_106
                    call shameloss from _call_shameloss_100
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    jump postworktrans
                "Politely Decline" if stripclubwork4 == 0:
                    mc "Sorry, my boss might get mad at me if I did that!"
                    customer "Ahh, what a shame. Perhaps you could join us next time."
                    "Wait, ‘us’? Hm…"
                    "Regardless, I continue the shift as is."
                    play sound success
                    $ moneygain = 30
                    call moneygain from _call_moneygain_53
                    "I get paid a comfortable $[fmoney] for my work. It feels nice not having to rely on tips."
                    jump postworktrans
        "Serve drinks as normal" if True:
            "I work the bar, serving drinks."
            play sound success
            $ moneygain = 30
            call moneygain from _call_moneygain_54
            "I get paid a comfortable $[fmoney] for my work. It feels nice not having to rely on tips."
            jump postworktrans

label stripclubworkintro:
    if stripclubwork1intro == 0:
        $ stripclubwork1intro = 1
        $ hypnotised = 0.0
        $ hmult = 100.0
        "I walk over to Twilight near the bar and ask her a question."
        show twilight:
            xpos 1200
        with d
        twilight "Did I hear that right? You want to work here?"
        mc "Yup! I even have one of your bunny suits to the same specification."
        if clothes == 5:
            twilight "So you do..."
        elif True:
            twilight "Really? From that sex store? Huh..."
        twilight "To tell you the truth, I'm the 'big mama' around here, so I deal with the hiring and wellbeing of the girls."
        twilight "I just... Are you really okay working in a place like this? It's perhaps not as glamourous as you think."
        twilight "I wouldn't want to subject one of my students to the seedier parts of this career."
        show mce horny with d
        mc "I can take it, well, if it pays!"
        twilight "It does indeed pay well. It's more a question of how long you're willing to put up with it..."
        twilight "*Sigh* So you have money problems, and that's why you're here?"
        "She sways back and forth for a few moments while thinking."
        twilight "Tell you what. I'll take you in on a smaller role, and just let you do what you feel comfortable with."
        twilight "That being said, I can't watch over you all the time, so don't do anything reckless."
        mc "Thank you so much!"
        if clothes == 5:
            twilight "Well, you're already dressed and ready, you might as well get to work."
        elif True:
            twilight "The changing room is just back there, go ahead, get changed, and you can serve drinks."
        play sound equip
        scene bg black with d
        scene bg stripclub
        call clothesbunnysuit from _call_clothesbunnysuit_10
        show mce happy
        with d
        "Hooh! I feel adorable in this! I'm kinda excited."
        "All suited up, I begin my shift!"
        jump scw1m2
jump postworktrans

label hypnosiseffect:
    play sound hypnosis
    show pink with hypno:
        alpha 0.5
    hide pink with d
    $ hypnotised += 5
    return

label twilightdance:
    stop ambience
    show twilight:
        xpos 1200
    with d
    twilight "You want a dance…? From me? That’ll cost you!"
    mc "Yeah, I know! I’m ready."
    twilight "Oh, are you sure? I’m not used to girls asking for dances."
    mc "Gimmie the good stuff, like any other customer."
    twilight "In that case, come with me!"
    play music action
    scene bg booth with d
    show twilightdance 1 with d
    "Escorted into a private room, the head stripper, Twilight, happily shows her stuff."
    "Her dancing is exquisite, and she really doesn’t hold back on the sexier stuff."
    "Between twirling around and showing off her ass at many spectacular angles."
    "To pressing her glorious bosom against me and in my face."
    "And even spreading her legs and grinding her pelvis against me, my thigh and anything but where I want it most (my face)."
    twilight "You like what you see, baby?"
    twilight "Maybe if you give me a little more, you could see a little extra, hehe…"
    mc "H-Huh? R-Really?"
    twilight "Ohh, don’t get all flustered, now… You told me to just treat you like anyone else… And I know a horny girl like you wants to see more."
    mc "Maybe…"
    menu sbm2:
        "Money: $[money]"
        "Pay for Nude Dance (-$40)" if True:
            if money < 40:
                "I don't have enough money for that."
                jump sbm2
            $ money -= 40
            twilight "Why, thank you, cutie! You’re about to love what happens next."
            play sound equip
            show twilightdance 2 with d
            "Slipping off her bunny suit piece by piece, Twilight’s gorgeous body is slowly unveiled to me."
            "And wow, it’s amazing."
            "Performing an even lewder dance, with some spreading, rubbing, and fondling. I get good glimpses of her ass, breasts and pussy."
            "It seems the more you pay, the better the service, as Twilight even takes my hands and places them on her breast, allowing me to grope. While not technically breaking the no-touching rule, I still manage to get a handful of exactly what I want."
            twilight "This would be the part where you have a boner, and I tease your erection through your pants, but you don’t really have that, do you?"
            mc "Nope, no surprises in my pants for you."
            twilight "In that case, think you could spread your legs? I think I can improvise."
            "Hard to not comply, as I spread my legs and open myself up to Twilight."
            "Getting between my legs, she performs several teasing motions which would no doubt delight a guy, but what I really enjoy is every grind and graze she performs between my thighs as she expertly teases me."
            "And in the finale, she locks our legs together and playfully mimics scissoring, although she cuts it awful close to actually performing the act as our pelvises do briefly touch and my clit gets a little touch of love which sends all the right kinds of shivers through me."
            twilight "Mmhh, look at you! You’re far cuter than my usual, I can tell by your hot, horny blush that you want more."
            mc "Uhmm, could there be anything ‘more’, than this?"
            twilight "I think we both know the answer to that question, don’t we?"
            mc "Yeahh… I think so…"
            twilight "All I need is another $50, and I can send you straight to heaven."
            menu sbm3:
                "Sexual Desire: [sd]. Money: $[money]"
                "Receive Cunnilingus (-$50, 40 Sexual Desire)" if True:
                    if sd < 40:
                        "I'm not really horny enough to do something so drastic."
                        jump sbm3
                    if money < 50:
                        "I don't have enough money for that."
                        jump sbm3
                    $ money -= 50
                    mc "Here’s your money, Twilight."
                    twilight "I feel bad for getting so much out of one of my own students. But then again, it wouldn’t be the first time, and secondly, I’ll make you feel like every single dollar was worth it."
                    scene twilightcunnilingus 1 with d
                    "I sit back as Twilight gets between my legs and spread them apart."
                    if nude == 0:
                        "Stripping my bottom half in a hurry..."
                    play sound2 foreplay2 fadein 3.0
                    "She takes a moment to marvel at my pussy before tentatively flicking her tongue against my swollen clit."
                    twilight "Mmphh, let’s not waste any time with you… Judging by how wet and swollen your pussy is, you’re desperate for some lady love, aren’t you?"
                    mc "Aahhh, y-yeah… Your dance really turned me on, mmphh…"
                    twilight "Hehe, you’re so sweet. Both in heart, and down here, mm… *Lick, lick*"
                    "Her tongue expertly flickers against my clit, in a remarkably focused and diligent act of cunnilingus. She wastes no time focusing on any area that won’t elicit the most pleasure possible from me."
                    "It’s almost overwhelming, and the intense euphoria surging through my body causes me to spasm and squirm so much that Twilight holds me down by my thighs to keep my pussy in place."
                    mc "Mmphh, aahhh, haaaahh!"
                    "However, in a teasing fashion, she controls the tempo with short bursts of speed contrasting longer slower moments."
                    "This essentially edges me, causing my body to grow more sensitive each time, and the pleasure from each burst of speed to grow exponentially."
                    mc "Ohh god, aaahhh, haaahhhh! T-Twilight… aahhh…"
                    "The entire time, Twilight keeps a close eye on my body language, to try and catch when I pass the point of no return."
                    "And after several edges, she finally pushes me over the edge, and prepares to finish me off."
                    play sound cum
                    scene twilightcunnilingus 2 with cum
                    "Flicking her tongue rapidly against my clit, my entire body is racked with bliss as I experience a full body orgasm."
                    play sound cum
                    scene twilightcunnilingus 2 with cum
                    "Despite normally being a non-squirter, I squirt excessively, releasing a lot of juice all over Twilight’s face. The orgasm really is that intensive compared to what I’m used to."
                    stop sound2 fadeout 1.0
                    "This ecstasy, and Twilight’s tongue, last half a minute before finally coming to a stop, leaving me in a daze."
                    scene twilightcunnilingus 1 with d
                    twilight "Well now, I wasn’t expecting all that squirt. But I’m used to being covered in cum, so it’s not too different."
                    mc "Ahh, s-sorry Ms… I don’t usually do that!"
                    twilight "Heh, it just means I did a good job. That’s nothing to be ashamed of."
                    twilight "But maybe you’d return the favour to make up for it, hmm? Hehe, kidding, I’d never ask that of you unless I was a paying customer."
                    scene bg booth
                    call clothes from _call_clothes_2
                    show mce horny
                    show twilight:
                        xpos 1200
                    with d
                    twilight "You’ve got a few minutes more to catch your breath and freshen up. Thanks for coming to my club!"
                    mc "Haahhh, thanks for the amazing service."
                    scene bg booth
                    show masturbation3b
                    if tan == 1:
                        show masturbation3btan
                        if pregnancyshowing == 1:
                            show masturbation3btanp
                    if hair == 1:
                        show masturbation3h black
                    if hair == 2:
                        show masturbation3h blonde
                    if piercingson == 1:
                        show masturbation3piercings
                    if pregnancyshowing == 1:
                        show masturbation3e pregnant
                    with d
                    "As Twilight leaves the room, giving me a few minutes of privacy before I have to leave, I decide that time is best spent rubbing another one out."
                    mc "Aahhh, haahhh… ahhhh… Oh, Twilight… That was so amazing…"
                    $ twilightdance3 = 1
                    $ lesbian += 1
                    $ status += 1
                    $ sdgain = 2
                    $ shameloss = 1
                    call sdgain from _call_sdgain_138
                    call shameloss from _call_shameloss_101
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    jump postworktrans
                "Pass" if True:
                    if personality == 2 and sd > 50 and money > 100:
                        "(Always Horny) I've got plenty of money, so I definitely should do this!"
                    jump dancefinishup
        "Finish up" if True:
            label dancefinishup:
                pass
    mc "It was a nice dance, but that was enough."
    twilight "Ahh, you’re welcome any time. Maybe you learnt a few tricks to woo your next man too."
    mc "Hehe, I sure did! Thank you, Twilight."
    play sound success
    $ sdgain = 1
    $ shameloss = 1
    call sdgain from _call_sdgain_139
    call shameloss from _call_shameloss_102
    "(+[fsd] Sexual Desire, -[fsd] Shame)"
    jump postworktrans



init:
    $ twilightdance3 = 0
    $ stripclubvisited = 0
    $ stripclubwork1 = 0
    $ stripclub1intro = 0
    $ stripclub2intro = 0
    $ stripclub3intro = 0
    $ stripclubwork1intro = 0
    $ stripclubwork2 = 0
    $ stripclubwork3 = 0
    $ sc3endured = 0
    $ stripclubwork4 = 0
    $ stripclubwork5 = 0
    $ sc1c = "Tails"
    $ hypnotised = 0.0
    $ sdreq = 0.0
    $ shamereq = 0.0
    $ hypnomult = 100.0
    $ hypnosd = 0.0
    $ hypnoshame = 0.0
    $ hundred = 100.0
    $ hmult = 100.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label park:
    if lewdoutfit == 1 and parkunlocked == 0:
        "Unlock this location by wearing a lewd outfit."
        if lewdoutfit == 1:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump parkintro
                "Back" if True:
                    jump postworldmap
    elif parkunlocked == 0:
        "Unlock this location by wearing a lewd outfit."
        jump postworldmap
label parkintro:
    play music girls
    if parkunlocked == 0:
        $ parkunlocked = 1
        scene bg park with d
        "A little later, while I'm on a walk..."
        if lewdoutfit == 0:
            call clothesbar from _call_clothesbar_15
            show mce happy
            with d
            "I had decided to wear something a little naughty to express myself. The bar uniform is certainly slutty, but it wasn't over the top."
        elif True:
            call clothes from _call_clothes_76
        show mce happy
        with d
        "I feel so lewd wearing this outfit outdoors... It's pretty exciting!"
        unknown "Kyahaha, I didn't take you as the type to wear that, [mc]!"
        show mce neutral with d
        mc "H-Huh?! Who's there?"
        show hana:
            xpos 1200
        with d
        unknown "It's me! Can'tcha see me?"
        "No way! Is that the invisible girl from my class? She's... naked!"
        if nude == 1:
            "I mean, I am too, but I never imagined I'd find a naked invisible girl too."
        python:
            hana = renpy.input("Name the Invisible Girl. Leave blank for the default name 'Hana'.")
            hana = hana.strip()
            if not hana:
                hana = "Hana"
        show mce laughing with d
        mc "Oh my gosh, is that you, [hana]?!"
        hana "I could say the same about you! I couldn't believe my eyes."
        hana "Is this some kind of exhibitionism I'm seeing?"
        show mce horny with d
        mc "Yeah, I guess you could call it that!"
        hana "Nooo waaay! And you're not even invisible! As a fellow exhibitionist I am envious of that confidence!"
        show mce laughing with d
        mc "Ohh? So this entire time we've had an invisible girl, in the nude, sneaking around? Haha!"
        hana "A little! Maybe it's TMI, but it really gets me off! Although considering what we're both wearing, I imagine nothing's off limits, kyahahah."
        hana "Seeing this has really inspired me... Say, [mc], how about we take our love of showing off to the next level?"
        show mce happy with d
        mc "You've got my interest."
        hana "Kyahaha, I've always wanted to do a little more than just wander around naked."
        hana "What about you?"
        mc "You mean like, maybe something sexual in public? I'd be lying if I said it hadn't crossed my mind."
        hana "I'm trying to build up some confidence to try it, though! And you seem way more confident than me, you're not even invisible."
        mc "Heh, I can see what you mean..."
        hana "Do you think you could help me? Maybe be like a friend with benefits?"
        mc "Like, lesbian?"
        hana "Hmm, I was thinking of getting a guy, but... Argh, I'm just not ready to do something quite like that outdoors yet..."
        menu:
            "You want me to show you how it's done?" if True:
                hana "Oh, yes please!"
                hana "Hmm, what about that guy, over there? Would you fuck him?"
            "Yeah, me neither, it's a bit extreme" if True:
                hana "Hehe, well, hypothetically... What about that guy, over there? Would you fuck him?"
        show mce horny with d
        mc "You certainly picked a hot one... Uhmm..."
        menu pim1:
            "Sexual Desire: [sd], Shame: [shame]."
            "Sexual Desire: [sd]."
            "Yeah, I'd have sex with him. (50 Sexual Desire)" if True:
                if sd < 50:
                    "Nope! I don't even know that guy!"
                    jump pim1
                hana "That'd be so hot!"
                show mce neutral with d
                hana "Heyyy, cutie!"
                "Eek! She's actually going up to him!"
                show student3:
                    xpos 50
                with d
                hunk "Uhmm... What's going on? Why is there a naked invisible girl and a random scantily clad perv in the park?"
                hana "This scantily clad perv said she wants t-"
                mc "Shhhhhush!"
                hunk "Huh? What was that?"
                menu pim2:
                    "Sexual Desire: [sd], Shame: [shame]."
                    "Fuck him behind some trees. (70 Sexual Desire, <30 Shame)" if True:
                        if sd < 70 or shame > 30:
                            "Not a chance!"
                            jump pim2
                        show mce horny with d
                        mc "I'm going to walk into those trees and undress, hunk, if you want to come with me, I'll let you do anything you want."
                        hunk "Oohhh, lead the way, you sexy slut."
                        jump parkfrombelow
                    "Pussy out!" if True:
                        show mce horny with d
                        mc "Sorry, what my perverted invisible friend meant, is that you should have sex with her!"
                        hana "H-Hey, I never mentioned that! I wanted to warm up by watching you do it!"
                        hunk "With an invisible girl? I don't know, ladies... Would I be able to see my own dick inside? That's kinda weird."
                        hana "Hey, listen here ya dick, my invisible pussy will drive you wild!"
                        hunk "Man, this is getting way too weird for me. I'm getting out before I lose a kidney or something."
                        hide student3 with d
                        hana "Daaamniiiit! Why is getting men so hard when you're invisible?!"
                        mc "Ahaha, funnily enough, I think this is one of the situations where you might be even more enticing if you were wearing clothes."
                        hana "Hmm... You think? Let's try this again another time."
                        hana "I live on the same floor as you, but you probably haven't seen me walking around, kyahahah!"
                        hana "Come see me if you ever want to get frisky in public!"
                        mc "I'll consider it, you sneaky perv!"
                        jump prebedroom
            "But I'm still a virgin!" if virgin == 0:
                hana "Whaaaat?! And you're dressed like that in public?"
                mc "I'm just expressing myself! Hehe."
                hana "Kyahaha, well, I was a virgin when college started too, I suppose."
                jump prebedroom
            "In the park? No way!" if True:
                show mce laughing with d
                mc "That might be a bit extreme even for me!"
                hana "If you ever change your mind, I live on the same floor as you, but you probably haven't seen me walking around, kyahahah!"
                hana "Come see me if you ever want to get frisky in public!"
                mc "I'll consider it, you sneaky perv!"
                jump prebedroom
    elif True:
        scene bg park with d
        call clothes from _call_clothes_77
        show mce happy
        show hana:
            xpos 1200
        with d
        if lewdoutfit == 0 and nude == 0:
            hana "Hey, [mc]! You're not wearing anything lewd today? You totally should!"
            mc "It's okay, I can strip wherever I want! Hehe."
            hana "Oohh, pull your panties down and just take it! I like your style."
        elif True:
            hana "*Drool* You're so hot as always, [mc]!"
            mc "Ohh, you'll make me blush! Are you sure you're not becoming a voyeur too?"
            hana "Kyahah, being a voyeur is half the enjoyment when you're invisible!"
        hana "So what devious things shall we get up to today? Hmm?"
        menu parkm1:
            "Sexual Desire: [sd], Shame: [shame]."
            "Fuck a Stranger (80 Sexual Desire, <20 Shame)" if True:
                if sd < 80 or shame > 20:
                    "Not a chance!"
                    jump parkm1
                jump parkfrombelow
            "Park Gangbang (120 Sexual Desire, 0 Shame)" if True:
                if parksex == 0:
                    "I need to complete the previous event first."
                    jump parkm1
                if sd < 120 or shame > 0:
                    "Not a chance!"
                    jump parkm1
                jump parkgangbang
            "Back" if True:
                jump worldmap
label parksex:
    label parkfrombelow:
        "No harm in having a little fun, right? Hehe..."
        play music action
        scene bg sky
        show chikanb
        if tan == 1:
            show chikanbtan
        if hair == 1:
            show chikanh black
        if hair == 2:
            show chikanh blonde
        show chikan park1
        with d
        "With [hana] and the Hunk watching, I expose myself against a tree."
        play sound2 foreplay1 fadein 3.0
        play sound fondle
        show chikan park2
        with d
        $ groped += 1
        "Oooohhh... Even though I'm behind some trees, and hard to spot, the park is still a crowded environment, how exciting!"
        "And I was the instigator, the one in control, it's really turning me on."
        "My pussy drips, and my thighs start to burn up. Almost more instinct than sense, I begin subtly grinding my nude butt against the buldge in the hunk's pants."
        hunk "You're getting cheeky, aren't you? How about this!"
        play sound spank
        show chikan park3 with cum
        play sound spank
        mc "Offt, how rough!"
        "Two clean spanks leave my cheeks are left rosy."
        "Finally, he's taking out his cock! Ohhh, this is turning me on a lot! [hana] was really onto something with this suggestion..."
        "As the stranger behind me nonchalantly rubs my pussy, my body shivers in response to the building pleasure..."
        $ condomon = 0
        if condoms > 0 and pregnancyshowing == 0:
            menu:
                "Use a condom? Condoms: [condoms]. [fertilityrate]."
                "Yeah." if True:
                    $ condomon = 1
                    $ condoms -= 1
                "Fuck the rules! (Without protection!)" if True:
                    $ condomon = 0
        "Despite being in a crowded park, despite the fact anyone could look over and see me getting fucked..."
        "He takes his cock and slides the tip up and down my labia."
        play sound cum
        show chikan park4 with d
        "Then, he positions it against my lips, and pushes inside."
        if virgin == 0:
            $ virgin = 1
            "Ahhh, I can't believe I just lost my virginity to a stranger in the park!"
        play ambience sex fadein 3.0
        "My pussy is so dripping wet that his thick member easily slides in with a lewd schlick. I arch my back slightly to give it a better angle, and coo as I'm filled up."
        "My lover starts to slowly move their hips. It's a gentle fuck that savours every inch of the act, but in these daring circumstances it's euphoric."
        "Not only that, but since we're standing and my legs are together, my pussy is even tighter around his throbbing shaft."
        "The result was ecstasy, beyond amazing, even when moving slowly."
        "Ahh, I'm going to come already! My insides started to constrict around my partner's tight cock in rhythmical waves, squeezing and sucking for more."
        "Fucking faster and harder, I could feel the pressure building as his shaft throbbed and it was evident that he wouldn't be able to hold back much longer."
        play sound cum
        show chikan park5 with cum
        play sound cum
        show chikan park5 with cum
        "Then cum exploded from his tip as he relentlessly and carelessly pounded my pussy."
        play sound cum
        show chikan park5 with cum
        play sound cum
        show chikan park5 with cum
        "Our orgasms overlapped so much I could barely tell; all whilst my insides were pumped with semen."
        "As our orgasms fade, and we slow down, I hadn't even realized that I was moving my hips too."
        stop ambience fadeout 1.0
        stop sound2 fadeout 1.0
        play sound cum
        show chikan park6 with d
        "Pulling out, the stranger quickly covers himself up, gives us a knowing nod and walks away as if nothing at all happened."
        "I look around me and it seems a miracle that no one noticed, especially near the end... Although maybe it was a situation where anyone that noticed pretended not to."
        if condomon == 0:
            call pregnancyroll from _call_pregnancyroll_18
        stop music fadeout 3.0
        "I look down and notice that my pussy is dripping cum onto the floor."
        scene bg park with d
        call clothesnude from _call_clothesnude_75
        show mce neutral
        show hana:
            xpos 1200
        with d
        hana "That was soooo hot!"
        mc "Don't think I didn't catch those gloves of yours rubbing between your legs like you were in heat!"
        hana "Kyahaha, next time I want you to watch me!"
        "She may be one of the worst role models I've ever been around, but damn if it doesn't feel good."
        play sound success
        $ sdgain = 2
        call sdgain from _call_sdgain_150
        $ moneygain = 20
        call moneygain from _call_moneygain_75
        $ status += 1
        $ vaginalsexes += 1
        $ publicdisplays += 1
        $ parksex = 1
        "(+$[fmoney], +[fsd] Sexual Desire)"
        if qsecretlydepraved == 1:
            call sdgain from _call_sdgain_151
        "(For doing a depraved act, you gain another [fsd] sexual desire!)"
        jump postworktrans
    label parkgangbang:
        play music action
        if parkroute2 == 0:
            hana "After watching your amazing rut, I think I’m ready to try it for myself."
            mc "Ohh? How exciting! Shall we go find someone?"
            hana "Uhhmm, uuuhhmmm…"
            mc "Still nervous? Come on, I’ll join in. And I’m visible, so I’d draw more attention."
            hana "Okie, let’s try it. I know a place where not many people pass. We just need two guys."
            show mce horny with d
            mc "Easy peasy, let’s just walk up to some guys and ask them to fuck."
            hana "Is it really that easy?"
            mc "Sure is! I have about a 50%% success rate asking strangers."
            hana "Damn… I had no idea you were so… uhh…"
            show mce laughing with d
            mc "Slutty? Hehe, I might be a little addicted to sex, but it’s fine, I’m only gonna be young and dumb once."
            hana "I want to try too! Let’s go."
        scene bg black with d
        "After finding two guys, [hana] leads us to a quiet area in the corner of the park. Far enough to be unrecognized by prying eyes, but not far enough to be unseen."
        play sound2 foreplay2 fadein 3.0
        show parkgangbangb
        if tan == 1:
            show parkgangbangbtan
        if pregnancyshowing == 1:
            show parkgangbangbp
            if tan == 1:
                show parkgangbangbtanp
        if piercingson == 1:
            show parkgangbangbpiercings
        if hair == 1:
            show parkgangbangh black
        if hair == 2:
            show parkgangbangh blonde
        with d
        hana "Haaahhh, I can’t believe we’re doing this. *Lick, suck*."
        "Latching her lips around my nipple, [hana] playfully suckles my teat as the two guys we seduced get into position."
        $ condomon = 0
        if condoms > 0 and pregnancyshowing == 0:
            menu:
                "Use a condom? Condoms: [condoms]. [fertilityrate]."
                "Yeah." if True:
                    $ condomon = 1
                    $ condoms -= 1
                "Fuck the rules! (Without protection!)" if True:
                    $ condomon = 0
        hana "Oh crap, I don't have any condoms! Can I borrow one, [mc]?"
        menu:
            "Condoms: [condoms]."
            "Sure!" if condoms > 0:
                $ condoms -= 1
                hana "Thanks, [mc], you're a lifesaver."
            "I don't have any (Lie)." if condoms > 0:
                hana "Aahh, damn... It's okay, I'll think of something."
            "I don't have any." if condoms == 0:
                hana "Aahh, damn... It's okay, I'll think of something."
        guy1 "Huh, where’s your pussy anyway, invisible girl?"
        "He asks while prodding and poking his cock into the [hana]’s butt."
        hana "Kyahaha, let me guide you in, sexy."
        play sound cum
        show parkgangbang 1 with d
        "Fortunately, the guy that picked me has no trouble, and before we know it, we’re both penetrated with a satisfying schlick."
        "My clit throbs intensely, getting filled up and fucked in a public park is melting my mind with pleasure, and [hana] feels much the same."
        hana "Oohhh, yessss! So good!"
        guy1 "Damn, this is the wettest pussy I’ve ever been in!"
        guy2 "You too? Maybe the tightest over here too, damn. I can’t get enough of these sex-crazed college sluts."
        play ambience sex fadein 2.0
        "Holding onto my thighs as leverage, my partner begins to ram his hips back and forth. Whilst [hana]’s partner manages to find her hips and pounds her doggystyle with equal fervour. "
        "There’s no foreplay, there’s no time. We have to fuck furiously and fast before we draw too much attention. This is well represented by how fast the two men start thrusting their hips, already moving as fast as a guy would at the peak of sex."
        "I’ve been in a lot of wild sexual situations, but this one might take the award for craziest. A gangbang in a public park. At any moment someone could look in our direction."
        "The guys are still dressed, they only lowered their pants slightly to take their cocks out, and [hana] is completely invisible. Meaning if anyone looks in this direction, I’m entirely the center of attention, and I think everyone here realizes that."
        "I can feel my clit burn with desire at the mere thought of a jogger passing by, or someone walking their dog catching a glimpse from the distance. My pussy throbs and tightens, eagerly milking the sliding shaft inside me."
        mc "Aaahh, oh gosh… Don’t hold back! If you keep going like that I’m going to come like crazy."
        guy2 "Tcchhh, your pussy is crazy, it’s going to make me cum too quickly."
        hana "Mmphh, fuck me harder too!"
        guy1 "Will I be able to see my cum inside you? I can’t wait!"
        "[hana] and I enthusiastically rock our hips back and forth, fucking our partners as much as they fuck us."
        "Pleasure builds as we rapidly approach our explosive orgasms, and as we reach that peak, our bodies spasm as euphoria fills our minds."
        hana "Ohhh god, I’m coming! Aaahh, kyaaahhh!"
        mc "F-Fuck, me too…"
        play sound cum
        show parkgangbang 2 with cum
        play sound cum
        show parkgangbang 2 with cum
        "Tightening and throbbing, my partner’s cock swells up and erupts inside of me, filling my pussy up with hot, white cum."
        play sound cum
        show parkgangbang 2 with cum
        play sound cum
        show parkgangbang 2 with cum
        stop ambience fadeout 3.0
        stop sound2 fadeout 3.0
        "Adjacent to me, [hana] is also served a generous helping of cum, directly into her pussy and womb."
        "Miraculously, all four of our orgasms barely manage to converge, leaving all four of us rutting blissfully the entire time."
        if condomon == 1:
            "Thanks to the condom, I don't need to worry about getting pregnant."
        elif True:
            call pregnancyroll from _call_pregnancyroll_27
        play sound cum
        show parkgangbang 3 with d
        "The men are quick to withdraw as the pleasure fades, cleaning themselves up and pulling up their pants so they don’t appear exposed any longer than they have to."
        "[hana] and I, however, have to take a little longer to enjoy the afterglow."
        guy1 "Uhm, so… Thanks, ladies. We’ll be heading out."
        guy2 "Wait, now would be the perfect time for a picture."
        hana "*Wiggle* Ohhh, yeah, take a picture!"
        play sound camera
        show parkgangbang 3 with cum
        mc "H-Hey, wait, don’t show anyone!"
        guy2 "Ahaha, I’ll throw it in my wank bank to commemorate this moment."
        play sound equip
        play ambience ambienceday
        stop music fadeout 3.0
        scene bg park with d
        call clothes from _call_clothes_102
        show mce happy
        show hana:
            xpos 1200
        with d
        if nude == 0:
            "I get up, and get dressed."
        elif True:
            "I get up, and since I came without any clothes, I remain nude."
        hana "Haahh, that was so exciting! I came super hard!"
        "Barely catching me off guard, [hana] hugs me tightly."
        show mce horny with d
        mc "Maybe I’m not the best influence, but that was some of the most exciting and intense sex I’ve ever had."
        hana "Definitely something I can take to the grave, kyahaha."
        if parkroute2 == 0:
            show mce neutral with d
            mc "Oh god, yeah… Even if I fall in love with someone in ten years, and marry them, I don’t think I could ever tell them about this."
            if boyfriend == 1:
                hana "Wait… That reminds me, don’t you have a boyfriend?"
                mc "Aahh, uhhmm…"
                menu:
                    "Yeah…" if True:
                        hana "O-Ohhh, I see!"
                        mc "I can’t tell him about this stuff… I feel ashamed that I’m doing it, but I can’t really control myself."
                        hana "I won’t judge you, don’t worry, [mc]. It was me that asked you to do these naughty things, and I wasn’t thinking straight."
                        mc "Yeah, but it’s not like I needed to do it. I’m not exactly innocent."
                        hana "I trust you’ll do the right thing, you’re a good person!"
                        show mce happy with d
                        mc "Thanks, [hana]."
                        "Am I really, though? Do good people have gangbangs in the park?"
                    "It’s an open relationship (Lie)" if True:
                        hana "Aahh, that’s perfect! So, he can fuck other girls too?"
                        "I think for a moment, a tinge of jealousy sinks my heart."
                        mc "Y-Yeah, sure…"
                        "I just realized, I’d be angry with him if he cheated, yet here I am. When did I become such a hypocrite?"
                    "No (Lie)" if True:
                        mc "That’s just a close friend, and maybe a bit of a fuckbuddy."
                        hana "Aahh, I see… Ohh, I need one of those…"
                        mc "Yeah, that’s maybe a more sensible decision than asking strangers."
            show mce neutral with d
            "I feel oddly ashamed of my actions. I've gotten so used to being open and sexual that maybe I've been taking it too far lately."
            "There's a difference between having fun, and then doing something I'll never be able to take back."
            "What if someone were to find out what I did here? This is a public park; anyone could have seen me in this busy student city."
            "Even so, everything ended up fine, right? And I had a lot of fun."
            show mce horny with d
            "Why shouldn’t I do more things like this?"
        $ vaginalsexes += 1
        $ groupsexes += 1
        $ parkroute2 = 1
        $ status += 3
        $ sdgain = 2
        $ shameloss = 2
        call sdgain from _call_sdgain_181
        call shameloss from _call_shameloss_129
        play sound success
        "(+[fsd] Sexual Desire, -[fshame] Shame.)"
        if qsecretlydepraved == 1:
            call sdgain from _call_sdgain_182
            "(Secretly Depraved) And since you enjoyed the depraved act! (+1 Sexual Desire!)"
        jump postworktrans
init:
    $ parksex = 0
    $ parkroute2 = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

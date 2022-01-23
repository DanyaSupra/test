label bar:
    play music club
    scene bg bar
    call clothes from _call_clothes_6
    show mce happy
    if nude == 1 or lewdoutfit == 1 and bartoldoff == 0:
        if clothes == 10:
            pass
        elif True:
            $ bartoldoff = 1
            show mce horny
            show student5:
                xpos 1200
            with d
            stu "Are you aware of what you're wearing right now?"
            show mce neutral with d
            "Eek, it's the guy running this place!"
            mc "U-Uhhm, yeah?"
            if nude == 1:
                stu "I know you're working here, but this is too much. At least wear... {i}something{/i}."
                menu:
                    "Is there anything I could do to convince you?" if True:
                        stu "You can start by putting some clothes on. Get out of here until then."
                    "Sorry!" if True:
                        pass
                show mce sad with d
                mc "Right... Sorry!"
                scene bg street with d
                "You got kicked out of the bar!"
                menu:
                    "Change into something suitable temporarily?" if True:
                        "I'll just quickly put on my bar uniform."
                        $ clothes = 10
                        $ nude = 0
                        scene bg bar with d
                        call clothes from _call_clothes_34
                        show mce happy
                        jump prebarmenu
                    "Return to the map." if True:
                        pass
                jump worldmap
            elif True:
                stu "Well... Power to you..."
                hide student5
                show mce horny
                with d
    with d
    if bar == 1:
        menu prebarmenu:
            "What are you going to do at the bar? Intoxication Level: [drunk]/4"
            "Buy some Alcohol" if drunk < 3:
                if pregnancyshowing == 1:
                    "I really shouldn't drink while pregnant."
                    jump prebarmenu
                menu barrbarmenu:
                    "Money: [money]. Intoxication Level: [drunk]/4. The effects of alcohol last until morning. Your character won't drink past her limits without peer pressure."
                    "Spirit ($10) (+10 Sexual Desire, -10 Shame) (+2 Intoxication)" if drunk <2:
                        if money < 10:
                            "I can't afford it."
                            jump barrbarmenu
                        play sound success
                        if qlightweight:
                            $ sd += 10
                            $ shame -= 10
                            "As a lightweight, you feel twice the effects from the alcohol."
                        $ sd += 10
                        $ shame -= 10
                        $ money -= 10
                        $ drunk += 2
                        "The bartender serves my order and I don't waste any time trying to swallow it's bitter taste down."
                    "Cocktail ($5) (+5 Sexual Desire, -5 Shame) (+1 Intoxication)" if True:
                        if money < 5:
                            "I can't afford it."
                            jump barrbarmenu
                        play sound success
                        if qlightweight:
                            $ sd += 5
                            $ shame -= 5
                            "As a lightweight, you feel twice the effects from the alcohol."
                        $ sd += 5
                        $ shame -= 5
                        $ money -= 5
                        $ drunk += 1
                        "The bartender serves my order and I take my time savouring the sweet taste."
                    "Back" if True:
                        jump prebarmenu
                if drunk == 1:
                    "Ahh! A light buzz!"
                elif drunk == 2:
                    "Phew... I'm really feeling it."
                elif drunk == 3:
                    "Mmm... I'm quite drunk now..."
                jump prebarmenu
            "You're too drunk to buy any more alcohol" if drunk > 3:
                jump prebarmenu
            "Work" if True:
                pass
            "Leave" if True:
                jump worldmap
        jump barroute
    call clothes from _call_clothes_7
    show mce happy
    with d
    "Upon closer inspection, is this really a bar? It seems more like a club; it has a dance floor!"
    "The manager offers me a simple waitress job in the evenings when it's busy."
    "Apparently the bar has a very high turnover rate, so they're pretty flexible about accepting work."

    call clothesbar from _call_clothesbar_2
    show mce sad
    with d
    "I go into the back and change my clothes before coming back out."
    "Feels a little... revealing?..."
    "Ahh... I think it's a few sizes too small. How unfortunate."
    menu:
        "There's no way I'm working in this." if True:
            "I shake my head and return to get dressed into my own clothes."
            call clothes from _call_clothes_8
            show mce angry
            with d
            "Everyone has a boundary they don't want crossed, and I'm afraid something that revealing is mine."
            "I return to my dorm shortly, with enough time to do something else tonight."
            jump bedroom
        "No, no, I need money." if True:
            show mce happy with d
            play sound success
            $ shameloss = 1
            call shameloss from _call_shameloss_29
            "(-[fshame] Shame!)"
            "It feels comfortable and breezy. How could I complain, really? It's bound to get hot in here after all."
        "I feel kinda sexy." if True:
            show mce horny with d
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_51
            "(+[fsd] Sexual Desire!)"
            "I'll be nervous at first, but I can slowly see myself getting more comfortable with this."
    $ bar = 1
    "And no one will be able to see my panties as long as I don't bend over too far..."
    play sound success
    "Received Bar Uniform."
    $ baroutfit = 1

label barroute:
    play music club
    scene bg bar
    call clothesbar from _call_clothesbar_3
    show mce happy
    with d
    "I begin my shift at the bar as a waitress and barrista."
    if barroute == 0:
        $ moneygain = 10
        call moneygain from _call_moneygain_15
        "Nothing unusual happens, and I get paid a comfortable $[fmoney]."
        show mce sad with d
        "$[fmoney]...? Is that it?"
        "In the corner of my eye, I notice a busty waitress receiving a tip from a patron."
        "!!!"
        show mce angry with d
        "I didn't get any tips! Grrr... If I knew all I had to do was show a tiny bit of cleavage..."
        "As if this outfit isn't revealing enough..."
        play sound success
        $ sdgain = 1
        call sdgain from _call_sdgain_52
        $ shameloss = 1
        call shameloss from _call_shameloss_30
        "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
        $ barroute += 1
        jump postworktrans
    if barroute == 1:
        "Ah, that reminds me. I was going to try and make more of an effort to get tips this time."
        menu br1m:
            "Go through your shift normally." if True:
                if personality == 2 and sd > 3 and shame <98:
                    "(Always Horny) Mmphh... I should do something sexy..."
                    jump br1m
                "Yeah... I think it'd be a bit silly to use my body in such a petty way to get tips."
                "Maybe another day when I'm feeling more desperate, haha."
                scene bg bar with d
                play sound success
                $ moneygain = 10
                call moneygain from _call_moneygain_16
                "Other than that, the shift goes as normal, and I get paid a cozy $[fmoney]."
                "Wow, they really do squeeze us students dry. What a rough deal."
                jump postworktrans
            "Expose your cleavage slightly. (3 Sexual Desire, <98 Shame)" if True:
                if sd < 3 and shame > 98:
                    jump br1m
                "Propping up my breasts slightly, I make sure they're flattering without flashing a nip."
                "Wow, even I'd stare at myself if I was a customer. This is sure to get at least some notice..."
                "Ehh... I'm having second thoughts, but before I even have the chance to, I'm quickly swarmed with work."
                "Customer after customer. Yet nothing new or special happens."
                "I should have figured, the uniform was revealing enough already..."
                "Maybe it's my attitude?"
                "Before I dwell on my doubts too long, a customer takes notice."
                call clothesbar from _call_clothesbar_4
                show mce happy
                show student2:
                    xpos 1200
                with d
                "'Heyy, I didn't realize this was hooters! Are you in a contest with the other hot waitress to see who's hottest?'"
                menu:
                    "Legends say my breasts get pushed out a little more with every tip I receieve." if True:
                        pass
                    "Maybe you should tip who you think the 'winner' is." if True:
                        pass
                    "Haha, nothing like that... Just trying to get myself noticed in a competitive environment." if True:
                        pass
                "The man replies 'Is that so? In that case, have $5 on me. If that can make you keep coming to this table and serving me, I'll come every night.'"
                hide student2 with d
                scene bg bar
                call clothesbar from _call_clothesbar_5
                show mce neutral
                with d
                "I thank the generous student, and return to the bar feeling giddy."
                "Although... I also feel this strange sense of shame."
                "Using my body like that to get money... Something about it doesn't entirely sit right with me."
                "I'll put it down to it being nervous on my first time."
                "I slip the $5 down my bra, and set my clevage back to normal."
                "After all that, I think I realized that the tips come from the way I carry myself, more than just my appearance."
                play sound success
                $ moneygain = 15
                call moneygain from _call_moneygain_17
                $ sdgain = 1
                call sdgain from _call_sdgain_53
                $ shameloss = 1
                call shameloss from _call_shameloss_31
                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                $ barroute += 1
                jump postworktrans
        jump postworktrans
    if barroute == 2:
        "I'm slowly getting more used to this environment."
        "And honestly working here is great for my college life, I get immersed in student culture and lots of opportunities to socialize."
        "Slowly getting better at talking to customers, getting the occasional tip comes naturally now."
        show mce neutral with d
        "Although a part of me can't quite tell if it's my outfit or my attitude yet."
        "Looks like I'll recieve $15 today... Am I really going to be able to make $72,000?"
        "Let's do some quick math..."
        "If I work every single day, for four years..."
        "... Oh god, that's not even close to $72,000..."
        "I can't keep working like this for $10 and small tips!"
        "I need to, I need to..."
        show student3:
            xpos 50
        show student4:
            xpos 1200
        with d
        stua "Hey, why so panicked? You're making us all stressed with those faces."
        stub "Yeah, come chill out a bit."
        "Hm... Might be an opportunity to get a tip..."
        show mce happy2 with d
        mc "Hey boys, did you want some drinks, or did you want me? Hehe."
        stua "I didn't realize you were on the menu."
        stub "Damn, your uniform is even more revealing than the other waitresses, what's the deal?"
        show mce neutral with d
        mc "Uhmm, w-well... It's a few sizes too small, and..."
        stua "I'll give you a tip if you let me cop a feel of your ass."
        "*Gulp*... Dare I even ask?"
        mc "H-How much?"
        "Oh god, I asked..."
        stua "Heh, figures. $5 for a squeeze, then we'll order our drinks."
        "$5 for a 'squeeze', a singular squeeze on my ass? How humiliating..."
        "Yet, it's such a small action. I mean, it's just a freaking squeeze. Why should I be so ashamed?"
        menu barmenu2:
            "Sexual Desire: [sd], Shame: [shame]"
            "Ignore their flirting." if True:
                if personality == 2 and sd > 6 and shame <94:
                    "(Always Horny) Getting my ass felt up and getting paid? That's a win-win."
                    jump barmenu2
                show mce happy with d
                mc "I'm sorry boys, I'm not actually on the menu. I can take your drink orders though."
                "Yeah... I think it'd be a bit silly to use my body in such a petty way to get tips."
                "Maybe another day when I'm feeling more desperate, haha."
                scene bg bar with d
                play sound success
                $ moneygain = 15
                call moneygain from _call_moneygain_18
                "Other than that, the shift goes as normal, and I get paid a meager $[fmoney]."
                jump postworktrans
            "Let them feel your ass for the tip. (6 Sexual Desire, <94 Shame)" if True:
                if sd < 6 or shame > 94:
                    "No, not a chance!"
                    jump barmenu2
                show mce horny with d
                mc "Deal..."
                play sound success
                $ sdgain = 1
                $ shameloss = 2
                call shameloss from _call_shameloss_67
                call sdgain from _call_sdgain_101
                "(+[fsd] Sexual Desire, -[fshame] Shame)"
                scene bg bar
                show bar2a
                with d
                "Inconspicuously, I stand next to the tall student with my rear beside him."
                "With a casual tilt toward, leaning on his table, my butt becomes quite accessible with this short skirt."
                "It honestly makes me wonder just how many times I've accidentally flashed my panties while working here."
                play sound fondle
                show bar2b with d
                "!"
                "Eep! I feel fingers dig into my skin and squeeze my butt from behind."
                "No amount of preparation would have prevented this from catching me off guard."
                play sound fondle
                "... He just keeps squeezing! I thought it would just be a quick thing, but he really goes for it."
                "Mmphh... And I let him keep going..."
                show bar2c with d
                "Until, he's finally satisfied... And, I am a bit too..."
                scene bg bar
                show student3:
                    xpos 50
                show student4:
                    xpos 1200
                call clothesbar from _call_clothesbar_6
                show mce horny
                with d
                mc "Uhhm... Hehe..."
                stua "A well earned $5."
                "I take the two student's orders and continue my shift as normal..."
                scene bg bar
                show bar2d
                with d
                "All whilst my panties were a bit damp..."
                play sound success
                $ groped += 1
                $ moneygain = 20
                call moneygain from _call_moneygain_19
                "(Gained $[fmoney] over the entire shift!)"
                $ barroute += 1
                jump postworktrans
    if barroute == 3:
        "Back at the bar, and getting tips at a faster rate than ever."
        "At this rate, I think I'll be able to make $20 a day."
        "I think I'm starting to understand why we're paid so little, the tips are supposed to compensate."
        "It's pretty scummy, but that means there's no upper boundary to what I can earn, right?"
        "In the corner of my eye, I spy one of the students that flirted with me last time."
        "Ahh, it's the guy that {i}didn't{/i} get to touch my butt..."
        "Maybe, just maybe, I could do something for him."
        "I justify it in my head as merely a 'continuation' of what happened last time."
        show student4:
            xpos 1200
        with d
        stub "Ohh, hey! You're the easy girl from before."
        show mce neutral with d
        mc "H-Huh?! That's not what I want to be known as..."
        stub "Say, $10 if I can see your breasts, go on."
        show mce angry with d
        mc "Eh?! That's outrageous!"
        stub "Hey, no one's looking over here right now. What's the problem?"
        show mce neutral with d
        "But... That's technically asking less than before, isn't it? He didn't even ask to touch them... He only wants to {i}see{/i} them..."
        "Oh god..."
        stub "Come on, offer expires in... ten seconds."
        menu barmenu3:
            "Sexual Desire: [sd], Shame: [shame]"
            "Ignore their flirting." if True:
                if personality == 2 and sd > 10 and shame < 90:
                    "(Always Horny) Quick, quick! Say yes!"
                    jump barmenu3
                "I shake my head, and he looks away with a fairly neutral expression."
                "Flashing someone in public is too far, and I guess even he realizes that."
                scene bg bar with d
                "Other than that, the shift goes as normal."
                play sound success
                $ moneygain = 20
                call moneygain from _call_moneygain_20
                "(+$[fmoney])"
                jump postworktrans
            "Flash your breasts for a tip. (10 Sexual Desire, <90 Shame)" if True:
                if sd < 10 or shame > 90:
                    "No, I don't think so... Maybe if we weren't so blatantly in public."
                    jump barmenu3
                show mce horny with d
                mc "*Sigh* Five seconds, no touching?"
                stub "Heck yeah! I've always wanted to see 'em."
                "I roll my eyes and quickly undo the tie in my shirt."
                call clothesbar3 from _call_clothesbar3_2
                with d
                "Whether it's due to the cold or arousal, my nipples quickly erect to attention to the student's awe."
                "He gets a good eyeful before I tie the shirt back up."
                call clothesbar from _call_clothesbar_7
                with d
                stub "Damn, that was absolutely worth $10. Here!"
                play sound success
                "(+$10)"
                show mce neutral with d
                "It was worth $10 for him, but was it worth $10 for me...?"
                "I thank the student and return to my shift, that thought haunting me throughout the evening."
                scene bg bar with d
                "During the rest of the shift, I earn some extra money."
                play sound success
                $ moneygain = 30
                $ publicdisplays += 1
                call moneygain from _call_moneygain_21
                $ sdgain = 1
                call sdgain from _call_sdgain_55
                $ shameloss = 2
                call shameloss from _call_shameloss_33
                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                $ barroute += 1
                jump postworktrans
    if barroute == 4:

        "Phew... I think I should just relax this shift. I've been doing so many crazy things lately."
        "I should be able to get a decent pay through tips alone."
        show mce horny with d
        "I've learnt how to take advantage of my sexuality and assets to get more tips than before."
        "Having my work uniform be two sizes too small may have been a blessing in disguise."
        "After a fairly normal shift, I receive a fairly unremarkable pay."
        play sound success2
        $ moneygain = 20
        call moneygain from _call_moneygain_22
        show mce angry with d
        "(+$[fmoney])"
        mc "$[fmoney]? Meeehh!"
        "I'm getting sick of the low pay here."
        show student2:
            xpos 50
        with d
        stua "Heyy, why not come and have one on us if you're that short on money!"
        show student4:
            xpos 1200
        with d
        stub "Yeh, we'll buy you a few."
        show mce neutral with d
        mc "Huh?"
        "Looks like a good opportunity to socialize with some of the regulars."
        "(Alcohol will raise your sexual desire, and lower your shame for a single evening. It may cause you to do something you otherwise wouldn't. Careful!)"
        $ barroute += 1
        menu:
            "Sexual Desire: [sd], Shame: [shame]"
            "Ignore their invitation." if True:

                show mce laughing with d
                mc "Sorry, boys. I really need to be getting back home, I haven't eaten and I'm starving!"
                "It's a simple white lie, and they accept it with no problem at all."
                "Maybe I should have just accepted their offer? They seem like good people."
                play music club
                scene bg bar
                call clothesbar from _call_clothesbar_8
                show mce happy
                with d
                "Before I head home, I really need to pee!"
                jump br4pd
            "Accept the offer for a drink. (+10 Sexual Desire, -10 Shame)" if pregnancyshowing == 0:
                $ drunk += 2
                $ sd += 10
                $ shame -= 10
                if qlightweight == 1:
                    $ sd += 10
                    $ shame -= 10
                    "As a lightweight, you feel twice the effects from the alcohol."
            "Accept the offer for a drink. (Non-Alcoholic)" if pregnancyshowing == 1:
                pass
        show mce happy with d
        mc "Alright, lads! If you're offering, I could use a little something after my shift."
        stua "Yeah, you could! I saw how you were moving around, definitely overworked."
        mc "Ohh, it's not so bad!"
        scene bg black with d
        stop music
        "An hour and more than a single drink later..."
        play music club
        scene bg bar
        call clothesbar from _call_clothesbar_9
        show mce happy2
        show student2:
            xpos 50
        show student4:
            xpos 1200
        with d
        mc "Phew, I'm really starting to feel it."
        "I find myself quite enjoying the company of these guys. They're friendly, socialable and local."
        "It's always nice to make new friends at university."
        show mce angry with d
        "But aahhh, I really, really need to pee! I drank way too much."
        show mce happy with d
        mc "Sorry, boys, but I'm going to head out now."
        stua "It's been great, see you around."
        stub "Yeah! Have a nice night, [mc]."
        show mce laughing with d
        mc "Byyeeee!"
        label br4pd:
            pass
        stop music fadeout 5.0
        scene bg black with d
        scene bg toilets with d
        "Ahh, the toilets here are unisex."
        "I can definitely see the benefits for parents, but for a university bar? Seems a little extra."
        if pregnancyshowing == 1 or drunk == 0:
            "Whatevers, I get into one of the end stalls."
        elif True:
            "Whatevers, just drunk enough to turn my gait into a leisurely stumble, I get into one of the end stalls."
        show bg toiletstall with d
        play sound flush
        "Haaahhh... I held that in way too long..."
        show floatingpenis with d
        "Wait... What the heck is that? Am I hallucinating? There's just a random penis sticking out of the wall!"
        "Some muffled, nervous voice on the other side sounds..."
        stranger "$20?"
        mc "$20 for what?! Want me to slap it?"
        $ moneygain = 40
        call moneycalculate from _call_moneycalculate_2
        stranger "$[fmoney], then!"
        mc "$[fmoney]... That's more than my shift paid..."
        "Sighing, I look almost longingly at the cock, it does look quite nice..."
        if drunk > 0:
            "I don't know if that's me of the alcohol talking, but for some reason I can picture myself doing it."
        "Sitting here with my panties around my ankles, I'm starting to get aroused at the thought!"
        play sound success
        $ sdgain = 1
        call sdgain from _call_sdgain_56
        "(+[fsd] Sexual Desire)"
        menu br4m:
            "Sexual Desire: [sd], Shame: [shame]."
            "Scream!" if True:
                if personality == 2 and sd > 25 and shame < 80:
                    "(Always Horny) I really want that cock in my mouth."
                    jump br4m
                "I gasp for air, and then, scream!"
                hide floatingpenis with d
                "Haha, that made him put his cock away quickly."
                "And the man clumsily leaves the bathroom."
                "A gloryhole... I never thought I'd ever see something like that!"
                scene bg toilets
                "As I exit the toilet stall, I notice something interesting on the three end stalls."
                "There's a small 'GH', for 'gloryhole' drawn onto all three of these stall doors... The middle stall says 'F', while the others say 'M'."
                "So it wasn't a coincidence, I had just accidentally stumbled into something rather lewd."
                jump postworktrans
            "Ignore it." if True:
                if personality == 2 and sd > 25 and shame < 80:
                    "(Always Horny) I really want that cock in my mouth."
                    jump br4m
                "I grimace and finish off, pulling up my panties as I try my best to ignore the fleshy stick in my peripheral."
                hide floatingpenis with d
                "Eventually the guy gets the message and leaves me in peace."
                "A gloryhole... I never thought I'd ever see something like that!"
                scene bg toilets
                "As I exit the toilet stall, I notice something interesting on the three end stalls."
                "There's a small 'GH', for 'gloryhole' drawn onto all three of these stall doors... The middle stall says 'F', while the others say 'M'."
                "So it wasn't a coincidence, I had just accidentally stumbled into something rather lewd."
                "Quickly exiting the bathroom, I return home."
                jump postworktrans
            "Taste it... (25 Sexual Desire, <80 Shame)" if True:
                if sd < 25 or shame > 80:
                    "No, no way!"
                    jump br4m
                play music action fadein 5.0
                "Ahh, I can't resist. The idea of having that cock down my throat is just far too arousing."
                if pregnancyshowing == 0 or drunk >= 1:
                    "And I'm already sat here with my pussy out, it's all just too much for my drunk mind to handle."
                elif True:
                    "And I'm already sat here with my pussy out, it's all just too much for my aroused mind to handle."
                "Not wanting to get my work shirt messy, I pull at the knot in the middle and allow it to fall down as I get on my knees before the cock."
                label gloryholebj:
                    pass
                $ gloryholeblowjob = 1
                play ambience oral1 fadein 3.0
                scene gloryholebjb
                if tan == 1:
                    show gloryholebjbtan
                if hair == 1:
                    show gloryholebjh black
                if hair == 2:
                    show gloryholebjh blonde
                if piercingson == 1:
                    show gloryholebjpiercings
                show gloryholebj 1
                with d
                "I begin by bringing my mouth level to its tip and accepting it into my mouth, swirling my tongue around the edge of the glans for a high pleasure start."
                "Meanwhile my hands begin to naturally caress the cock, my left jacking it off while my right delicately massages the balls."
                if pregnancyshowing == 0 or drunk >= 1:
                    "As my thighs brush together I shiver with desire, there's something so hot and erotic about this, at least to my drunk, addled mind."
                elif True:
                    "As my thighs brush together I shiver with desire, there's something so hot and erotic about this."
                "Occasionally I suck the head, and flick my tongue across the sensitive tip of the erection. Experimenting just for fun in this sloppy blowjob."
                "I love the way it throbs in response to my movements, swelling up in my mouth."
                "I can't help but get more passionate, my finger grip moving faster as the desire to have my mouth filled up with hot cum grows."
                "Escalating further, I wrap my mouth around the glans and move it back and forth in a fucking motion, sucking and squeezing with each movement."
                "These motions are most similar to vaginal sex, it should be the easiest way to make him cum, and the tense throbbing in his cock is affirming my thoughts."
                if pregnancyshowing == 0:
                    "Using my drunken stamina I go all out to bring the stranger to climax, fucking his cock with the tight grip of my lips, while jacking him off quickly and flicking my tongue against his tip."
                elif True:
                    "Using the last of my stamina I go all out to bring the stranger to climax, fucking his cock with the tight grip of my lips, while jacking him off quickly and flicking my tongue against his tip."
                play sound cum
                show gloryholebj 2 with cum
                play sound cum
                show gloryholebj 2 with cum
                "And it works to great success as his cock unleashes several hot loads of cum into the back of my throat."
                play sound cum
                show gloryholebj 2 with cum
                play sound cum
                show gloryholebj 2 with cum
                "Load after load, I manage to swallow each and every drop. A feat even I wasn't quite expecting."
                stop ambience
                scene bg toiletstall with d
                "I finish up the job, and he withdraws his rapidly shrinking cock through the hole."
                if gloryholecall == 1:
                    return
                "And I'm rewarded with two $20 bills pushed through the gap. Yikes! I almost forgot about that."
                mc "T-Thanks..."
                show bg toilets with d
                "Awkwardly I redress myself and wait for the guy to leave before I excuse myself too."
                "A gloryhole... I never thought I'd ever try something like that!"
                "But as I exit the toilet stall, I notice something interesting on the three end stalls."
                "There's a small 'GH', for 'gloryhole' drawn onto all three of these stall doors... The middle stall says 'F', while the others say 'M'."
                "So it wasn't a coincidence, I had just accidentally stumbled into something rather lewd."
                play sound success
                $ moneygain = 40
                call moneygain from _call_moneygain_23
                $ sdgain = 1
                call sdgain from _call_sdgain_57
                $ shameloss = 2
                call shameloss from _call_shameloss_35
                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                $ blowjobs += 1
                jump postworktrans
            "(Smooth Operator) Steal" if personality == 3:
                "I'll lie, tell him to hand me the money first, then ditch him."
                mc "Okay, send the money through..."
                "I wait a few seconds, and the sucker does so."
                "I take the wad and slip it into my bag."
                "And then..."
                scene bg toilets
                "Run!"
                scene bg bar
                call clothesbar from _call_clothesbar_10
                show mce happy2
                with d
                "Heh, he'll have no idea it was me. Easy money."
                $ moneygain = 40
                call moneygain from _call_moneygain_24
                play sound success
                "(+$[fmoney])"
                jump postworktrans
    if barroute == 5:

        show mce neutral with d
        "I'm actually pretty agitated this entire shift."
        "Rather than merely be accepting of my meager pay, I'm actively looking for money making opportunities."
        "I don't know if I'd go as far as last time. But... If I can make good money doing that, there's gotta be something better I can do."
        show student1:
            xpos 50
        stu "Yooo, I can see your thong straps!"
        show mce horny with d
        mc "You can always see more for a little extra."
        "I respond with a practiced flirtatious voice. That'll definitely get me some tips, I hope."
        "For at least a $10 tip, I don't mind flashing my panties. That's easy peasy compared to what I've already done."
        stu "Huh? I'm not so sure about paying for something I'll forget, but how about something I'll remember you by?"
        mc "What do you have in mind, cutie?"
        stu "I'll buy your thong!"
        show mce angry with d
        mc "Eh?! But I've had this for ages, it's one of my favourites!"
        stu "Even better! Ever masturbated in them?"
        show mce neutral with d
        mc "Y-Yeah, I rub myself off in them from time to time."
        "I avoid the desire to cringe as I say that. I don't even know why I did, especially since it was mostly a lie. I guess a part of me was curious to see how much he'd pay."
        $ moneygain = 50
        call moneycalculate from _call_moneycalculate_3
        stu "Okay, how's $[fmoney]?"
        "A devil on my shoulder whispers to me, 'it may be your favourite, but $50 for something you paid $5 for is a x10 markup!"
        "The angel on my other shoulder rightly retorts, 'but your pussy will be exposed in this short skirt for the rest of your shift!"
        $ br5offer2 = 0
        menu br5offmenu1:
            "Ignore their offer." if True:
                if personality == 2 and sd > 30 and shame < 75:
                    "(Always Horny) Working without any panties... That's kinda hot."
                    jump br5offmenu1
                show mce sad with d
                $ br5offer2 = 1
                mc "No, no... But thanks for the offer anyway."
                $ moneygain = 60
                call moneycalculate from _call_moneycalculate_4
                stu "Wait, how about $[fmoney]]?"
                "I gulp and somehow I can't avoid considering his offer again."
                menu br5offmenu2:
                    "Ignore the new offer" if True:
                        show mce angry with d
                        mc "N-No, you're missing the point, it isn't about money."
                        stu "Oohh, right, right..."
                        stu "Damn, shame..."
                        "The student and I awkwardly glance at each other before I walk off and return to my shift."
                        hide student1 with d
                        "The rest of the shift goes well, and I manage to actually scrape a little extra from tips than usual."
                        scene bg black with d
                        play sound success
                        $ moneygain = 25
                        call moneygain from _call_moneygain_25
                        "(+$[fmoney])"
                        jump postworktrans
                    "Remove your panties and give them to the man. (25 Sexual Desire, <80 Shame)" if True:
                        if sd < 25 or shame > 80:
                            "No way! Just think of how many times I'll accidentally flash my pussy this shift."
                            jump br5offmenu2
                        show mce neutral with d
            "Remove your panties and give them to the man. (30 Sexual Desire, <75 Shame)" if True:
                if sd < 30 or shame > 75:
                    "No way! Just think of how many times I'll accidentally flash my pussy this shift."
                    jump br5offmenu1
        $ barroute += 1
        show mce horny with d
        play sound equip
        call clothesbar2 from _call_clothesbar2_2
        with d
        "I start by lifting up a knee, bringing my hands to my hips and slipping down my thong by its straps."
        "Carefully, I use my skirt to shield my pelvis to avoid flashing everyone as I slip my panties off one leg, then the next."
        "Awkwardly I crunch it up in my hand and hold it out to the student."
        if br5offer2 == 0:
            stu "Niiiiice... Here's a crisp $[fmoney]!"
            play sound success
            $ moneygain = 70
        elif True:
            stu "Niiiiice... Here's a crisp $[fmoney]!"
            play sound success
            $ moneygain = 80
        show mce happy with d
        mc "Thanks, I think! Uhmm, have fun?"
        stu "Ohhohhh, yeahhh, I will."
        "He puts them in his pocket and continues drinking, leaving me to continue my shift without any panties."
        hide student1 with d
        "Was that a good idea? I mean... It's not like I sucked someone's dick this time, and I got paid even more!"
        "Nothing wrong with just selling second-hand panties, right?"
        "I kinda like the idea that student is going to use my panties to masturbate with. I don't have to do much, and I still get paid."
        show mce horny with d
        "But, then again.. I'm commando in public... While I'm wearing a tiny skirt..."
        "For the rest of the shift I definitely have to hold my skirt down when I bend over."
        "Gosh, I'm becoming an absolute gremlin for money, aren't I?"
        "What next? Strip naked and run through a retirement home for $[fmoney]?"
        show mce laughing with d
        "Why am I genuinely weighing the pros and cons of that? Hahaha."
        scene bg black with d
        play sound success
        "And, you gain some additional money for completing your shift."
        play sound success
        call moneygain from _call_moneygain_26
        $ sdgain = 1
        call sdgain from _call_sdgain_58
        $ shameloss = 1
        call shameloss from _call_shameloss_36
        "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
        call shameloss from _call_shameloss_37
        jump postworktrans
    if gloryholeblowjob == 1 and gloryholesex == 0 and gloryholesex2 == 0:

        $ gloryholesex2 = 1
        "Let's try to keep all my articles of clothing this shift."
        "I wonder if I need to tone my behaviour down. If word gets out that I'm doing sexual favours for tips, I might get fired."
        "And I really don't want to get a reputation... Hard to get rid of that."
        "After a fairly normal shift, I receive a fairly unremarkable pay, but I'm pretty well known with the regulars now, and manage to squeeze a few more tips than usual."
        play sound success
        $ moneygain = 25
        call moneygain from _call_moneygain_27
        show mce happy2 with d
        "(+$[fmoney])"
        "Speaking of regulars!"
        show student2:
            xpos 50
        with d
        stua "[mc], drinks on us today?"
        show student4:
            xpos 1200
        with d
        stub "Yeah, come and take a breather, drinks taste better when you're around."
        "Looks like a good opportunity to socialize."
        "(Alcohol will raise your sexual desire, and lower your shame for a single evening. It may cause you to do something you otherwise wouldn't. Careful!)"
        menu:
            "Ignore their invitation." if True:
                show mce laughing with d
                mc "Sorry, boys, no time today!"
                "No need to lie, they accept it with no problem at all."
                hide student2
                hide student4
                with d
                show mce happy with d
                "Before I head out though, I just need to head to the toilet real quick."
                jump br6pd
            "Have 'a few' drinks with them. (+10 Sexual Desire, -10 Shame)" if pregnancyshowing == 0:
                $ drunk += 2
                $ sd += 10
                $ shame -= 10
                if qlightweight == 1:
                    $ sd += 10
                    $ shame -= 10
                    "As a lightweight, you feel twice the effects from the alcohol."
            "Have 'a few' drinks with them. (Non-Alcoholic)" if pregnancyshowing == 1:
                pass
        "Ahh, I can't resist having a few cold ones with the boys."
        scene bg black with d
        stop music
        "An hour and more than a single drink later..."
        play music club
        scene bg bar
        call clothesbar from _call_clothesbar_11
        show mce happy2
        show student2:
            xpos 50
        show student4:
            xpos 1200
        with d
        mc "I'm feeling that comfortable buzz!"
        "I enjoy chatting with my friends, and this good sociable atmosphere has made working here a breeze too."
        show mce neutral with d
        "But as I'm drinking and chatting, I can't get this image out of my head... The gloryholes in the back."
        "How much did I get last time? About $50? All I have to do is sit in there and wait..."
        "And that'd make me a total of $75 today."
        "I can't resist, I really can't."
        show mce happy with d
        mc "Sorry, boys, I just realized I have somewhere to be."
        stub "Have a nice night, [mc]."
        stua "Yeah! It's been great, see you around."
        show mce laughing with d
        mc "Byyeeee!"
        stop music fadeout 5.0
        scene bg black with d
        scene bg toilets with d
        "Half-sneakily, I slip into the toilets and manage to get into the middle gloryhole stall."
        label br6pd:
            stop music fadeout 5.0
        scene bg toiletstall with d
        "Thankfully it's empty, but that also means there aren't any customers."
        "I guess this gives me a fair opportunity to pee and contemplate the life choices that got me here."
        if gloryholeblowjob == 0:
            "Why did I choose to pee in the gloryhole stall..? Am I really feeling that tempted?"
        play sound flush
        "Double my day's wage for a blowjob? That is a lot of money, mmm..."
        "Ahh, I hear someone, and they went to the stall to my left."
        stranger "Someone in there?"
        "Huh...? I... recognize that voice..."
        "Oh god, it's one of the guys I was drinking with!"
        "Half-heartedly putting on a deeper, less recognizable voice, I reply..."
        mc "Yeah! I'm ready."
        $ moneygain = 80
        call moneycalculate from _call_moneycalculate_5
        stranger "Pussy for $[fmoney]?"
        mc "Uhh, uhmm..."
        "Completely caught off guard, I hadn't even thought of that as a possibility!"
        "I mean... I can see it now, as I picture myself pressing my ass against the hole, but..."
        "My god, doing that for $[fmoney]? I just... I don't know..."
        "With my panties already around my ankles, my loins burn with desire as I imagine it more and more."
        "Just what am I going to do?"
        show floatingpenis with d
        "Eek! His penis just appeared, and it looks amazing!"
        $ gloryholecall = 0
        menu brm6:
            "Sexual Desire: [sd], Shame: [shame]."
            "Blowjob only." if True:
                mc "S-Sorry, blowjobs only."
                $ moneygain = 30
                call moneycalculate from _call_moneycalculate_6
                stranger "Uhh, yeah, that's fine I guess. I'll do $[fmoney] for that."
                "J-Just $[fmoney]?"
                "I'm already in way to deep to back out now... Right?"
                play music action
                $ gloryholecall = 1
                call gloryholebj from _call_gloryholebj
                "My friend on the otherside slips in $30 and thanks me."
                "Gosh, if he only knew it was me... So crazy."
                "Awkwardly I redress myself and wait for the guy to leave before I excuse myself too."
                show bg toilets with d
                play sound success
                call moneygain from _call_moneygain_28
                $ sdgain = 1
                call sdgain from _call_sdgain_59
                $ shameloss = 1
                call shameloss from _call_shameloss_38
                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                $ blowjobs += 1
                jump postworktrans
            "Do it! (50 Sexual Desire, <60 Shame)" if True:
                if sd < 50 or shame > 60:
                    "Hah, no way!"
                    jump brm6
            "Code Red! Get out of there!" if True:
                if personality == 2 and sd > 50 and shame < 60:
                    "(Always Horny) I can't refuse him like this, I'm far too horny..."
                    jump brm6
                "I'm in way over my head, time to get out!"
                "With his dick in the hole, I have a headstart and quickly headout."
                jump postworktrans
            "(Smooth Operator) Steal" if personality == 3:
                "I'll lie, tell him to hand me the money first, then ditch him."
                "Putting on an unrecognizable voice, I whisper..."
                mc "Okay, send the money through..."
                "I wait a few seconds..."
                stranger "Half now, half after. Or no deal."
                "Hmph..."
                mc "Sounds good to me!"
                "He hands over half the money."
                "I take the wad and slip it into my bag."
                "And then..."
                scene bg toilets
                "Run!"
                scene bg bar
                call clothesbar from _call_clothesbar_12
                show mce happy2
                with d
                "Heh, he'll have no idea it was me. Easy money."
                $ moneygain = 40
                call moneygain from _call_moneygain_29
                play sound success
                "(+$[fmoney])"
                jump postworktrans
        play music action
        mc "Yeah, I'll do it."
        label gloryholesex:
            pass
        $ gloryholesex = 1
        play sound equip
        "His penis throbs once in place as I remove my clothing."
        $ condomon = 0
        if condoms > 0 and pregnancyshowing == 0:
            menu:
                "Use a condom? Condoms: [condoms]. [fertilityrate]."
                "Yeah." if True:
                    $ condomon = 1
                    $ condoms -= 1
                "Fuck the rules! (Without protection!)" if True:
                    $ condomon = 0
        play sound cum
        show gloryholesexb
        if tan == 1:
            show gloryholesexbtan
        if piercingson == 1:
            show gloryholesexpiercings
        if hair == 1:
            show gloryholesexh black
        if hair == 2:
            show gloryholesexh blonde
        if pregnancyshowing == 1:
            show gloryholesexe pregnant
            if tan == 1:
                show gloryholesexe tanpregnant
        with d
        "Alright... I take hold of his erection, and guide it into me as I push back against the wall of the stall."
        if virgin == 0:
            call virgin from _call_virgin_2
            "What a shameful way to lose my virginity."
            "But..."
        if pregnancyshowing == 0  or drunk >= 1:
            "This feels so naughty, and thrilling! I guess it's because I'm drunk, but my pussy is a lot more sensitive and wet than usual."
        elif True:
            "This feels so naughty, and thrilling! My pussy is a lot more sensitive and wet than usual."
        play sound sex
        "I start moving my butt back, and while the depth of motion is quite shallow, it focuses on some pleasureful points for both of us as his large cock presses against my clit."
        "I'm actually so wet, it's creating this lewd squelching sound. It's so hot, but it makes it so obvious we're fucking. I hope no one else comes into the toilets."
        "It's tight too, I can feel my insides squeezing and sucking around his throbbing shaft. My hips gyrate softly around the cock, and the student starts to rock his hips back and forth as we both fuck each other equally."
        "My back arches and I shudder as pleasure surges through me. The genuine catharsis of the moment is giving me goose bumps."
        "Moving faster, I start to bounce my hips against the stall wall, causing it to rattle. Orgasmic waves of bliss crash into my mind, melting my mind with desire."
        "The orgasm consumes my entire body as I spasm against the wall, my partner picks up the slack as he begins to pound my butt through the hole."
        "My pussy contracts and tightens rhythmically around his cock, even as it swells, indicating that ejaculation is imminent."
        play sound cum
        show gloryholesex cum with cum
        play sound cum
        show gloryholesex cum with cum
        "Cumming already! That didn't take long!"
        play sound cum
        show gloryholesex cum with cum
        play sound cum
        show gloryholesex cum with cum
        "He fills my pussy with his thick, hot cum in a formidable orgasm."
        if condomon == 0:
            call pregnancyroll from _call_pregnancyroll_5
        play sound cum
        stop ambience
        "I'm left panting a little as I pull away with a schlick."
        scene bg toiletstall
        with d
        if gloryholecall == 1:
            return
        "Wow, that was quite an experience..."
        play sound success
        "And as promised, the man slips his payment through the hole. I really ought to ask for payment before I do the deed next time..."
        "N-Next time? Did I really think that so easily?"
        "Ahh, who am I kidding. I just fucked a 'stranger's' cock in a public toilet stall. I hardly have standards at this point."
        play sound success
        $ barroute += 1
        $ moneygain = 80
        call moneygain from _call_moneygain_30
        $ sdgain = 1
        call sdgain from _call_sdgain_60
        $ shameloss = 1
        call shameloss from _call_shameloss_39
        "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
        $ vaginalsexes += 1
        $ status += 1
        "But hey, who says that needs to be a bad thing?"
        if qsecretlydepraved == 1:
            "The enjoyment of the depraved act causes you to gain an additional [fsd] sexual desire!"
            call sdgain from _call_sdgain_152
        scene bg black with d
        "With the coast clear, I sneak out of the bathroom and return home."
        jump postworktrans
    if gloryholesex == 1 and barthreesome == 0 and barthreesomeopportunity == 0:

        $ barthreesomeopportunity = 1
        "Today's shift is a little boring. I've gotten so confident doing this that it's becoming second nature and less of an adventure."
        "Although I still can't forget the crazy thing that happened last time. I actually fucked one of the regulars through the gloryhole..."
        "And I can barely look him in the eyes when he comes in with the usual friend."
        play sound success
        $ moneygain = 30
        call moneygain from _call_moneygain_31
        "I comfortably manage to complete my shift however, and even manage to break my record by earning $[fmoney]."
        show mce neutral with d
        "Although, I know that's not {i}really{/i} my record, is it?"
        show student2:
            xpos 50
        show student4:
            xpos 1200
        with d
        stua "Hey, come talk with us a second."
        mc "I-Is everything okay?"
        "Oh shit, it's them."
        stub "I didn't realize you were the gloryhole girl."
        show mce sad with d
        mc "N-No! You must be mistaken, that wasn't - I mean, I haven't..."
        stua "I saw you walk in there, [mc], and you didn't come back out."
        show mce neutral with d
        "Ahh, that's the guy I fucked too!"
        stua "This guy's a little jealous he didn't get an opportunity. If you're interested, maybe you could do something for both of us?"
        stub "Yeah, doesn't even have to be in the toilets, unless you prefer that for some reason."
        mc "Uuuhhhhhhh..."
        "I blank out slightly."
        menu brm7:
            "Sexual Desire: [sd], Shame: [shame]"
            "Refuse, and insist they have the wrong girl." if True:
                if personality == 2 and sd > 100 and shame < 40:
                    "(Always Horny) But they absolutely have the right girl..."
                    jump brm7
                mc "N-No, sorry. I'm definitely not that girl."
                stua "I see... Sorry for bothering you, then."
                hide student2
                hide student4
                with d
                "I slip away."
                "Am I really the 'gloryhole' girl, now?"
                "God damnit... I actually wanted to go there again today too."
                menu brm72:
                    "Visit the gloryholes" if True:
                        scene bg black with d
                        "Regardless, I manage to get into the toilets again and go to the designated toilet stall and wait."
                        scene bg toiletstall with d
                        "It doesn't take long for a customer to arrive, and he merely asks 'what do you do?'"
                        menu brm7b:
                            "Sexual Desire: [sd], Shame: [shame]"
                            "Vaginal (50 Sexual Desire, <60 Shame)" if True:
                                if sd < 50 or shame > 60:
                                    "Hah, no way!"
                                    jump brm7b
                                $ moneygain = 80
                                call moneycalculate from _call_moneycalculate_7
                                mc "I'll fuck you for $[fmoney]"
                                stranger "Hohh, yeah! That's awesome."
                                "The guy on the otherside slips in the payment and thanks me as he pushes his cock inside."
                                call gloryholesex from _call_gloryholesex
                                "I redress myself and wait for the guy to leave before I excuse myself too."
                                show bg toilets with d
                                play sound success
                                call moneygain from _call_moneygain_32
                                $ sdgain = 1
                                call sdgain from _call_sdgain_62
                                $ shameloss = 1
                                call shameloss from _call_shameloss_40
                                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                                $ status += 1

                                $ vaginalsexes += 1
                                jump postworktrans
                            "Oral (25 Sexual Desire, <80 Shame)" if True:
                                if sd < 25 or shame > 80:
                                    "I just... can't do it..."
                                    jump brm7b
                                $ moneygain = 40
                                call moneycalculate from _call_moneycalculate_8
                                mc "BJ for $[fmoney]."
                                stranger "Sweet, you got it."
                                "The guy on the otherside slips in the payment and thanks me as he pushes his cock inside."
                                "The difference to how I'd act before is stark. I'm so much more confident it kinda hurts."
                                play music action
                                call gloryholebj from _call_gloryholebj_1
                                "I redress myself and wait for the guy to leave before I excuse myself too."
                                show bg toilets with d
                                play sound success
                                call moneygain from _call_moneygain_33
                                $ sdgain = 1
                                call sdgain from _call_sdgain_63
                                $ shameloss = 1
                                call shameloss from _call_shameloss_41
                                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                                jump postworktrans
                            "Chicken out" if True:
                                "I'm not doing this."
                                show bg toilets with d
                                "I quickly leave the guy on the other side and return home."
                                jump postworktrans
                    "Go home" if True:
                        if personality == 2 and sd > 80 and shame < 60:
                            "(Always Horny) Let's go get some cock from the gloryholes first, hehe..."
                            jump brm72
                        "It's been a long, tiring shift anyway. Let's get out of here."
                        jump postworktrans
            "Accept?! (100 Sexual Desire, <40 Shame)" if True:
                if sd < 100 or shame > 40:
                    "I don't think so."
                    jump brm7
        label barthreesome:
            $ barthreesome = 1
        $ moneygain = 80
        call moneycalculate from _call_moneycalculate_9
        mc "$[fmoney] each?"
        "Fuck, did I just say that?"
        "What's wrong with me lately?"
        if massageroute4 == 1:
            "The massage parlour is one thing, but soliciting sex from people like this is kinda wild."
        elif True:
            "This is straight up prostiution! At least with the gloryhole I had an excuse that there was a wall of anonymity."
        stub "Hm... $[fmoney]? That's quite a lot."
        stua "I think that's fair, consider what we're asking."
        mc "The wage here just isn't enough, you know?"
        stub "Okay, but I want dp."
        mc "DP?"
        stua "Double penetration. You up for it?"
        mc "As long as you pay, whatever."
        scene bg black with d
        scene bg bedroomnight
        call clothesbar from _call_clothesbar_13
        show mce horny
        show student4:
            xpos 0
        show student2:
            xpos 1200
        with d
        play music action
        play sound equip
        call clothesunderwear from _call_clothesunderwear_2
        with d
        "I drop several articles of clothing to the floor, one by one as the students sit on my bed and wait."
        stub "Daaamn, that body looks as fine as I thought it would."
        stua "Yeah, definitely better than some gloryhole."
        mc "Ahh, don't be silly. My bar uniform barely hides more than this."
        play sound equip
        call clothesnude from _call_clothesnude_32
        with d
        mc "You should have saved your compliments until now."
        stub "Yeah, I'll have to keep that in mind for next time."
        "My loins are burning with desire. Which is fortunate, any sense of being nervous is slowly being replaced with lust"
        mc "Shall we get right to it, then? I think I'm ready."
        scene bg black with d
        play sound equip
        scene fmmthreesomeb
        if pregnancyshowing == 1:
            show fmmthreesomea pregnant
        if tan == 1:
            show fmmthreesomebtan
            if pregnancyshowing == 1:
                show fmmthreesomebtanp
        if hair == 1:
            show fmmthreesomeh black
        if hair == 2:
            show fmmthreesomeh blonde
        if piercingson == 1:
            show fmmthreesomepiercings
        show fmmthreesome 1
        if pregnancyshowing == 1:
            show fmmthreesomea pregnant
        with d
        "Getting onto the bed, I readily expose my lustfully wet pussy."
        mc "Well... Who wants which hole?"
        mc "Don't be shy, now."
        if pregnancyshowing == 0:
            if condoms > 0:
                menu:
                    "Condoms: [condoms]. [fertilityrate]."
                    "Use a condom?" if True:
                        $ condoms -= 1
                        $ condomon = 1
                    "Nah!" if True:
                        $ condomon =  0
        "The two students get undressed and position themselves in a way to tag-team me vaginally and anally."
        play sound cum
        show fmmthreesome 2
        with d
        "The first student lays down beneath me, and I get ontop of him in a pseudo-reverse cowgirl position as he positions his cock against my ass. With lubrication, his cock manages to slip inside just easily enough to not be uncomfortable."
        "The second student takes a more direct position infront of me and the bed, and fortunately it puts him at the perfect height to easily slide his cock into my pussy."
        play ambience sex fadein 3.0
        "They both clumsily roll their hips back and forth, fucking me slowly as I adjust to the girth."
        "And damn, I really need to adjust to the girth! It's intense, but it's delightful. It's like I'm experiencing the best of both worlds."
        "The intense feeling of being filled this much is exceptional, and as I slowly get used to it, the boys find their footing and begin thrusting in tandem with each other."
        "The guy on the bottom is especially eager, as the lubrication allows him to sink deeply and pound my tight ass however he likes."
        "Meanwhile my pussy only gets wetter allowing the second student to fuck me freely."
        "The pleasure builds tremendously, spiralling me closer to an orgasm, faster than I could have ever imagined."
        "I feel overwhelmed with a sense of languor, my mind blanking as pleasure fills my mind and body."
        "The two guys use me almost like a toy as they experiment and push themselves."
        "The position for them is just awkward enough to not let them go all-out and cum, meaning I have to endure their pounding for far longer than a normal session."
        "There's nothing but the deep feeling of being totally filled up, combined with the outrageous pleasure and constant orgasmic rises causing me to lose count."
        "My mind simply switches off and I just begin to 'feel' everything in such an attuned way."
        "There's nothing but bliss and ecstasy until the two guys find a pace that enables them to push towards their orgasms."
        "Going back and forth in intervals, my pussy is filled, and them my ass, faster and faster..."
        play sound cum
        show fmmthreesome 3 with cum
        play sound cum
        show fmmthreesome 3 with cum
        "Until they both erupt in a glorious crescendo of euphoria as they simultaneously stuff both my holes full of hot cum."
        play sound cum
        show fmmthreesome 3 with cum
        play sound cum
        show fmmthreesome 3 with cum
        stop ambience fadeout 3.0
        "Another few blasts of cum are enough to make me come again, as the guys fuck until they go sensitive."
        play sound cum
        show fmmthreesome 4 with d
        "They both pull out, creating a messy mixture of cum and my juices."
        if condomon == 1:
            "Thanks to the condom, I don't need to worry about getting pregnant."
        elif True:
            call pregnancyroll from _call_pregnancyroll_4
        "We all take a moment to cool down and catch our breath..."
        scene bg bedroomnight
        call clothesnude from _call_clothesnude_33
        show mce happy
        show student4:
            xpos 0
        show student2:
            xpos 1200
        with d
        mc "Well, I hope you enjoyed it. Thank you."
        stua "Want us to tell our friends, help you get some more business? Ahaha, just kidding."
        stub "Here's the pay."
        $ moneygain = 160
        call moneygain from _call_moneygain_34
        play sound success
        "(+$[fmoney])"
        "Goodness me, that's so much..."
        mc "Thank you! This really helps me a lot."
        stub "Right, then! See ya, [mc]."
        stua "Yeah, always happy to tip you at the bar."
        mc "Later, guys."
        hide student4
        hide student2
        with d
        show mce neutral with d
        "There was a very noticable air of awkwardness, even as they step out. It was pretty uncomfortable, actually."
        "I feel like the jovial atmosphere we had just chatting and drinking in the bar will never be something we can achieve again."
        "But that might not be the only thing I lost today."
        "Just what kind of person am I becoming?"
        "I don't feel myself at all."
        "The bright-eyed, innocent version of me that arrived here [days] days ago..."
        "Is that something that's gone forever too?"
        stop music
        play sound success
        $ sdgain = 2
        call sdgain from _call_sdgain_64
        $ shameloss = 2
        call shameloss from _call_shameloss_42
        "(+[fsd] Sexual Desire, -[fshame] Shame)"
        if qsecretlydepraved == 1:
            "The enjoyment of the depraved act causes you to gain an additional [fsd] sexual desire!"
            call sdgain from _call_sdgain_65
        $ status += 2
        $ vaginalsexes += 1
        $ analsexes += 1
        $ groupsexes += 1
        if persistent.barscare == False:
            $ persistent.barscare = True
            show red:
                alpha 0
            show red:
                linear 5.0 alpha 0.5
            play sound heartbeat
            show bg bedroomnight with pixellate
            pause 0.5
            play sound heartbeat
            show bg bedroomnight with pixellate
            pause 0.5
            play sound heartbeat
            show bg bedroomnight with pixellate
            pause 0.5
            play sound heartbeat
            show bg bedroomnight with pixellate
            pause 0.5
            play sound heartbeat
            show bg bedroomnight with pixellate
        elif True:
            mc "You did this."
        $ dream = 0
        jump morning
    if barroute >= 6:
        "Feeling confident, I breeze through this shift like it's no work at all!"
        "Question is, am I going to do something to try and get extra pay today?"
        menu br6m:
            "Sexual Desire: [sd], Shame: [shame]"
            "Just have a normal shift." if True:
                "Let's forget about money for today and have a normal shift."
                "Ahh, there's something relaxing about not having to try too hard."
                "And hey, I still get..."
                play sound success
                $ moneygain = 30
                call moneygain from _call_moneygain_35
                "(+$[fmoney]!)"
                jump postworktrans
            "Visit the glory holes." if True:
                scene bg black with d
                "Regardless, I manage to get into the toilets again and go to the designated toilet stall and wait."
                scene bg toiletstall with d
                "It doesn't take long for a customer to arrive, and he merely asks 'what do you do?'"
                $ gloryholecall = 1
                menu brm8b:
                    "Sexual Desire: [sd], Shame: [shame]"
                    "Vaginal (50 Sexual Desire, <60 Shame)" if gloryholeblowjob == 1:
                        if sd < 50 or shame > 60:
                            "Hah, no way!"
                            jump brm8b
                        $ moneygain = 80
                        call moneycalculate from _call_moneycalculate_10
                        mc "I'll fuck you for $[fmoney]"
                        stranger "Hohh, yeah! That's awesome."
                        "The guy on the otherside slips in $[fmoney] and thanks me as he pushes his cock inside."
                        call gloryholesex from _call_gloryholesex_1
                        "I redress myself and wait for the guy to leave before I excuse myself too."
                        show bg toilets with d
                        play sound success
                        $ moneygain = 80
                        call moneygain from _call_moneygain_37
                        $ sdgain = 1
                        call sdgain from _call_sdgain_66
                        $ shameloss = 1
                        call shameloss from _call_shameloss_43
                        "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                        $ gloryholesex = 1
                        $ vaginalsexes += 1
                        jump postworktrans
                    "Oral (25 Sexual Desire, <80 Shame)" if True:
                        if sd < 25 or shame > 80:
                            "I just... can't do it..."
                            jump brm8b
                        $ moneygain = 40
                        call moneycalculate from _call_moneycalculate_11
                        mc "BJ for $[fmoney]."
                        stranger "Sweet, you got it."
                        "The guy on the otherside slips in $[fmoney] and thanks me as he pushes his cock inside."
                        "The difference to how I'd act before is stark. I'm so much more confident it kinda hurts."
                        play music action
                        call gloryholebj from _call_gloryholebj_2
                        "I redress myself and wait for the guy to leave before I excuse myself too."
                        show bg toilets with d
                        play sound success
                        $ moneygain = 40
                        call moneygain from _call_moneygain_38
                        $ sdgain = 1
                        call sdgain from _call_sdgain_67
                        $ shameloss = 1
                        call shameloss from _call_shameloss_44
                        "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                        $ blowjobs += 1
                        jump postworktrans
                    "Chicken out" if True:
                        "I'm not doing this."
                        show bg toilets with d
                        "I quickly leave the guy on the other side and return home."
                        jump postworktrans
            "Seduce one of the customers. (75 Sexual Desire, <50 Shame)" if True:
                if sd < 75 or shame > 50:
                    "Not a chance!"
                    jump br6m
                "Well, I'm not against selling myself for sex. It's something I can enjoy and get paid to do."
                "Let's see... I need an easy target for the night, then I'll invite them back to my place after my shift..."
                "Ah, that guy."
                $ moneygain = 100
                call moneycalculate from _call_moneycalculate_14
                scene bg black with d
                "After flirting with the customer all night, I manage to entice him with the promise of sex for $[fmoney]."
                scene bg bedsex with d
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
                "Heh, that was so easy I almost feel bad. Some men just can't help themselves, can they?"
                "Then again, how can I talk? I can't help myself either!"
                mc "Now give me that thick, juicy cock!"
                $ condomon = 0
                if pregnancyshowing == 0:
                    if condoms > 0:
                        menu:
                            "Condoms: [condoms]. [fertilityrate]."
                            "Use a condom?" if True:
                                $ condoms -= 1
                                $ condomon = 1
                            "Nah!" if True:
                                $ condomon =  0
                "With my legs held up high, I teasingly wiggle my butt and spread my cheeks."
                play sound cum
                play ambience sex fadein 2.0
                show legs-upsex 2 with d
                call virgin from _call_virgin_3
                "He taps the tip of his cock against my mound a few times before lining it up with my vagina and pushing in deep."
                "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                "With my legs held together like this, it feels tighter and totally amazing for me. I love the way it grinds against all the sensitive spots deep inside."
                mc "Aahhh, mmmpphhmmm... Your cock feels great!"
                "Encouraged by my moans, he starts to thrust faster while reaching down to rub my clit."
                "Even as the customer, he generously treats me as a lover, giving me as much pleasure as possible."
                "And that pleasure soon overwhelmes me, turning my mind blank as my body trembled towards a powerful orgasm."
                mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                play sound cum
                show legs-upsex 2
                with cum
                "I tightly grip my ass and legs as I climax, my pussy clenching hard around the customer's throbbing cock."
                "And he only speeds up, motivated by my climax, he pushes towards his own."
                play sound cum
                show legs-upsex 3 with cum
                play sound cum
                show legs-upsex 3 with cum
                "His tight cock explodes a hot load deep into my pussy as he ravishes me."
                play sound cum
                show legs-upsex 3 with cum
                play sound cum
                show legs-upsex 3 with cum
                "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                play sound cum
                show legs-upsex 4 with d
                stop ambience fadeout 3.0
                "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my labia and butt."
                if condomon == 1:
                    "Thanks to the condom, I don't need to worry about getting pregnant."
                elif True:
                    call pregnancyroll from _call_pregnancyroll_7
                scene bg black with d
                "Afterwards, we clean up and my client leaves."
                play sound success
                call moneygain from _call_moneygain_39
                $ sdgain = 1
                call sdgain from _call_sdgain_68
                $ shameloss = 1
                call shameloss from _call_shameloss_45
                "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame)"
                $ status += 1
                $ vaginalsexes += 1
                jump postworktrans
            "Take the two customers threesome offer. (100 Sexual Desire, <40 Shame)" if barthreesome == 0 and gloryholesex == 1:
                if sd < 100 or shame > 40:
                    "I don't think so."
                    jump br6m
                $ barthreesomeopportunity = 0
                show student2:
                    xpos 50
                show student4:
                    xpos 1200
                with d
                mc "Heyyy, uhhh..."
                jump barthreesome


scene bg bedroomnight with d
call clothespjs from _call_clothespjs_5
show mce happy
with d
"After my shift at the bar, I return home late and fall asleep soon after."
jump morning

init:
    $ gloryholeblowjob = 0
    $ gloryholesex = 0
    $ barthreesome = 0
    $ gloryholecall = 0
    $ barthreesomeopportunity = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

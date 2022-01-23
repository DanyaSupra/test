label studio:
    if studiounlocked == 0:
        "Unlock this location by having <70 Shame."
        if shame <= 70:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump studiounlock
                "Back" if True:
                    pass
        jump postworldmap
    play music studio
    if studioroute1 == 0:
        $ studioroute1 += 1
        scene bg street with d
        call clothes from _call_clothes_37
        show mce happy
        with d
        mc "Hmm... What's this?"
        "'Looking for amateur actresses to particpate in popular internet movies, instant cash!'"
        mc "Ooohh! Well, I gotta check this out."
        scene bg studio with d
        call clothes from _call_clothes_38
        show mce happy
        with d
        "Cozy! The sofa looks quite nice. Although a little worn perhaps."
        "Opposite the sofa and table is a reception. While there's no one currently at the desk, someone notices me and greets me."
        show stranger1:
            xpos 1200
        stranger "Hey there, how can I uhh, help you?"
        show mce happy2 with d
        mc "Hello! I saw the advert out the front, about amateur actresses, right?"
        if lewdoutfit or nude == 1:
            stranger "I see! Judging by your appearance, you'll fit right in."
        elif True:
            stranger "I see, I see! You'll be very welcome."
        stranger "You'd definitely be accepted, we could actually start right now, but I do need you to sign a consent contract."
        show mce neutral with d
        mc "Eh? Ohh, so you can use my likeness in your material? Wait, what are we filming?"
        stranger "Perhaps it'd be best if you just read the form..."
        show mce laughing with d
        mc "Okie dokie! Show me your worst."
        show mce happy with d
        "Being an actress sounds like fun! Might be easy money..."
        show mce neutral with d
        "Hmm, this is quite a long contract, I guess this is the kind of thing you just skip and sign like the terms and conditions on a website..."
        "Ahh, nudity, huh?"
        mc "Uhhm, what kind of nudity will this be?"
        stranger "We'll pay you based on how extreme the act is."
        if sd > 80:
            "So it's thaaat kind of 'acting', I feel really stupid for not realizing it earlier."
            mc "Awesome, I might build myself up to the naughtier acts then."
            stranger "You're considering this long term? We usually do one girl and move on, but you'd probably be quite popular."
        elif sd > 40:
            "Is this porn? Hmm..."
            mc "Do you take actresses that just do oral and blowjobs?"
            stranger "A young student like yourself? Sure, we could market you as an innocent virgin."
            if virgin == 0:
                mc "But I am an innocent virgin!"
                stranger "Even better."
        elif True:
            "I don't know what he means, but I'm not entirely sure if I'd be comfortable acting in the nude."
            "I mean, even if I was a background extra my parents would want to watch the movie."
        menu sm1:
            "Sexual Desire: [sd], Shame: [shame]"
            "Sign the contract?"
            "Accept (40 Sexual Desire and <60 Shame)" if True:
                if sd < 40 or shame > 60:
                    "I have a strange feeling in my gut, and if this is a lewd thing, I'm definitely not ready for it."
                    jump sm1
                $ studioroute1 += 1
                stranger "Alright! Now we're talking."
                dire "You can call me the director, I'll be filming your movies."
                mc "Mm, okay! What are we going to do first?"
                jump studioroute1
            "Back out" if True:
                mc "Ahh, I think I'll need to think about it a little more! Sorry."
                stranger "That's fine. You can keep hold of the contract."
                "I sheepishly take the contract and return home. I might search what these guys do on my laptop later."
                jump worldmap
    elif studioroute1 == 1:
        scene bg studio with d
        call clothes from _call_clothes_39
        show mce happy
        show stranger1:
            xpos 1200
        with d
        stranger "Oh, it's you again. Here to do a shoot?"
        jump sm1
    elif studioroute1 == 2:
        jump studioroute2

label studioroute2:
    scene bg studio with d
    call clothes from _call_clothes_88
    show mce happy
    show stranger1:
        xpos 1200
    with d
    "I step into the shady 'studio' again, and the director soon joins me at the reception."
    if lewdoutfit == 1 or nude == 1:
        dire "Heh, look at you. Are you eager to film, or something?"
    if studioroute2intro == 0:
        $ studioroute2intro = 1
        dire "It's great to see you again. Your video performed excellently on XTube."
        if xtube1 == 1:
            "XTube? I use that! I should search for my video tonight."
        dire "Want to see the video?"
        if xtube1 == 1:
            "Oh, nevermind."
        show mce laughing with d
        mc "Go for it! It'll be weird seeing me in a third person perspective like that."
        scene bg thecouch
        show lyingb
        if pregnancyshowing == 1:
            show lyinge pregnant
        if tan == 1:
            show lyingbtan
            if pregnancyshowing == 1:
                show lyingbtanp
        if hair == 1:
            show lyingh black
        if hair == 2:
            show lyingh blonde
        if piercingson == 1:
            show lyingpiercings
        show lying 1
        with d
        pause 0.5
        scene bg black
        show bg thecouch
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
        pause 0.5
        scene bg black
        show bg thecouch
        show doggy2b
        if pregnancyshowing == 1:
            show doggy2e pregnant
        if tan == 1:
            show doggy2tan
            if pregnancyshowing == 1:
                show doggy2tanp
        if hair == 1:
            show doggy2h black
        if hair == 2:
            show doggy2h blonde
        if piercingson == 1:
            show doggy2piercings
        show doggy2 1
        with d
        pause 0.5
        if studioroute1sex == 1:
            play sound cum
            show doggy2 4alt with cum
            pause 0.3

            "Ahh, it even shows me getting fucked! Oh my god! I can't believe there's a video of me getting fucked on the internet!"
            "It didn't really hit me until now, but, aahhh!"
        scene bg studio with d
        call clothes from _call_clothes_41
        show mce horny
        show stranger1:
            xpos 1200
        with d
        dire "Great video, right?"
        mc "Y-yeah! I think so."
        dire "Let's do another!"
        mc "Uhhhmmm..."
    menu studiorm1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Double Penetration Video (80 Sexual Desire, <20 Shame)" if studioroute4 == 1:
            if sd < 80 or shame > 20:
                "Something that intense? No way! It's bad enough that there are videos out there that my parents could see."
                jump studiorm1
            show stranger2 with d:
                xpos 50
            mc "Oh, there’s someone else here today?"
            if studioroute5 == 0:
                dire "Uh yeah, he’s uh… Just a friend."
                show mce horny with d
                mc "I see… Is he joining in?"
                unknown "Join in what?"
                dire "Well, I wasn't planning on her coming today, but she’s here to get fucked, you interested?"
                unknown "Hah, how’d you land this hottie?"
                dire "Money, that’s all."
                unknown "Well fuck, I guess it must be worth it."
                show mce neutral with d
                stop music fadeout 3.0
                "Somewhat speechless, I watch the two friends lounge around, and- what on earth is that?"
                dire "We were going to inject some of this new stuff, it’s called Euphoria, and apparently it feels even better than sex."
                dire "Hey, why don’t we compare? You in?"
                mc "I-I’m not really… I mean, I’m just here for the film…"
                unknown "Ah come on, we’ll treat you. I’ll show you how it’s done, totally safe, c’mere."
            elif True:
                mc "Oh, it's you again! Hiya!"
                unknown "Hey, nice to see you."
                unknown "You here to take some Euphoria with us? Or are you just the dessert?"
            "Pulling out a needle, the stranger beckons me to sit next to him."
            $ drugtaken = 0
            menu:
                "Accept (???)" if True:
                    $ finaldrugtaken = 1
                    $ drugtaken = 1
                    $ drugstaken += 1
                    "Cautiously I allow the man to inject the unknown substance into my arm."
                    unknown "Just relax for a bit, and let the best fucking feeling in the world take over."
                    "I lay back on the black couch as her injects the director, and then himself."
                    "It doesn’t take long at all…"
                    "I feel extremely sluggish, and euphoric."
                    "Woah… It’s like I’m floating on a cloud."
                    scene bg black with d
                    stop ambience fadeout 3.0
                    pause 1.0
                    "And then, I’m gone."
                    pause 1.0
                "Refuse" if True:
                    mc "No, really… I’m not taking anything."
                    unknown "You don’t know what you’re missing."
                    "He injects the director, and them himself. The effects kick in extremely quickly and the languor, euphoria and relaxation is immediately clear by their body language."
                    mc "How are you two supposed to fuck me if you’re spaced out?"
                    dire "We’re a little more lucid than you think… It just feels so good that we probably look a little dopey."
                    mc "What’s that even supposed to mean?"
                    unknown "He means, we can fuck you, and it’ll feel even better than if we were sober."
                    mc "Set the camera up, and give me your best shot, then."
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
            show standingdp 1
            play sound2 foreplay2 fadein 3.0
            play ambience doublepenetration fadein 3.0
            if drugtaken == 1:
                show black border
                show black:
                    linear 2 alpha 0.5
                    linear 2 alpha 0.1
                    repeat
                with d
                "Briefly flickering in and out of consciousness, I feel myself relentlessly railed in both holes at once, only adding to the intense, unbelievable euphoria that’s shattering my mind and body."
            with d
            mc "Uuuaa, oooo… Aaaahhhh! My mind is blank…"
            "The director fucks my soaking wet pussy with reckless abandon. I’m so wet that there’s no resistance, no matter how deep and how fast he goes, my body wholly accepts it."
            "Meanwhile at my backside, the stranger pounds my anus, which offered a little more resistance, lowered by the lubricant we ended up using. Even so, it was tight, extremely tight."
            "Having both holes filled up from this angle made both my pussy and ass clench. The pressure I was exerting around the two men was enough to really milk them for all they’re worth."
            dire "Phewww, I could get used to this!"
            "Precum was streaming out of the tip, mixing with my fluids."
            "Moaning loudly, I throw my head back against the other man."
            unknown "Tcch! What an ass! It keeps squeezing."
            "Using me like a toy, the two men both pound me, their faces warped with pleasure."
            if drugtaken == 1:
                "Between this and the drug, my mind is broken with pleasure. All I can really make out between the pure ecstasy was the wet sound of our bodies hitting together."
                "I was losing my mind, being thoroughly used, and all on camera too. But my mind was so messed and addled with pleasure that nothing else mattered except getting the next drop of pleasure."
            elif True:
                "I was a lot more lucid than them, since I didn’t take anything, I was in more control than you’d expect as I rocked my hips back and forth. I play my part appropriately for the camera, while still enjoying every drop of pleasure that comes my way."
                "Each time their members roughly pushed in and out, I clamped my holes down all whilst grinding my ass for them."
            "Drooling and groaning, I reach my limit and I’m overwhelmed by a genuinely powerful orgasm."
            "And their cocks swell up in my slippery walls, as they too were brought to climax, milked by my pussy."
            dire "Aaaaa, fuuuck!"
            unknown "Can’t hold on! *Pant*"
            play sound cum
            show standingdp 2 with cum
            play sound cum
            show standingdp 2 with cum
            "Hot, thick semen bursts out both holes almost simultaneously. This aids my own orgasmic trance, as I moan loudly and rock my hips."
            play sound cum
            show standingdp 2 with cum
            play sound cum
            show standingdp 2 with cum
            stop ambience fadeout 1.0
            stop sound2 fadeout 1.0
            "Semen seeps into my womb and ass, all whilst my body squeezes and tries to milk them for more."
            if drugtaken == 1:
                scene bg black with d
                "And then- I’m gone. Again."
                scene bg thecouch
                show lyingb
                if pregnancyshowing == 1:
                    show lyinge pregnant
                if tan == 1:
                    show lyingbtan
                    if pregnancyshowing == 1:
                        show lyingbtanp
                if hair == 1:
                    show lyingh black
                if hair == 2:
                    show lyingh blonde
                if piercingson == 1:
                    show lyingpiercings
                show lying 1b
                show lyingcum
                show black border
                show black:
                    linear 2 alpha 0.5
                    linear 2 alpha 0.1
                    repeat
                with d
                mc "Ehh…?"
                "I don’t even sit up; I just merely lay in a haze as I try to get my head together."
                "Eugh, am I still high? Probably a little."
                "The ‘studio’ is empty… I check my phone and it’s quite late too."
                "Seems like there’s cum dripping from my ass and pussy, that’s not a surprise, but I don’t think he used a condom…"
                call pregnancyroll from _call_pregnancyroll_23
                mc "They could have at least put me in the recovery position… Assholes."
                "I take the situation surprisingly well, I suppose I did consent to everything that happened. Also, there’s some money left behind for me, so I guess they’re not all bad."
                "Sluggishly, I get up and stumble around to collect my things."
                play sound equip
                scene bg studio
                call clothes from _call_clothes_89
                show mce neutral
                show black border
                show black:
                    linear 2 alpha 0.5
                    linear 2 alpha 0.1
                    repeat
                with d
                "I get dressed, take my money and head out."
                "It's not even that much after everything I've been through..."
                "I should probably never come back here…"
                scene bg black with d
            elif True:
                scene bg black with d
                scene bg studio
                call clothesnude from _call_clothesnude_59
                show mce happy
                "Practically dropping me when they’re done, I seem to be the last left standing as they wearily stumble back onto anything they can sit on."
                mc "Looks like you boys overdid it. I feel great, though!"
                "Wordlessly they brush me off, but it’s all too clear that they’re not up for anything more. It’s up to me to turn off the camera, then."
                dire "Eehh, pay yourself. There’s money on the counter."
                unknown "Hey, that’s my money!"
                dire "I’ll get you some more later, chill. The porn videos are paying plenty."
                "I take some of the money left and decide it’s probably best to leave these two to their bad decisions."
            $ moneygain = 140
            $ groupsexes += 1
            $ status += 2
            $ vaginalsexes +=1
            $ analsexes += 1
            $ studioroute5 = 1
        "Sex Video 2 (70 Sexual Desire, <30 Shame)" if studioroute3 == 1:
            if sd < 70 or shame > 30:
                "This guy's a pretty bad influence, so... I should probably stop working with him."
                jump studiorm1
            dire "Great to see you."
            "Taking out a lighter, the director ignites what seems to be a self-made cigarette, but judging by the smell it’s definitely not tobacco."
            show mce laughing with d
            mc "Mm, yup! Somehow you’ve still not scared me off."
            if studioroute4 == 0:
                dire "I’ve got a new idea for a sex video."
                show mce horny with d
                mc "Oh right? Let’s here it."
                mc "No nonsense as always, perfect. Essentially there’s this popular pose, and I figured you’re likely an athletic hero, you’ll be able to do this no problem."
                scene bg black with d
                "The director spends a few moments showing me the pose online."
                scene bg studio
                call clothes from _call_clothes_90
                show mce happy
                show stranger1:
                    xpos 1200
                with d
                dire "What do you think?"
                mc "Hmm… Yeah, I bet I can do that."
            dire "Let me just finish off my blunt… Hm, you might as well have one too while you’re waiting. I already have another rolled up."
            if studioroute4 == 0:
                show mce neutral with d
                mc "Having me take some strange substance again, eh? You’re a bad influence, you know."
                dire "I’m making you shoot porn for money, nothing about this is good."
                show mce happy with d
                mc "Ah… That’s kinda harsh, being a sex worker isn’t so bad…"
                dire "And you’re saying my smoking is? It’s just something to relax you, don’t be such a suckler for the rules. Lighten up."
                "He hands me the other blunt."
            $ drugtaken = 0
            menu:
                "Go for it." if True:
                    $ drugstaken += 1
                    $ drugtaken = 1
                    "Throwing caution to the wind, I bring the cigarette to my lips, and light it myself."
                    play sound hypnosis
                    show green with d:
                        alpha 0.1
                    dire "*Cough* You’re right, you know… I really shouldn’t be encouraging you to get into this stuff. *Puff*"
                    show mce laughing with d
                    mc "Hmph, now you say that? *Puff*"
                    dire "I suppose a part of me is just trying to get rid of it, so I don’t have as much of it to smoke myself."
                    dire "But it’s not really fair for me to leverage that onto you."
                    show mce neutral with d
                    mc "What, you have a problem, or something?"
                    dire "Don’t we all? We all find ways to cope."
                    dire "How about you? Anything you do to cope with the stresses of your daily life?"
                    mc "Hm… I think I might be becoming a sex addict. But I mean… not really…"
                    dire "Heh… If only bad things didn’t feel so good."
                "Refuse" if True:
                    dire "Your loss… You’ll have to wait for me to finish, then. *Puff*"
                    mc "That’s fine, I’ve got my phone on me."
            scene bg black with d
            play music action fadein 3.0
            mc "How’s this? It’s not an easy pose, but I’m flexible enough to just barely get it!"
            show jackob
            if tan == 1:
                show jackobtan
            if pregnancyshowing == 1:
                show jackoe pregnant
                if tan == 1:
                    show jackoe tanpregnant
            if hair == 1:
                show jackoh black
            if hair == 2:
                show jackoh blonde
            show jacko 1
            if drugtaken == 1:
                show green:
                    alpha 0.1
            with d
            dire "Phew, your fat ass is really accentuated from this pose! I bet your pussy is going to be extremely tight too!"
            mc "Hmph, if you wanna fuck me, that’ll costs extra."
            dire "*Whipering* Ohh, yes! Pretend you’re a prostitute!"
            mc "Pretend? I am a prostitute! I’m fucking you for money, dolt!"
            dire "Oh yeah, I guess you are…"
            dire "Let me just get a few more angles of your ass first! Such a fine ass, such a damn fine ass."
            "While circling around the camera, he settles behind me and begin teasing my wet pussy"
            mc "Mmphh, that feels so good… Haaahh…"
            dire "Well… I’m going in!"
            "After gliding the tip back and forth against my labia, he finally sinks it inside."
            play sound cum
            show jacko 2 with d
            call virgin from _call_virgin_11
            "Pushing all the way in, he doesn’t waste time rocking his hips back and forth. It’s a little fast at first, but I manage to adapt fairly easily."
            dire "Ohhh, this tight pussy never gets old."
            mc "Ohh, pretty amazing, right? Worth every penny."
            play ambience sex fadein 1.0
            play sound2 foreplay2 fadein 3.0
            "His cock throbs rhythmically in my pussy as he only speed speeds up, pounding my ass with enough force to create wet slapping sounds."
            "With a fair amount of effort, I maintain the difficult position and avoid falling forward. I can’t help but feel a little proud at that."
            "Hmm, the camera is on my face too, I better play it up so the footage is good."
            mc "Aaahhh, your cock… It’s so thick… I’ve already come like twice on it!"
            dire "R-Really? I feel like I’m going to come soon!"
            "No… Not really… I don’t feel as much pleasure doing this for work as I do for leisure."
            "He tenses up, as his fingers dig into my hips for leverage."
            mc "That’s right! I want you to fill me up!"
            "While maintaining pace, he starts doing long, deep, sensual thrusts, and it feels really good."
            mc "Oohhh, that’s it! Right there! A little faster!"
            "I start to feel the pleasure more and more as he begins to mess up my sensitive insides."
            mc "Mmphh, y-you’re actually going to make me come too!"
            "It doesn’t take long until we’re both going fast and intense again."
            dire "Auughh! That’s it, I’m gonna cum!"
            mc "Ahh, mmphh, me too!"
            play sound cum
            show jacko 3 with cum
            play sound cum
            show jacko 3 with cum
            "Instantly, my pussy is filled up by several waves of thick jism."
            play sound cum
            show jacko 3 with cum
            play sound cum
            show jacko 3 with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 3.0
            "There’s so much that it splatters out, dribbling down my thighs and dripping onto the floor."
            mc "Mmphh, yeaahhh… *Pant, pant*"
            play sound cum
            show jacko 4 with d
            "Fatigued, the director pulls out of my well-fucked pussy, causing even more cum to seep out."
            mc "Oophhh… I think I’m stuck in this position…"
            dire "Uhh, need some help?"
            mc "Y-Yes please…"
            scene bg black with d
            scene bg studio
            call clothesnude from _call_clothesnude_60
            show mce happy
            show stranger1:
                xpos 1200
            if drugtaken == 1:
                show green:
                    alpha 0.1
            with d
            "My body cricks and aches as I accept the payment for the shoot. That one was tough! It’ll take me a few hours to recover from fucking in that pose."
            $ moneygain = 120
            show mce happy2 with d
            if studioroute4 == 0:
                mc "Ahh, you're paying me a little more than last time? Thanks for that, director."
                dire "What can I say? Your videos are popular, you can always check them out on XTube, they’re getting five figure view counts now."
                show mce neutral with d
                stop music fadeout 3.0
                mc "D-Damn… That many people are seeing me get fucked?"
                "I shudder a little, unnerved at the thought."
                dire "Yep! You get way more views than the other bimbos I bring in."
                show mce angry with d
                mc "Heyy, I’m not a bimbo!"
                dire "Exactly, that’s why you get paid. People recognize the good stuff when they see it."
                dire "They click this, and they see an innocent girl too horny and needy for her own good. They feel that authenticity."
                show mce neutral with d
                mc "What are you even talking about… I’m putting on an act for the camera, and being more enthusiastic because you pay me for it…"
                dire "Heh, but you’re still a real person, and the person watching knows that. The story behind the actress is sometimes more interesting than the person they’re playing."
                dire "And anyway, I clickbait that you’re a ‘Neohero Student’ in every video."
                show mce angry with d
                mc "YOU DO WHAT?! REMOVE THAT RIGHT NOW!"
                mc "What if someone were to search Neohero City and recognize me! Oh my god! You’re such a dick!"
                dire "I’m sorry, I’m sorry! I’ll change it to just ‘Student’."
                show mce neutral with d
                mc "Hmph… I’m outta here…"
                dire "Alright, swing by any time."
                play ambience ambienceday
                scene bg street with d
                call clothes from _call_clothes_91
                show mce neutral
                with d
                "That guy… He doesn’t respect me at all."
                "I really am just an object for him to profit off, and that’s obvious by the subtext of everything he says."
                "Calling me a bimbo, and desperate, among other things…"
                "I-I’m not a bimbo! I-I’m not… desperate…"
                "Oh god, I’m fucking on camera just for a pittance of what I intend to earn…"
                "Everything he’s saying… It’s completely true, isn’t it?"
                "Eugh… I need to get over myself. What I’m doing isn’t anything to be ashamed of!"
                "I’m empowered, he’s not using me, I’m using him! That’s right… That’s right…"
            $ studioroute4 = 1
            $ vaginalsexes += 1
            $ status += 1
        "Sex Video 1 (60 Sexual Desire, <40 Shame)" if studioroute2 == 1:
            if sd < 60 or shame > 40:
                "A porn video? If I record that, it'd exist even longer than my debt."
                jump studiorm1
            if studioroute1sex == 1:
                dire "I know this isn’t your first rodeo, but let’s do a ‘proper’ sex shoot."
                mc "Yeah, you really blew your load with that ‘moving slow’ thing you suggested at first."
            elif True:
                dire "Let’s do a ‘proper’ sex shoot."
            if studioroute3 == 0:
                show mce horny with d
                mc "Sounds good. A sex shoot sounds like it’d be even easier than a blowjob one."
                dire "Yeah, quite likely. It’ll be mostly my job."
            dire "So, if you don’t mind me, I’m just gonna take a hit to prepare."
            show mce neutral with d
            if studioroute4 == 0:
                mc "A hit?"
                "Pulling out a baggy of white powder, the director snorts the strange stimulant, causing him to shudder."
                dire "Here, I made a line for you too."
                mc "Uhh, what is it?"
                dire "It’s called ‘Sugar’, makes everything feel more fun and exciting. Definitely good for this line of business, I ensure you."
            elif True:
                dire "You want some?"
            $ drugtaken = 0
            menu:
                "Go for it." if True:
                    $ drugstaken += 1
                    $ drugtaken = 1
                    play sound hypnosis
                    show bg studio with vpunch
                    show pink with d:
                        alpha 0.1
                    "Throwing caution to the wind, I bring my nose to the line and snort in a smaller amount than him."
                    dire "That’a’girl!"
                    show mce laughing with d
                    mc "*Sniff* Anything to make porn acting more tolerable, haha, kidding."
                "Refuse" if True:
                    dire "Yeah, no worries. This shit ain’t cheap anyway, consider it a potential bonus if you ever change your mind."
                    mc "Right… I’ll stick to just fucking for now."
            scene bg black with d
            dire "Alright, I’m ready, lay down and lift up your legs. We’re going in hard and tight."
            mc "How’s this?"
            play music action fadein 3.0
            play sound equip
            scene bg thecouch
            show buttupb
            if tan == 1:
                show buttupb tan
            if hair == 1:
                show buttuph black
            if hair == 2:
                show buttuph blonde
            show buttup 1
            if drugtaken == 1:
                show pink:
                    alpha 0.2
            with d
            dire "Phew, your fat ass is really accentuated from this pose! I bet your pussy is going to be extremely tight too!"
            if drugtaken == 1:
                $ condomon = 0
                mc "Yess! Fuck my tight pussy raw!"
            elif True:
                $ condomon = 1
                mc "You might have to go a little slowly, oh, and don’t forget the condom."
                dire "Right you are, boss, let me grab that."
            dire "Such a fine ass, such a damn fine ass."
            play sound cum
            show buttup v2 with d
            "He begins by teasing my wet pussy, gliding the tip back and forth against my labia, until he finally sinks it inside."
            mc "Mmphh, that feels so good… Haaahh…"
            call virgin from _call_virgin_12
            play sound2 foreplay2 fadein 2.0
            play ambience sex fadein 2.0
            "Pushing all the way in, he doesn’t waste time rocking his hips back and forth. It’s a little fast at first, but I manage to adapt fairly easily."
            dire "Oh yeah? Do you like my thick cock inside of you, bitch?"
            if drugtaken == 1:
                mc "Ohh, yesss… I love it when you call me names, do it again!"
            elif True:
                mc "U-Uhmm, y-yeah... Aahhh, hahhh..."
            "His cock throbs rhythmically in my pussy as he only speed speeds up, pounding my ass with enough force to create wet slapping sounds."
            if drugtaken == 1:
                "Excitable from the powder stimulant, my hips instinctively grind back and forth to get as much pleasure as I can."
            dire "Eugghh, yes! You are just a worthless whore, coming in here and getting fucked for cash."
            "H-Hey, that’s a little too real! But the sex is too fast and frantic for me to dwell on that for long."
            if drugtaken == 1:
                mc "Aaahhh, *sniff*, your cock… So thick…"
            dire "I feel like I’m going to come soon!"
            "He tenses up, as his fingers dig into my hips for leverage."
            mc "W-Wait, don’t come yet! I’m not even close!"
            if drugtaken == 1:
                mc "Keep going, keep going! *Sniff* I want to come around your cock."
            "Understandably, he slows down ever so slightly. If not for me, for the footage he’s recording from his handheld camera."
            "Instead of fast, shallow thrusts, he starts doing long, deep, sensual thrusts, that really tickle my deep spots."
            mc "Fuuuuck, that’s it! Right there! A little faster!"
            "And then, he starts doing fast, deep thrusts, beginning to really mess up my sensitive insides."
            mc "FUUUCK!"
            "It doesn’t take long until we’re both going fast and intense again."
            dire "That’s it, I’m gonna cum!"
            mc "Yeah, yeah, me too!"
            play sound cum
            show buttup v3 with cum
            play sound cum
            show buttup v3 with cum
            "Explosively and instantly, my pussy is filled up with a barrage of hot cum."
            play sound cum
            show buttup v3 with cum
            play sound cum
            show buttup v3 with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 3.0
            "To such a degree that it seeps out, and pools around my thighs, ass and the sofa."
            mc "Mmphh, yeaahhh… *Pant, pant*"
            play sound cum
            show buttup 4 with d
            "Fatigued, the director pulls out of my well-fucked pussy, causing even more cum to dribble out."
            if drugtaken == 1:
                mc "Ahh… *Sniff* I want to go again…"
            dire "Do it yourself, then. We’re done here."
            mc "Hmph… Was the footage good?"
            scene bg black with d
            scene bg studio
            call clothesnude from _call_clothesnude_61
            show mce happy
            show stranger1:
                xpos 1200
            if drugtaken == 1:
                show pink:
                    alpha 0.2
            with d
            dire "We got some good footage."
            show mce horny with d
            mc "Ahh, great. We’re getting pretty efficient at this."
            dire "That’s mostly because we’re not doing it ‘properly’. We're recording ourselves fucking. But that’s a better deal for both of us."
            show mce happy with d
            mc "I see… Well, I’m happy as long as I get paid."
            dire "Absolutely, your videos get a lot of views."
            $ moneygain = 100
            if studioroute4 == 0:
                hide stranger1 with d
                show mce neutral with d
                "So… Is this not a real porn studio? What exactly is this, then? Just some guy hiring prostitutes for amateur porn, and profiting off them?"
                "He doesn’t seem to be doing so bad for himself either, his drug habit has gotten more expensive."
                play sound equip
                call clothes from _call_clothes_92
                with d
                "Regardless of what I think of it, it happened. All I can do for now is get dressed, and get paid."
                if drugtaken == 1:
                    show mce happy with d
                    "I’m still completely overexcited from snorting that stuff… Feels really good, can’t lie. Not a bad employment benefit, heh."
            $ vaginalsexes += 1
            $ status += 1
            $ studioroute3 = 1
            if condomon == 0:
                call pregnancyroll from _call_pregnancyroll_24
        "Paizuri Video (50 Sexual Desire, <50 Shame)" if True:
            if sd < 50 or shame > 50:
                "I don't really like the idea of recording something so pornogrpahic."
                jump studiorm1
            show mce horny with d
            if studioroute2 == 0:
                mc "Is this like a blowjob while using my breasts? I don’t mind that… Even if it is for a porn video."
                dire "We can shoot it amateur-style if you’d like."
                mc "Amateur? What’s that?"
                dire "Essentially that’d just be you giving me a regular blowjob while I record."
                mc "Oh, uhm… Sure!"
            dire "You seem a little tense, here, why not take some of this to take the edge off?"
            "Reaching into a strange baggie, he takes out a blue tablet and offers it to me."
            show mce neutral with d
            if studioroute2 == 0:
                mc "W-What the heck is that?"
                dire "Yeah, it’s nothing serious. It’s called Blue, just something on the market that people are taking these days to relax."
                mc "Eehhh…"
            elif True:
                mc "That again?"
            $ drugtaken = 0
            menu:
                "Take it?" if True:
                    $ drugstaken += 1
                    $ drugtaken = 1
                    show mce horny with d
                    mc "Ah, I’m already doing something ridiculous, why not?"
                    "I take the tablet, place it on my tongue and swallow it."
                    if studioroute2 == 0:
                        mc "Won’t we be done before this kicks in?"
                        dire "Not these ones, these aren’t just some shit off the street, this stuff goes hard and quick."
                        show mce neutral with d
                        mc "Uhh, I wish you’d have told me that before I had it!"
                        "I shiver slightly as my body flushes. Whether that was a mistake or not, I’ll know soon."
                    elif True:
                        "I shiver slightly, my body already anticipating the feel-good tingly effects."
                    play sound hypnosis
                    show blue with d:
                        alpha 0.1
                    show mce happy with d
                    mc "Thanks, I guess…"
                "Refuse." if True:
                    $ drugtaken = 0
                    show mce happy with d
                    mc "Nah… I’m just here to work, but uhh, thanks?"
            dire "You’re welcome, let’s get to work, then."
            scene bg black with d
            if drugtaken == 1:
                "Hot and hazy, I undress and lower myself between the legs of the other actor, as he directs the camera at me."
            elif True:
                "We both undress and I lower myself into position as he directs the camera at me."
            play music action fadein 3.0
            play sound equip
            scene bg thecouch
            show paizurib
            if tan == 1:
                show paizuribtan
            if hair == 1:
                show paizurih black
            if hair == 2:
                show paizurih blonde
            if piercingson == 1:
                show paizuripiercings
            show paizuri 1
            if drugtaken == 1:
                show blue:
                    alpha 0.1
            with d
            if studioroute2 == 0:
                mc "Mphh, how intimate…"
                dire "Don’t say anything stupid."
            play ambience oral1 fadein 3.0
            if studioroute2 == 0:
                show paizuri 1b with d
                mc "S-Sorry… *Lick*"
            dire "Try dirty talking."
            show paizuri 1 with d
            mc "Uhmm… Gosh, your cock is so big… Mmphh… Aahh…"
            "He nods as I twirl my tongue around his tip, coating it with a lot of saliva."
            if drugtaken == 1:
                "My heart has started beating really fast, whatever I took is kicking in, leaving me feeling hot and horny. I can’t help but get a little more excited and passionate into the messy blowjob."
            elif True:
                "He really does have a nice cock, and as I worship it with my tongue, it leaves me feeling wet and excited."
            dire "You have a fantastic pair of tits, actually, how about you lift yourself up and put them to good use?"
            if drugtaken == 1:
                mc "Haaah, haahh… Yeah…"
                show paizuri 2 with d
                "Without really thinking, as if it were a blur, I lift myself up and encapsulate the entirety of his cock in my pillowy breasts."
            elif True:
                mc "Ohh, I bet you’d like that, wouldn’t you?"
                show paizuri 2 with d
                "I lift myself up and encapsulate the entirety of his cock in my pillowy breasts."
            play sound2 sex fadein 3.0
            "The saliva acts as perfect lubrication as I begin to grind his cock between my breasts. I put my entire body into it to deliver the most sensual experience possible."
            dire "Ohh, not bad! Keep it up, you slut!"
            if drugtaken == 1:
                "Slut… Yeaaahhh…"
            elif True:
                "S-Slut? That was probably just for the camera."
            "I follow his lead, and play into my role like an actress should. After all, this is a porn shoot, not exactly an act to be enjoyed."
            if drugtaken == 1:
                "I’m starting to feel a little wired, and tingly. Haahh… I should just focus on the titjob."
            "I squish my breasts together tightly around his throbbing shaft and use my hands to aid the movement of my body."
            "With my hands in the mix, this allows me to speed up, and he reacts favourably to it. I keep it up in the hopes of bringing him to climax."
            mc "Mmphh, *Chu*, cum for me, big boy!"
            if studioroute2 == 0:
                if drugtaken == 1:
                    "I can’t tell if this drug is making me horny or not, but my pussy is absolutely dripping right now."
                elif True:
                    "I'm so horny! My pussy is absolutely dripping..."
            "Biting my lip, I watch the tip of his cock swell up as it prepares to unload."
            play sound cum
            show paizuri 3 with cum
            play sound cum
            show paizuri 3 with cum
            "Pushing forwards and moving my hands faster, he’s successfully brought to climax."
            play sound cum
            show paizuri 3 with cum
            play sound cum
            show paizuri 3 with cum
            "Several lavish loads of cum end up in my hair, on my face and dripping down my breasts. I can’t help but enjoy it, no acting needed."
            stop ambience fadeout 1.0
            stop sound2 fadeout 1.0
            dire "Phew, your tits are as good as they look."
            mc "Mm, I’m glad you liked them…"
            scene bg studio
            call clothesnude from _call_clothesnude_62
            show mce happy
            show stranger1:
                xpos 1200
            if drugtaken == 1:
                show blue:
                    alpha 0.2
            with d
            "I pull away and clean myself up a little, the director soon joins in wiping off a few stray drops of cum with a wet wipe."
            if drugtaken == 1:
                show mce neutral with d
                "Oh god, standing up and not focusing on something has suddenly made me realize how out of it I am right now."
                "Everything looks so blue..."
                if studioroute2 == 0:
                    mc "Haahh… I’m so hot, I need some water."
                    dire "Oh, no you don’t, your body isn’t as thirsty as you think."
                    mc "B-But… Eugh… Haahh…"
                elif True:
                    mc "Haahhh... I need to get fucked..."
                scene bg black
                show bg thecouch
                show lyingb
                if pregnancyshowing == 1:
                    show lyinge pregnant
                show lyingb
                if pregnancyshowing == 1:
                    show lyinge pregnant
                if tan == 1:
                    show lyingbtan
                    if pregnancyshowing == 1:
                        show lyingbtanp
                if hair == 1:
                    show lyingh black
                if hair == 2:
                    show lyingh blonde
                if piercingson == 1:
                    show lyingpiercings
                show lying 1b
                if drugtaken == 1:
                    show blue:
                        alpha 0.3
                with d
                "I lay down on the black couch and catch my breath."
                if studioroute2 == 0:
                    dire "Hey, don’t you feel good?"
                    mc "Y-Yeah, I do, actually… I feel all cuddly and excited…"
                    mc "Hey, why don’t you come and sex with me? No fair that only you got anything from that…"
                dire "How can I refuse that? I’m glad you’re enjoying the special mix I gave you."
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
                show missionarysex 2
                if drugtaken == 1:
                    show blue:
                        alpha 0.4
                with d
                call virgin from _call_virgin_13
                $ status += 1
                $ vaginalsexes += 1
                play ambience sex fadein 1
                play sound foreplay2 fadein 1
                mc "Aahh, haaahhh.. Y-Yesss, fuck me! Mmphhh…"
                play sound cum
                if pregnancyshowing == 1 and tan == 0:
                    show missionarysexa pregnant2
                show missionarysex 3
                with cum
                "Why am I so horny? Haaahhh, fuuuuck! I-I’m gonna come!"
                play sound cum
                show missionarysex 4
                with cum
                stop ambience fadeout 1.0
                stop sound2 fadeout 1.0
                "Oh… I wasn’t the only one who came…"
                show missionarysex 5 with d
                dire "Don’t sweat it, I had a condom on."
                mc "W-Wait, are you recording?"
                dire "’Course, I am, this is a porn studio. You’ll get paid for any footage you produce."
                mc "Haahhh… Right…"
            elif True:
                mc "How’d I do?"
                if studioroute2 == 0:
                    dire "A little tense, but I’m surprised how much you were willing to push past your inexperience to do your best."
                elif True:
                    dire "Really good, you're getting better at this."
                mc "What can I say? If I do a good job, I’ll get paid what I deserve, right?"
                dire "Oh yes, absolutely."
            play sound equip
            scene bg black with d
            scene bg studio
            call clothes from _call_clothes_40
            show mce happy
            show stranger1:
                xpos 1200
            if drugtaken == 1:
                show blue:
                    alpha 0.2
            with d
            "I get dressed, and get paid."
            $ moneygain = 70
            $ studioroute2 = 1
        "Nude Shoot" if True:
            call nudeshoot from _call_nudeshoot
            "Standing up and moving back, the director zips his pants back up and returns to the reception desk."
            "Guess I'll get dressed too..."
            play sound equip
            scene bg studio with d
            call clothes from _call_clothes_42
            show mce neutral
            with d
            dire "Fantastic, another great video for our website. You'll be a hit."
            mc "Sure, can I have the money?"
            $ moneygain = 50
            call moneygain from _call_moneygain_62
            "He takes out $[fmoney] and hands it to me."
            if genericvariable == 1:
                "Sooo... I didn't get paid more for getting penetrated? Eugh..."
            mc "Thank you! Uhhmm, I think I'll head out now."
            dire "Do come back."
            scene bg black with d
            $ folgain = 5
            "With the video uploaded, the slight amount of attention causes me to gain a slight following from it! (+[ffol] Followers!)"
            scene bg street with d
            call clothes from _call_clothes_43
            show mce neutral
            with d
            "Ahh, working there feels weird, but the pay is excellent."
            $ sdgain = 1
            $ shameloss = 1
            $ masturbations += 1
            call shameloss from _call_shameloss_79
            call sdgain from _call_sdgain_116
            play sound success
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            jump postworktrans
        "Leave" if True:
            jump worldmap
    $ pornshoots += 1
    $ folgain = 2 + fol/100
    $ sdgain = 1
    $ shameloss = 1
    play sound success
    call moneygain from _call_moneygain_79
    call folgain from _call_folgain_25
    call sdgain from _call_sdgain_170
    call shameloss from _call_shameloss_120
    "(+$[fmoney])"
    call folgain from _call_folgain_26
    "The upload of my porn media gets spread around slightly, causing me to gain a few followers indirectly. (+[ffol] followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans

label studioroute1:
    "The director scratches his chin as he eyes me up and down."
    dire "For you, I think we'll take it slowly. How about just some nude modelling for now?"
    if sd > 50:
        mc "No problem at all. How much money will that be paying, though?"
    elif True:
        mc "E-Eh? Nude modelling, I guess I can do that for the right pay..."
    dire "Don't worry about the money, our lovely ladies get paid more than enough in straight cash."
    "The director takes out his wallet and slips out a few bills, it's enough to pique my interest."
    show mce happy2 with d
    mc "Okay! That should be good."
    dire "Okay, undress and try this pose."
    show mce neutral with d
    mc "Uhhhmm, like this?"
    label nudeshoot:
        pass
    $ pornshoots += 1
    scene bg black
    show bg thecouch
    show lyingb
    if pregnancyshowing == 1:
        show lyinge pregnant
    show lyingb
    if pregnancyshowing == 1:
        show lyinge pregnant
    if tan == 1:
        show lyingbtan
        if pregnancyshowing == 1:
            show lyingbtanp
    if hair == 1:
        show lyingh black
    if hair == 2:
        show lyingh blonde
    if piercingson == 1:
        show lyingpiercings
    show lying 1
    with d
    "Laying on my back, I push out my breasts as the director moves his camera over my body, already recording."
    "Oh gosh, I feel a heat in my cheeks as I grow nervous. What do I say, what do I do? People online will see this!"
    if studioroute2intro == 0:
        dire "So is this your first porn shoot?"
        "Ah?! Why is he asking questions?"
        mc "Uhh, yeah! I've never done anything like this before..."
        if chatfaproute2 == 1:
            "Does being a camgirl count? Probably, probably not? This does feel different."
        dire "What made you come here today?"
        mc "I thought it'd be a fun way to earn some money, heh... I guess I don't like to think about it much."
        dire "Are you going to the college?"
        mc "Yeaaahhh, it's soooo expensive..."
        dire "You'll definitely get some cash doing this. But maybe you'll get more if you spread your legs."
        mc "Uhmm, pardon?"
    "Lowering the angle of his camera, the director positions himself infront of me and aims the camera at my pussy."
    scene bg black
    show bg thecouch
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

    "Almost instinctively my thighs tense up slightly, but I gradually ease up and spread them slightly. I follow up by gliding a finger up and down my vulva."
    "Even I'm slightly shocked by how wet I am... When did this happen?"
    if studioroute2intro == 0:
        mc "Is this what you want?"
        dire "Yeaahh, I think you'll be very popular online, and you know what they say about very popular girls in this industry."
    "My fingers speed up slightly."
    if studioroute2intro == 0:
        mc "Uuuhhm, what do they say about popular girls?"
        dire "They earn tons of money."
    "I keep my finger pressed against my sensitive clit, rubbing faster, and squirming a little as pleasure runs through me."
    if studioroute2intro == 0:
        mc "Ahh, i-is that so? Mmm..."
    "The director holds the camera steady on my pussy as I freely masturbate to the view of potentially anyone online."
    "I'm just horny enough for this strange situation to not prevent me from enjoying myself, although admittedly there's something enjoyable about doing something so lewd in the first place."
    "Rubbing faster, I start to get closer to my orgasm. My body tenses up and my clit throbs as I prepare to push for the finish."
    dire "Okay, let's turn around and get a good shot of your butt."
    mc "Ahh, wha? O-Okay..."
    "Just short of my orgasm, I disappointedly stop and turn around. Damnit, I really needed that... I was so close."
    scene bg black
    show bg thecouch
    show doggy2b
    if pregnancyshowing == 1:
        show doggy2e pregnant
    if tan == 1:
        show doggy2tan
        if pregnancyshowing == 1:
            show doggy2tanp
    if hair == 1:
        show doggy2h black
    if hair == 2:
        show doggy2h blonde
    if piercingson == 1:
        show doggy2piercings
    show doggy2 1
    with d

    play music action fadein 3.0
    "I click my tongue as I lift my butt into the air and show myself off to the camera."
    "It was naive of me to assume shooting adult videos would be so easy, it's not as simple as just coming on camera, is it?"
    dire "Excellent! Your ass really is your best asset."
    mc "Hehe, it is pretty nice, isn't it?"
    "The director unzips his pants and begins to fondle his already erect cock. The swift and sudden nature of his actions cause me to briefly panic."
    "But I'm left more confused on how I should feel more than anything. Not just confused but... Horny..."
    "How come he gets to masturbate, but I have to pose like this? Grr..."
    dire "You like this cock, hm?"
    mc "Ah? Y-Yeah, uhm, maybe..."
    "Moving into position behind me, he... Heyy, we didn't agree to this..."
    "He starts to grind the tip of his cock up against my labia, my highly aroused and sensitive state can't help put stifle a few moans as he does so."
    "It's so frustrating, I really want to cum, but, but...!"
    menu sr1m2:
        "Resist your urges." if True:
            if personality == 2:
                "I can't resist! I really need to come!"
                jump sr1m2
            $ genericvariable = 0
            play sound equip
            scene bg studio with d
            call clothesnude from _call_clothesnude_63
            show mce neutral
            show stranger1:
                xpos 1200
            with d
            "I wiggle out of the way and awkwardly stand up."

            mc "Uuhhmmm... Let's not go there."
            dire "That should be great, a fun little tease at the end there for people that want more."
            mc "R-Right!"
        "Let him fuck you!" if True:
            $ genericvariable = 1
            $ studioroute1sex = 1
            "I just let it happen. I keep my ass raised up, and soon enough I feel his tip pressing against the entrance to my pussy."
            "And then...!"
            play sound cum

            play ambience sex
            play sound2 foreplay1
            play sound cum
            show doggy2 2 with d
            "Aaahhh, his cock slides straight inside! Oh gosh, no condom either..."
            if virgin == 0:
                $ virgin = 1
                "I'm such a fool; losing my virginity like this..."
            "Mmphh, but that's the last of my worries right now, as he begins to pound me from behind."
            mc "Aahh, that's juuuust what I needed, mmm..."
            dire "You're so wet! God damn."
            "I can barely contain myself as the pleasure comes rushing back all at once. My mind goes blank with bliss as I tightly grip the couch."
            mc "Ohhh, aaahh, c-coming! Ahhh!"
            "More primal lust than sense, the orgasm hits me like a truck. The director, who continues filming me from behind, fucks me wildly. It's actually incredible."
            "Although the reason for his fast pace becomes clear, as his cock swells and throbs inside me."
            play sound cum
            show doggy2 4alt with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 2.0
            "Pulling out, he quickly jacks himself off to a finish. He ejaculates several generous loads onto my ass, pussy and thighs, all whilst praising me."
            play sound cum
            show doggy2 4alt with cum
            dire "Yeaahh! Excellent work."
            mc "Meehh..."
            "The post-nut clarity hits me like a truck, and I realize I was probably used there."
            if sd > 60 and shame < 50 or personality == 2:
                "But it's okay, right? I had fun, and I'll probably get paid more."
            $ vaginalsexes += 1
            $ status +=1
    if studioroute2intro == 1:
        return
    "Standing up and moving back, the director zips his pants back up and returns to the reception desk."
    "Guess I'll get dressed too..."
    play sound equip
    scene bg studio with d
    call clothes from _call_clothes_44
    show mce neutral
    with d
    dire "Fantastic, fantastic. I'll be uploading this onto our website, but you'll get your cut right now."
    mc "O-Okay, can I have the money?"
    $ moneygain = 50
    call moneygain from _call_moneygain_63
    "He takes out $[fmoney] and I sheepishly accept it."
    if genericvariable == 1:
        "Sooo... I didn't get paid more for getting penetrated? Eugh... What a sleazy bastard."
    mc "Thank you! Uhhmm, I think I'll head out now."
    dire "Alright, come back later if you're interested in recording another video."
    scene bg black with d
    $ folgain = 5
    call folgain from _call_folgain_16
    "With the video uploaded, the slight amount of attention causes me to gain a slight following from it! (+[ffol] Followers!)"
    scene bg street with d
    call clothes from _call_clothes_45
    show mce neutral
    with d
    "What a strange experience!"
    "Is this industry right for me? Having another person in charge, telling me what to do, and not necessarily being trustworthy is somewhat concerning."
    "But $[fmoney] for an hour of work? That's good, right? I mean, that's amazing."
    $ sdgain = 1
    $ shameloss = 1
    $ masturbations += 1
    call shameloss from _call_shameloss_80
    call sdgain from _call_sdgain_117
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans

init:
    $ studioroute1sex = 0
    $ studioroute2intro = 0
    $ studioroute1 = 0
    $ studioroute2 = 0
    $ studioroute3 = 0
    $ studioroute4 = 0
    $ studioroute5 = 0
    $ studioroute6 = 0
    $ studioroute7 = 0
    $ drugtaken = 0
    $ drugstaken = 0
    $ finaldrugtaken = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

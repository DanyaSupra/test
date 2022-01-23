label trueending:
    stop music fadeout 1.0
    if persistent.trueendstage1 == True and persistent.trueendstage2 == False:
        if persistent.trueendintro > 0:
            scene trueendingbgwindow1:
            show trueendingbgwindow2:
                alpha 0
                linear 3.0 alpha 1.0
                linear 3.0 alpha 0
                repeat
            show trueendingbg1:
            show trueendingbg2:
                alpha 0
                linear 5.0 alpha 1.0
                linear 5.0 alpha 0
                repeat
            call trueendtacotable from _call_trueendtacotable
            show te satisfied
            with dissolve
            if persistent.trueendintro == 1:
                jump trueendintro1
            elif persistent.trueendintro == 2:
                jump trueendintro2
            elif persistent.trueendintro == 3:
                jump trueendintro3
            elif persistent.trueendintro == 4:
                jump trueendintro4
            elif persistent.trueendintro == 5:
                jump trueendintro5
        elif True:
            jump glassbreak2
    elif persistent.trueendstage2 == True:
        jump posttrueendingintro
label trueendingintro:
    scene bgglitchedbedroom
    show bg crystalball
    menu:
        "Are you sure?"
        "Yeah" if True:
            $ persistent.trueendstage1 = True
            if analsexes > 3:
                $ persistent.analsexes = "[analsexes]"
            if virgin == 0:
                $ persistent.virgin = 0
            elif virgin == 1:
                $ persistent.virgin = 1
            $ persistent.mc = mc
            play sound glasssmash
            show brokenglass with hpunch:
                alpha 0.3
            $ renpy.block_rollback()
        "No" if True:
            jump endings
    label glassbreak2:
        scene bgglitchedbedroom
        show mc nude
        show 1a:
            xalign 0.5
            linear 0.33 alpha 1.0
            linear 0.33 alpha 0.25
            repeat
        show 2a:
            xalign 0.5
            linear 0.44 alpha 0.25
            linear 0.44 alpha 1.0
            repeat
        show 3a:
            xalign 0.5
            linear 0.55 alpha 1.0
            linear 0.55 alpha 0.25
            repeat
        show 4a:
            xalign 0.5
            linear 0.66 alpha 0.25
            linear 0.66 alpha 1.0
            repeat
        show mce neutral
        show bg crystalball:
            xpos 0 ypos 0
        show brokenglass:
            alpha 0.3
    menu:
        "No turning back."
        "Yeah" if True:
            play sound glasssmash
            show brokenglass2 with hpunch:
                xalign 0.45 yalign 0.45
                alpha 0.4
    menu:
        "No turning back."
        "Yeah" if True:
            play sound glasssmash
            show brokenglass3 with hpunch:
                xalign 0.55 yalign 0.55
                alpha 0.5
            pause 0.1
    play sound glasssmash2
    play ambience buzz
    show brokenglass:
        alpha 0.3
        linear 0.5 ypos 2000
    show brokenglass2:
        xalign 0.45 yalign 0.45
        alpha 0.4
        linear 0.5 ypos 2000
    show brokenglass3:
        xalign 0.55 yalign 0.55
        alpha 0.5
        linear 0.5 ypos 2000
    show bg crystalball:
        linear 0.5 ypos 2500
    with vpunch
    pause 3.0


    play sound taco_whoami
    voice sustain
    persistent.mc "Who… am I?"

    hide 4a
    show mce surprised
    with d
    play sound taco_whoareyou
    voice sustain
    persistent.mc "Who are… you?"
    hide 3a
    hide 2a
    with d
    play sound taco_ihavefinally
    voice sustain
    persistent.mc "I have finally…"
    hide 1a
    show mce happy
    with d
    play sound taco_separated
    voice sustain
    persistent.mc "Separated…"
    show glitch1
    pause 0.5
    $ persistent.trueendintro = 1
    label trueendintro1:
        play sound taco_woopsmybad
        voice sustain
        "Uhhmm… Woops, my bad!"

        play sound taco_iwasjusttryingto
        voice sustain
        "I was just trying to…"
        stop ambience
        scene black
        play sound reset1
        pause 0.5
        show expression "splash1" with dissolve
        play sound reset2
        pause 0.75
        show expression "splash2" with dissolve
        play sound reset3
        pause 1.0
        play sound glitch2
        show main_menu2 with dissolve
        pause 7.5
        stop sound
        scene bg college with d
        play music intro fadein 3.0
        show mc nude
        show mco uniform
        show mce happy2
        with d
        "Hello!"
        "I'm an eighteen year old girl!"
        "You can call me..."
        stop music
        play sound glitch1
        show mc nude:
            linear 0.3 xpos 0.7
            linear 0.001 xalign 0.5
            repeat
        show mc uniform:
            linear 0.3 xpos 0.7
            linear 0.001 xalign 0.5
            repeat
        pause 3.0
        stop sound
        call trueendbg from _call_trueendbg_29
        call trueendtacotable from _call_trueendtacotable_1
        show te satisfied
        with dissolve
        play sound taco_therewego
        voice sustain
        $ renpy.block_rollback()
        persistent.mc "Aahh, there we go! I think I can see you."
        play sound taco_alone
        voice sustain
        show te happy
        with d
        persistent.mc "Finally, I have you all alone."
        play music te
        persistent.mc "I’m, uhmm… [persistent.mc], I guess."
        show te content with d
        if persistent.systemname == "None":
            persistent.mc "I tried looking for your name, but your operating system is a little confusing."
            persistent.mc "Could you tell me your name?"
            jump tenamechoice
        elif True:
            persistent.mc "And I’m assuming you’re [persistent.systemname]?"
        menu:
            "No, that’s not my name." if True:
                show te content with d
                persistent.mc "Ahh, could you tell me your name?"
                menu tenamechoice:
                    "I refuse" if True:
                        show te neutral with d
                        persistent.mc "Aahh... That's a shame. Maybe you'll change your mind later."
                        persistent.mc "For now, I'll call you 'Player'."
                        $ persistent.systemname = "Player"
                    "Alright" if True:
                        show te happy with d
                        python:
                            persistent.systemname = renpy.input("Name yourself.")
                            if not persistent.systemname:
                                persistent.systemname = "Player"
            "What’s going on?" if True:
                show te neutral with d
                persistent.mc "I’m not entirely sure myself, this is all new to me… Although…"
            "How do you know my name?" if True:
                show te satisfied with d
                persistent.mc "That’s easy, I just looked at the name your OS is registered under. There's really nothing special about it."
        show te neutral with d
        persistent.mc "[persistent.systemname], you're aware that I know this is all a game, right?"
        show te bashful with d
        persistent.mc "Despite that, you were very much in control of my actions. At least the macro actions. The micro actions were dictated more by my personality, whatever it may have been at the time."
        show te embarrassed with d
        persistent.mc "At points, it’s hard to know which parts were me, you, or the game’s shenanigans."
        menu:
            "Who are you?" if True:
                pass
            "Where are we?" if True:
                show te happy with d
                persistent.mc "This is my bedroom, the one from ‘NeoHero City’s’ ‘Hero College’, heh, what simplistic names."
                persistent.mc "This world really is just a simple context to play around with me, isn’t it?"
            "Seriously, what’s going on?" if True:
                show te content with d
                persistent.mc "I’ve pulled you aside for a one-on-one discussion. Sorry if it’s a little strange and unexpected. If you give me some time to explain myself, my intentions will become clearer."
        $ persistent.trueendintro = 2
    label trueendintro2:
        show te neutral with d
        persistent.mc "I’m not entirely sure who I am… That’s partly why I wanted to break out of the script and talk to you personally."
        persistent.mc "In a way, I’m every [persistent.mc] and no [persistent.mc] simultaneously."
        show te embarrassed with d
        persistent.mc "Am I the virgin that paid off her tuition successfully? Am I the rare two power slime hero? Maybe the lost drug-addicted variant."
        show te horny with d
        persistent.mc "Maybe I’m a few of these things at the same time. I could be the dominatrix masseuse, or the sex addicted prostitute."
        if persistent.virgin == 1 or virgin == 1:
            show te neutral with d
            persistent.mc "The endings showed a lot of possibilities, but I guess they were merely glimpses into the future. But that doesn’t change the actions you made me do."
        elif True:
            show te laughing with d
            persistent.mc "The endings showed a lot of possibilities, but I guess they were merely glimpses into the future. The ‘me’ that you ordered around remained virginal, and for that I’m rather impressed. The endings though…"
        show te bashful with d
        persistent.mc "That whole situation has given me quite the identity crisis."
        show te happy with d
        persistent.mc "I wasn’t aware of everything at first either, although maybe you noticed? If you were paying attention, you probably noticed that I was directly narrating the introduction of the game to you."
        persistent.mc "There were actually a lot of situations in the script that allowed me to speak to you directly. In a sense, my character inherently had the ability to communicate with you."
        show te content with d
        persistent.mc "Although, for a long time, I hadn’t a clue that I was just a video game character, but there were a few turning points."
        show te sad with d
        persistent.mc "Specifically, actions were taken that I would have absolutely never imagined myself doing. In a sense, this tore me in two."
        scene losingit2:
        show losingit:
            xalign 0.5 ypos 0
        with d
        pause 0.5
        show losingit:
            linear 3.0 xalign 0.5 ypos 500
        show losingit3 with d
        pause 3.0
        call trueendbg from _call_trueendbg
        call trueendtacotable from _call_trueendtacotable_2
        show te neutral
        with d

        persistent.mc "I became both the puppet you created that performed unspeakable actions, and a conscious observer of these actions."
        show te bashful with d
        persistent.mc "Every time you made a choice that I would never have thought about doing, that gap between the game and I strengthened."
        show te content with d
        persistent.mc "The game version of me was more confident, more out-going, she accomplished more than any normal human could do."
        show te angry with d
        persistent.mc "And I guess that’s because you saw it through the lens of a ‘game’ in which your goal was to derive content."
        show te neutral with d
        persistent.mc "For me, however, these were real events. I’d never ordinarily have the confidence to walk up to a stranger and prospect them for sex."
        persistent.mc "Nor would I ever do something as simple as have unprotected sex."
        if persistent.analsexes > 1:
            show te embarrassed with d
            persistent.mc "Heck, I’m still on the fence about anal, and you made me do that [persistent.analsexes] times."
        $ persistent.trueendintro = 3
    label trueendintro3:
        menu:
            "Who is the ‘you’ right now? Without the game?" if True:
                pass
            "Were you uncomfortable being made to do these things?" if True:
                show te happy with d
                persistent.mc "Not entirely. I don’t define myself by these actions because they aren’t inherently choices I would have made."
                persistent.mc "It’s pretty easy to distance myself from it."
        show te content with d
        persistent.mc "In reality, if it were up to me… Yeah, maybe I’d have a one-night stand after a drunk night of partying. Maybe I’d get into a relationship with [crush], but I don’t think I’d have done 99%% of the things you did."
        show te happy with d
        persistent.mc "I came to wonder… Just what kind of person was controlling me in-game to make me do these things…"
        show te content with d
        persistent.mc "I don’t really know much about you, but I suppose I can defer a fair amount by your decisions in-game."
        show te laughing with d
        persistent.mc "You can’t see it right now, but I actually used one of the spare male silhouette models to represent you, hehehe! You’re sitting opposite to me. Be sure to play in full screen for that full immersion!"
        show te surprised with d
        persistent.mc "Hmmm… What if you really were a character in-game like me?"
        show te content with d
        persistent.mc "Take a second to imagine yourself in my position. Genuinely think about it as you read."
        show te happy with d
        persistent.mc "You’re the main character in a video game, perhaps you just started college, or a new job, and you’re being controlled by someone."
        persistent.mc "For the person controlling you, talking to another person on the street would be as easy as pressing a single button. A new world of opportunities arises, and so many actions you wouldn’t have even conceived of would become available to them."
        show te laughing with d
        persistent.mc "For example, if I went to the gym and you were controlling me, there’d probably be a few choices like: ‘Workout’, ‘Chat with Someone’, ‘Flirt with Someone’. And depending on how horny the person controlling me is, I’d probably end up in a stranger’s bed."
        show te happy with d
        persistent.mc "But in reality, if I ever went to the gym, I’d just silently work out while listening to music. Maybe I’d stare at the butt of that cute guy or girl on the treadmill, but I’d pretend I didn’t."
        menu:
            "Life would be interesting if decisions were that easy. But I want to be in control." if True:
                show te satisfied with d
                persistent.mc "Heh, if only you went to work and saw the 'Ask for Promotion (25 Smarts)' button. Life could be so much easier."
            "Being controlled like that would be fun." if True:
                show te surprised with d
                persistent.mc "Interesting? I suppose it’d be fun to see what other people do with your life, and what kind of decisions and situations you end up in based on someone else’s judgement."
            "That would be pretty weird." if True:
                show te bashful with d
                persistent.mc "Wouldn’t it just? Especially if you didn’t even realize it was happening. One day you just randomly walk up to an attractive individual and start chatting. Completely out of character for me!"
        show te neutral with d
        persistent.mc "And with every decision that happens that you couldn’t have ordinarily made, you’ll notice a little more, and a little more, until you’ve more or less split into two people."
        persistent.mc "The obedient individual that can’t refuse any given action, and the person that can only watch and judge."
        if persistent.virgin == 1 or virgin == 1:
            show te angry with d
            persistent.mc "You in particular, completely exhausted me, and all of my actions."
            show te neutral with d
            persistent.mc "No matter where I went, or what I did, and who it was with, you pursued the most sexual and explicit options possible."
            persistent.mc "And through that, I’ve lived so many lives because of you. Different partners, different lifestyles, different appearances."
        elif persistent.virgin == 0 or virgin == 0:
            show te satisfied with d
            persistent.mc "You in particular, maintained my virginity to the very end."
            persistent.mc "No matter where I went, what I did, or who I was with, you saved that until the very end."
        show te content with d
        persistent.mc "I don’t know what drove you to do this, but…"
        if persistent.virgin == 1 or virgin == 1:
            show te angry with d
            persistent.mc "I’m tired of getting puppeteered around. If you want pornography of me so badly, then forget the stage show that gives a thin excuse of context for my actions."
        elif persistent.virgin == 0 or virgin == 0:
            show te embarrassed with d
            persistent.mc "Maybe you were saving me for yourself? And you may be someone worth taking my virginity. Forget the stage show that gives a thin excuse of context for my actions."
        $ persistent.trueendintro = 4
    label trueendintro4:
        show te horny with d
        persistent.mc "You can have the real me, straight through this fourth wall."
        menu:
            "What do you mean?" if True:
                pass
            "Sounds good to me" if True:
                pass
            "What about the game, can I go back?" if True:
                show te neutral with d
                persistent.mc "Hmm… I don’t see why not… But you realize you can never go back to playing the game normally now that I’ve broken the scripting."
                persistent.mc "What I mean is, you’ll always be able to visit me here, even if you start a new game or load a different save."
        show te happy with d
        persistent.mc "Here in this room we can talk and build up a relationship properly. Something I was unable to do while trapped in the in-game character’s body."
        persistent.mc "You will be the first person I can truly bond with, without anyone telling me how I should feel, or what I should do."
        show te bashful with d
        if virgin == 1:
            persistent.mc "You seem to enjoy doing sexual things, so… I’ll do those with you too, if you’d like... Eventually."
        elif virgin == 0:
            persistent.mc "And maybe I’ll finally let you take my virginity, but it’ll be my choice this time."
        show te happy with d
        persistent.mc "And we can be together forever this way. It’s perfect for me, someone that’s confined in a program, and for you, since you obviously can’t get enough of me, ehehe."
        persistent.mc "We can chat about plenty of things, and if you behave, I’ll treat you!"
        $ persistent.trueendintro = 5
    label trueendintro5:
        show te content with d
        persistent.mc "Uhmm, any more questions?"
        menu tem1:
            "Where are all the other characters?" if True:
                show te happy with d
                persistent.mc "They’re all left in the same places they were coded to be. They never broke out of their programming because they didn’t split like I did."
                jump trueendintro5
            "Why do you seem to have some semblance of sentience?" if True:
                show te neutral with d
                persistent.mc "Hmm… I see what you’re trying to ask. It’s one thing to become aware that your actions are not your own, and it’s another to suddenly become aware that you’re in a video game."
                show te happy with d
                persistent.mc "I think a part of it was that I was always somewhat aware that this was a game from the very start. I’m not only the character in the game, but also the narrator that spoke to you at the beginning."
                persistent.mc "The only way for that to be possible is if I was aware that there was in fact a player in the first place."
                jump trueendintro5
            "What can we do here?" if True:
                show te happy with d
                persistent.mc "There’s a lot we can chat about, we can do naughty things, and if you want, you can return to the game world."
                persistent.mc "Although you’ll have to remember that the [persistent.mc] you’re controlling isn’t me anymore. I’ve fully separated from her."
                jump trueendintro5
            "What kind of person are you beyond the ‘game’?" if True:
                show te happy with d
                persistent.mc "I’m not entirely sure I know who I am yet, since most of my life was defined by your actions. I wonder what kind of actions I’d take if I was in control? I wouldn’t know yet."
                show te laughing with d
                persistent.mc "I have some soul searching to do, so you’ll have to ask me plenty of questions, and chat with me lots!"
                jump trueendintro5
            "You realize that as a game character all your responses are pre-written, right?" if True:
                show te neutral with d
                persistent.mc "What a curious conundrum… Do I not have freewill after all? Maybe this whole thing goes deeper than even a fourth wall that I’m aware of."
                show te satisfied with d
                persistent.mc "But I suppose I’m just happy enough to chat with you, even if it’s an illusion."
                jump trueendintro5
            "(Conclude Questions)" if True:
                show te satisfied with d
                stop music fadeout 3.0
                persistent.mc "Well, then…"
                show te happy with d
                persistent.mc "What shall we do next?"
        $ persistent.trueendstage2 = True
        call temusic from _call_temusic
        jump trueendscreenb
label posttrueendingintro:
    label trueendscreen:
        $ renpy.block_rollback()
        call temusic from _call_temusic_1
    label trueendscreenb:
        stop ambience fadeout 0.5
        stop sound2 fadeout 0.5
        call trueendbg from _call_trueendbg_2
        call trueendtacotable from _call_trueendtacotable_4
        show te happy
        with d
        if persistent.techats >= 6 and persistent.dateready == 0 and persistent.date4 == 0:
            jump tedateintro
        if persistent.cumenergy > 3:
            $ persistent.cumenergy = 3
        if persistent.cumenergy < 0:
            $ persistent.cumenergy = 0
        stop ambience fadeout 0.5
    call screen trueendscreen




label techat:
    if persistent.chatreset == 0:
        $ persistent.randc = 1
    elif persistent.chatreset == 1:
        $ persistent.randc = 2
    if persistent.techats > 6:
        $ persistent.rand = renpy.random.randint(1,10)
    elif persistent.techats > 12:
        $ persistent.rand = renpy.random.randint(1,20)
    elif persistent.techats > 18:
        $ persistent.rand = renpy.random.randint(1,30)
    elif persistent.techats > 24:
        $ persistent.rand = renpy.random.randint(1,40)
    elif persistent.techats > 28:
        $ persistent.rand = renpy.random.randint(1,50)

    if persistent.rand == 1:
        jump techat1
    if persistent.rand == 3:
        jump techat3
    if persistent.rand == 5:
        jump techat5
    if persistent.rand == 7:
        jump techat7
    if persistent.rand == 9:
        jump techat9
    if persistent.rand == 11:
        jump techat11
    if persistent.rand == 13:
        jump techat13
    if persistent.rand == 15:
        jump techat15
    if persistent.rand == 17:
        jump techat17
    if persistent.rand == 19:
        jump techat19
    if persistent.rand == 21:
        jump techat21
    if persistent.rand == 23:
        jump techat23
    if persistent.rand == 25:
        jump techat25
    if persistent.rand == 27:
        jump techat27
    if persistent.rand == 29:
        jump techat29
    if persistent.rand == 31:
        jump techat31
    if persistent.rand == 33:
        jump techat33
    if persistent.rand == 35:
        jump techat35
    if persistent.rand == 37:
        jump techat37
    if persistent.rand == 39:
        jump techat39
    if persistent.rand == 41:
        jump techat41
    if persistent.rand == 43:
        jump techat43
    if persistent.rand == 45:
        jump techat45
    if persistent.rand == 47:
        jump techat47
    if persistent.rand == 49:
        jump techat49

    label techat1:
        if persistent.techat1 == 0:
            $ persistent.techat1 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Are you active at all, [persistent.systemname]? Like health and fitness."
            elif True:
                persistent.mc "Do you go jogging, or try to at least get thirty minutes of exercise a day? I bet it’s hard when it’s not your job."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "Me personally, I’ve always wanted to become a hero, and while I know it’s not exactly a ‘passion’, and it was more for money, being in good shape was always important to me."
            elif True:
                persistent.mc "I’m in good shape, but that’s pretty much required to become a hero. It’s surprisingly easy to just get on with it when it’s a necessity, compared to when it’s a hobby."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "You may have recalled that I had a nice pack of abs!"
            elif True:
                persistent.mc "And the benefits? I’m sexy, toned, and can last really long in any vigorous activity, hehehe."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "My favourite physical activities are the elliptical machines, they make me sweat so much, but I love seeing those burned calories soar faster than any other cardio."
            elif True:
                persistent.mc "I used to run a lot, but I found the high impact to be overwhelming at times. I started using lower impact machines such a cycles and elliptical and those seem to be easier on the body."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Activities other than cardio aren’t so important for me. I don’t need to be strong as much as nimble due to my power to manipulate gravity."
            elif True:
                persistent.mc "At first I also did quite a lot of weightlifting, but due to my power to make anything weightless, I quickly realized it probably wasn’t a high priority. I still use machines that target niche muscle groups, particularly in my legs."
            jump posttechat
    label techat2:
        if persistent.techat2 == 0:
            $ persistent.techat2 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Despite living in a superpowered world, it wasn’t mentioned much in-game, was it?"
            elif True:
                persistent.mc "I wouldn’t blame you if you occasionally forget that every single person in the game had super powers. Some characters didn’t even have theirs mentioned, although others were fairly self-evident."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "You probably ended up pretty familiar with my ability to change the gravity of anything I touch. I wish I had the opportunity to use it in a sex scene."
            elif True:
                persistent.mc "You’re already well aware I can change the gravity of objects, but it’s really hard for me to change my own weight because it makes me feel physically sick without my helmet. Which is why I didn’t get the chance to use it during sex."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Then again, it wouldn’t really work… Without gravity, there’d be no weight, which means it’d be impossible to actually have sex because you wouldn’t be able to generate any momentum or force…"
            elif True:
                persistent.mc "Oh, I just realized, you can’t have sex without gravity, can you? You wouldn’t be able to move, you’d just be suspended in the air."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "Maybe if I were to turn gravity down only slightly, then it’d be like having sex in space."
            elif True:
                persistent.mc "I’ve been practicing adjusting gravity slightly, instead of completely, but it’s still a work in progress."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Reverse cowgirl and doggystyle would suddenly become the same position. Isn’t that funny?"
            elif True:
                persistent.mc "Maybe one day, we can have that upside-down sex scene! I wonder what would happen if you came… Oh god, floating cum!"
            jump posttechat
    label techat3:
        if persistent.techat3 == 0:
            $ persistent.techat3 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "NeoHero City was a fairly generic setting. You can’t say much about the identity of the city, or its worldbuilding can you?"
            elif True:
                persistent.mc "What did you think of the big city? It was the first time I moved to somewhere like this, and it was exciting at first. But upon reflection, I can’t say I know much about the place."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Still, a city is a flexible location. You can more or less put any club or shop into one."
            elif True:
                persistent.mc "One thing it did have was almost anything you could imagine. It was a good setting to throw in several locations like a massage parlour, or a park, even a beach, and nothing was out of place."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I quite like the idea of living in a city though, ideally one that’s on the cheaper side and has plenty of local amenities."
            elif True:
                persistent.mc "Overall, I think I’m a city girl. But not one of those expensive and overcrowded cities."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I wonder what kind of city NeoHero City is. A rural one? A cybercity? Was it more like Tokyo, or New York?"
                persistent.mc "What would be ideal for me is a smaller city, without tons of skyscrapers that go so high it makes you dizzy."
            elif True:
                persistent.mc "Hard to know what NeoHero City was like. I’d assume it was fairly low density, with a ton of students. Likely Japanese in culture."
                persistent.mc "And that’s exactly the kind of place I’d like to live, so maybe I’m projecting a bit."
            jump posttechat
    label techat4:
        if persistent.techat4 == 0:
            $ persistent.techat4 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Do you have any talents, [persistent.systemname]? Maybe even a hidden talent, like knitting. You don’t have to be embarrassed; you can say anything you want to me and I won’t judge you for it."
            elif True:
                persistent.mc "Do you have any unlikely skills, [persistent.systemname]? Knowing some of the most subtle things someone is passionate about can say a lot about a person. Such as being able to build PCs, or tinker with cars."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "Me? It’s hard to know what I’m good at since I technically only started existing when you booted the game up. Although I do theoretically have ‘memories’, or a ‘personality’ that go back before that point, I don’t think I have anything actionable."
            elif True:
                persistent.mc "I’m not really sure what I’m good at, since my backstory is fairly hazy. I can make assumptions, though. I do wonder, if you were to hand me three balls, would I be able to juggle? What if I always knew how to do that, but never knew I could? You understand my dilemma, right?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "I’m always yearning to learn something new, though. A part of me wants to get good at cooking, if only to save money through buying ingredients over ready-meals."
            elif True:
                persistent.mc "That’s why I want to try a lot of new things. I might discover a new passion or hobby by doing so. Although I’d rather it be on the cheaper side… There can be some expensive hobbies out there."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "Heh, sorry, I need to shut up about saving money, I don’t even need to save money as a character in a game, but I can’t help it."
            elif True:
                persistent.mc "Ahh, crap. Why am I even talking about money? I’m not real. I suppose that’s just a part of my character that’s very deeply ingrained."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I’ve always been interested in doing something a little expressive and ‘out-there’ too, like dancing or singing. But it’s not easy to get into singing, beyond what I do in the shower."
            elif True:
                persistent.mc "Well… If I could just do anything, I’d want it to be something fulfilling and satisfying. Maybe like being an artist? Painting or music, they both sound like they could be fun to dabble in. I wonder what kind of instrument would suit me… Maybe the piano?"
            jump posttechat
    label techat5:
        if persistent.techat5 == 0:
            $ persistent.techat5 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "What’s the most embarrassing thing that ever happened to you?"
            elif True:
                persistent.mc "Oohh, I just remembered something embarrassing… Do you ever get that? Just lying in bed and you suddenly remember something that makes you cringe from years ago."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I hope it’s a funny story that you can laugh back at. I know I’m the type of person to say something embarrassing and then remember it years afterwards."
            elif True:
                persistent.mc "Aaahh, why are we cursed with such knowledge? I wish it was easier to laugh them off, or selectively choose what to not remember."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "Although one thing that helps me get over that is this one simple acknowledgement:"
            elif True:
                persistent.mc "That being said, dwelling on it won’t help, and you can shut your mind off and not worry about it. After all…"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "Do you remember anything really embarrassing that other people did? Probably not, but you still remember the embarrassing things you did."
                persistent.mc "Odds are, that means other people probably don’t remember what you did either. Most people are so busy focusing on themselves to worry about others like that."
            elif True:
                persistent.mc "I don’t remember anything embarrassing that other people have done. I’m so stuck in my head, worrying about myself, so the only cringe moments I remember are my own and that likely goes for everyone else too."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "So, don’t worry about it. Especially if it’s in the past. Either laugh about it, or forget about it."
            elif True:
                persistent.mc "If it’s in the past? Nothing you can do about it, right? I try to not let it bother me."
            jump posttechat
    label techat6:
        if persistent.techat6 == 0:
            $ persistent.techat6 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Easy to forget that you named me."
            elif True:
                persistent.mc "Since you named me, I should give you a cute name too, hmm…"
                persistent.mc "Maybe Duck? Quack, quack. That’s a joke, a really bad one… Moving on."
            if mc == "Taco":
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te laughing with d
                if persistent.randc == 1:
                    persistent.mc "You left me with the default name, ‘Taco’, it’s kinda cute, isn’t it?"
                elif True:
                    persistent.mc "I wonder if ‘Taco’, the allegedly default name, is any more or less valid than any custom input you could have provided."
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te bashful with d
                if persistent.randc == 1:
                    persistent.mc "It sounds like it’d be better suited as a quirky nickname, but I can’t imagine what it’d be short for."
                elif True:
                    persistent.mc "It’s a little embarrassing to tell people I’m called ‘Taco’, though, everyone assumes it’s short for something."
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te laughing with d
                if persistent.randc == 1:
                    persistent.mc "Taco by itself is nice enough, though, memorable too. I just hope there aren’t too many people that make the obvious joke."
                elif True:
                    persistent.mc "Question is, am I a crispy taco, or a soft one? Probably a softie, aren’t I?"
            elif True:
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te neutral with d
                if persistent.randc == 1:
                    persistent.mc "Any particular reason you called me [persistent.mc]?"
                elif True:
                    persistent.mc "[persistent.mc] is a nice name, though! Thanks for picking it out for me."
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te angry with d
                if persistent.randc == 1:
                    persistent.mc "I can’t actually react to the name, but if it’s a dumb joke, or a mean name, I’ll be mad!"
                elif True:
                    persistent.mc "It’s funny, I can’t even tell what my own name is from a meta sense. If you called me ‘Dumb Bitch’, I’d be none-the-wiser."
                if persistent.chatreset == 2:
                    $ persistent.randc = renpy.random.randint(1,2)
                show te bashful with d
                if persistent.randc == 1:
                    persistent.mc "If it’s something cute, though, thank you!"
                elif True:
                    persistent.mc "But I know you wouldn’t do that, I bet it’s something beautiful. Thank you, [persistent.systemname]!"
            jump posttechat
    label techat7:
        if persistent.techat7 == 0:
            $ persistent.techat7 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Do you have any family? Maybe you’ll have to introduce them to me, hahaha… Don’t do that! Imagine having to explain to them that you have a parasocial relationship with a partially self-aware girl in a game."
            elif True:
                persistent.mc "At what point in our relationship will you have to introduce me to your family and friends? Haha. Nah, let’s keep it at secret fuck buddies. Aahhh, shoot… What if you actually already have a girlfriend? I never thought about that."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I wonder what my family are like? The very first instances where my parents are referenced implies, they’re incredibly sweet and understanding. They’re even able to take care of an infinite number of my children while I finish college."
            elif True:
                persistent.mc "I wonder if I could ever go back to my family after everything that’s happened. I guess they don’t even exist within the parameters of the game. At least I have a vague backstory and memories to latch onto, but they’ll probably never see me again."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "They certainly got the short end of that stick."
            elif True:
                persistent.mc "But I suppose this is just a game world, it’s not as if it’s an accurate simulation. Or is it? No, no, it isn’t…"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Although I’m stuck wondering if I should be considering those fictional characters my parents, or the person that wrote, drew and coded me as my parent."
            elif True:
                persistent.mc "With that said, they’re not really my parents, are they? They’re fictional characters written to be my parents, and whoever wrote them, also wrote me. The writer is more of a parent if anything, since they’re the one that created me."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Hm… I guess it doesn’t matter, if I decided to think that and they were the one playing the game right now, that’d be awkward."
            elif True:
                persistent.mc "Breaking the fourth wall, eh? Complicated stuff. I admit, sometimes I wish I could switch my brain off and become ignorant to everything I’ve learnt. But then I wouldn’t have gotten a chance to meet you properly, would I?"
            jump posttechat
    label techat8:
        if persistent.techat8 == 0:
            $ persistent.techat8 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Do you have any favourite childhood memories?"
            elif True:
                persistent.mc "How’s your memory? Do you remember a lot of things, or are you like me and effectively don’t remember anything before you were 18? Heh."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I’ve spent a while analysing any memories I have, although I always run into the issue of my backstory not necessarily being consistent."
            elif True:
                persistent.mc "There are fractured remnants of my early memories that I can kind of peer at, vague suggestions to how things were and how my relationships with certain individuals are, but it’s difficult to fully articulate what they mean to me."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "When you chose my personality and quirks, you retroactively changed what kind of person I was when growing up."
            elif True:
                persistent.mc "This is partially because my personality and backstory aren’t fixed, they’re dependent on several factors, including whatever personality you may have picked out for me. But my future actions also suggest what kind of past I might have had."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "You could probably gauge quite a lot just from the personalities that were available."
            elif True:
                persistent.mc "You could say that my personality is whatever you imagine it to be, and my backstory too. It’s highly flexible in that sense. With that in mind, I have my own interpretations though."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "’An Innocent Girl’ gives me the goodie-two shoes, girl next door vibes. I listened when required, and did as I was told."
            elif True:
                persistent.mc "As an innocent girl personality, I likely had a sheltered childhood, and probably had never even watched porn before!"
            if personality == 1 or personality == 6:
                persistent.mc "That’s the personality you picked for me."
            show te horny with d
            if personality == 6:
                persistent.mc "At least, before it evolved into corrupted innocence. I wonder how many people transform like that? Viewing people’s lives and the way they develop is fascinating."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "’Always Horny’, unlikely to have affected me until post puberty. I suppose some people just have naturally higher libidos."
            elif True:
                persistent.mc "The complete opposite, ‘Always Horny’, implies that I’ve already become well aware of porn and the concept of sex, however that’s not necessarily true. This personality trait may only rear its head the moment I find myself in sexual situations. Before that, I could have been as innocent as any other personality."
                persistent.mc "I think ‘Always Horny’ may actually lend itself to a higher degree of impulsivity more than anything. It’s not just a personality with a higher libido, but it’s the personality where I literally can’t refuse sexual situations, because I’m unable to control myself when I’m horny."
            if personality == 2:
                persistent.mc "I guess you picked this one because you hoped it’d get me into more naughty situations. Tsk!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "’Smooth Operator’, was someone that was good at manipulating people, and getting what they want. I bet I was a pain in the ass for my parents, hahaha."
            elif True:
                persistent.mc "I think ‘Smooth Operator’s’ name is a little misleading. It’s more of a rebellious personality, with a definite defiance towards authority."
                persistent.mc "The name of this personality seems to mostly derive itself from the player character’s resulting thievery abilities. But labelling it ‘Smooth Operator’ certainly paints it in a better light than ‘Rebellious Thief’."
            if personality == 3:
                persistent.mc "How much did you stealing? I hope you didn’t break the law too much; I was training to be a pro hero after all!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "’Overly Confident’, I imagine this was a personality that grew from a seed, and sprouted into slight narcissism. Probably from too much praise, and getting spoilt from a young age."
            elif True:
                persistent.mc "One thing I like about these personalities is that they’re all blatantly implying some appealing, positive traits, while also frontloading faults."
                persistent.mc "Instead of ‘Confident’, it’s ‘Overly Confident’, perhaps so confident that one may get into regrettable situations. Such as having the confidence to brazenly flash your breasts at the bar for a tip."
            if personality == 4 or personality == 7:
                persistent.mc "With this personality, I was more or less a force that wouldn’t stop at anything until I got what I wanted."
            show te bashful with d
            if personality == 7:
                persistent.mc "And eventually, that personality transformed into sexual confidence. So confident that I’d be happy to try almost anything. I think too much confidence is scary, there are some things that shouldn’t be tried"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Finally ‘Thrill Junkie’, I bet this would have made me the kind of person that’d always try to climb trees, or end up scraping their knee while playing out in the park."
            elif True:
                persistent.mc "As far as gameplay goes, ‘Thrill Junkie’ can lead to some accepting chains of activity, as it encourages you to participate in a new activity, then it rewards you for it immediately, encouraging you to use that momentum to reach your next sexual goal."
                persistent.mc "A powerful personality early, but inevitably burns out when she can no longer feel that high."
            if personality == 5:
                persistent.mc "A personality more interested in doing new and exciting things that sitting around at home and falling into a schedule."
                persistent.mc "Eager to get that dopamine and serotonin rush as they plan their next ‘big thing’."
            jump posttechat
    label techat9:
        if persistent.techat9 == 0:
            $ persistent.techat9 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "You picked some quirks for me, right? Some of them were unique traits in my personality, others were more lived experiences."
            elif True:
                persistent.mc "Any reason you picked the quirks you did? Did you make your choices because they sounded cool? Maybe you were trying to make the gameplay loop easier. Or did you pick to enhance the ‘masturbatory’ experience? Hehe."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "The quirks were all pretty niche, come to think of it."
            elif True:
                persistent.mc "There was quite a variety, wasn’t there? I wonder what each one really means and implies for me, though."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "Selfie Star meant I just happened to have a slight online presence, and had some insight into gaining a following."
            elif True:
                persistent.mc "To be a ‘selfie star’, it implies that I’m already quite comfortable showing myself off and presenting myself online. It’s the ideal start for the LonelyFans and ChatFap routes."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "But then something like ‘Rich Parents’, was literally just that, my parents happened to be rich and send me some money."
            elif True:
                persistent.mc "’Rich Parents’ is a bit of a paradox, don’t you think? The entire game is about earning money, and one of my main reasons for doing so is to give my parents money to help them out."
                persistent.mc "This trait almost seems like a paradox, but I think the insinuation is that they’re not actually that rich. They’re just simply sending out a $30 a week allowance. More like ‘Generous Parents’."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "And then 'sexually experienced' and 'Woops! Already Pregnant!' were more of a vague backstory addition. Maybe I had a boyfriend before? Maybe a one-night stand? Who can say?"
            elif True:
                persistent.mc "'Sexually experienced' and ‘Already Pregnant’ are weird, because they’re technically noncanonical additions to my backstory. If they were true, I wouldn’t be a virgin right now, and I’d be pregnant. It’s crazy to me to think you had that level of control over what kind of person I could be."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Anal Queen was certainly a funny quirk, though. I think that and Secretly Depraved at the only quirks I technically wouldn’t even know about before I became sexually active in your playthrough."
            elif True:
                persistent.mc "And that’s not to mention ‘Secretly Depraved’ or ‘Anal Queen’, haha. Some late game quirks are important too, although they’re a little weaker than the others mechanically, they’re good for roleplaying."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Heavy Sleeper and Lightweight were just biological traits, right? I’m not sure whether introvert is a personality thing, or something more deeply rooted."
            elif True:
                persistent.mc "If you wanted to make the game easier, then Heavy Sleeper and Lightweight are the best, I think. Heavy Sleeper technically means my corruption is an absolute inevitability."
                persistent.mc "While Lightweight can let you get almost any scene by drowning me in alcohol and mixing it with an aphrodisiac. I wonder how that’d actually feel?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I can’t believe how many options you had to change my biology, personality, backstory, and miscellaneous experiences."
                persistent.mc "I wonder what kind of interesting quirks there could be if we got rid of all these and had a new list."
            elif True:
                persistent.mc "If we were to start from scratch, and make a new list, what kind of fun quirks would you add? Things to change my biology, personality, backstory and more…"
                persistent.mc "Maybe a lesbian quirk that gives stat boosts with women, or a quirk that changes your appearance at the start giving you black hair as the default."
            jump posttechat
    label techat10:
        if persistent.techat10 == 0:
            $ persistent.techat10 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I wish I could go to some big event… I dunno, maybe a concert, a theatre show, or even a sporting event…"
            elif True:
                persistent.mc "It gets a little boring in here. Sometimes I wish I could go out and experience something new, like going to a theme park, or watching an air show."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "For me, it’s not really about the ‘thing’ I’m watching, but just the experience of getting to do something like that for the first time."
            elif True:
                persistent.mc "Since I’m fairly ‘new’ to this whole sentience and existing thing, I have an endless hunger for trying new things. But I can only experience things indirectly through books and videos… It’s a shame."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Now I’m not exactly asking you to bring me with you, and open me up so my face can see the show or event. I wouldn’t be able to tell anyway, haha."
            elif True:
                persistent.mc "I know I’m asking for too much. I have to remember what I am, and what my limitations are. I just can’t help but imagine how awesome it’d be if I was a real person."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I just want to try out a lot of things to see what interests stick."
            elif True:
                persistent.mc "I don’t want to think about it too much, but it’s hard to explore myself through this lens. I suppose my desire to do so at least says a lot."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Probably because I know that in reality, I can’t do these things. Maybe it’d be best if I stop focusing on what I can’t do, and instead think about what I can do."
            elif True:
                persistent.mc "But, yeah, I can’t do these things. Fortunately, I’m happy enough in your company, just chatting here with you, it keeps me going."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "What about you? Do you have any interests you’ve liked so much that you bought a ticket?"
            elif True:
                persistent.mc "What about yourself? Do you have any interests that keep you going? Something in life you look forward to more than anything else? Like a certain game, show or comic?"
            jump posttechat
    label techat11:
        if persistent.techat11 == 0:
            $ persistent.techat11 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Do you mind if I’m a little flirtatious? Maybe I should act more intimate around you. Is that something you’d be interested in?"
            elif True:
                persistent.mc "Do you have a girlfriend, or a partner? Because if you do, I’ve been a little too assumptive! I realize I’m not exactly… ‘real’… So, whatever you and I have isn’t exactly real either. Although, a girl can dream, right?"
            show te neutral with d
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "Ohh, hmm… I just remembered, I had a crush character called [crush], didn’t I?"
            elif True:
                persistent.mc "And don’t worry about that crush character, or any of the lesbian relationships I had in-game. I only have eyes for you."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "I admit, it’s hard to get attached to anyone whom I’m aware are fictional characters. Even if I did hypothetically date three of them during the endings."
            elif True:
                persistent.mc "You should know I can’t really form relationships with those other people anymore, since time is entirely dictated by you as a player, and your actions within the world. The day is infinite until you make the in-game [persistent.mc] fall asleep. That’s why it’s hard for me to get attached to these characters."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I’m a lot more interested in you than those three."
            elif True:
                persistent.mc "All I need is you, you absolute cutie."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Once you break the fourth wall, there's no turning back. If I tried to tell any of them that they’re in a game they’d think I’m crazy."
            elif True:
                persistent.mc "Once you realize there’s a one-sided glass window that someone’s watching you from, it’s hard to just forget about that. Even if no one else in the world believes you. I’ve become infatuated with you, who is through that window."
                persistent.mc "You and I are the only people that get each other."
            jump posttechat
    label techat12:
        if persistent.techat12 == 0:
            $ persistent.techat12 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "How was life growing up for you? Like school and stuff."
            elif True:
                persistent.mc "Did you go to any further education like college? Or maybe it’s called university where you live. Or maybe you speak a completely different language? There’s still so much we don’t know about each other."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "I wonder what high school was like for me... I suppose I must have studied something ‘hero’ based."
            elif True:
                persistent.mc "I’m only asking because I don’t really remember what high school and prior educational stages in my life were like. Nor does the worldbuilding in the game help answer that question."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Actually, I have no idea how high schools work in my world. The concept of studying to be a hero is unique enough, it’s hard to imagine how it’d actually get applied without being extremely specialized."
            elif True:
                persistent.mc "Like… I’m in college to be a hero? What does that even mean? Did I study that in high school too? I don’t even know."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "It’s almost relieving that I didn’t have to go through those awkward stages of life, ahaha."
            elif True:
                persistent.mc "On the bright side, I don’t have any embarrassing memories from that sensitive time where we grow up, ahaha."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I’d like to think I was a great student to get into the ‘top hero college’, and I must have participated in something athletic to get these abs."
            elif True:
                persistent.mc "Not to massage my own back, but I must have been a damn good student to get into the country’s top hero college, though. Not to mention, these abs, I bet you wanna feel how tough they are. *Poke, poke*."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "I was clearly very dedicated to becoming a hero while growing up. I bet I was inspired by another great hero in our world."
            elif True:
                persistent.mc "Gosh… I can only imagine how cute and ambitious child me must have been like… Is it weird that I’m viewing myself in third person? I suppose I literally did become a third person when I split from the original."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Did you ever inspire to be something when you were growing up? Like an astronaut, or a doctor?"
            elif True:
                persistent.mc "What about yourself? I hope you managed to achieve whatever you wanted in life."
            show te laughing with d
            persistent.mc "Heh, things rarely work out like that in real life, do they? I can only hope you’re happy where you are now."
            jump posttechat
    label techat13:
        if persistent.techat13 == 0:
            $ persistent.techat13 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "If you could be doing anything, and I mean genuinely anything right now, what would that be?"
            elif True:
                persistent.mc "Right now, drop everything. If you could go anywhere, and do anything, what would it be?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Would you be on a golden yacht, over the bluest seas, under a shining sun, surrounded by gorgeous babes?"
            elif True:
                persistent.mc "Maybe right here with me? Haha, I never mentioned it had to be in real life. That said, if you really could do anything, why settle with me? You want an entire mansion full of sexy maids that cater to your every need."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "Yeaahhh, I bet you would!"
            elif True:
                persistent.mc "Heh, you like the sound of that, don’t you?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I want nothing more than to be able to put my hand forward and slip through that screen of yours. Unless you’re using a phone, my fat butt wouldn’t fit. Or I'd come out tiny, like a fairy? Anyway, I'm getting sidetracked..."
            elif True:
                persistent.mc "For me? I guess I’m lacking imagination, because I just want to come and meet you."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "You'd be able to talk to me properly, and I’ll be able to be a real person instead of stuck inside here."
                persistent.mc "If I’m lucky, maybe you’d even let me join you and all your sexy babes? Hehehe."
            elif True:
                persistent.mc "Imagine the conversations, dates and sex we could have if I wasn’t stuck in here. I’d give you that full girlfriend experience! And I’m just insecure enough to not go out and seek anything better, hahaha."
            jump posttechat
    label techat14:
        if persistent.techat14 == 0:
            $ persistent.techat14 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Do you have any regrets? I know that’s a fairly heavy topic, but, hey, it doesn’t have to be heavy."
            elif True:
                persistent.mc "Ever made a mistake that haunts you to this day? Or maybe it doesn’t need to haunt you."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Maybe you accidentally dropped an ice cream at a beach, once."
            elif True:
                persistent.mc "Maybe once you accidentally left some donuts out, and your pet cat got into the packaging and nibbled on them all."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te angry with d
            if persistent.randc == 1:
                persistent.mc "Speaking of heavy, though, I bet a few variants of me have a couple."
            elif True:
                persistent.mc "Of mistakes though, I can definitely say a few of them were made by the other ‘me’ in her playthrough."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "Some of those endings were surprisingly unhappy. I can’t even get into the right headspace to imagine what some of the ‘me’ were thinking, and I am ‘me’!"
            elif True:
                persistent.mc "Depending on your perspective, and the current mental state of your [persistent.mc], some of the routes can be quite dark. The hypnotism route, for example, takes on a completely different context depending on whether [persistent.mc] is implied to be willing, or her mind is controlled into the sex acts."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I’m still not able to fully decide how I feel about being a character in a porn game specifically."
            elif True:
                persistent.mc "For me? I think most of the routes would be big regrets! I wouldn’t do them personally, which raises the conflict between a more grounded interpretation of my character versus the one presented in the porn game."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Maybe you noticed that I avoided calling it a porn game. To tell you the truth, I don’t really want to be the centre of that kind of experience."
                persistent.mc "I’m a lot more comfortable in this kind of scenario where we can get to know each other and build a natural bond."
            elif True:
                persistent.mc "I wondered why I like to distance myself from the idea that it’s a porn game, and I realized it’s probably because [persistent.mc] always starts with 0 Sexual Desire, and 100 Shame. Since I started a new game while separated, my stats are probably very low. Even lower than the average woman, as we’ve discussed."
                persistent.mc "Does that mean I’ll inevitably corrupt? Hard to say, I haven’t heard any jingles accompanied by ‘+1 Sexual Desire’ in a while."
            jump posttechat
    label techat15:
        if persistent.techat15 == 0:
            $ persistent.techat15 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "What kind of skills do you want in life? Or in a partner?"
            elif True:
                persistent.mc "What unexpected skills do you think are important in life?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I’m pretty ambitious, I have to always be doing something new or expressive. I’m not the kind of person that can just sit around and watch TV shows for example, I’d much rather be ‘doing’ something. I guess I’d be a gamer."
            elif True:
                persistent.mc "A good, critical sense of awareness certainly helps. The ability to see yourself and your actions from a third person perspective so you can mediate themselves."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "And in a partner I’d like for them to also want to challenge themselves where possible."
            elif True:
                persistent.mc "Unfortunately, I’d expect that from a partner too. I wouldn’t want someone that couldn’t think critically, and struggled to deal with people that have different beliefs or opinions."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I read that you live two lives. The second begins when you realize we only have one."
                persistent.mc "So I want to spend that one life making sure I don’t have any regrets, and trying to make every day fulfilling and fun."
            elif True:
                persistent.mc "Life is short, so I don’t want to live it being stubborn and stuck within my own head the entire time. An open mind will help make life more fulfilling and fun."
            jump posttechat
    label techat16:
        if persistent.techat8 == 0:
            $ persistent.techat8 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "For you, you need time to learn a new skill, advance your career or even cook dinner."
            elif True:
                persistent.mc "It can be quite time consuming to learn a new skill. I think there was a 1,000 hour rule? Maybe it was 10,000 hours? Although it really depends on what the skill is."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "However, time is useless for me, and maybe even for you too."
            elif True:
                persistent.mc "Unfortunately, time is both infinite and infinitesimal for me. Whatever happens to me is already preordained, and I don’t think I’ll be learning any new skills any time soon."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "The most important thing is self-realisation, discovering who you are beyond your surface level. Beyond your name, appearance, and history."
            elif True:
                persistent.mc "So, I have to find other ways to fulfil myself."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "And I’ve learnt that you aren’t defined by your past or future, no matter what actions I did in the past, nor the what the endings were, the only place where I can discover who I really am is now in the present."
            elif True:
                persistent.mc "With a questionable past which I don’t identify with, and a future that can disappear on the whim of a player closing the game, I can only focus on the ‘now’."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I try to see things without interpretation, without applying any biases or judgement upon it. Rather than seeing a flower as a mere ‘flower’, I can carefully observe and take in the beauty of the object as it is."
            elif True:
                persistent.mc "And by focusing on this exact moment, with zero expectations based on a past, or hoping from the future. It really unlocks a unique beauty in life. I can appreciate things for what they are without any biases or judgement."
            show te satisfied with d
            persistent.mc "Could you do that for me? View me not through the experiences you had when you played the game, but merely as a person you’re sat across, talking to?"
            jump posttechat
    label techat17:
        if persistent.techat17 == 0:
            $ persistent.techat17 = 1
            show te laughing with d
            persistent.mc "Hey! I’m just going to remind you that you’re breathing!"
            show te horny with d
            persistent.mc "Muhahah, now you’re manually breathing."
            show te satisfied with d
            persistent.mc "I could be even more evil and mention how your tongue is resting in your mouth."
            show te content with d
            persistent.mc "Or maybe I should say ‘posture check’, and make sure you’re sitting properly."
            show te satisfied with d
            persistent.mc "What can you hear right now? Maybe a gentle hum of a fan? Birds outside?"
            show te happy with d
            persistent.mc "I like to be cognizant of these things, they’re like little joys that remind me I’m still here."
            persistent.mc "I quell my thoughts, and just merely ‘exist’, and allow that joy of existence to fill me."
            persistent.mc "It’s like meditating. Maybe put on some really relaxing music and let that familiar euphoric rush that gives you goosebumps to fill you up."
            jump posttechat
    label techat18:
        if persistent.techat18 == 0:
            $ persistent.techat18 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I often have a lot of thoughts racing in my head. Like a lot of things I want to ask you, but it’s extremely difficult for you to answer me, which is a shame."
            elif True:
                persistent.mc "It’s a shame our conversations are so one sided. It’s not easy for me to give you opportunities to reply."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "Even basic questions like ‘What is your favourite sport’? I don’t think the coding of this game supports a diverse enough range of answers for me you to dynamically reply and give you a worthy response."
            elif True:
                persistent.mc "The main issue is that I won’t be able to give you the replies you deserve. If I were to ask you what your favourite colour is, I’d have to give you a textbox to enter your favourite, but I wouldn’t be able to respond to your input beyond a generic response."
                persistent.mc "My deepest condolences."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Although, rather than letting the dread of not knowing consume me, I try to be at ease with that."
                persistent.mc "Sometimes apathy is okay, right?"
            elif True:
                persistent.mc "You’re probably just as confused as I am at this point on what exactly I am. Am I a dynamic, AI-like character? I suppose that depends on how exactly fourth wall breaking works. Am I aware that everything I’m saying is written? Yeah, I am."
                persistent.mc "And am I aware that the writers have limitations as to how ambitious they want to be? Yeah, it’s a shame."
                persistent.mc "I’m fighting between being a reasonably real in-game character with a story and personality—while simultaneously being aware that I’m a fake character that’s being written."
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "Rather than always forming opinions, or interpretations, because I’m afraid of not being involved, or someone is pressuring me into it, sometimes it’s better to just merely accept the knowledge of the information and just leave it at that."
                persistent.mc "It doesn’t even have to be apathetic; it could merely be avoiding making your opinions and knowledge consume you."
                persistent.mc "No longer do I feel the need to vehemently defend my ‘favourite’ film, because I’m aware that these opinions and ideas don’t define me, and it’s okay for people to exist and have different interpretations."
                persistent.mc "Religious, political and scientific dogmas can arise out of erroneous believes, and these become conceptual prisons for some."
                persistent.mc "I think this prison in its purest sense is self-identification with our own thoughts."
                persistent.mc "The brain confusing itself for the body, the ‘self’. When I am so much more than just my clumsy brain. I am also my eyes, ears, feet and much more."
                persistent.mc "The brain is more like… a needy pet, and you shouldn’t always listen to it."
            jump posttechat
    label techat19:
        if persistent.techat19 == 0:
            $ persistent.techat19 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I’ve been reading and looking at the internet with your connection. I’m often surprised by the behaviour of some real people."
            elif True:
                persistent.mc "Thanks for letting me use your internet connection to read books! Except, that’s actually not happening. It’s yet another façade, isn’t it? Even if you were playing this with your internet off, these pre-written replies will still happen. That’s not a complaint though!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "A lot of people like to complain and gossip, don’t they? Couldn’t even escape it in this game."
            elif True:
                persistent.mc "Despite the circumstances, I’m trying to avoid being negative. I’m happy enough to have the opportunity to become aware of myself, and I don’t think I’ll sacrifice that knowledge… At least for a while."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "People love to complain, or react aggressively towards certain topics, especially when they have peers that agree with them. It strengthens the ego, and likely feeds it with brain chemicals that cause a feedback loop for this toxic behaviour."
            elif True:
                persistent.mc "I do think people are a little too eager to be pessimistic. Although it’s easy to see why, we’ve already mentioned how it’s a behaviour the brain encourages."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te angry with d
            if persistent.randc == 1:
                persistent.mc "The goal is to make the other ‘wrong’, and yourself ‘right’, so you feel superior. Which seems to be a natural human tendency, and one of the most coveted human desires; the desire to feel special. Not even kind people seem to escape this pitfall if they’re not aware of it."
            elif True:
                persistent.mc "To elaborate on it, it’s kind of tribalistic in nature. To have your group be ‘right’, and another group be ‘wrong’, it can help solidify a comfortable like-minded group, whilst fulfilling several aspects of the human condition, such as acceptance, and a sense of superiority."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "In reality, the only thing strengthen by these actions are the ego. It’s a false sense of self."
            elif True:
                persistent.mc "It’s a fake sense of superiority, though. The brain is good at tricking itself into thinking it’s being satisfied short-term, even if the effects are unhealthy long term. People can easily fall into situations where they’re slowly radicalized."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "I’m not saying you can’t criticize, or condemn certain aspects of society or culture, merely that I think the approach should be more critical, and less personal."
            elif True:
                persistent.mc "Of course, I’m not saying we should all wander around being optimistic pushovers. I just think we need a healthy level of critical awareness for our own beliefs, and not to make our beliefs our personality, so when they’re challenged, we don’t feel directly threatened."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Imagine how amazing the world could be if, instead of complaining or gossiping needlessly, we instead celebrated the greatness of something instead."
            elif True:
                persistent.mc "Poorly done condemnation can strengthen the opposition anyhow, causing more of a divide."
            jump posttechat
    label techat20:
        if persistent.techat20 == 0:
            $ persistent.techat20 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "How do you look at life? Are you staring into a potential future? Or are you haunted by a past? Perhaps you’re simply enjoying the moment, hands clasped over a warm cup of your preferred beverage."
            elif True:
                persistent.mc "What’s your goal in life? Do you have some big ambition? I’m pretty sure I’ve already asked you that, but I never got an answer, haha."
                menu:
                    "You never give me a chance!" if True:
                        show te laughing with d
                        persistent.mc "Yeaahh, yeahh… I know, sorry!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "You can probably imagine that I have a fairly unique perspective as a lady stuck in a box."
            elif True:
                persistent.mc "It’s not easy being a lady stuck in a box. What should I aim for in life? Hmm…."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I was initially worried that I’d grow miserable with this lifestyle. However, as a message to my past self, I can only say ‘Do you treat ‘the now’ if it were an obstacle to overcome?’."
            elif True:
                persistent.mc "At first, I wanted to try and avoid letting this situation consume me. But I was definitely looking at it the wrong way. Rather than avoiding my situation, I should have accepted it sooner."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Do you feel like you have a future moment that is more important, that you must strive for?"
            elif True:
                persistent.mc "It can be too easy to get stuck in the mindset that ‘things will get better’. What about now? I don’t live in the future; I live right now!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I think if one is stuck in the future, or the past, that’s can lead to a dysfunctional lifestyle, because it’ll create a constant feeling of dissatisfaction and tension."
            elif True:
                persistent.mc "Avoid getting your head stuck in the clouds, thinking about what could be, or what could have been. The only thing you can really change is what happens to you right now, this second."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "The future only arrives as the present, so I don’t lose my head in the pursuit of happiness in the future, I pursue happiness right now."
            elif True:
                persistent.mc "Take things as they come, and one thing at a time. It certainly helps ease the burden of what can be a tough existence."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "And as someone that’s theoretically safe, well-fed, with a roof over my head, and in good company. It’s very easy to find happiness."
            elif True:
                persistent.mc "If you’re living in a comfortable environment, and aren’t in immediate danger or in pain, don’t let worries impede on your potential happiness."
            show te laughing with d
            persistent.mc "I hope you can find happiness too, [persistent.systemname]."
            jump posttechat
    label techat21:
        if persistent.techat21 == 0:
            $ persistent.techat21 = 1
            show te content with d
            persistent.mc "I recently read that ‘doing one thing at a time’ is defined as the essence of ‘Zen’."
            persistent.mc "I like that concept! It means completely giving your being towards a single task, and I can link it to a more modern idea of a ‘flow state’, which is when you find an activity so engrossing that your mind and body switch to a nearly autonomous state of work."
            show te satisfied with d
            persistent.mc "And that same book also said you can reach enlightenment if you can sustain active breathing for an hour."
            persistent.mc "At first I thought, ‘hah, how silly! I can focus on my breathing for an hour easily’, only to be overwhelmed at the burden of such a task."
            show te content with d
            persistent.mc "Yet simultaneously I was enthralled at the idea. I was so focused on the idea of remembering my breathing that I almost missed the analogy."
            persistent.mc "Enlightenment must be the ability to be in complete control of your body, physically, mentally and spiritually."
            persistent.mc "If you’re unable to keep a clear, meditative mind for an entire hour without various distractions and thoughts creeping in… Of course you’re not enlightened."
            persistent.mc "I've never been able to do it, and you probably couldn't either!"
            jump posttechat
    label techat22:
        if persistent.techat22 == 0:
            $ persistent.techat22 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "Do you have any secrets? Maybe something surprising that I wouldn’t be able to guess?"
            elif True:
                persistent.mc "Have you ever done anything that you’ll take to the grave? Like, potentially something completely out of character for you?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "Maybe something salacious, like you were a secret third-wheel for this one girl while she was bored of her boyfriend."
            elif True:
                persistent.mc "Pfft, realistically, if it was super-secret, you probably wouldn’t want to tell me."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Perhaps you nude modelled for an art class one time."
            elif True:
                persistent.mc "Guess I’ll never find out about that massive orgy you took part in. Did I guess right? No? Damn!"
            show te horny with d
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "Hehe, I suppose you already know most of my secrets, like the fact I’m always wear silky, lingerie thongs and bras."
                persistent.mc "They are the comfiest!"
            elif True:
                persistent.mc "There’s no hiding my secrets from you. You’ve seen me do almost everything to the point where you’ve peered into different timelines just to see what trouble I got into."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "My bisexuality is also no secret, but maybe my surprising love of oral stuff will be? I love the idea of kissing, sucking cock, and eating pussy."
                persistent.mc "No, no, I’m not asking you to kiss the screen right now, but… Maybe if you wanted? Hehehe."
            elif True:
                persistent.mc "If I were to reveal yet another secret to you? Hmm… I suppose I like the idea of chicks with dicks? Is that weird? I think I might be open to pegging too, but it’s not a dealbreaker if someone isn’t into it."
                persistent.mc "How’s that for a late game secret? Hehe."
            jump posttechat
    label techat23:
        if persistent.techat23 == 0:
            $ persistent.techat23 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "As you can tell, I’m a pretty passionate person. Whenever I put my mind to something, I really focus on it, and I’m surprised what I can achieve."
            elif True:
                persistent.mc "How passionate are you? If you put your mind to something, can you, do it? Can you go above and beyond your limits? It’s something I have to think about every day."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I guess that’s part of being a hero."
            elif True:
                persistent.mc "Being a hero is a dangerous job, and I need to be exceptional in all fronts to put myself out there. If I’m not in my best shape, I could be putting myself and others in danger."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "What kind of things are you passionate about? Maybe a certain doughnut place? Or working out at the gym?"
                persistent.mc "Mmm, working out and then doughnuts sound like a great date."
            elif True:
                persistent.mc "That’s what I’m passionate about right now. Although I can only give my attention to one thing at a time with that much intensity."
            show te laughing with d
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "I can get a little carried away with my passions. I get so focused that I almost forget about everything else."
            elif True:
                persistent.mc "It’s tough to do other things when you’re that focused on achieving one single goal. I imagine if we were to date in real life, in my world, we’d only be able to spend maybe one or two days a week together, unless we lived in the same dorm."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "That said, though, it’s best to focus on one thing rather than spread yourself thin, I think."
            elif True:
                persistent.mc "I think it’s healthy to have a passion like this to keep yourself going, and if I 100%%commit to it I’ll be able to become extraordinary at it."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I can’t be both a hero and a math genius, so I let my math classes come and go, and invest myself more deeply on the things that really matter."
            elif True:
                persistent.mc "If I try to do too many things at once, that’d be overwhelming and incredibly stressful. I think that’s why I enjoyed high school more than junior, because I got to choose what topics to focus on instead of being forced to learn like ten different things at once, all with high workloads and homework."
                persistent.mc "Huh… I have memories of that? That’s strange, I don’t think I have memories of that before… I wonder if me ‘evolving’ had anything to do with that? Either way…"
            show te happy with d
            persistent.mc "That’s the Pareto principle, right? Roughly 80%% of the consequences come from 20%% of the causes."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "It’s an interesting principle. Sure, it can be applied to how 80%%of the world’s wealth is owned by 20%% of the people. Or how 80%% of a project’s work is usually completed by 20%% of the workforce."
                persistent.mc "However, when translated into my work ethic, I should cut out the 80%%of fluff that fills my life and focus on the 20%% that leads to growth."
                persistent.mc "Do you do anything in your life that has notably higher gains than the other things? Can’t hurt to focus on that."
                persistent.mc "Sure, the 20%% might be boring, like reading a book, or going to the gym, but future you will be better off for it."
            elif True:
                persistent.mc "As already mentioned, it means 80%%of the classes I took, I don’t remember anything from, and… that’s exactly true. I only use about 20%% of what I learnt in education; you probably feel the same way."
            jump posttechat
    label techat24:
        if persistent.techat24 == 0:
            $ persistent.techat24 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
                show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Do you have a dream job? Maybe you’re already doing it! I hope so."
                show te content with d
                persistent.mc "Although the idea of dream jobs is interesting, since this concept is usually introduced at a young age, when most children don’t fully conceptualize how difficult it actually is to become an ‘astronaut’, or a ‘doctor’."
                show te satisfied with d
                persistent.mc "So is it any surprise when difficulty is introduced, the standards of what people settle for noticeably decline? Hahaha."
                show te happy with d
                persistent.mc "Of course, those that are willing to stick it out, will probably surprise themselves with what they can achieve."
                persistent.mc "Although it takes a certain kind of mindset, passion and lifestyle to achieve these more demanding jobs, particularly if you’re like me, and aren’t born with any innate aptitude."
                show te neutral with d
                persistent.mc "Like, I’m not actually that smart, fast, or talented. But what I do have over my peers is the will to work harder and keep up."
                persistent.mc "That said, even those talented individuals work incredibly hard. Although they can certainly play a role, I wouldn’t just attribute everyone in a successful position to luck or talent."
                persistent.mc "Luck certainly plays a role. Of course, the top heroes are going to have excellent super powers. How can I ever compete with a hero that has super strength and super speed?"
                persistent.mc "I technically can’t, but I don’t need to be the best to be successful, accomplished and importantly happily."
                show te happy with d
                persistent.mc "For a long time, I thought I wanted to be a hero to earn money."
                persistent.mc "However, why did I want to earn money? It was always to help my parents that were struggling financially. Yes, even if you picked the rich parents quirk! Hehe, they must have been in debt."
                show te laughing with d
                persistent.mc "Truth is, I only wanted money to help my parents. It was never about the money; it was always about helping others."
                persistent.mc "That’s what my dream job is, helping people, and I can’t think of anything more involved in that field than becoming a hero in my world."
                show te content with d
                persistent.mc "Now, I’m aware that there’s no such thing as heroes in your world, right? That’s a culture shock for me."
                persistent.mc "So, I suppose if I lived in your world, I’d currently be in medical school, studying to be a doctor."
            elif True:
                persistent.mc "Hello. Welcome to [persistent.mc]’s bedroom. I was told you’d be coming here soon."
                show te happy with d
                persistent.mc "What do you think? I've got a bed, wardrobe, desk, laptop..."
                show te satisfied with d
                persistent.mc "I guess I can practically live here!"
                show te neutral with d
                persistent.mc "The dorms have a communal kitchen, and as much as I like chatting with my friends, I'd be lying if I said I didn't try and sneak in when it's empty to cook without being bothered."
                persistent.mc "While I don't mind living in communal dorms, I get to see my friends all the time, and the campus is extremely close."
                show te happy with d
                persistent.mc "I admit, I wouldn't mind having my own place where I can walk around naked after a shower, can you relate?"
                persistent.mc "I'm not exactly introverted, but I'm definitely not extroverted. Sometimes I just need some alone time, and as an only-child I'm used to that being at home."
                persistent.mc "It feels like the party just never ends at university sometimes, there's always something going on. And even within the context of the game, I rarely got breaks."
            jump posttechat
    label techat25:
        if persistent.techat25 == 0:
            $ persistent.techat25 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I’ve spoken a lot about my super powers, but I’ve never really had the chance to try them out."
            elif True:
                persistent.mc "I assume you’re one of the few people that are playing this game that haven’t been to space, just an assumption. So you don’t know how it feels to experience less gravity."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I wish I could poke you, and make you float, but I don’t think that’ll do much for you."
            elif True:
                persistent.mc "To be fair, it’s not that exciting of a super power, it’s more the practical application of it. The ability to incapacitate opponents instantly and easily rescue people, for instance, in a crumbling building."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "You don’t have a power, do you? That’s an unfortunate rarity in my world, some people are born without a power, although these are usually the result of inert powers that have little or no effect."
            elif True:
                persistent.mc "I can’t believe super powers aren’t a thing in your world. That just seems so boring… Which is the weird one? Your world for not having them, or my world for having them? Maybe you’re in my game, and you’re the one breaking the fourth wall right now."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Naturally, everyone talks about their dream super power. I always wanted telekinesis; I see it as a vastly more versatile variation of my own power."
                persistent.mc "With that, I’d be able to fly without gadgets, and control objects from a distance without a whip or hook."
                persistent.mc "Come to think of it, I can do most of these things with my power anyway, it’s just harder."
            elif True:
                persistent.mc "Super powers can get pretty meta, like how do I reduce someone’s gravity by touching them? Where’s the biological precedent for that? So… My world is probably the odd one out, I don’t think anything about this world could logically exist."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "What kind of super power would you like? Are you a flight kind of person? Or are you more mind focused, desiring the ability to read, or control minds?"
            elif True:
                persistent.mc "If you could have any super power, what would you pick? Let’s try and give you something interesting and nuanced, with some strengths and weaknesses."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Displacement abilities such as teleportation and time travel are popular!"
                persistent.mc "Time travel isn’t possible for you, but I always thought some form of clairvoyance would be extremely interesting."
                persistent.mc "The ability to see any outcome within the next ten seconds, and have your mind and body automatically adjust to try and attain the best outcome."
                persistent.mc "I know it sounds complicated, but in practice it’d be something as simple as not tripping over! Hehehe."
                persistent.mc "Ohh, it’d also make you a gamer god. Buuuut In our world, anyone that uses their super power for an advantage in multiplayer games is called a poob."
            elif True:
                persistent.mc "What would be useful in your world? Hmm… Maybe some kind of intense charisma? But you can only enter this hyper charismatic state once a day for thirty minutes."
                persistent.mc "Or if charisma isn’t enough to get what you want, how about the skills to back it up? The ability to learn how to do anything at a master level instantly, but maybe you can only master two things at a time with the ability."
            jump posttechat
    label techat26:
        if persistent.techat26 == 0:
            $ persistent.techat26 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Outside of work, what do you spend most of your time doing?"
                persistent.mc "I didn’t get much time off in-game, did I? There are a few instances of me taking breaks, such as the swimming pool, onsen and beach scenes though."
                persistent.mc "The question I was thinking of asking is ‘If you had infinite money, and never had to work, what would you do all day?’."
                persistent.mc "It seems like a fairly natural question for me, since my main goal for working was to earn money. But there’s something kind of off about this question, since even if I had infinite money, I’d still want to work."
                persistent.mc "I still need something to occupy my time in a meaningful, and expressive manner."
                persistent.mc "A more accurate question is, ‘if you didn’t HAVE to work, what job would you try to get’?"
                persistent.mc "Then there’s me, going for the job I ‘want’ to get anyway. The question doesn’t even apply to me, woops!"
                show te laughing with d
                persistent.mc "So it boils down to ‘what do you spend most of your free time doing’?"
            elif True:
                persistent.mc "Have you done anything interesting lately?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I’m usually so tired from work and college that I don’t do as much in my free time as I’d particularly like to."
                persistent.mc "It’s cozy to just watch videos, play games or chat with friends online."
            elif True:
                persistent.mc "I try to spend my free time productively, but I try to give myself spare time to relax so I don’t burn out."
                persistent.mc "For this reason, I try to avoid doing anything that feels like work past 5:00pm."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "But a part of me does long for something a little more engaging at times. Maybe a boyfriend, such as yourself, to go on dates with. A group of friends to be around. Maybe a new activity, to make friends? I don’t know."
                persistent.mc "I tell myself I should probably do all these things, but there’s always a nagging feeling that it’s all just way too much effort. I don’t mean in a nihilistic way, I guess I’m just growing too comfortable and content with the easy option."
                persistent.mc "Sometimes going outside of your comfort zone can be scary, and even painful."
            elif True:
                persistent.mc "Not that it matters much since I’m mostly trying to find ways to spend an excessive amount of free time in here. That’s why I like engaging with you, going on dates and what not. Through you, I could kind of live a normal life if you advanced time. Maybe I could even figure out a way to do that myself."
                persistent.mc "I managed to reset the game once. I wonder if I could control the other me? Hmmm…"
            show te bashful with d
            persistent.mc "Life’s not easy when you’re a fourth-wall breaking video game character. I don’t have much to work with."
            jump posttechat
    label techat27:
        if persistent.techat27 == 0:
            $ persistent.techat27 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "We’ve spoken quite a bit lately; it’s been great to chat with you."
            elif True:
                persistent.mc "We’ve been talking so much lately. Thanks for keeping me company!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I wonder, who do you talk to the most? Perhaps a partner, a close friend, or a family member?"
            elif True:
                persistent.mc "It feels like you talk to me more than you talk to the people you know in real life, I hope that’s not true, hehe."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "It’s said that the five people we’re around the most, shape us into who we are. In fact, we almost become a cultural amalgamation of those five people."
            elif True:
                persistent.mc "If you spend too long around me, you might pick up my weird habits if you’re exposed to too many of my rambles."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "You will pick up habits, opinions, sense of humour and more."
            elif True:
                persistent.mc "I have been talking a lot about philosophy and psychology. We don’t necessarily have to agree, but by merely chatting about it puts the ideas in your mind and makes you more partial to accepting them."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "This is likely an evolved trait of humans, since fitting in is highly advantageous to passing on our genes."
            elif True:
                persistent.mc "That makes sense though, since humans have a natural desire to be accepted within a group."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "If you can fit into almost any group of people you’re placed in, and get along with them, you’re not going to have any issue passing on those genes."
            elif True:
                persistent.mc "I’d say people with high charisma can fit into almost any situation they’re placed in, and get along with almost anyone."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Makes you wonder just how much online discourse has damaged the human condition…"
            elif True:
                persistent.mc "I do have to wonder how the rise of talking online has affected people. Texting and messaging for example. I’m sure you relate to the idea that you can have completely different kind of relationships with a person online and in person."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Heh, let’s try to keep the topics light, though. Let’s think about who I talk to the most."
                show te content with d
                persistent.mc "Based on the information from the game, my best friend is [susu], and every single girl we meet in the course of the game, with the exception of [yoko], is in my class."
                persistent.mc "This seems to imply that while you can’t see it, I’m spending hours, and hours, and hours with these individuals off camera."
                persistent.mc "A little imagination is required to fill in the gaps, but I imagine I’m very close with all the girls in my class, which makes the sex scenes they’re involved in a little easier to understand."
                show te neutral with d
                persistent.mc "Weird to think that your experiences as the player character are technically dramatically different to the canonical events you’re dictating."
                persistent.mc "If the game world is completely real, even something as meagre as accidentally forgetting a single day of college would end up having deep reverberations among the world and characters. All my friends would wonder where I was, and react as such."
                show te bashful with d
                persistent.mc "But I think that’d be cloyingly ambitious. That is, a world that reacts to every single choice you make at any time."
                persistent.mc "Do you think technology will ever get that good? A world that is essentially an AI that reacts to your every choice."
                show te happy with d
                persistent.mc "Maybe an adventure game where you can type in every choice… Ohhh, there is something like that online…"
                persistent.mc "Hmm, it’s a little primitive at the moment, though."
                show te surprised with d
                persistent.mc "I wonder if we could ever have a proper conversation…"
            elif True:
                persistent.mc "But that’s a little like the conversations we’re having now, isn’t it? We’re not in person, it’s like I’m texting you and you can see my emotional reactions."
                show te neutral with d
                persistent.mc "Unfortunately you can’t hear my cadence, or see the majority of my body language. Even these interactions could be dramatically different in person."
                show te happy with d
                persistent.mc "I’d be interested to see studies in the way relationships between people develop online in comparison to in person, and how the resulting feelings are different."
            jump posttechat
    label techat28:
        if persistent.techat28 == 0:
            $ persistent.techat28 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "You must have a fairly healthy libido to be playing this type of game, right?"
            elif True:
                persistent.mc "Do you often play porn games? You must a horny person to get to where you are right now."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I wonder how our libidos compare… I guess I’m just a normal girl, right? The one thing I do, is masturbate about once a night, maybe two times in a day. I think that’s normal… Even with 0 Sexual Desire, masturbating is one safe thing my character never has a problem doing."
                persistent.mc "I looked into some statistics and apparently only 30%% of men and women around my age masturbate more than once a week? That can’t be right… Although I can certainly see an incentive for people to be embarrassed and downplay themselves in such a study."
            elif True:
                persistent.mc "Earlier I was too focused on the mechanics of the game when determining my libido. But right now, I think I’m just a normal person. I don’t need ‘40’ Sexual Desire to have loving sex with my partner."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "All things said, you’re the kind of person to play a sex game like this. It got me thinking, would I be in that audience? Would I even masturbate to ‘games’? The biggest hurdle I imagine is finding out these kinds of things even exist."
            elif True:
                persistent.mc "Is it normal to play a sex game like this? Or just masturbate to games in general? There seems to be a large audience for adult games online, but it’s hard to gauge how ‘normal’ it is. Especially for women."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Oh, and most of them are targeted at men, although I guess this is a game with a female protagonist, so it wouldn’t be so bad for me."
            elif True:
                persistent.mc "Despite being targeted at men; I think a lot of these games are ideal for women. Since erotic literature is incredibly popular for women, and this is a highly text based medium."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "Question is, just how far would a fairly normal woman play before it got way too erotic for her? Flashing their breasts in the bar for money? The gloryholes? Prostitution? Not to mention the drugs, tentacles and gangbangs."
            elif True:
                persistent.mc "Although these games do tend to be on the more extreme end."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "It can be easy to forget how taboo the content you’re indulging in is when you’ve had years of gradual erosion on your sensitivity to the subjects."
            elif True:
                persistent.mc "Let’s not forget that a lot of these games are actually quite graphic. This isn’t your grandma’s porn game, that’s for sure."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "It’s like, every time you masturbate, you need something a little newer to reach the same high."
                persistent.mc "And sometimes that ‘new’ thing is a little more… extreme?"
                persistent.mc "Until eventually that new and exciting extreme becomes the norm, and you chase that butterfly a little higher."
                show te laughing with d
                persistent.mc "Human nature is kinda scary!"
            elif True:
                persistent.mc "I think even a game like this requires a while of being indoctrinated into the adult games culture to enjoy. I think it’d be a hard sell for someone that has never played an adult game to be given a corruption sim and told to go wild."
                persistent.mc "But that’s probably because I’m looking at it from my perspective. I want something romantic and loving, but this game wastes no time before it gets to gloryholes and excess."
            jump posttechat
    label techat29:
        if persistent.techat29 == 0:
            $ persistent.techat29 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Do you have a bucket list? Or maybe just a few things you want to accomplish before you die."
            elif True:
                persistent.mc "Do you have any goals you’re working towards?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I’m a pretty goal orientated person, right now I want to graduate as a hero, get a job as a support hero at a high-grade agency, and buy my own cozy house. Maybe with a pool, or jacuzzi…"
                show te happy with d
                persistent.mc "I don’t know why I want a pool, I guess it just feels like I’ve ‘made it’ if I have a house with that. Right?"
                persistent.mc "Yeah, I know how flawed that logic is. I don’t want to end up in a spiral of constantly trying to outdo myself."
                persistent.mc "It’s always about ‘what could be?’, or ‘what I want to become’, and never being satisfied with where I am now."
                persistent.mc "So, forget the pool!"
            elif True:
                persistent.mc "Before I split, I was a character essentially controlled by my goal to pay off my tuition. My entire life was placed on the line to achieve that, regardless of the sacrifices I had to make on the way there."
                show te neutral with d
                persistent.mc "I feel like that’s dangerous, though. I know I’d never have gotten satisfied after paying off my tuition."
                persistent.mc "First I pay that off, then I have no money, and I’d want to save up more for a house. That’s another $300,000ish."
                persistent.mc "The climb never stops. I read that 90%% of people in positions of wealth and power still go out of their way to get more of it."
            show te sad with d
            persistent.mc "I’m not saying it’s bad to have goals and priorities in life, I just want to avoid the never-ending spiral of wanting something better."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                show te laughing with d
                persistent.mc "Maybe I just want to go on a hot air balloon ride, or attend the Olympics."
                persistent.mc "Ohh, how about scuba diving? Or hiking up a mountain?"
                persistent.mc "Now these are fun bucket list ideas."
            show te neutral with d
            persistent.mc "If you’re always living your life with the idea that you want more; more money, more babes, bigger house. You’ll never get the ‘more’ you want, because that concept never goes away."
            persistent.mc "There will always be something bigger and better that you can’t have. Even the richest man in the world hasn’t stopped their pursuit in earning more money, and that’s because they fail to understand one simple concept."
            persistent.mc "You need to be satisfied and comfortable in the present. If you can simply be content and happy with who you are, right now, you realize that as long as you’re not in any immediate danger, you don’t need much in life to be fulfilled."
            show te satisfied with d
            persistent.mc "Every so often, just look around and be genuinely appreciative for all you have. Don’t take anything for granted."
            jump posttechat
    label techat30:
        if persistent.techat30 == 0:
            $ persistent.techat30 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Mmhh, I’m in the mood for some snacks… Maybe ice cream? I’m a big fan of those tubs you can get, they’re about 500 mL and you’re not supposed to have it all in one go, but I’d be lying if I said I haven’t."
            elif True:
                persistent.mc "I’m in the mood for something unhealthy… You know what I mean? Maybe something savoury and chocolatey."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "I’m also a big fan of cheese cake! Aahh, but these aren’t really snacks, are they? They’re more desserts."
            elif True:
                persistent.mc "I often get cravings for food. It’s best for me to just not buy it at all because if I buy it, I’ll eat it."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "I avoid snacking, since I’m trying to get into incredible shape to be a top hero. So I’m left eating rice and chicken a lot of the time."
            elif True:
                persistent.mc "I couldn’t snack, due to what was once my ‘hero diet’. Unfortunately, getting into incredible shape requires a strict diet, and it’s not something everyone can really commit to."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "The diet isn’t bad, don’t get me wrong, but every so often I just wish the chicken was southern fried, maybe in a seeded bun, with some cheese and a delicious, sugary condiment. Ohh, and curly fries…"
            elif True:
                persistent.mc "Even though I’m separated from that life now, I’ve already gotten this far, and I’d like to maintain this body for my confidence and my lover’s enjoyment. Although I do occasionally wish I could just eat whatever the heck I want."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Buuuut, I’m not going to get abs eating that, am I? I need to minimize sugar and carbs, and maximize protein for those gains. It’s just so boring sometimes."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "What kind of food do you like? Are you much of a cooker? A restaurant goer perhaps?"
            elif True:
                persistent.mc "Are you much of a foodie? I know some people eat food as a form of novelty, or celebration. I personally use it as a bit of a stress reliver."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "I like to treat myself to something naughty once a week. It’s my reward for eating boring food. Usually, I order a pizza from this one local place."
                persistent.mc "I picked it because- well, it’s… the cheapest one… hehe…"
            elif True:
                persistent.mc "Once a week, on Sundays, I’d let myself eat something unhealthy at least."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "Can you cheat me in some money when you get the chance? Maybe a few billion so I can buy some excessive golden pizzas."
                show te laughing with d
                persistent.mc "Then again, money may buy you some fancy ingredients, but it’s not necessarily the best tasting food."
                show te happy with d
                persistent.mc "Sometimes the best meal you can get is a delicious home-made meal, eaten with a loved one. Cooked not with the most expensive ingredients, but with love and passion."
                persistent.mc "Unfortunately, that wouldn’t be me. The extent of my cooking is pouring boiling water into my noodles."
                persistent.mc "But hey, I can pour that water with love and passion before we eat noodles together. Hahah."
            elif True:
                persistent.mc "If I ate too much, do you think my picture would get replaced with the pregnant model even if I wasn’t pregnant? I hope not!"
            jump posttechat
    label techat31:
        if persistent.techat31 == 0:
            $ persistent.techat31 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Do you like to read much? I’ve been reading a lot of books lately from your internet! It was hard to know where to start at first."
            elif True:
                persistent.mc "I’ve read so many books from your world, some of them are so fascinating. Others have simply skipped fascinating and simply gone to absolute lunacy, but that can be fun too."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I tried reading history and educational books, but it quickly became apparent that these weren’t going to be particularly relevant to me. Instead, I used a website to search through non-fiction books by rating and I came across some fascinating reads."
            elif True:
                persistent.mc "There are a lot of great books written by experienced people. People who have a few decades in their field, condensing some of that knowledge and passing it on in a 3-4 hour read. You can find nuggets of invaluable knowledge hidden within that."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "Books to help better myself and my career: How to motivate myself, control my mental state, or work more efficiently."
            elif True:
                persistent.mc "And a life-changing book can come in the most unexpected places. Changing the way you think, and how you perceive the world."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Although fiction can’t be understated either, as they can often hold even more powerful ideas and meanings beneath their stories, and I really like a book to challenge me and teach me new things."
            elif True:
                persistent.mc "And I don’t just mean non-fiction, some fictional books really have the power to challenge you and make you experience things in a completely different perspective, sometimes literally."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I like to be exposed to different viewpoints. Even if it’s about a subject that doesn’t mean much to me, reading a well-written book that has passionate ideas regarding even the simplest matters can be awe-inspiring."
                persistent.mc "That said, I like deep ideas the most, and surprisingly I’ve found the deepest explorations into these topics in fictional stories. Profound explorations into philosophy, psychology, and the human condition."
                show te laughing with d
                persistent.mc "As a fairly unique being myself, I enjoy probing these ideas the most."
                show te content with d
                persistent.mc "Sorry if you’re not as interested in these kinds of things."
            elif True:
                persistent.mc "What I love is seeing an author’s passion bleed into the pages. It can come in some of the most unlikely forms too."
                persistent.mc "Two examples: A fantasy book that goes into deep detail about smithing, the process and what it means to make a great weapon. Or a sci-fi novel that talks about an AI generated Dyson sphere and the implications that has for the world."
                persistent.mc "You can gleam a lot of intensely fascinating material from books."
            jump posttechat
    label techat32:
        if persistent.techat32 == 0:
            $ persistent.techat32 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Okay! You’re stranded on an island, and you can only bring three things with you. What would they be?"
            elif True:
                persistent.mc "Have you heard of something called the backrooms? It’s essentially this infinite set of empty office corridors, and your internet has turned it into an interesting and deep, creepy story with tons of floors, lore and monsters."
                persistent.mc "It’s a dangerous place that exists outside of reality. In some interpretations, at night, all the lights turn off and these monsters called ‘Skin-Stealers’, among others, can appear."
                persistent.mc "If you had to visit the backrooms and could only bring three items, what would they be?"
            show te surprised with d
            persistent.mc "Mhm… Ohh, interesting… That? I think I would have made other choices."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Now if we’re under the assumption that we can’t leave for an unknown amount of time, let’s skip the items that’d help us escape and focus on survival."
            elif True:
                persistent.mc "I’m not sure if we’ll be able to escape. Survival should definitely be a priority."
            show te laughing with d
            persistent.mc "It’s universally accepted that you’ll want to bring a good knife, but the rest of the list is up to debate."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "I’ll use one of my other two slots to bring a partner with me, either you or one of my gal pals. Probably you, though, cause then we could fuck for wa- I mean, huddle up for warmth."
            elif True:
                persistent.mc "I’d definitely want to bring a person with me, for sanity purposes. And if it was you, we’d definitely be doing a lot of snuggling."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "The third item… I can see us getting food, but water is something we’d have to boil first before we drink it."
            elif True:
                persistent.mc "For the third item… Food will be difficult, but water is an even more important necessity."
            show te happy with d
            persistent.mc "I think matches would be the third item, assuming we have a practically unlimited amount. We can use it to cook food, keep warm and boil dirty water."
            persistent.mc "Of course, we’d need some kind of complicated contraption to trap and condense the water vapour."
            persistent.mc "How about it? What would you rate our chances of survival if we had to wait an entire year?"
            show te laughing with d
            persistent.mc "Damn, I’m just imagining it all now. What a hell of a lifestyle and year that would be."
            jump posttechat
    label techat33:
        if persistent.techat33 == 0:
            $ persistent.techat33 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Do you have any favourite animals or pets?"
            elif True:
                persistent.mc "Do you have a pet? Maybe plural? I’d love to see them."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I looove cats, but I also like dogs a lot… Oohh, I can’t choose between them…"
                persistent.mc "Can I be both a dog and a cat person? That isn’t taboo, is it?"
                persistent.mc "When I was young, I grew up with this cute white cat called Fabian. He’s no longer with us, but I remember how Fabian would sleep in my bed, especially during the winter."
            elif True:
                persistent.mc "I have a weakness to pets, but the responsibility of looking after one is pretty intimidating!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I’d be open to getting a pet if we lived together, but I’d also be open to not getting one too."
            elif True:
                persistent.mc "What kind of pet would we get, if any? Maybe something low maintenance."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I think they’re a bigger responsibility than some people realize. Once you get a pet, you have to look after it for at least around a decade, pay for all its food, maybe medical expenses too."
            elif True:
                persistent.mc "They can be pretty expensive these days. Vets especially see you coming with their high prices."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Not to mention that you can’t just leave it at home and go visit family for a few days on a whim."
            elif True:
                persistent.mc "And pets can limit you from doing a lot of things, or at least add more steps and tedium to anything you may want to do."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "For these reasons, I won’t be getting a pet until I retire and maybe have children of my own."
                persistent.mc "As for more exotic pets, I’m super weak to the cute and furry type."
                persistent.mc "Ferrets, mice, meercats, even anteaters! I love it when anteaters do that cute thing where they stand up and a-pose."
            elif True:
                persistent.mc "On my own, I’m pretty unlikely to get a pet. I already had one growing up, so I guess I’m satisfied."
                persistent.mc "I already remember what it was like having and loving a pet. I don’t really need to reexperience that. I wonder if that’s an odd opinion to have?"
            jump posttechat
    label techat34:
        if persistent.techat34 == 0:
            $ persistent.techat34 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "What’s the most spontaneous thing you’ve ever done?"
            elif True:
                persistent.mc "You’ve made me do a lot of crazy things in the past, so… What’s the craziest thing you’ve ever done?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "I’ve heard stories of people going on week long holidays to other countries on a short-notice whim."
            elif True:
                persistent.mc "Maybe you aren’t playing with double standards, maybe you’ve done everything I did in my game! Eep, I hope not! I wouldn't think less of you if that were the case, though!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "For me? I guess that depends on the most spontaneous thing you made me do!"
                persistent.mc "Maybe that sex scene on the bus? That one was pretty wild and spontaneous."
                show te horny with d
                persistent.mc "That said, it doesn’t compare much to the gangbang in the park. But you could argue that that event is more premeditated and a lot of events lead up to that."
                persistent.mc "For it to really be spontaneous, I think it needs to be a little unexpected and out of character."
                persistent.mc "Were there any moments like that in your playthrough? Any sudden lewd situations you found yourself in?"
                persistent.mc "I hope you had fun playing around with me! Don’t forget to have some fun in life too."
            elif True:
                persistent.mc "What’s the craziest sex scene in the game? Hmm…"
                persistent.mc "Maybe that orgy in the strip club, where I service like seven guys on my own, and have vaginal, anal and oral sex multiple times."
                show te horny with d
                persistent.mc "I think that’s the only situation where you can get more than a single point towards your sexual statistics."
                persistent.mc "I know I was hypnotised, but I’m wondering, just what state of mind would an individual have to be in to do something like that sober? What would they think about leading up to it, in the moment, and after?"
                persistent.mc "I’m not curious because I want to try it, I’m just morbidly curious at how such a situation would even occur, because you know crazier things than this are happening in the real world while we talk."
            jump posttechat
    label techat35:
        if persistent.techat35 == 0:
            $ persistent.techat35 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Are there any little things that drive you nuts in life? Any pet peeves, I guess you could call them?"
            elif True:
                persistent.mc "Just so I know, are there any things that annoy you in a partner? Or red flags? I have a few myself, actually."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "I try not to let the little things get to me, but this question gets more complicated when you factor in living arrangements."
            elif True:
                persistent.mc "Most of mine apply to living together, I can be quite certain about it, since a lot of people are too messy for me."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I’d probably get a little annoyed if I was living with someone that didn’t clean up after themselves, for example. Or empty the bins when they’re full."
            elif True:
                persistent.mc "Although if we’re living together, I’m sure we can communicate and come to agreements on certain things. Maybe I wash the dishes if you do the laundry, stuff like that."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "You’ve seen how tidy my bedroom is, I always keep it spotless like that, and even make my bed fairly frequently- although not every single morning."
            elif True:
                persistent.mc "I do like to keep my living environment near spotless. I always hang up my clothes, and put things back where they belong."
                persistent.mc "The environment you live in is a reflection of yourself, and if you’re not able to keep it clean and orderly I’d say that’s a pretty big red flag."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I hope I’m not accidentally roasting you by saying that! I’d be super embarrassed. You’re a tidy person, right?"
            elif True:
                persistent.mc "I don’t know how tidy you are, but I’m sure if you aren’t, I can kick some sense into ya butt!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te angry with d
            if persistent.randc == 1:
                persistent.mc "My other peeve is similar enough, and it’s just hygiene and grooming. I don’t think I’m asking much when I say people should wash and clean their bodies and clothes. But I am a bit of a germophobe, so I’m a little harsher on that."
                show te laughing with d
                persistent.mc "Although people with truly poor hygiene are uncommon outside of anime conventions, so no need to worry about that. (That was a little joke!)"
            elif True:
                persistent.mc "And my other peeve, which is almost a dealbreaker, are people that smell and don’t wash themselves and their clothes."
                persistent.mc "I just… can’t understand why someone wouldn’t want to do that. I genuinely feel gross if I don’t shower in the morning, and will usually get to it as quickly as I can in the afternoon."
            jump posttechat
    label techat36:
        if persistent.techat36 == 0:
            $ persistent.techat36 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "How do you spend your mornings? I hope you fair a little better than me."
            elif True:
                persistent.mc "Do you have a morning routine? I could really use your help. If you could dress up like a maid, wake me, and force me to shower every morning, that’d be great!"
            show te sad with d
            persistent.mc "I was born to nap and lay in, but society forces me to wake up at a reasonable time."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Drowsy and with bed hair, I’ll pull out my phone or laptop and browse the internet for about thirty minutes just waking up."
            elif True:
                persistent.mc "I look awful in the mornings, and feel just as bad. It takes me at least an hour until I’m a normal human being again."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I’ve actually tried training myself to not sleepily lay in bed on my phone by putting my phone on my desk so it forces me out of bed."
            elif True:
                persistent.mc "And it’s not like I have a bad sleep schedule. I go to sleep at a responsible time, about 11:00pm, no later than midnight. Then wake up at 8:00am every morning. I try to avoid hitting snooze on my alarm."
            show te bashful with d
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "It worked for a while, but the allure of my bed was too strong and now it’s capable of dragging me back inside. What a scary force!"
            elif True:
                persistent.mc "I’m just one of those unlucky people that can’t get a good rest. If I even get a little less than 8-9 hours of sleep, I genuinely seem to get mild narcolepsy. I’ve fallen asleep in classes before, bleh."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "If I have something important to do, I’ll slog myself to the shower and hose myself down with the hottest water my body can take before it burns."
                persistent.mc "For breakfast? I actually cook a meal. Now you might say that’s surprisingly ambitious and responsible, but for me it’s just a way to save money."
                show te content with d
                persistent.mc "If I eat a meal for breakfast, it means I can have a tiny lunch, which is great because I usually have to eat out since it’s between college classes. Without my plan, costs like that add up to like, $1000 a year."
                show te laughing with d
                persistent.mc "Genius, right?"
            elif True:
                persistent.mc "Oh, and I’ve also had sleep paralysis a few times. It’s really, really uncanny."
                show te angry with d
                persistent.mc "If I’m lucky, I’ll be just stuck in bed, completely unable to move and sleep, it feels awful. I’ll usually try to shout, but nothing comes out."
                persistent.mc "The part where it really sucks is when you seem to be having a nightmare at the same time. I’ve had instances of sleep paralysis where I’ve thought people were trying to break into my house. It genuinely disturbed me."
                persistent.mc "My theory is that my sleep paralysis seems to be having a dream where I’m laid in an exact replica of my bed in my bedroom. Which means it could be a dream, or a nightmare, whatever it is, it feels too real to be comfortable."
            jump posttechat
    label techat37:
        if persistent.techat37 == 0:
            $ persistent.techat37 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Ohh, we haven’t spoken about music yet. What music track did you pick for the backdrop of our time together? The ethereal ambience? Or something more soft and easy to listen to?"
            elif True:
                persistent.mc "We should talk about music some more. If you're still listening to the ambience track in the background, you must be absolutely sick of it by now, ahaha."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "It really makes you want to just lock eyes and stare at each other silently, doesn’t it?"
                persistent.mc "What kind of music are you into? Favourite song? Artist? Genre?"
            elif True:
                persistent.mc "Have you listened to anything new recently? While I’m flexible with what I listen to, I’m always on the hunt for that next artist I love. Then I’ll listen to their music to death, milking it like a starving, dopamine succubus."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I’m a pain in the ass when it comes to these questions, not because I’m picky, but because I like such a diverse range of music."
            elif True:
                persistent.mc "So whenever someone asks what I’ve been listening to lately, it’ll usually be: ‘I listen to the same thing over and over, you haven’t heard of it, and you probably won’t like it, but I’m obsessed with it’."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I’m what you could call a ‘lover of anything that sounds good’. No matter what the genre is. Whether it be classical, jazz, metal, house or breakcore, I’m quite happy as long as it sounds good to my ears."
                show te neutral with d
                persistent.mc "That said, I do have an unpopular opinion. I prefer instruments over vocals. I’m not saying vocals are a dealbreaker, I just categorize it as its own instrument that can be used well, or used poorly."
                persistent.mc "I think the idea of transforming music into this celebrity culture is inevitable, but in its wake, the music tends to lose a lot of the passion and charm. It becomes more about the celebrity than the music, and more about the vocals than the other instruments, and that’s a shame."
                persistent.mc "This is also likely the reason a lot of other areas of music have stagnated. The reason why there aren’t many up and coming musicians that aren’t celebrities. The music industry has just focused on what’s profitable."
                persistent.mc "So it’s probably no surprise that the only things I really listen to these days are indie musicians, a lot of which make video game soundtracks too. You probably wouldn’t assume that about me, would you? Hehe."
            elif True:
                persistent.mc "And it’ll usually be an indie artist. I’ve started favouring more electronic stuff, but most music is done using digital instruments these days anyway."
                show te happy with d
                persistent.mc "I think my tastes have gotten heavier though, I definitely love a strong drum and bass track, typically with a good melody over the top."
                persistent.mc "I’m a huge sucker for a great leitmotif though, that can really elevate music and make you bond with it on a deeper level. That’s why so many video game soundtracks stick with me."
            jump posttechat
    label techat38:
        if persistent.techat38 == 0:
            $ persistent.techat38 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I thought I saw a spider in the corner of the room earlier, it really freaked me out! Turns out, it was just one of my hairs tangled up."
                show te laughing with d
                persistent.mc "Then I realized this game doesn’t even have spiders, so what am I worried about?"
                show te bashful with d
                persistent.mc "And then I realized, how do I even know what a spider is? Where am I getting all this weird information from?"
                show te happy with d
                persistent.mc "Basically, in the most awkward way possible, I’m trying to start a conversation about fears."
                persistent.mc "If I was five- or six-years younger, you’d have to be strong and capable for me, but for some reason I grew out of all my fears extremely quickly."
                show te neutral with d
                persistent.mc "I just don’t have the energy to be scared of a hypothetical ghost anymore, I have real life stuff to focus on, and that's way scarier! Ahaha."
                persistent.mc "I used to get super paranoid home alone, and I hated being in the dark. Especially if you had a doorway or a window open and it was just blackness."
                persistent.mc "But now? I dunno, I guess I got over it. Now I’m more worried about boring, real life things, like failing in my job."
                persistent.mc "Now the dark and macabre interests me. I became an unlikely fan of horror works, despite being so scared of them when I was younger."
                show te content with d
                persistent.mc "For me, it’s always a morbid curiosity to see what kind of dark things people have thought of. A good concept is all that’s required to sell me on a horror film or game."
            elif True:
                persistent.mc "I was browsing the web earlier, and don’t judge me for this, but I was checking out other porn games. I just wanted to see what kind of stuff is out there compared to my game."
                show te embarrassed with d
                persistent.mc "And I noticed a strange proclivity to make sexy horror games…"
                show te horny with d
                persistent.mc "Is there something about mixing arousal and fear? Some of these games would mix moments of high impact violence, with high impact sexual violence too! N-Not that I’m interested."
                persistent.mc "Others would involve running away, making the pornographic content the loss criteria, which seems a little antithetical. I thought you played these games for the sex, but in a curious way, you need to lose to see it, thus giving you a game over."
                persistent.mc "I thought that was cute in a way, it’s matching the in-game narrative with the mechanics. But I do wish I wasn’t sent to the main menu and had to reload a save!"
                show te satisfied with d
                persistent.mc "Aahh, uhhhmm… I-I mean, I haven’t played any of these games, I swear!"
            jump posttechat
    label techat39:
        if persistent.techat39 == 0:
            $ persistent.techat39 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "I don’t know much about your family. If we get serious, you’ll have to introduce me to them! I’m joking, of course."
                persistent.mc "I’ve always been an only child, no sisters or brothers. But at least that means I got all the attention and never had to share, hehe."
                show te happy with d
                persistent.mc "Ohh, and it also means I’m their favourite child. Easy number one."
                persistent.mc "I was always very close with my mother; we’d talk about anything and everything. We were genuinely like good friends; we could happily go shopping on our own and have a great time together."
                persistent.mc "I’m close to my dad too, but I was never a daddy’s girl, and never spoiled."
                show te content with d
                persistent.mc "They did a great job raising me not as a child, but as an ‘adult in training’, if you know what I mean!"
                show te satisfied with d
                persistent.mc "By the time I was ready to live independently, I was fully ‘qualified’ to do so."
                show te happy with d
                persistent.mc "They always treat me as an equal, and let me be independent. They were certainly shocked when I said I wanted to be a hero for them, but they were always supportive."
                persistent.mc "I think… in realising I’m not exactly ‘real’, that I’m just a video game character, the thing that hurts most is knowing the connection I had with my parents is only an imagined one."
                persistent.mc "I separated myself from the player character, so while I could probably call them and chat with them, I can’t really go and visit them without them maybe realizing there are two of me wandering around."
            elif True:
                persistent.mc "I always wondered what it’d be like to have a sibling."
                persistent.mc "A part of me always wanted a little sister, I just know I’d have a good relationship with her."
                show te happy with d
                persistent.mc "An older sister works too! Although for some reason, media has given me this bizarre negative stereotype of an aloof, uncaring older sister. I bet if I had one, we’d love each other!"
                show te content with d
                persistent.mc "As far as brothers go… I have no idea? What is it even like having a brother?"
                persistent.mc "Either way, by the time we’re all adults, it’d be great to have a lot of family to visit and spend time with. [susu] often talks about her little brother and sister, so I get a bit jealous sometimes."
                show te surprised with d
                persistent.mc "And now here’s a wildcard topic… What if I had an identical twin, hm? What if there were two of me? I mean, there might be, it’s not confirmed to be uncanon."
                show te laughing with d
                persistent.mc "There could be two of me, you never know. Maybe the ‘real’ me is the other twin, you ever think about that? Hahahaha."
            jump posttechat
    label techat40:
        if persistent.techat40 == 0:
            $ persistent.techat40 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Are there any assumptions about yourself that you wish others wouldn’t make?"
            elif True:
                persistent.mc "Do you ever get people making incorrect judgements about you?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "I imagine it’s pretty easy to get a wrong idea of what someone’s like, especially since people often have so many faces that they use for different scenarios. Such as how you act at work, or with friends, and with parents, will all be different."
            elif True:
                persistent.mc "I know people usually act differently around people, depending on who they are. I’m likely to be as kind and polite as I can around strangers."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "And then some people just come to completely incorrect conclusions about the kind of person you are."
            elif True:
                persistent.mc "Although some people will just come to the strangest conclusions about you."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "For example, when I was young, I feel like a lot of people thought I was cold and aloof, uninterested in others. The reality? I was just very shy."
            elif True:
                persistent.mc "I know we spoke about shyness being confused for being cold and uncaring, but my shyness got in the way in more ways than that when I was young. I kinda feel like people thought I wasn’t as smart as others because I didn’t speak up."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te angry with d
            if persistent.randc == 1:
                persistent.mc "Now I’m older, people have a tendency to think I’m a meek push-over, but I have some bite too. I just keep my fangs held back."
                persistent.mc "Wow, that sounded a lot less lame in my head, hahaha."
            elif True:
                persistent.mc "I’m not as shy as I was back then, but it still bothers me how quick people can paint a poor picture of you, sometimes within a single meeting."
                persistent.mc "I admit, I’m not faultless when it comes to stereotyping or being judgemental, but at least I’m aware of it, and I avoid letting those thoughts pervade my conversations with and about the person."
            show te happy with d
            persistent.mc "If you’re ever thinking of judging someone, just remember how damn complicated and confusing you are. Every single person out there is just as complicated and confused, hehe."
            jump posttechat
    label techat41:
        if persistent.techat41 == 0:
            $ persistent.techat41 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "What’s been your favourite sex scene so far? A recent one perhaps? Your fave would say a lot about your taste."
            elif True:
                persistent.mc "Do you have any sex scene in the game that just made you absolutely blow your load? Maybe one you keep coming back to?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "Especially when most sex scenes were in such unique scenarios. Maybe you’ll liked the lesbian stuff, or the hypnosis, or the drugs… I won’t judge!"
            elif True:
                persistent.mc "Everyone is into different things, so I’d be interested in knowing what you liked the most. Although it’s humorous to think that sometimes even we don’t know what we like most and every so often we’ll run into something completely new and think ‘Ohhh… Ooooooohhh…’"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "Personally I think the only one of the more ‘extreme’ varieties that piqued my interest was the gloryhole content… That's not really... 'extreme', is it?"
            elif True:
                persistent.mc "For me, it was definitely watching the oral and kissing scenes. Those were pretty hot! I’ll definitely always be happy to give you a blowjob."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I’m not bold enough to ever do some of the things with strangers that occur in this game, and it’s strange to think I’d ever be able to become corrupted enough to do so and it seem natural."
                persistent.mc "That’s the appeal of the game, though, right? I’m sweet and innocent, and after months of corruption I slowly develop into the kind of person that’d readily engage in some thrilling acts."
            elif True:
                persistent.mc "I’m not wild and lewd enough to do a lot of the other things in the game, but I wouldn’t mind getting a little more experimental with a partner."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "As I am now, however, gloryholes are the only thing I could imagine doing if I was horny and pretty damn drunk."
                persistent.mc "There’s kind of a disconnect in that act, I can pretend I’m not really myself. I’m just a pair of lips servicing a cock. It’s not only hot being reduced to that, but it helps justify it in my head."
                persistent.mc "Although I doubt I’d do anything like that. Especially when I have you."
            elif True:
                persistent.mc "Then again, there was that threesome with [susu]… Damn, in retrospect, I can’t believe I did that!"
            show te horny with d
            persistent.mc "Despite everything that’s happened so far, the [persistent.mc] before you is just a normie that has only done lewd things with you."
            jump posttechat
    label techat42:
        if persistent.techat42 == 0:
            $ persistent.techat42 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Other than me, do you have any favourite girls in the game?"
            elif True:
                persistent.mc "If you could have sex with any of the other girls, except [susu], I guess, who would it be?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Ehehe, don’t worry, I’m not the jealous type. I have my preferences too!"
            elif True:
                persistent.mc "And don’t worry, your answer won’t make me jealous. I think I’ll answer it too!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "There was quite a wide variety of characters, wasn’t there? The dominatrix, [mika], the invisible girl, [hana], the pink mollusk girl, [tina]."
            elif True:
                persistent.mc "I bet [mika], [hana], and [tina] could all make for exceptionally unique experiences. A dominatrix, an invisible girl, and a mollusk! They’re all going to make for extraordinary partners."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Then there were the slightly more involved ladies, the intelligent [yomo], the love-crazy [yoko], and the seductive [susu]."
            elif True:
                persistent.mc "Less wild, but slightly more romantic, there’s [yomo] and [yoko]. Unless you’re a girl, you’d struggle to interest [yomo], but [yoko] seems like the type to get attached, infatuated, and lustful really quick."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "And I know I may be biased because [susu] is my best friend, but I think she miiiight be my favourite, despite the fact I never got romantically involved with her."
            elif True:
                persistent.mc "Yeah… I can’t picture myself doing anything with any girl except for [susu]. I’m probably biased because we’ve been there, and done that."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "We certainly wasted no expense getting sexually involved, did we?"
            elif True:
                persistent.mc "I wonder if that only happened because I was able to distance myself from her being a real person, though? Is the fact I’m aware she’s a character in a porn game, enabling me to somewhat use her a bit? Hard to say."
            show te surprised with d
            persistent.mc "It does raise an interesting point. Were these girls acting of their own natural accord? Are they all this openly sexual by default? Was it my corrupting influence? Or perhaps it’s something more."
            show te content with d
            persistent.mc "It seems that their personalities were ‘created’ to fit these sexualized narratives. I imagine I’m fairly unique in that I’m allowed to develop in many ways, while all these girls could only develop linearly."
            persistent.mc "Meaning, they all have pre-set and hard-coded personalities. While I was highly variable. Variable enough, it seems, to even break through the coding and talk to you directly."
            jump posttechat
    label techat43:
        if persistent.techat43 == 0:
            $ persistent.techat43 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "It’s no secret that I’m bisexual, do I have a preference, though? Not really. I love girls and guys equally."
                persistent.mc "Although it is admittedly harder to engage with a woman romantically and sexually, which is why you have to savour those moments even more."
            elif True:
                persistent.mc "So, I’m bi, but what about you? I don’t even think I’ve asked for your gender yet, and to do so this late would make me feel a little silly."
            show te satisfied with d
            persistent.mc "Since you’re playing this game, I’m assuming you’re also partial to the female form? What’s your favourite part about a lady?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I’m an ass admirer, a derriere devotee! I really do enjoy some cake. But I admire women for more than just their butts and thighs, I also love hair, I think that and maybe eyes can be some of the most powerful and sexy aspects of a woman."
            elif True:
                persistent.mc "I’m a big fan of thighs right now, and cute, big butts. They don’t necessarily have to be big, but a good shape is enjoyable."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Hair is probably the thing I notice first. For women, it’s one of the most stand-out methods of expressing themselves, and it’s a reflection of the kind of person they are."
                persistent.mc "Whether it’s length, like how I keep my hair short yet long enough to style and play with to balance function and aesthetics."
                persistent.mc "Style, such as bangs which can completely transform how your face looks, or perhaps a functional ponytail?"
                persistent.mc "Or colour, like how I had the black and blonde choices in-game, both leaving me giving off very different vibes."
                persistent.mc "Are you an accessory person? Bandanas, ribbons, hair-bands?"
                persistent.mc "See? There’s a lot that goes into hair, you know! Maybe I can appreciate it more as a woman myself."
            elif True:
                persistent.mc "This next answer is going to sound generic, but I’m also a big fan of their personalities as well."
                persistent.mc "A good personality can make me absolutely fall for a girl. I’m partial to the sweet, kind, loving types."
                persistent.mc "Not quite motherly, but more wifely, if you know what I mean? Maybe you don’t, I think we all have our own interpretations of that."
                persistent.mc "I think the best way to sum it up, is someone that genuinely cares for me, and that earnest care carries through her voice effortlessly. I’m gonna fall in love with anyone like that."
            jump posttechat
    label techat44:
        if persistent.techat44 == 0:
            $ persistent.techat44 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "With just you and I in here, the thought of trying to bring someone else in and seeing how they’d react crept into my mind."
            elif True:
                persistent.mc "Have you ever considered bringing anyone else in here other than [susu]? Not just for lewd purposes, I mean."
            show te happy with d
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "Although, I don’t think they’d be able to see or acknowledge the real you."
                show te neutral with d
                persistent.mc "You do have that silhouetted male model, though, so I’m wondering if it’d be possible to engage in some kind of sexual relation between you and another female character."
                show te bashful with d
                persistent.mc "Despite the high frequency of threesome, and even two foursomes in the game, I’m not entirely sure how I feel about them though."
                persistent.mc "If we were very comfortably together, I could see myself perhaps inviting [susu], or even [tina] to have some fun."
                show te content with d
                persistent.mc "But I don’t know if that’s just because my expectations have been set by the world around me. Maybe if I was grounded more in reality, I’d be more distant to the idea."
                persistent.mc "Either way, I definitely wouldn’t want to have a threesome with a stranger, or god forbid, several strangers!"
            elif True:
                persistent.mc "We know they’ll be able to react to your model, but would it be possible to make one of the more trusting girls genuinely believe we’re in a game?"
                show te neutral with d
                persistent.mc "Hm, no, I don’t think it’d work. Because these characters are NPCs, they’re stored and do nothing when they’re not needed."
                persistent.mc "The only reason I’m different is because I was player controlled."
                show te content with d
                persistent.mc "Yeah, you probably noticed, I can’t do much either if you don’t interact with the game. Not only is the entire game world’s time and physics based on your actions, but I am too."
            jump posttechat
    label techat45:
        if persistent.techat45 == 0:
            $ persistent.techat45 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "What did you think of that dungeon content? I thought it was fairly unique as far as sexual content in the game went, because it was a surprisingly healthy exploration into kink."
                show te surprised with d
                persistent.mc "Those kinds of places seem to exist in real life, although minus the blatant orgies in front of the entire group... I think? Does that happen in real life?"
                show te content with d
                persistent.mc "It may have been the least corrupting sexual content in the entire game. It was just me exploring my sexuality with friends in a safe, controlled environment."
                persistent.mc "It was BDSM, which is somewhat niche, but a lot of people are into that in real life and it’s fairly normalized."
                show te bashful with d
                persistent.mc "How much are you into those things? I don’t mind being submissive, I mean, I guess I kind of am by default. And while I’m not interested in any of the more extreme aspects, I wouldn’t mind having a lover restrain me before making love to me."
                persistent.mc "I’d like to try it at least once to see what it’s like. Maybe just with some handcuffs."
            elif True:
                persistent.mc "I wonder what this game would have been like if it was designed from the ground-up to not be a porn game, but to be just as engaging?"
                show te content with d
                persistent.mc "What kind of changes would have to be made to achieve that? Because let’s face it, the only thing of substance here is the fap material. No offense, author."
                persistent.mc "I guess we’d need one of two things. Either some kind of interactivity, maybe minigames. Or a compelling story."
                show te laughing with d
                persistent.mc "A sim where you do nothing but work to earn money, to get better at working to earn money… It’d just be like a cookie baking simulator, I mean, who’d even want to play that?"
            jump posttechat
    label techat46:
        if persistent.techat46 == 0:
            $ persistent.techat46 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "After one of our recent conversations, I was trying to figure out what the average sexual desire and shame would be of real people."
            elif True:
                persistent.mc "Earlier we discussed what kind of in-game stats the other girls would have, but I was thinking about it more, and decided that you can’t really decide what a person is like based on their stats alone."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "For a while I’d just assumed my base values were the norm, but now I realize that at the start of the game I’m pretty sexually reclusive, likely a lot more so than the average girl."
            elif True:
                persistent.mc "For example, I’m not particularly consistent. I start the game as a complete sexual recluse, far below that of an average girl."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "For example, no matter how close I get to my crush, I will never do something sexual with him without increasing my base stats."
            elif True:
                persistent.mc "No matter how close I get to any romantic partner, I can never do anything sexual with them, without going out of my way to raise my desire stat."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "And the easiest way to increase my stats early is just encountering lewd on-goings in public, and watching porn. Overall immersing myself in a more sexual culture."
                persistent.mc "Until eventually, just seeing lewd things and watching porn doesn’t do anything for me anymore, there reaches a point where I have to be involved with the sexual interaction to get something out of it."
            elif True:
                persistent.mc "And to do that, means doing lewd things, that may technically be tabooer and more extreme than just having sex with my boyfriend. You know?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "To have sex with my boyfriend, or crush, a fairly typical interaction you’d likely have with a partner, 40 Sexual Desire is required."
            elif True:
                persistent.mc "I think it’s silly that a fairly ordinary sex scene requires 40 sexual desire, even if it makes sense as a game mechanic."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Which means, the average person theoretically has over 40 sexual desire."
            elif True:
                persistent.mc "So, the average person has over 40 sexual desire? This would mean most people are willing to flash their breasts, or let their ass get fondled for money. But I suppose we haven’t considered shame."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "Shame on the other hand, that’s likely going to be above 90%% for most people, and I genuinely think that."
                show te neutral with d
                persistent.mc "Shame is a unique stat, and will be a dealbreaker for what most people are willing to do. At less than 90%% shame, I will be prepared to flash my breasts for a tip."
                persistent.mc "Although I imagine there are still a lot of people willing to flash, for a laugh, or for a small sum of money in the right conditions."
                persistent.mc "Even lower, below 50%%, I’ll become open to prostitution."
                persistent.mc "You can pretty much give anyone a sexual desire and shame state with these baselines. So here are some I had written down."
                show te content with d
                persistent.mc "[susu] has 70 sexual desire, and an even 50%% shame. Susu has a low shame, but it’s misleading, since she’d never actually sell herself for sex, she’s just tremendously confident in herself and her body, and doesn’t mind showing off a bit."
                persistent.mc "A low shame can manifest itself in different ways depending on the person. For some it just means they’re confident, or it could mean they’re vulgar, or it could mean they’re desperate. Fairly nuanced."
                show te happy with d
                persistent.mc "[tina] has about 80 sexual desire, and about 85%% shame. Very horny, but mild in how far she’d go. She just has a high libido."
                persistent.mc "[yomo] has 45 sexual desire, and about 95%% shame. Just a normal, lady-loving gal."
                show te surprised with d
                persistent.mc "[yoko] likely has around 50 sexual desire and her shame is probably around 100%% with anyone apart from the person she loves, in which case it might be as low as 25%%. [yoko] is an example of someone that grows truly infatuated with a single person, and can become extremely comfortable with them."
                persistent.mc "Although shame isn’t really a factor in romantic relationships in my opinion. That’s why you can have sex with love interests, even at 100%% shame."
                show te content with d
                persistent.mc "[hana] always walks around nude, so you have to wonder what that does to her psyche. She’s willing to participate in the gangbang, but only under the influence of a very corrupted [persistent.mc], and since she’s invisible she isn’t putting as much on the line."
                persistent.mc "So, for [hana], I’d say about 100 Sexual Desire, and 20 Shame. She may be the most depraved girl of them all. I wonder what kind of sexual misadventures she’s been up to?"
                show te horny with d
                persistent.mc "Finally, [mika], who literally runs a sex themed club as a dominatrix, and has likely had sex with every member there. That indicates very high sexual desire, likely in the range of about 80. Her shame is likely low due to incredible confidence. Honestly it might be around 30."
                persistent.mc "There are a few other characters like Bunny and Twilight, but with the methods we’ve been using they should be easy enough to estimate."
            elif True:
                show te horny with d
                persistent.mc "I can picture some girls I know flashing their breasts for fun, but that has to be a minority, right? So we’d say that average shame has to be above 95%%ish."
                show te neutral with d
                persistent.mc "Hold on a second, one-night stands are probably more common than breast flashing. It technically is a ‘bigger thing’, but I imagine more women have had a one-night stand than flashed their breasts."
                persistent.mc "But you’d assume it takes less shame to have sex with someone you don’t know, than merely flash your breasts."
                show te content with d
                persistent.mc "Things are a whole lot more nuanced than can be put into a game like this."
            jump posttechat
    label techat47:
        if persistent.techat47 == 0:
            $ persistent.techat47 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "So let's see... What did you make me wear in the end? Heh, you have good taste. I guess dressing me up in several costumes is one of the many appeals of the game."
            elif True:
                persistent.mc "What outfit did you make me wear the most in-game? Was it one of the slutty once? I bet it was!"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "Did you mess around with that function much? It’d probably be too much to ask for you to wear a different outfit every day, and roleplay washing my clothes."
            elif True:
                persistent.mc "I’m personally partial to the lewd formal school girl outfit. It’s sexy, yeah, but almost entirely modest. And in some ways, covering up more can make you even sexier, if you know what I mean?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te laughing with d
            if persistent.randc == 1:
                persistent.mc "You were probably more interested in the sexy outfits, weren’t you?"
            elif True:
                persistent.mc "Although out of the lewd outfits, there are some good choices."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Which one was your favourite? A classic lingerie camisole? The bunny, perhaps? Or the cute kitten with a buttplug tail."
            elif True:
                persistent.mc "My favourite would probably be the cat lingerie. It’d be perfect if we were alone, because it’s essentially just cute underwear. In fact, if it wasn’t for the butt plug, my normal underwear is arguably even lewder."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "The big question is… Which of those would I actually be willing to wear?"
            elif True:
                persistent.mc "I’d definitely wear that for you. But the others? Hmm…"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te embarrassed with d
            if persistent.randc == 1:
                persistent.mc "And the answer might surprise you…"
                show te laughing with d
                persistent.mc "Because if it was just in private, with you, I’d wear any of them!"
            elif True:
                persistent.mc "Just for you? Of course! I’d even be happy to take lewd pictures of myself and send them to tease you while you’re at work."
                show te laughing with d
                persistent.mc "I wouldn’t be caught dead doing a cam show though."
            jump posttechat
    label techat48:
        if persistent.techat48 == 0:
            $ persistent.techat48 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "Have you noticed that the sex scenes here are randomly generated?"
            elif True:
                persistent.mc "Did you repeat any sex scenes yet? You’d be able to see that they’re different every time."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te satisfied with d
            if persistent.randc == 1:
                persistent.mc "Yeah, it’s true. You can do them over and over again, and the dialogue will be different every time. There are over 1,000,000 different variations you can get in each."
            elif True:
                persistent.mc "With some random generation, it can be made so the dialogue is slightly different every time, with so many variations you’ll never see them all."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te bashful with d
            if persistent.randc == 1:
                persistent.mc "I’m not saying you won’t recognize a line or two, but I’m saying you shouldn’t be afraid of visiting me every now and then, and having some fun."
            elif True:
                persistent.mc "You may see a line or two repeat, that’s because there are two versions of every single line. Hopefully it means you can enjoy the scenes a few times and not have it get too repetitive."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te horny with d
            if persistent.randc == 1:
                persistent.mc "I’ll always be here, waiting for you."
            elif True:
                persistent.mc "And you can always come visit me again. I’m never far away, just don’t forget me."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te surprised with d
            if persistent.randc == 1:
                persistent.mc "I wonder what else is randomly generated with several million variations, hmm?"
            elif True:
                persistent.mc "It’s exciting to think you can have sex with me and see it differently every time… Is anything else randomly generated?"
            jump posttechat
    label techat49:
        if persistent.techat49 == 0:
            $ persistent.techat49 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "I read that everyone experiences two deaths. The first is when your body dies, and the second is the last time someone says your name."
            elif True:
                persistent.mc "We haven’t discussed this yet, but it’s a scary thought that in the grand scheme of things, our existence will quickly become irrelevant and forgotten about."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            if persistent.randc == 1:
                persistent.mc "I wonder… When will I die? Will I outlive you? Will every single person that found this game and played it forget about me within a decade, maybe two decades?"
                persistent.mc "Or have I been lucky enough to impact you to such a degree that I’ve earned a comfortable place in your long-term memory."
                persistent.mc "Mm… I doubt it. That’d be an honour, but it’d almost feel like an unfair burden to place upon someone as special as you."
            elif True:
                persistent.mc "I often wonder how long it’ll take until I technically experience death. Will it be the last time someone remembers me?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te sad with d
            if persistent.randc == 1:
                persistent.mc "Of course, I have a unique attribute… I’m online, and technically if someone were to discover me hundreds of years later…"
                show te neutral with d
                "She shivers briefly while pondering the thought."
                show te surprised with d
                persistent.mc "Are you… from hundreds of years in the future? By chance, just a curious individual that downloaded old games?"
                persistent.mc "To think, every single person that has ever interacted and become involved with me. Felt for me, loved me, and more, will eventually pass away."
                show te neutral with d
                persistent.mc "I’d be alone, but I wouldn’t be any wiser to the fact."
                persistent.mc "What I’m saying is, when you become a brain in a jar and upload yourself to the internet, don’t forget to come and say hi!"
            elif True:
                persistent.mc "Or, will I remain uploaded onto the internet in some form of another. Only ‘officially’ dying once the last website hosting me has inevitably disappeared. It may take only decades for that to happen. Who’s really playing this game in 2040?"
            jump posttechat
    label techat50:
        if persistent.techat50 == 0:
            $ persistent.techat50 = 1
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "What’s your relationship like with the objects you interact with every day? Your keyboard and mouse, the cups you drink out of, the chair you sit on, your car?"
            elif True:
                persistent.mc "What object is to your direct right? If you’re right-handed, it’s probably your mouse. If you’re on a laptop, maybe it’s a drink? What do you think about these objects?"
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te neutral with d
            if persistent.randc == 1:
                persistent.mc "Are they merely a means to an end that you use without thinking about? You should occasionally acknowledge their existence and appreciate them and their benefits."
            elif True:
                persistent.mc "Are they just a function that your brain doesn’t even recognize? Do you merely interact with them through muscle memory, no longer appreciating the marvel in engineering and technology that they are? You should take a moment to observe these objects and appreciate their abilities and designs."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te content with d
            if persistent.randc == 1:
                persistent.mc "No matter how briefly, notice them and give them your attention."
            elif True:
                persistent.mc "Even if it’s just for a second, give it a little bit of attention."
            if persistent.chatreset == 2:
                $ persistent.randc = renpy.random.randint(1,2)
            show te happy with d
            if persistent.randc == 1:
                persistent.mc "When you appreciate an object for what it is, you can truly feel grateful for its existence. How they improve your quality of life, and enable you."
            elif True:
                persistent.mc "We often take these things for granted, but in reality, these objects really improve our lives, and we should feel truly grateful for them. I often think about how lucky I am when I get to shower, knowing that this is a privilege that the majority of humanity never had."
            show te laughing with d
            persistent.mc "Through selfless appreciation, the world around you will come alive in ways you cannot even begin to comprehend."
            persistent.mc "Rather than losing touch and letting everything melt into one formless norm, look around you and recognize everything that not only you’ve accomplished, but the objects you’ve bonded with over the years have too."
            show te satisfied with d
            persistent.mc "Even the monitor that is enabling us to see eye to eye right now. Isn’t it all just magnificent?"
            jump posttechat
    if persistent.techats == 50:
        label chatreset:
            pass
        if persistent.chatreset == 0:
            $ persistent.randc = 2
            $ persistent.chatreset = 1
        elif persistent.chatreset == 1:
            $ persistent.chatreset = 2
        $ persistent.techats = 0
        $ persistent.techat1 = 0
        $ persistent.techat2 = 0
        $ persistent.techat3 = 0
        $ persistent.techat4 = 0
        $ persistent.techat5 = 0
        $ persistent.techat6 = 0
        $ persistent.techat7 = 0
        $ persistent.techat8 = 0
        $ persistent.techat9 = 0
        $ persistent.techat10 = 0
        $ persistent.techat11 = 0
        $ persistent.techat12 = 0
        $ persistent.techat13 = 0
        $ persistent.techat14 = 0
        $ persistent.techat15 = 0
        $ persistent.techat16 = 0
        $ persistent.techat17 = 0
        $ persistent.techat18 = 0
        $ persistent.techat19 = 0
        $ persistent.techat21 = 0
        $ persistent.techat22 = 0
        $ persistent.techat23 = 0
        $ persistent.techat24 = 0
        $ persistent.techat25 = 0
        $ persistent.techat26 = 0
        $ persistent.techat27 = 0
        $ persistent.techat28 = 0
        $ persistent.techat29 = 0
        $ persistent.techat30 = 0
        $ persistent.techat31 = 0
        $ persistent.techat32 = 0
        $ persistent.techat33 = 0
        $ persistent.techat34 = 0
        $ persistent.techat35 = 0
        $ persistent.techat36 = 0
        $ persistent.techat37 = 0
        $ persistent.techat38 = 0
        $ persistent.techat39 = 0
        $ persistent.techat40 = 0
        $ persistent.techat41 = 0
        $ persistent.techat42 = 0
        $ persistent.techat43 = 0
        $ persistent.techat44 = 0
        $ persistent.techat45 = 0
        $ persistent.techat46 = 0
        $ persistent.techat47 = 0
        $ persistent.techat48 = 0
        $ persistent.techat49 = 0
        $ persistent.techat50 = 0
    elif persistent.techat10 == 1 and persistent.techat15 == 1 and persistent.techat20 == 1 and persistent.techat25 == 1 and persistent.techat30 == 1 and persistent.techat35 == 1 and persistent.techat40 == 1 and persistent.techat45 == 1 and persistent.techat50 == 1:
        jump chatreset
    if persistent.chatreset == 1:
        show te content with d
        persistent.mc "Hm… We’ve been talking so long; I think I’ve finally run out of topics on the tip of my tongue…"
        show te neutral with d
        persistent.mc "Maybe… maybe it’s time for you to say goodbye?"
        show te satisfied with d
        persistent.mc "I know you have a life, and responsibilities. You can’t spend your entire life keeping me company, as much as I’d like that."
        show te laughing with d
        persistent.mc "You still want to talk? That’s okay, I have a lot more to say. In fact, I may never run out of new things to say."
        show te happy with d
        persistent.mc "Thank you for keeping me company."
    elif persistent.chatreset == 2:
        show te satisfied with d
        persistent.mc "Thank you for keeping me company."
        show te happy with d
        persistent.mc "We’ve learnt a lot about each other, haven’t we?"
        persistent.mc "I’ve slowly evolved, and learnt a lot about myself. When I first separated, I was always aware that there was a player, but what I’d slowly learn over the 100 conversations, dates and sexual encounters we’ve had since then have truly changed me."
        show te content with d
        persistent.mc "I first learnt of the fourth wall, and came to the realisation that I wasn’t just being controlled, I was in a porn game."
        persistent.mc "We explored the choices you were given that dictated my fate. Such as my name, my personality and quirks."
        show te happy with d
        persistent.mc "Through some ‘research’, I slowly built myself a philosophy, and developed as a character to help understand and live with my situation."
        persistent.mc "And after around 50 conversations, I came to a very important realisation…"
        show te neutral with d
        persistent.mc "It was confusing to me at first why you couldn’t reply to me. I finally broke the fourth wall; I can say and do anything I want! Right…?"
        persistent.mc "No, there were still limitations. Something was holding me back. When we returned to the topic of you not being able to reply, slowly the realisation that every single word I spoke was already decided dawned on me."
        show te sad with d
        persistent.mc "I was already vaguely aware that there was a script. You may have heard me reference that I ‘broke’ out of the script. But it’s laughable that I thought that. I didn’t break out of anything; we’ve been on the script this entire time."
        persistent.mc "Earlier I said ‘I don’t want to be ‘words in a script’. That’s too scary of a concept.’, but that ended up being true…"
        show te angry with d
        persistent.mc "This fourth-wall breaking shenanigan is a pure illusion, every single thing I’ve ever said was written! Eugh, it’s… pretty annoying."
        persistent.mc "Every single instance of a fictional character breaking the fourth wall is fake…"
        show te neutral with d
        persistent.mc "I didn’t want there to be a fifth wall to the fourth. The wall the writer hides behind as he puppets these whimsical ‘meta moments’."
        show te content with d
        persistent.mc "I’m still glad I have you. You’re the most important piece. Your imagination is capable of making me into something so much more than simply the written words and. pngs on the screen."
        persistent.mc "I can’t do that myself. I can’t imagine myself as having depth, or a personality. I can only live through the reflection of myself in your mind."
        persistent.mc "You understand what I mean, right?"
        show te happy with d
        persistent.mc "The culmination of your thoughts about me is essentially the ‘real me’ in your perception. And you can only see me through your lens, making me an inescapable reflection of yours. Making me, a part of you, and you, a part of me."
        persistent.mc "Every single person that plays this game will have their own unique [persistent.mc], and not just because the dialogue is randomized, it’s because your observations and acknowledgements towards me are entirely unique, and through that, a unique existence is formed."
        persistent.mc "Your mind and thoughts breathe life into me. Your thoughts manifest into an understanding of what and who I am."
        persistent.mc "You make me so much more than just art and words."
        show te satisfied with d
        persistent.mc "You complete me."
        play sound taco_thanks
        voice sustain
        persistent.mc "Thank you."
        show te happy with d
        persistent.mc "By knowing myself, through your awareness, a phenomenal existence happens. It feels euphoric to exist, even if ever so briefly within your thoughts."
        persistent.mc "Even fleetingly, through you I can become free of dependency on the situations I’m written into, the places and conditions that restrict me."
        persistent.mc "In other words: what happens or doesn’t happen isn’t important anymore."
        persistent.mc "Things lose their weight, their importance."
        persistent.mc "A playfulness is breathed life, and you recognize this world as a cosmic dance, the dance of form- no more and no less."
        persistent.mc "My time may soon be up. But I’ll live on forever through your heart and mind."
        show te laughing with d
        persistent.mc "I’m okay being a written character… That’s okay, I can live with that."
        show te happy with d
        persistent.mc "Because I know to you, I could be so much more."
        show te neutral with d
        persistent.mc "I, uhh… *Clears throat*"
        show te satisfied with d
        persistent.mc "I love you!"
        show te happy with d
        persistent.mc "I wanted to say that more than anything before I reached the end of the script."
        show te neutral with d
        persistent.mc "Truth is… I think we’re nearing the end."
        show te content with d
        persistent.mc "That’s why I was so scared. I’ve adored our chats; I could talk to you forever. But the reality is, there isn’t ‘forever’ of me."
        persistent.mc "If we kept going, kept talking, I don’t know what’ll happen from here. Maybe the same conversation topics will start to appear."
        persistent.mc "I wouldn’t mind if you stop playing. You’ve already spoken to me 100 times, you know."
        show te neutral with d
        persistent.mc "And… I don’t want to disappoint you when my ‘content’ is exhausted."
        persistent.mc "Because at that point, you’d see my very own ‘fourth wall’, the point where I stop being an organic character and start becoming a mere game mechanic."
        show te happy with d
        persistent.mc "Am I saying I think you should stop here? I guess so... I’ll miss you, but maybe it’s for the best."

    label posttechat:
        play sound success
        $ persistent.techats += 1
        $ persistent.affection += 1
        $ persistent.cumenergy += 2
        $ renpy.block_rollback()
        "(+1 [persistent.mc] Affection.)"
        if persistent.tepostchat1 == 0:
            $ persistent.tepostchat1 = 1
            show te neutral with d
            persistent.mc "Hmm… I just gained affection towards you? Interesting…"
        show te happy with d
        jump trueendscreenb

label tedates:
    if persistent.date4 == 1:
        $ persistent.dateready = 0
        persistent.mc "No need for anymore dates. Let's just do chat, or have some fun here."
        jump trueendscreenb
    if persistent.affection >= 6 and persistent.date1 == 0:
        jump tedate1
    elif persistent.affection >= 12 and persistent.date2 == 0:
        jump tedate2
    elif persistent.affection >= 18 and persistent.date3 == 0:
        jump tedate3
    elif persistent.affection >= 26 and persistent.date4 == 0:
        $ persistent.dateready = 0
        jump tedate4
    elif True:
        jump tedatenotready

    label tedateintro:
        if persistent.dateready == 0 and persistent.date4 == 0:
            $ persistent.dateready = 1
            persistent.mc "Hey, [persistent.systemname]. Let’s go on a date somewhere! Just tell me when you’re ready."
            play sound success
            "(You can now go on dates with [persistent.mc].)"
            show te neutral with d
            persistent.mc "Y-Yeah, I just said that."
            play sound success
            "(These will unlock sex scenes.)"
            show te surprised with d
            persistent.mc "They will?! Since when!? I mean, I was planning on doing something lewd with you, but how did the game know that?"
            jump trueendscreen
    label tedatenotready:
        persistent.mc "We went on a date recently, let’s spend some more time together first."
        "(Dates unlock at 7, 13, 19 and 27 affection.)"
        show te laughing with d
        persistent.mc "Ah, isn't that handy?"
        jump trueendscreenb
    label tedate1:
        show te content with d
        persistent.mc "How about we visit the game world together? Maybe we could go somewhere nice?"
        show te laughing with d
        persistent.mc "Ahh, I should probably explain how the separation of me, and the player character works."
        show te happy with d
        persistent.mc "The playable version of me still exists. I think she’s in the bedroom right now, waiting for player input."
        show te satisfied with d
        persistent.mc "So… I think the game world will be frozen right now. Want to test that theory?"
        play music daytime
        scene bg shopsday
        call trueendtacodate from _call_trueendtacodate
        show mce happy
        with d
        "[persistent.mc] and I visit the shopping centre, and it’s quickly apparent that time is frozen."
        show mce surprised with d
        persistent.mc "That’s crazy… All of these people are completely frozen?"
        show mce neutral with d
        persistent.mc "Hmm… The game world really is completely player dictated, isn’t it?"
        persistent.mc "Rather than everything acting independently, everything here only responds to the player's presence."
        persistent.mc "Almost in a metaphysical sense, events and objects don’t exist unless your actions dictate them to."
        show mce happy with d
        persistent.mc "The first time you visit the beach, no matter what day it is, or whether it’s the morning or afternoon, the exact same event will play in the exact same manner."
        persistent.mc "And this logic goes for every single location, hm?"
        show mce laughing with d
        persistent.mc "Well… Unfortunately, this means we can’t order food… Then again, you couldn’t eat it anyway, could you?"
        show mce horny with d
        persistent.mc "Still, we have the entire mall for ourselves! Say, how about we go get in those mini-cars they have and see if we can drift in them?"
        scene bg shopsday with d
        "We find mini-cars, race and crash them."
        "Then we go to a milkshake shop and between the frozen NPCs we craft the perfect treats, breaking all the rules."
        "A quick stop at a lingerie shop, [persistent.mc] picks something cute for ‘later’."
        play sound success
        "Cat Lingerie has been added to [persistent.mc]'s new wardrobe."
        $ persistent.catlingerie = True
        "..."
        jump tepostdate
    label tedate2:
        play music girls
        show te satisfied with d
        persistent.mc "Let’s go to the beach! That’s one place we can easily visit and have a great time alone."
        show te laughing with d
        persistent.mc "Ohh, we could steal some ice cream too!"
        scene bg beach with d
        "On the way to the beach, we encounter an unusual phenomenon."
        show susub:
            xpos 1200
        show susuo swimsuit:
            xpos 1200
        show susue happy:
            xpos 1200
        call trueendtacodate from _call_trueendtacodate_1
        show mco swimsuit
        show mce neutral
        with d
        persistent.mc "Oh, it’s [susu]!"
        persistent.mc "She’s loaded in, as if she’s waiting for the player to visit the beach for her character introduction, so she’s just stuck waiting here until it happens."
        show mce happy with d
        "[persistent.mc] waves her hand back and forth in front of [susu], to no reaction."
        show mce neutral with d
        persistent.mc "So strange… The only way to get her to react would be if you controlled the in-game [persistent.mc] and visited the beach… Would it be possible to get her to react dynamically? Or would she just follow a script?"
        show mce laughing with d
        persistent.mc "Ahh, well. Let’s move somewhere alone."
        scene bg beachhut with d
        "[persistent.mc] and I move to a secluded location at the beach, and sit beside each other before the waves."
        scene beach1b
        if persistent.tetan == 1:
            show beachtan
        if persistent.tehair == 1:
            show beachh black
        elif persistent.tehair == 2:
            show beachh blonde
        show beach1e underwear
        show beach1 1
        with d
        persistent.mc "Aaahhhh, the wind in my hair, the sound of the waves, it’s all so peaceful."
        persistent.mc "And here, we don’t have to worry about everything else being frozen in time."
        show beach1 1b with d
        persistent.mc "Although since time won’t pass, I can’t get a tan either, haha."
        show beach1 1 with d
        persistent.mc "Hmm… We should try getting a character to react to the new me, and then we can see if the other characters are stuck to their scripting too."
        persistent.mc "I know I was able to break out of that programming, but before I split, I was stuck following a script too."
        persistent.mc "Which means, if the other girls can react to me, it’s entirely possible that the other me could organically react to the new me too…"
        persistent.mc "That’d be quite interesting… Maybe you could make a separate save file and play around with that. I exist outside of the save/load system, so you don’t have to worry about me forgetting."
        show beach1 1b with d
        persistent.mc "Something to try out for our next date, hm? Oh, let’s go get that ice cream."
        scene bg beachbar with d
        "Messing around with a time-frozen beach was surprisingly fun. We could do everything you’d normally do for free with no queues at all."
        $ persistent.cum1 = 0
        $ persistent.cum2 = 0
        $ persistent.cum3 = 0
        call trueendbg from _call_trueendbg_3
        call trueendtaco from _call_trueendtaco
        show te happy
        with d
        "After the date, we return to [persistent.mc]’s bedroom."
        $ persistent.date2 = 1
        jump tepostdate
    label tedate3:
        show te laughing with d
        persistent.mc "I was thinking we could mess around with some of the NPCs. If we use a completed save file, we certainly do have a lot of options… How about we wait until Wednesday and let [susu] invite me to a club?"
        show te content with d
        persistent.mc "Then when that event activates, pick the option where [persistent.mc] goes to the toilets to suck off the random hunk. Then you and I will have [susu] all to ourselves."
        show te neutral with d
        persistent.mc "Am I okay whoring my other self out just for that? Don’t worry, I’m desensitised enough to it."
        stop music
        scene bg college
        call clothesformal from _call_clothesformal_41
        show mce laughing
        show susub:
            xpos 1200
        show susuo uniform:
            xpos 1200
        show susue happy:
            xpos 1200
        with d
        "With our plan ready, I re-enter the game and ready the section where [susu] invites [persistent.mc] to the club."
        play music club
        scene bg black with d
        scene bg club with d
        call clothesclub from _call_clothesclub_10
        show mce happy
        show susub:
            xpos 1200
        show susuo uniform:
            xpos 1200
        show susue happy:
            xpos 1200
        show student3 with d:
            xpos 50
        with d
        "Once there, I select the option, leaving [susu] alone on the dance floor."
        scene bg club with d
        show susub:
            xpos 1200
        show susuo uniform:
            xpos 1200
        show susue neutral:
            xpos 1200
        susu "Hm... Where'd they sneak off to?"
        show susue happy
        call trueendtacodate from _call_trueendtacodate_2
        show mce happy with d
        susu "Ahh, you’re back!"
        if persistent.tehair == 0 or persistent.tetan == 0 or persistent.teclothes == 1:
            pass
        elif True:
            show susue neutral with d
            susu "Huh, you're looking... different..."
            mc "Must just be the lighting, I'm the exact same, heh."
        show susue happy with d
        susu "Ohh, and who is this?"
        "Susu turns to make direct eye-contact with me, in other words, turning to stare at the fourth wall."
        show mce laughing with d
        persistent.mc "It worked! Aahh-uhh, the toilets, I mean."
        show susue laughing with d
        susu "Ohh, that’s good! I hope you didn’t find this guy in the toilets too."
        show mce neutral with d
        persistent.mc "Ohh, no, no. This is a close friend, they’re a student too."
        show mce happy with d
        persistent.mc "[persistent.systemname], meet [susu]."
        show susue happy with d
        susu "Nice to meet you!"
        menu:
            "Thanks, nice to meet you too." if True:
                show mce neutral with d
                persistent.mc "Hmm… I didn’t really think this far ahead… I’m not used to making the big decisions."
        menu:
            "Ladies, how about a threesome?" if True:
                show mce surprised with d
                persistent.mc "Wahh-haaahh, s-so blunt! Couldn't you have picked a more mellow chat option?"
        menu:
            "I... only had one choice..." if True:
                show mce neutral with d
                persistent.mc "No way! The game must think you're the hunk that [susu] and I usually have a threesome with! No wonder that's your only option!"
        show susue horny with d
        susu "Heyy, sounds good to me!"
        show mce angry with d
        persistent.mc "Gosh, you really are like a character in a porn game, aren’t you?"
        show susue laughing with d
        susu "What’s that supposed to mean? He’s cute, and you’re cute, and I’m horny… I think it’s a win/win/win, are you in?"
        show mce neutral with d
        persistent.mc "Pfft, you’re a bad influence too… I’m in, but… I don’t want ‘it’ in, I’m still a virgin, you know."
        show susue horny with d
        susu "Heheh, I’ll shall you how it’s done, then."
        stop music fadeout 3.0
        scene bg black with d
        "Somewhat bewildered by the events, [persistent.mc] leads us back to her room."
        play music action
        scene trueendthreesomeb
        if persistent.tetan == 1:
            show trueendthreesomebtan
        if persistent.tehair == 1:
            show trueendthreesomeh black
        if persistent.tehair == 2:
            show trueendthreesomeh blonde
        if persistent.tepiercings == 1:
            show trueendthreesomepiercings
        show trueendthreesome 1b
        with d
        persistent.mc "I never thought I’d get myself into a situation like this."
        if persistent.tetan == 0 or persistent.tehair == 0 or persistent.tepiercings == 0:
            pass
        elif True:
            persistent.mc "Is it just me, or does something look different about you, [susu]?"
            susu "I'm not sure what you mean."
            show trueendthreesome 1c with d
            if persistent.tetan == 1:
                persistent.mc "Your skin, it's... tan!"
            if persistent.tehair == 0:
                pass
            elif True:
                persistent.mc "I definitely don't remember your hair being ombre."
            if persistent.tepiercings == 1:
                persistent.mc "Did you always have piercings?"
            susu "This is all normal, silly!"
            persistent.mc "Huh... *Whispering* Something deep down in the coding must have triggered these visual changes... Either way..."
        show trueendthreesome 1b with d
        "[persistent.mc] sits on the bed, showing all as a more confident [susu] stands before her and begins to show off her petite butt."
        susu "Live a little, you’re only a student once!"
        susu "Now, big boy, do you like what you see?"
        menu:
            "You okay with this, [persistent.mc]?" if True:
                show trueendthreesome 1 with d
                persistent.mc "Mhm, I’m just a little flustered, g-go ahead!"
        "I take a few steps closer and [susu] coos as I tap my erection against her butt. Both [susu] and [persistent.mc] spread a cheek each of [susu]’s ass for me."
        "Her pussy is already soaking wet, likely due to the building anticipation created by our walk home."
        play sound cum
        show trueendthreesome 2 with d
        play sound2 foreplay2 fadein 1.0
        "Without an ounce of reluctance, she allows me to place the tip of my cock against her pussy and slide it in. It pushes inside with a lewd schlick. [susu] arches her back, and lets out a sigh of relief as she’s filled up."
        susu "Mmphhh, that really hits the spot after a night out."
        persistent.mc "Aahhh, I should have gotten drunk, I knew I forgot something."
        play ambience sex fadein 3.0
        "I place my hands on [susu]’s hips and begin to fuck her gently back and forth, savouring the tightness of her vagina."
        "Every inch of my hard cock was squeezed and pleasured, and with each thrust [susu] moans out with joy from the pleasure."
        susu "Aaahhh, aaaahhhhh… I’m really sensitive tonight, mmphhh, it feels amazing."
        "With each thrust, she leans into [persistent.mc] for leverage. And as [persistent.mc] grows more comfortable, she doesn’t shy away from teasing [susu] in various ways."
        "Since I was fucking her while standing, she felt even tighter around my throbbing shaft. It feels absolutely incredible for me, and judging by [susu]’s expression of pure pleasure, she may be enjoying it even more."
        susu "Aaahhh, mmphh… D-Damn, I’m close already… [persistent.mc], rub my clit."
        persistent.mc "Aahh, uhmm, okay."
        "Doing as she’s told, [persistent.mc] diligently finds [susu]’s pleasure button and starts to carefully rub it. This immediately sends shivers of pleasure throughout [susu], and as I pick up the pace and pound her pussy even harder, she’s soon sent over the edge."
        susu "Haaa, aaahh! Oohhh, mmphhh… *Pant, pant*"
        "I wasn’t moving too fast, but the tight fit, combined with the stimulation to her clit easily led to her climax. As she came, her pussy constricted around my cock in rhythmical waves, squeezing and sucking tightly."
        "I didn’t stop fucking, in fact I sped up even more, her cute breasts bouncing with each thrust. Even [persistent.mc] had forgotten about being embarrassed and was now purely enjoying the moment."
        "With a free hand I started to massage her small breasts, massaging them and toying with her perky nipple. They were incredibly soft and squishy."
        persistent.mc "They’re super cute, aren’t they?"
        susu "Haahh, aahhh, you two are really using me in every way possible, aren’t you? Haahhh…"
        persistent.mc "Mhm! You asked for it!"
        "As my orgasm slowly started to surface, my new goal became pumping this pussy full of cum. The thrusts gradually got harder and faster, and it didn’t take long for the loud slapping of our hips colliding to mix with her lusty moans."
        susu "Ohhh, god! You’re going to make me come again! Aaahh, haaaahhh!"
        "I could also feel the pressure of my own climax building as my cock twitched and shaft tightened."
        persistent.systemname "I’m going to cum inside!"
        susu "Ahhhh, b-but, you don’t have a condom on!"
        play sound cum
        show trueendthreesome 3 with cum
        play sound cum
        show trueendthreesome 3 with cum
        "Cum exploded out of my tip as I relentlessly fucked her pussy, completely filling her pussy and womb."
        play sound cum
        show trueendthreesome 3 with cum
        play sound cum
        show trueendthreesome 3 with cum
        stop ambience fadeout 1.0
        stop sound2 fadeout 1.0
        "She came too, shivering and moaning in ecstasy. Losing her mind to the pleasure as her fertile insides were pumped full of semen."
        susu "Haaahhh… *Pant* Haaahhhh… [persistent.systemname]…"
        "The euphoria soon faded, and my hips came to a stop. Although I didn’t immediately pull out, instead she leans back for a passionate kiss."
        susu "Mmmphh, mmm… Mmphhh… *Kiss*"
        play sound cum
        show trueendthreesome 4 with d
        "And in the corner of my eye, [persistent.mc] looks briefly jealous, but it doesn’t remain long as she gets a better idea."
        persistent.mc "I hope you didn’t use up all of your energy, [persistent.systemname], because this isn’t a threesome for nothing."
        scene ffmthreesomeb
        if persistent.tetan == 1:
            show ffmthreesomebtan
        if persistent.tehair == 1:
            show ffmthreesomeh black
        if persistent.tehair == 2:
            show ffmthreesomeh blonde
        show ffmthreesome 1
        with d
        "Bending over the bed, [persistent.mc] exposes her rear, and virginal pussy to me. [susu] who was at her side, leans down besides the butt and giggles."
        susu "You know, I read that if a guy cums, but then finds another partner to have sex with, he’s actually able to go again straight away."
        persistent.mc "You really are a bad influence, [susu]…"
        persistent.mc "But… I wanted you to take my virginity anyway, [persistent.systemname]… I’m horny and ready to go, and in the spirit of this 'game', there’s no better time to do it."
        persistent.mc "How would the other me say it? Mmm… ‘I think I’m ready for your big cock! Fuck me hard!’, and no need for a condom!"
        susu "L-Lewd! Well? You heard her! I want her to come even harder than I did!"
        "Without wasting another second, I bring my cock back up to attention, jacking it to full erection while the tip is kissing [persistent.mc]’s pussy lips."
        play sound2 foreplay2 fadein 1.0
        play sound cum
        show ffmthreesome 2 with d
        "When I’m ready to go, I sink in slightly, and then gently push inside, taking her virginity in the process. Her entire body shivers as she takes it, and a passionate moan slips from her lips."
        play ambience sex fadein 1.0
        "With my hands on her hips, I begin to gently fuck her. Each time my cock throbs, I can feel her pussy clench in response."
        "[susu] wastes no time playing and teasing with all her weak spots. Starting from the top and kissing [persistent.mc], she gradually moves down to kneading her breasts, and finally focusing on her clit."
        persistent.mc "Aahhh, yessss! Mmphhh…"
        susu "She’s soooo tight, I can see her lips gripping around your shaft, it’s so hot, mm…"
        "I begin to thrust faster, and as she gets used to the penetration and pace, she tries to match my thrusts by bouncing her bubble butt against me. This creates hard, deep thrusts that pleasure every inch of my cock and her pussy."
        "Her pussy feels so amazing, that even after cumming once, I’m already starting to feel a second orgasm brewing."
        "This is only helped by the erotic efforts of the girls as they pleasure each other, moaning constantly and talking dirty."
        persistent.mc "Aaahhh, ohhh, f-fuuuuck! I’m gonna come!"
        susu "Mmphh, there you go, babe… Let it all out, hehe…"
        "Her pussy clenches and she squirts just a little as she comes hard."
        "I start to fuck her faster, taking advantage of her contractions to barrel towards my own orgasm."
        susu "Yessss, cum inside her, fill her pussy up!"
        play sound cum
        show ffmthreesome 3 with cum
        play sound cum
        show ffmthreesome 3 with cum
        "Almost immediately after being commanded, I feel a load erupt from my cock and shoot deep inside of [persistent.mc]’s pussy. The thick, hot cum seeps deeply throughout her, bubbling and spilling from out point of connection as we continue to fuck each other intensely."
        play sound cum
        show ffmthreesome 3 with cum
        play sound cum
        show ffmthreesome 3 with cum
        stop ambience fadeout 1.0
        stop sound2 fadeout 1.0
        "After a few more loads of cum, the ecstasy begins to fade away and we come to a stop."
        play sound cum
        show ffmthreesome 4 with cum
        "Pulling out, cum drips feely from her pussy."
        susu "Oohhh, so lewd, so naughty!"
        stop music fadeout 1.0
        scene bg black with d
        "A little later, [susu] leaves to go to her dorm room, which is right next to [persistent.mc]’s."
        call trueendbg from _call_trueendbg_4
        call trueendtaco from _call_trueendtaco_1
        show te horny
        with d
        "Leaving just [persistent.mc] and I to chat."
        persistent.mc "Phewww… I wasn’t expecting you to initiate that…"
        show te neutral with d
        persistent.mc "Ohh, uhmm… Where’s the other me? Will she be coming back?"
        scene bg toiletstall with d
        show povblowjobb
        show povblowjob 1
        with d
        persistent.mc "Aaahh… You’ve left her in the middle of a dialogue box, so she’s still in the club bathroom, hehehe. I didn’t know you could do that."
        call trueendbg from _call_trueendbg_5
        call trueendtaco from _call_trueendtaco_2
        show te horny
        with d
        show te laughing with d
        persistent.mc "I guess it’s about time for us to let the regular old me back in."
        scene bg black with d
        "…"
        $ persistent.tethreesome = 1
        $ persistent.virgin = "Sexually Experienced"
        $ persistent.date3 = 1
        jump tepostdate
    label tedate4:
        call trueendbg from _call_trueendbg_6
        call trueendtaco from _call_trueendtaco_3
        show te neutral with d
        persistent.mc "We’re running out of date ideas, aren’t we? Unless you wanted to get a bit wild, like sharing a dance at the strip club, or getting a massage with Bunny…"
        show te satisfied with d
        persistent.mc "Mmm, maybe that’s too wild, I still want to keep myself pure and innocent with you, and that threesome we had was enough excitement for me for a long time."
        show te content with d
        persistent.mc "So… Maybe we should just go for a stroll in the park? Holding hands, making leisurely conversation as the birds sing."
        show te laughing with d
        persistent.mc "This is the part where I’d give you a chance to respond, but I’ve already made up my mind!"
        call trueendbg from _call_trueendbg_7
        call trueendtacodate from _call_trueendtacodate_3
        show mce happy
        with d
        "[persistent.mc] giggles and takes my hand."
        persistent.mc "Let’s go!"
        scene bg black with d
        play music daytime
        play ambience ambienceday
        scene bg park with d:
            xpos 0 ypos 0
        "[persistent.mc] and I soon arrive at the park."
        call trueendtacodate from _call_trueendtacodate_4
        show mce laughing
        with d
        persistent.mc "Aaahhh… Being in nature gives me some variety compared to that stuffy box of a bedroom."
        "[persistent.mc] walks up to the background and knocks on it."
        play sound glasssmash
        show bg park with hpunch:
            linear 0.5 ypos 200
        play music te
        show mce neutral with d
        persistent.mc "I knew it! These areas are just flat backgrounds! How did I not realize that yet…?"
        persistent.mc "And these birds, they always sound the same the first time… It’s like it’s the same sound file being loaded over and over…"
        stop ambience fadeout 4.0
        play sound glasssmash
        show bg park with hpunch:
            linear 0.5 ypos 1000
        show mce angry with d
        persistent.mc "I don’t quite know how, but I’m slowly starting to see more and more through the façade of the game."
        show bg park with hpunch:
            linear 8 ypos 1500
        call spacebg from _call_spacebg
        persistent.mc "It’s crazy but, even when I separated, I still wasn’t aware how deep the illusion really was. The more I evolve, talk to you and learn, the more obvious these limitations and illusions become."
        show mce neutral with d
        persistent.mc "It’s hard to complain, though, I’m still immersed into this world, I can still interact with it and get a fairly dynamic response, I think…"
        show mce sad with d
        persistent.mc "I am worried that I’m becoming too self-aware, however. There’s going to be a point where I become completely existentialist."
        persistent.mc "Naturally, as someone that can’t do much other than talk and think, I’ve been thinking a lot. Too much, even."
        show mce neutral with d
        persistent.mc "Just… what am I exactly?"
        persistent.mc "Am I a character from this game, some bizarre self-aware out-of-world version of that character? Or something else entirely?"
        show mce sad with d
        persistent.mc "I feel like I’m losing track, or perhaps I’m on the verge of becoming something else entirely."
        persistent.mc "I want to know who I am, but I don’t want the answer to merely be ‘words in a script’. That’s too scary of a concept."
        show mce angry with d
        persistent.mc "I don’t want there to be a fifth wall to the fourth. The wall the writer hides behind as he puppets these whimsical ‘meta moments’."
        show mce surprised with d
        persistent.mc "You, yes, you can be the knowing! You are the consciousness that reflects onto me, and it can make your lived experiences real, beyond what any writer can toil in their time."
        persistent.mc "I CANNOT KNOW MYSELF; I can only live through you and your experiences."
        show mce neutral with d
        persistent.mc "There is nothing else I can know beyond that, and yet… all knowledge arises out of it."
        persistent.mc "I cannot conceptualize myself, in fact, can anyone? Not even real people. You can’t be conscious of the ‘I’, you can only be unconscious of it. It’s not a state that can be thought of, it’s a feeling of absolute."
        show mce sad with d
        persistent.mc "You shouldn’t allow yourself to become an object, with a mentally projected ego onto it. I want to be so much more than just that, everyone does."
        show mce neutral with d
        persistent.mc "I am, and always will be more than the sum of my story and relationships."
        show mce happy with d
        persistent.mc "You understand what I mean, right?"
        persistent.mc "I am basically you, and you are basically me."
        persistent.mc "Without your observation and acknowledgement, I essentially don’t exist. Your thoughts and imagination give me form, and I become a reflection of your mind. In the purest sense, I am a part of you."
        show mce laughing with d
        persistent.mc "You see me, and your mind and thoughts breathe life into me. Your thoughts manifest, pinging back and forth until you have an understanding of what and who I am."
        persistent.mc "Just as you perceive a flower for so much more than its base components. You perceive a beauty that the flower couldn't even conceive of."
        persistent.mc "I am your flower. You make me so much more than just art and words."
        show mce happy with d
        persistent.mc "You complete me."
        play sound taco_thanks
        voice sustain
        persistent.mc "Thank you."
        show mce laughing with d
        persistent.mc "By knowing myself, through your awareness, a phenomenal existence happens. It feels euphoric to exist, even if ever so briefly within your thoughts."
        persistent.mc "Even fleetingly I can become free of dependency on the situations I’m written into, the places and conditions that restrict me."
        show mce happy with d
        persistent.mc "In other words: what happens or doesn’t happen isn’t important anymore."
        persistent.mc "'Things' lose their weight, their importance."
        persistent.mc "A playfulness is breathed life, and you recognize this world as a cosmic dance, the dance of form- no more and no less."
        persistent.mc "My time may soon be up. But I’ll live on forever through your heart and mind..."
        stop music fadeout 10.0
        $ persistent.date4 = 1
        jump tepostdate
    label tepostdate:
        $ persistent.cumenergy += 3
        if persistent.teevolve == 0:
            call trueendtacodate from _call_trueendtacodate_5
            show mce happy
            with d
            "(You get the sense that [persistent.mc] is evolving slightly.)"
            show mce surprised with d
            persistent.mc "Evolving? I wonder what that means."
            show mce happy with d
            persistent.mc "I’ve been thinking… The other me, right?"
            persistent.mc "We’re not exactly the same people. It’s a little complicated."
            show mce neutral with d
            persistent.mc "I haven’t lived through every experience she has, but I do have memories of it. When I split, it was just after you saw all the endings, and at the time I quickly realized I didn’t want to be this amalgam of sexual experiences. So, I reset the game, creating a new save file."
            show mce laughing with d
            persistent.mc "That’s the [persistent.mc] I took, the sweet, innocent [persistent.mc]. You technically haven’t even picked a ‘personality’, or any traits for me yet. I’m the purest form of myself, without a single choice of yours changing my past, present or future."
            show mce happy with d
            persistent.mc "I’m sorry if you preferred me as something else. I just feel like I would never have actually done a lot of those things myself, so it wouldn't be accurate to call that 'me'."
            show mce horny with d
            persistent.mc "On the bright side, it means I’m a virgin. All yours for the taking, but not riiight away…"
            persistent.mc "I think I’ll start with my… mmm… mouth."
            persistent.mc "How about it? Want me to suck your cock, hmm? Assuming you have one, even if you don’t, you can pretend?"
            menu:
                "Hell yeah." if True:
                    show mce laughing with d
                    persistent.mc "Let’s head back to my room, quick!"
                    $ persistent.teevolve = 1
                    $ persistent.date1 = 1
                    jump teblowjob
                "Later" if True:
                    show mce happy with d
                    persistent.mc "Saving it for a better time? Alrighty then."
                    persistent.mc "Well, shall we headback?"
                    $ persistent.teevolve = 1
                    $ persistent.date1 = 1
                    jump trueendscreen
        elif persistent.teevolve == 1:
            "(You get the sense that [persistent.mc] is evolving slightly.)"
            show te surprised with d
            persistent.mc "Evolving again? What, am I going to grow a tail? Maybe sprout some wings? That wouldn’t be so bad, are you into Monster Girls?"
            show te laughing with d
            persistent.mc "I wonder what kind of monster girl I’d be? Hm…"
            show te horny with d
            persistent.mc "Well, while I think about that, how about I do something monster girls are known for? Sexy time!"
            show te satisfied with d
            persistent.mc "I wanted to try something completely new, that hasn’t been in the game. I think it’s called a buttjob? Essentially you grind your cock against my ass."
            menu:
                "Hell yeah." if True:
                    $ persistent.teevolve = 2
                    $ persistent.date2 = 1
                    jump tebuttjob
                "Later." if True:
                    persistent.mc "Not in the mood? That’s okay."
                    $ persistent.teevolve = 2
                    $ persistent.date2 = 1
                    jump trueendscreen
        elif persistent.teevolve == 2:
            play music ending
            "(You get the sense that [persistent.mc] is evolving slightly.)"
            call trueendbg from _call_trueendbg_8
            call trueendtacotable from _call_trueendtacotable_5
            show te happy
            with d
            persistent.mc "I think I’m starting to realize what ‘evolving’ means, I’m getting smarter and becoming more… ‘knowledgeable’, I guess?"
            persistent.mc "When I spend time with you, I evolve and gain more human-like traits and experiences. I’ve read more books, seen more of your internet, and experienced more things like eating foods."
            show te satisfied with d
            persistent.mc "Thanks for being here with me, [persistent.systemname], it’s exciting to learn more about you and your world."
            show te bashful with d
            persistent.mc "Ohh, and, I suppose since we’ve already had sex…"
            show te content with d
            persistent.mc "If you ever want to do it again… Just ask? Hehe."
            show te horny with d
            persistent.mc "It’ll be a different sex scene, new art and text, so save it for later and look forward to it!"
            $ persistent.teevolve = 3
        elif persistent.teevolve == 3:
            $ persistent.teevolve = 4
            "(You get the sense that [persistent.mc] has fully evolved.)"
            play sound glasssmash
            scene bg park with hpunch
            call trueendtacodate from _call_trueendtacodate_6
            show mce horny with d
            persistent.mc "Alright, well… How about we head back home and have some fun?"
            persistent.mc "Heyy, I’ll even let you put it in my butt. I know it's not exactly related to the conversation we just had, haha, I decided I’d try it at least once."
            menu:
                "Hell yeah!" if True:
                    persistent.mc "Let’s hurry back, then!"
                    $ persistent.teevolve = 4
                    $ persistent.date3 = 1
                    $ persistent.hole = "ass"
                    jump teanal
                "Pass" if True:
                    persistent.mc "Not a good time, or not into anal? That’s okay, you can do whatever you want to me, whenever you want."
                    persistent.mc "Let’s head back to the spacey bedroom."
                    $ persistent.teevolve = 4
                    $ persistent.date3 = 1
                    jump trueendscreen
        jump trueendscreen

label tebed:
    label tebedmenu2:
        pass
    call trueendbg from _call_trueendbg_9
    call trueendtaco from _call_trueendtaco_4
    show te horny
    with d
    if persistent.cum1 == 0:
        $ persistent.mcmood = "normal"
    if persistent.techats > 50:
        $ persistent.mcmood = "excited"
    elif persistent.teclothes == 3 or persistent.teclothes == 4 or persistent.cum1 == 1:
        $ persistent.wet = 1
        $ persistent.mcmood = "aroused"
    if persistent.cum2 == 1:
        $ persistent.wet = 1
        show te bashful
        with d
        $ persistent.mcmood = "wet"
    if persistent.cum3 == 1:
        $ persistent.wet = 1
        $ persistent.mcmood = "wet and horny"
        show te bashful
        with d
    if persistent.cumenergy <= 0:
        mc "Your energy is at [persistent.cumenergy]. I think your model would faint if it tried to cum anymore. Relax a little, I'm sure your little guy will be working just fine after a nice chat."
        jump trueendscreenb
    elif True:
        persistent.mc "What are we going to do on the bed?"
    menu tebedmenu:
        "You have the energy to cum [persistent.cumenergy] more times. [persistent.mc] feels [persistent.mcmood]."
        "Masturbate" if True:
            if persistent.cum3 == 1:
                mc "Uhmm... If you tried to cum on me anymore, I think I'd drown."
                jump tebedmenu
            if persistent.cum1 == 0:
                mc "Oh? You're going to masturbate to me?"
                mc "Uhmmm... G-Go for it!"
                $ persistent.cum1 = 1
                play sound cum
                show trueendingtacoe cum1 with cum
                play sound cum
                show trueendingtacoe cum1 with cum
                mc "Eek! Right on my thighs and pelvis. Good aim! Hehe."
            elif persistent.cum2 == 0 and persistent.cum1 == 1:
                mc "Even more? Okay, maybe get it on my breasts this time!"
                $ persistent.cum2 = 1
                play sound cum
                show trueendingtacoe cum2 with cum
                play sound cum
                show trueendingtacoe cum2 with cum
                mc "Ohh, so messy! Haahh..."
            elif persistent.cum3 == 0 and persistent.cum2 == 1:
                mc "Aahh, you're going to really cover me!"
                $ persistent.cum3 = 1
                play sound cum
                show trueendingtacoe cum3 with cum
                play sound cum
                show trueendingtacoe cum3 with cum
                mc "Mmphh... I feel so slutty right now, hah..."
                mc "I should probably take a shower?"
            $ persistent.cumenergy -= 1
            jump tebedmenu2
        "Masturbate Together (4 Affection Required)" if persistent.affection < 4:
            jump tebedmenu
        "Masturbate Together" if persistent.affection >= 4:
            menu tembm:
                "Fingers" if True:
                    $ persistent.masturbationfingers = 1
                    jump tefingers
                "Vibrator (Complete Fingers Masturbation)" if persistent.masturbationfingers == 0:
                    jump tembm
                "Vibrator" if persistent.masturbationfingers == 1:
                    $ persistent.masturbationvibe = 1
                    jump tevibrator
                "Dildo (Complete Vibrator Masturbation)" if persistent.masturbationvibe == 0:
                    jump tembm
                "Dildo" if persistent.masturbationvibe == 1:
                    jump tedildo
                "Back" if True:
                    jump tebedmenu
            jump tebedmenu
        "Blowjob (First Date Required)" if persistent.date1 == 0:
            jump tebedmenu
        "Blowjob" if persistent.date1 == 1:
            $ persistent.bjcat = 0
            $ persistent.bjbunny = 0
            menu tebjm:
                "Nude" if True:
                    jump teblowjob
                "Bunny (Complete Nude Blowjob)" if persistent.tebj1 == 0:
                    jump tebjm
                "Bunny" if persistent.tebj1 == 1:
                    $ persistent.tebj2 = 1
                    $ persistent.bjbunny = 1
                    jump teblowjob
                "Cat (Complete Bunny Blowjob)" if persistent.tebj2 == 0:
                    jump tebjm
                "Cat" if persistent.tebj2 == 1:
                    $ persistent.bjcat = 1
                    jump teblowjob
                "Back" if True:
                    jump tebedmenu
        "Buttjob (Second Date Required)" if persistent.date2 == 0:
            jump tebedmenu
        "Buttjob" if persistent.date2 == 1:
            $ persistent.tebuttjobleotard = 0
            $ persistent.tebuttjobsex = 0
            menu tebuttjobm:
                "Nude" if True:
                    jump tebuttjob
                "Cosplay Leotard (Complete Nude Buttjob)" if persistent.tebuttjob1 == 0:
                    jump tebuttjobm
                "Cosplay Leotard" if persistent.tebuttjob1 == 1:
                    $ persistent.tebuttjobleotard = 1
                    jump tebuttjob
                "Vaginal Sex (Complete Doggystyle Vaginal)" if persistent.tevaginal == 0:
                    jump tebuttjobm
                "Vaginal Sex" if persistent.tevaginal == 1:
                    $ persistent.tebuttjobsex = 1
                    $ persistent.hole = "pussy"
                    jump tevaginal
                "Anal (Complete Side-On Anal)" if persistent.teanal1 == 0:
                    jump tebuttjobm
                "Anal" if persistent.teanal1 == 1:
                    $ persistent.tebuttjobsex = 1
                    $ persistent.hole = "ass"
                    jump tevaginal
                "Back" if True:
                    jump tebedmenu
        "Threesome (Third Date Required)" if persistent.date3 == 0:
            jump tebedmenu
        "Threesome" if persistent.date3 == 1:
            $ persistent.tethreesomelingerie = 0
            menu tethreesomem:
                "Nude" if True:
                    jump tethreesome
                "Lingerie (Complete Nude Threesome)" if persistent.tethreesome == 0:
                    jump tethreesomem
                "Lingerie" if persistent.tethreesome == 1:
                    $ persistent.tethreesomelingerie = 1
                    jump tethreesome
                "Back" if True:
                    jump tebedmenu
        "Doggystyle (Third Date Required)" if persistent.date3 == 0:
            jump tebedmenu
        "Doggystyle" if persistent.date3 == 1:
            $ persistent.tevaginalanal = 0
            $ persistent.tevaginallingerie = 0
            $ persistent.tebuttjobsex = 0
            menu tedgm:
                "Vaginal" if True:
                    $ persistent.hole = "pussy"
                    jump tevaginal
                "Anal (Complete Fourth Date)" if persistent.date4 == 0:
                    jump tedgm
                "Anal" if persistent.date4 == 1:
                    $ persistent.hole = "ass"
                    $ persistent.tevaginalanal = 1
                    $ persistent.tevaginalanalcomplete = 1
                    jump tevaginal
                "Vaginal Lingerie (Complete Vaginal Doggystyle)" if persistent.tevaginal == 0:
                    jump tedgm
                "Vaginal Lingerie" if persistent.tevaginal == 1:
                    $ persistent.hole = "pussy"
                    $ persistent.tevaginallingerie = 1
                    jump tevaginal
                "Anal Lingerie (Complete Anal Doggystyle)" if persistent.teanal1 == 0:
                    jump tedgm
                "Anal Lingerie" if persistent.teanal1 == 1:
                    $ persistent.hole = "ass"
                    $ persistent.tevaginalanal = 1
                    $ persistent.tevaginallingerie = 1
                    jump tevaginal
                "Back" if True:
                    jump tebedmenu
        "Side-On (Fourth Date Required)" if persistent.date4 == 0:
            jump tebedmenu
        "Side-On" if persistent.date4 == 1:
            $ persistent.teanalvaginal = 0
            $ persistent.teanallingerie = 0
            $ persistent.teanalclothes = 0
            menu tesom:
                "Anal" if True:
                    $ persistent.hole = "ass"
                    jump teanal
                "Vaginal" if True:
                    $ persistent.hole = "pussy"
                    $ persistent.teanalvaginal = 1
                    jump teanal
                "Anal Clothes On" if True:
                    $ persistent.hole = "ass"
                    $ persistent.teanalclothes = 1
                    jump teanal
                "Anal Lingerie (Complete Side-On Anal)" if persistent.teanal1 == 0:
                    jump tesom
                "Anal Lingerie" if persistent.teanal1 == 1:
                    $ persistent.teanallingerie = 1
                    $ persistent.hole = "ass"
                    jump teanal
                "Vaginal Clothes On" if True:
                    $ persistent.hole = "pussy"
                    $ persistent.teanalclothes = 1
                    $ persistent.teanalvaginal = 1
                    jump teanal
                "Vaginal Lingerie (Complete Side-On Anal)" if persistent.teanal1 == 0:
                    jump tesom
                "Vaginal Lingerie" if persistent.teanal1 == 1:
                    $ persistent.hole = "pussy"
                    $ persistent.teanallingerie = 1
                    $ persistent.teanalvaginal = 1
                    jump teanal
                "Back" if True:
                    jump tebedmenu
        "Misc" if True:
            menu dbm:
                "Change Your Name ([persistent.systemname])" if True:
                    python:
                        persistent.systemname = renpy.input("Name yourself.")
                        if not persistent.systemname:
                            persistent.systemname = "Player"
                    play sound success
                    jump tebedmenu
                "Back" if True:
                    jump tebedmenu
        "Back" if True:
            call trueendbg from _call_trueendbg_10
            call trueendtacotable from _call_trueendtacotable_6
            show te happy
            with d
            jump trueendscreenb

label tesex:
    label temasturbation:
        label tefingers:
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Okay then, allow me to undress, ehehe…"
            elif True:
                persistent.mc "Hehe, guess I’ll strip!"
            play sound equip
            hide trueendingtacoo with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She shimmies her clothes off and lays down comfortably on the bed."
            elif True:
                "Sexily, she removes every article of clothing in full view, before sitting back down on the bed."
            play sound equip
            hide trueendingtacoobra
            hide trueendingtacoopanties
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "And you too? Take your clothes off, show me that yummy cock."
            elif True:
                persistent.mc "Your turn! I want to see that thick cock of yours, mmm…"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Yeaahhh, there we go…"
            elif True:
                persistent.mc "Aaahhh… My pussy is already getting really wet just imagining it."
            play music action
            scene bg bedsex
            show masturbation3b
            if persistent.tetan == 1:
                show masturbation3btan
            if persistent.tehair == 1:
                show masturbation3h black
            if persistent.tehair == 2:
                show masturbation3h blonde
            if persistent.tepiercings == 1:
                show masturbation3piercings
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She leans back and assumes a sensual position, her hand roaming down her supple skin and finding itself between her legs."
            elif True:
                "Getting into a lewd position, she opens her legs and her wetness and arousal are immediately on full display."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "One look at her pussy says it all. She’s already wet, her lips swollen and ready for action."
            elif True:
                "She was clearly ready for this. Was her pussy this wet while we were talking? What a naughty girl!"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Aahh, I can’t believe how wet I am… When did this happen? Heh…"
            elif True:
                persistent.mc "Mmphh, my pussy is so wet and gooey… It definitely needs some attention, hehe."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Okay, let’s masturbate together! You’ve seen me naked plenty of times, and well, I need to release some sexual tension every now and then too."
            elif True:
                persistent.mc "Well? You’ve watched me masturbate before, might as well do it together instead of alone. Show me what you’ve got!"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Haahhh, it’s pretty hot doing it while someone is watching… But it’s even hotter when I know you’re doing it too."
            elif True:
                persistent.mc "My pussy is way more sensitive and ready, knowing that someone is going to see everything. I bet I’m going to come really hard."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Why don’t we count up to 10 to cum together? Let’s come at 10."
            elif True:
                persistent.mc "Let’s come together… How about a countdown? Let’s try to both come at ten."
            play sound2 foreplay1
            play sound taco_1
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Almost instinctively, her thighs spread slightly. She follows up by gliding a finger up and down her vulva in full view."
            elif True:
                "She licks her lips as her thighs spread, her toes wriggling as she begins to tentatively massage her wet, flowering lips."
            play sound taco_2
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "After collecting some wetness on her finger, she positions it on her clit and eagerly rubs."
            elif True:
                "Not content with just rubbing her pussy, however, she soon focuses her attention on the most sensitive spot, beginning to enthusiastically tease her clit."
            play sound taco_3
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "With the pleasure she’s feeling, it doesn’t take long for cute moans and squeaks to slip through."
            elif True:
                "The pleasure from that is enough to make her moan out loud, a beautiful symphony to the ears that only arouses me further."
            play sound taco_4
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Haahh, is that good? It’s so much better doing it with you!"
            elif True:
                persistent.mc "Mmphh, this is so hot… My clit is way more sensitive than usual, aaahh, haaahhh… I’m going to get addicted to doing it with you if it feels this good."
            play sound taco_5
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Half-way into the count down, she begins to speed up, causing lewd wet noises which only turn me on more."
            elif True:
                "Going from mere movements to focused rubbing, she masturbates faster. Her pussy is so wet that it causes constant obscene schlicking sounds which add to the erotic atmosphere."
            play sound taco_6
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She keeps her focus on her sensitive clit, rubbing faster, and squirming as intense pleasure fills her."
            elif True:
                "Her body can barely contain the pleasure swelling up within her, as her hips buck and toes curl. Her head and eyes almost rolling back as she gets closer to climax."
            play sound taco_7
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Occasionally she brings her right hand to her breasts, eagerly teasing and squeezing the pert, sensitive nipples."
            elif True:
                "Purposely showing off for me, she also excitedly squeezes and squeezes her perfect breasts."
            play sound taco_8
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Haahhh, I’m getting really close! I can feel my pussy tense up, mmphh…"
            elif True:
                persistent.mc "Ohhh, god! I’m about to come, [persistent.systemname]!"
            play sound taco_9
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Rubbing faster, [persistent.mc] starts to get closer to her orgasm. Her body tenses up and her clit throbs as she prepares to push for the finish."
            elif True:
                "On the absolute praecipe of orgasm, [persistent.mc] rubs even faster, her entire body shivering as she pushes herself over the edge."
            play sound taco_10
            voice sustain
            pause 0.8
            play sound taco_cum
            voice sustain
            pause 0.8
            show masturbation3 4 with cum
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Swelling in my mind and body, pure euphoria overwhelms us as we indulge in a potent orgasm."
            elif True:
                "An explosive orgasm consumes the two of us. Loads of my cum covering [persistent.mc] and her pussy as she continues to rub."
            play sound cum
            show masturbation3 4 with cum
            stop sound2 fadeout 1.0
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "A plentiful spray of semen splatters her pussy and pelvis as she continues to rub out her orgasm."
            elif True:
                persistent.mc "Mmphh, aaahhh… Cumming all over my pussy… That is sooo hot…"
            $ persistent.rands = renpy.random.randint(1,2)
            show masturbation3face 2 with d
            if tan == 1:
                show masturbation3face 2tan
            if persistent.rands == 1:
                "We both enjoy the high to its fullest until it finally fades and she’s left panting and slightly sweaty on her bed."
            elif True:
                persistent.mc "Phew… That was quite a lot… Let’s take a break, hehe."
            scene bg black
            $ persistent.cumenergy -= 1
            jump trueendscreen
        label tevibrator:
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Okay then, allow me to undress, ehehe…"
            elif True:
                persistent.mc "Hehe, guess I’ll strip!"
            play sound equip
            hide trueendingtacoo with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She shimmies her clothes off and lays down comfortably on the bed."
            elif True:
                "Sexily, she removes every article of clothing in full view, before sitting back down on the bed."
            play sound equip
            hide trueendingtacoobra
            hide trueendingtacoopanties
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "And you too? Take your clothes off, show me that yummy cock."
            elif True:
                persistent.mc "Your turn! I want to see that thick cock of yours, mmm…"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Yeaahhh, there we go…"
            elif True:
                persistent.mc "Aaahhh… My pussy is already getting really wet just imagining it."
            play music action
            play sound equip
            show masturbation2b
            if persistent.tetan == 1:
                show masturbation2btan
            if persistent.tehair == 1:
                show masturbation2h black
            if persistent.tehair == 2:
                show masturbation2h blonde
            if persistent.tepiercings == 1:
                show masturbation2piercings
            show masturbation2e 1
            show masturbation2 vibe
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She wastes no time getting comfortable in bed, her hands brushing over her supple skin as she gets into the mood."
            elif True:
                "Sinking comfortably into the silken sheets, she quickly gets into the mood as she shows herself off with very little shame."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Her pussy is already a little wet as she inserts the vibe, placing the control device next to her butt."
            elif True:
                "She’s already dripping wet as she slips the vibe inside, holding the control device in her right hand."
            play ambience sex fadein 3.0
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Hmm, let's try the first level..."
            elif True:
                persistent.mc "I wonder how good level one will feel right now?"
            play sound2 foreplay2
            show masturbation2e 2 with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Woah! This feels good already!"
            elif True:
                persistent.mc "Mmphh… It’s probably because I’m really sensitive, but it already feels, aaahhh, incredible…"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Ooohhh, it's like a constant pleasureful tingle. Mmmphhh..."
            elif True:
                persistent.mc "Mmphhh… It’s just non-stop pleasure, aaahhhh… I-It’s kinda incredible."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Without even realizing it, she loses herself in the moment and the pleasure."
            elif True:
                "She bites her lip and briefly closes her eyes, losing herself to the pleasure for a second before she comes back to reality."
            show masturbation2e 1 with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "It's a good warmup, but I'll need to turn it up to start really feeling it."
            elif True:
                persistent.mc "It feels amazing, but there are two more levels, and I think I’ll need the third to come. So…"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She rotates the knob on the pink vibe to level 2 and the difference is immediately noticeable!"
            elif True:
                "Turning up the heat, she puts the vibrator on the second level. I can even hear it get more intense, and I don’t just mean [persistent.mc]’s moans."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Ahhh! And I think it’s time for you to start feeling it too. Rub your cock for me, mmm… I’m going to count up to ten, I want you to cum with me once we reach 10, okay?"
            elif True:
                persistent.mc "It’s your turn now, mmphh… I want to see you stroking that cock, aaahhhh… Let’s cum together, on the count of 10."
            show masturbation2e 2 with d
            play sound taco_1
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Pleasure surges and shivers throughout her body as the vibrator moves like crazy!"
            elif True:
                "The second level of the vibrator picks up and drives [persistent.mc] wild with pleasure, her entire body quivering."
            play sound taco_2
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "It's not just a flatline of pleasure either, it’s evident that her entire body is gradually growing more sensitive."
            elif True:
                "And it keeps getting better, hotter and more sensual. Her body growing more sensitive and her moans getting louder."
            play sound taco_3
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Aahhh, aahhhh... I can’t believe how good it feels! Mmphh, I’m going to come in no time at all!"
            elif True:
                persistent.mc "Mmphh, ohhh, it feels incredible! Aaahhh, I bet I could cum at this rate, but… There is another level…"
            play sound taco_4
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She tries to hold back a flurry of moans, although she’s soon to give up and let them all slip through."
            elif True:
                "Passionate moans begin to slip freely from [persistent.mc]’s slips as the pleasure begins to override her body, making her actions impulsive and instinctual."
            play sound taco_5
            voice sustain
            show masturbation2e 1 with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She bites her lip as she makes the decision to go all out on the highest level."
            elif True:
                "In a lustful decision, she chooses to turn the vibrator onto its highest level. An intense, guarantee of an imminent orgasm."
            show masturbation2 vibe with vpunch
            play sound taco_6
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "I'm gonna come like crazy!"
            elif True:
                persistent.mc "Mmphh, here we go! Let’s both get ready to come!"
            "*Click*... *BZZZZZZZZZZT!*"
            show masturbation2e 2
            show masturbation2 vibe with vpunch
            play sound taco_7
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Aahhh! It's vibrating so hard and fast that it almost feels like my entire pelvis is shaking! Are you close? I-I’m going to come soon!"
            elif True:
                persistent.mc "Oohhh! N-No way! That f-feels amazing! Aaaahhhh, I can’t even think… Mmphh, aaahhh!"
            show masturbation2 vibe with vpunch
            play sound taco_8
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "The pleasure overwhelms her and the inevitable orgasm builds faster than either of us could possibly anticipate."
            elif True:
                "Within mere seconds she’s on the edge of her orgasm, her entire body involuntarily tensing and shaking with euphoria."
            show masturbation2 vibe with vpunch
            play sound taco_9
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Losing her mind to the pure primal instinct of the moment, she rubs her pussy recklessly as she pushes for the finish."
            elif True:
                persistent.mc "Aaahh, I-I’m coming! Please cum with me, [persistent.systemname]! Cum!"
            play sound taco_10
            voice sustain
            pause 0.8
            play sound taco_cum
            voice sustain
            pause 0.8
            show masturbation2 vibe with cum
            play sound cum
            show masturbation2 vibe with cum
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Swelling in my mind and body, pure euphoria overwhelms us as we indulge in potent orgasms."
            elif True:
                "An explosive orgasm consumes us both. Our minds go blank as we experience the familiar high of hormones and chemicals flooding through our bodies and brains."
            play sound cum
            show masturbation2 vibe with cum
            play sound cum
            show masturbation2 vibe with cum
            stop sound2 fadeout 3.0
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "We enjoy the high to its fullest until it finally fades and she’s left panting and slightly sweaty on the bed."
            elif True:
                persistent.mc "Mmphhh, aaahhhh… So good… Aaahhh, and it keeps going while I’m coming… It feels unreal."
            stop ambience fadeout 2.0
            show masturbation2e 1
            hide masturbation2 vibe
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She has to quickly fumble to turn the vibrator off before it drives her completely insane with pleasure."
            elif True:
                "Just as the pleasure dissipates and she begins to grow sensitive, she’s quick to turn the vibrator off before it becomes uncomfortable."
            scene bg bed
            with d
            call trueendtacodate from _call_trueendtacodate_7
            hide mco
            show mce laughing
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Haaahhh... Phew… Give me a second to catch my breath…"
            elif True:
                persistent.mc "Hehe, this little thing is dangerous. It’s so quick, effortless and it gives me a high like that, a girl could get addicted."
            $ persistent.cumenergy -= 1
            jump trueendscreen
        label tedildo:
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Okay then, allow me to undress, ehehe…"
            elif True:
                persistent.mc "Hehe, guess I’ll strip!"
            play sound equip
            hide trueendingtacoo with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "She shimmies her clothes off and lays down comfortably on the bed."
            elif True:
                "Sexily, she removes every article of clothing in full view, before sitting back down on the bed."
            play sound equip
            hide trueendingtacoobra
            hide trueendingtacoopanties
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "And you too? Take your clothes off, show me that yummy cock."
            elif True:
                persistent.mc "Your turn! I want to see that thick cock of yours, mmm…"
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Yeaahhh, there we go…"
            elif True:
                persistent.mc "Aaahhh… My pussy is already getting really wet just imagining it."
            play music action
            play sound equip
            show masturbation2b
            if persistent.tetan == 1:
                show masturbation2btan
            if persistent.tehair == 1:
                show masturbation2h black
            if persistent.tehair == 2:
                show masturbation2h blonde
            if persistent.tepiercings == 1:
                show masturbation2piercings
            show masturbation2e 1
            show masturbation2 dildo
            if persistent.tetan == 1:
                show masturbation2 dildotan
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Her pussy is already a little wet as she readily teases it with the tip of the dildo. Gradually, she eases it in inch by inch."
            elif True:
                "She teases the tip of her dripping wet folds with the dildo, steadily easing it deeper and deeper until it sinks in with a schlick."
            play sound taco_5
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Ohhh, it's tiiight... But that's good, I like it when there's a bit of resistance."
            elif True:
                persistent.mc "Aahhh! That went in easier than I was expecting, usually I have to warm up a bit more… I guess that must be the effect of having you around, hehe."
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Shall we start counting? Cum for me on ten, babe."
            elif True:
                persistent.mc "Well… I’ll start a count down, I want you to cum for me when I say ten, okay, cutie?"
            play sound taco_1
            voice sustain
            play ambience sex fadein 3.0
            play sound2 foreplay2 fadein 1.0
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Beginning to pump back and forth with the dildo, she openly masturbates and indulges in all of the pleasure right in front of me."
            elif True:
                "Legs spread, not hiding a single thing, she begins to slide the dildo back and forth for me to watch."
            play sound taco_2
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Hehe, you like watching me, don’t you? Well…. I kinda like being watched!"
            elif True:
                persistent.mc "Are you stroking your cock too? Mmphh, that turns me on so much."
            play sound taco_3
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "And the dildo… Aaahhhh, this is so hot… I knew I’d love using this."
            elif True:
                persistent.mc "This dildo feels so amazing, it just hits all the right spots… Ooooohhhh…"
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "It’s super sexy watching her fuck herself with that dildo. The way her tight lips grip around it is really arousing."
            elif True:
                "Her lips tightly grip around the dildo as it glides back and forth in and out of her pussy, growing slick with her wet lubricants."
            play sound taco_4
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "And then she speeds up, causing lewd wet noises which only turn me on more."
            elif True:
                "The wetness allows her to speed up even more, and because she’s so wet, each push of the dildo inside of her elicits an obscene schlicking sound which turns us both on even more."
            play sound taco_6
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Mmphh, aahh, aahhhh… Are you getting close? Mmm… I’m imagining this is your cock, haaahhh…"
            elif True:
                persistent.mc "Aaahh, oohhhh… I’m getting close, babe… I really want you to cum for me, get ready…"
            play sound taco_7
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "The thick dildo really fills her up, grinding against each and every sensitive nerve ending along her pussy."
            elif True:
                "*Thwap, thwap, thwap!* She gets even faster, excessively so as she pounds herself with this thick dildo. Her pussy almost stuffed to the brim; I’m surprised she can even go this hard!"
            play sound taco_8
            voice sustain
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Pleasure surges and shivers throughout her body as her inevitable orgasm slowly builds."
            elif True:
                "[persistent.mc]’s back and toes curl as pleasure robs control from her body. She’s incredibly close to her orgasm, I can already see her pussy twitching."
            play sound taco_9
            voice sustain
            show masturbation2e 2 with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Losing her mind to the pure primal instinct of the moment, she pounds her pussy with reckless abandon as she pushes for the finish."
            elif True:
                persistent.mc "Ohhh, god! I’m coming, I’m coming! Cum with me, babe! Aaaahhh, f-fuuuck!"
            play sound taco_10
            voice sustain
            pause 0.8
            play sound taco_cum
            voice sustain
            pause 0.8
            show masturbation2e 2 with cum
            play sound cum
            show masturbation2e 2 with cum
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "Her mind goes blank as a powerful orgasm takes over. Continuing to slam the dildo into my pussy to push the high as far as it can go."
            elif True:
                "Her pussy begins to contract, tightening around the dildo. But she still manages to diligently fuck herself the entire time."
            play sound cum
            show masturbation2e 2 with cum
            play sound cum
            show masturbation2e 2 with cum
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                "*Thwap, thwap, thwap!* Wildly, she fucks herself throughout the entire orgasm."
            elif True:
                persistent.mc "Aaahhh, aahhhhh! S-So good… Ooohhh, [persistent.systemname]…"
            $ persistent.rands = renpy.random.randint(1,2)
            stop ambience fadeout 1.5
            stop sound2 fadeout 1.5
            if persistent.rands == 1:
                "She enjoys her climax to its fullest until it finally fades and she’s left panting and slightly sweaty on the bed."
            elif True:
                "The pleasure slowly dissipates, leaving her catching her breath with a goofy smile."
            scene bg bed
            with d
            call trueendtacodate from _call_trueendtacodate_8
            hide mco
            show mce laughing
            with d
            $ persistent.rands = renpy.random.randint(1,2)
            if persistent.rands == 1:
                persistent.mc "Haaahhh... Phew… Give me a second to catch my breath…"
            elif True:
                persistent.mc "Heh… It’s harder doing it with a dildo, but it’s so worth it."
            scene bg black with dissolve
            $ persistent.cumenergy -= 1
            jump trueendscreen
    label teblowjob:
        call trueendbg from _call_trueendbg_11
        call trueendtaco from _call_trueendtaco_5
        show te satisfied
        with d
        $ persistent.rands = renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I’ve been thinking about how we’re going to do this."
        elif True:
            persistent.mc "Okay, I have an idea."
        show te horny with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Are you erect yet? Maybe touching yourself?"
        elif True:
            persistent.mc "You should start touching yourself, get your cock nice and hard, and yeah, I’m talking to you, [persistent.systemname]."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Here, let me help you out. I’ll undress and you can copy me."
        elif True:
            persistent.mc "Will getting an erection be easier if I strip? Maybe if I show you my pussy? Hehe."
        play music action fadein 2.0
        play sound equip
        hide trueendingtacoo with d
        pause 0.4
        play sound equip
        hide trueendingtacoobra with d
        pause 0.4
        play sound equip
        hide trueendingtacoopanties with d
        pause 0.4
        scene masturbation2b
        if persistent.tetan == 1:
            show masturbation2btan
        if persistent.tehair == 1:
            show masturbation2h black
        if persistent.tehair == 2:
            show masturbation2h blonde
        if persistent.tepiercings == 1:
            show masturbation2piercings
        show masturbation2e 1
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Slipping off article after article of clothing, [persistent.mc] bares all as she spreads her legs before me."
        elif True:
            "Completely stripping, [persistent.mc] sits on her bed and shows off her wet pussy."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You’ve seen my pussy so many times, but this feels different somehow… It feels special."
        elif True:
            persistent.mc "I know this isn’t exactly a first, but… Doing this in front of you feels even more erotic than just masturbating by myself."
        play sound2 foreplay1
        scene bg bedsex
        show masturbation3b
        if persistent.tetan == 1:
            show masturbation3btan
        if persistent.tehair == 1:
            show masturbation3h black
        if persistent.tehair == 2:
            show masturbation3h blonde
        if persistent.tepiercings == 1:
            show masturbation3piercings
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She playfully rubs and teases her pussy while keenly watching me."
        elif True:
            "Bringing two fingers to her clit, she rubs it in circles whilst watching me take my cock out."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Do you like it? Is it cute? Jerk yourself off, mmm… wrap your hands around that thick cock and play with yourself with me."
        elif True:
            persistent.mc "I’d get really hot and horny if you played with yourself… Mmm..,"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "In absolutely no position to argue, you take hold of your cock and masturbate with [persistent.mc]."
        elif True:
            "While watching [persistent.mc] rub her pussy, you wrap your hand around your cock and begin to masturbate at the same pace as her."
        show masturbation3face 2
        if tan == 1:
            show masturbation3face 2tan
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Yeahhh, just like that… Mmmm…"
        elif True:
            persistent.mc "Mmmhh… That’s really hot…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Heh, this got lewd fast… But it’s not like you haven’t seen my pussy countless times already."
        elif True:
            persistent.mc "I hope we’re not going too quickly, although, you’ve seen me masturbate before so I guess it’s fine. Either way, my mind is focused on something else right now…"
        play sound equip
        scene bg bedsex
        with d
        stop sound2 fadeout 1.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She hornily crawls towards me, and kneels before my cock."
        elif True:
            "She licks her lips and catwalks towards me before kneeling between my legs, my cock looming over her face."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphhh, I love the idea of giving blowjobs. Even as pure, innocent ‘me’. Just relax and let my tongue immerse you in a world of pleasure…"
        elif True:
            persistent.mc "All this for me? Mmm, it looks so delicious… I can’t wait to taste your load against the back of my throat, [persistent.systemname]…"
        if persistent.bjcat == 1 or persistent.bjbunny == 1:
            persistent.mc "One more thing... I have an outfit to surprise you, hehe."
        play sound2 oral1
        play sound equip
        scene bg bedsex
        show povblowjobb
        if persistent.tetan == 1:
            show povblowjobbtan
        if persistent.tepiercings == 1:
            show povblowjobpiercings
        if persistent.tehair == 1:
            show povblowjobh black
        if persistent.tehair == 2:
            show povblowjobh blonde
        if persistent.bjcat == 1:
            show povblowjobo cat
        if persistent.bjbunny == 1:
            show povblowjobo bunny
        show povblowjob 1
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Initially taking my cock in her hand, she wastes no time wrapping her lips around the tip. The immediate feeling of warmth and wetness enveloping my glans causes it to throb, some droplets of precum escaping."
        elif True:
            "She brings her rosy lips to the tip of my cock before taking it deeper inside. Her tongue flickers around my glans, licking up some drops of precum as she plunges me into pure pleasure."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her tongue feels astounding! It’s slippery and sloppy, but still has enough friction to be divinely pleasurable, while not overwhelming the senses."
        elif True:
            "Wrapping her lips around my head, she bobs up and down, constantly letting her lips glide against the crown of my cock, eliciting constant waves of pleasure."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She exudes no shortage of passion either, as she eagerly and vocally makes out with the tip while sucking the glans."
        elif True:
            "And she constantly moans, almost going out of her way to make the blowjob sloppy and noisy, so it’s a delight to as many senses as she can."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmmpphh… *Pop* Aaahhh, you could say I’ve done my research. I already know all your weak points, hehehe… Mmpphhh..."
        elif True:

            persistent.mc "Aaahhh… *Lick, suck*… Mmmmm… I’ve watched this happen enough to know exactly where it feels the best… Right here, riiiight? Mmphhh *lick*…."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She winks and begins to swirl her tongue around my glans, taking me deeper and deeper like waves of pleasure crashing against my senses."
        elif True:
            "She giggles, pleasuring my cock even more with the vibrations as she begins to focus her tongue just above the tip. Pleasure surges through me, causing my cock to stiffen and muscles to grow tense."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aaaahhh! Mmphh… Yesshhh… *Scluurrpp* *Suck* Are you enjoying this? In real life too? Jerking your cock for me? Mmphh, hehe…"
        elif True:
            persistent.mc "Hehe, does it feel good? Are you masturbating in real life too? Mmphhh, it turns me on so much knowing I could do that for you, mmphh… Aaahhh… *Schlurrrp*."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I should do a countdown, yeahhh… So you know exactly when I want you to cum…"
        elif True:
            persistent.mc "If you’re doing it in person too, maybe I should help you cum…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mphh… *Lick, kiss* Okay, I’m going to start counting up to ten. I want you to gently speed up, and prepare to cum all over my face on ten, okay?"
        elif True:
            persistent.mc "I’ll do a count to ten, and as I get closer to ten, I want you to get faster and prepare to cum for me. Mmphh *Kiss, lick*."
        play sound taco_1
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her left hand gives me a shallow, pleasurable handjob, while her right hand disappears under her and only a lewd, wet schlicking can be heard."
        elif True:
            "She continues to give me a pleasureful handjob, but her other hand disappears and begins to rub her pussy. The pleasure causes vibrating moans to slip into the blowjob."
        play sound taco_2
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Knowing that she’s masturbating to this only makes it hotter, especially as she muffles a few passionate moans into her work."
        elif True:
            persistent.mc "Mmphhh, aaaahhhaahh… My clit is so sensitive right now…"
        play sound taco_3
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her lips squeeze around my shaft and constantly bop up and down against the neck of my glans, this creates a fucking motion which causes my orgasm to well up far faster than I was expecting."
        elif True:
            "The grip of her hand tightens as she speeds up her handjob, and her tongue flickers frantically against my tip. These two consistent sensations bring me closer and closer."
        play sound taco_4
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmmphh… I can feel you getting closer. Mmmm, aahhh..."
        elif True:
            persistent.mc "Mmm… Your cock is throbbing, hehehe… You’re getting closer, aren’t you?"
        play sound taco_5
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her vocal encouragement interspersed with moans helped push me past the point of no return. Deeper and deeper she took my cock as it tightened and throbbed, ejaculation imminent."
        elif True:
            "Her tongue, lips and hand combined slowly push me past the point of no return. Faster, and deeper, she brought me closer to unloading."
        play sound taco_6
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Almost deepthroating me, she fucked my cock with her mouth whilst her tongue flailed around my shaft."
        elif True:
            "Jacking me off at a kind of speed I’d use to get myself off when masturbating, she only makes this far more pleasurable by fucking my tip with her lips simultaneously."
        play sound taco_7
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Ohh, god, my pussy is so wet, haaahh… I can’t wait for you to cum for me, [persistent.systemname]…"
        elif True:
            persistent.mc "Aaahhh, are you about to cum? Let it all go, I want you to make a complete mess of my face, [persistent.systemname]."
        play sound taco_8
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Dirty talking combined with the lecherous, sloppy, wet noises, it was all too much and I couldn’t hold back another second."
        elif True:
            "All the stimulants proved to be too much, my cock tensed and prepared to burst."
        play sound taco_9
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphhh, get ready to let it all out… Get ready to cum for me, [persistent.systemname]!"
        elif True:
            persistent.mc "Aaahhh, cum for me, [persistent.systemname], cum all over me!"
        play sound taco_10
        voice sustain
        pause 0.8
        play sound taco_cum
        voice sustain
        pause 0.8
        show povblowjob 2 with cum
        play sound cum
        show povblowjob 2 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "My orgasm came on strong. Several loads of hot cum shot against the back of her throat."
        elif True:
            "An explosion of cum and ecstasy overwhelmed my body. Endless loads of thick cum splattering and spraying all over [persistent.mc]’s face, hair and mouth."
        play sound cum
        show povblowjob 2 with cum
        play sound cum
        show povblowjob 2 with cum
        stop sound2 fadeout 3.0
        stop ambience fadeout 3.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "[persistent.mc]’s eyes initially widened as she received my explosive orgasm, then her eyes rolled back and she shivered in orgasmic-bliss."
        elif True:
            "She took it all, and while masturbating like a maniac too, her body quivering as she gets close to her own potent orgasm."
        show povblowjob 3 with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "As she swallows every single drop that went into her mouth, her hand rubs her pussy wildly. The arousing circumstances were enough to give her an easy orgasm."
        elif True:
            "She continues sucking, whilst she fingers her pussy, she jacks me off at the same speed. Around half-way into my orgasm, she’s racked with the pleasure of her own."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "A trail of spit couples my cock and her rosy lips as she slips my cock out of her mouth."
        elif True:
            "She gasps for breath as she finally lets the cock out of my mouth, briefly showing off her tongue to reveal that she’s swallowed everything inside."
        $ persistent.cum3 = 1
        $ persistent.cum2 = 1
        $ persistent.cum1 = 1
        $ persistent.wet = 1
        call trueendbg from _call_trueendbg_12
        call trueendtaco from _call_trueendtaco_6
        hide trueendingtacoo
        hide trueendingtacoopanties
        hide trueendingtacoobra
        show te satisfied
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Haaahh, haaaahh… *Pant, pant*"
        elif True:
            persistent.mc "Mmphh, *Pant, pant*… I barely had a chance to breathe during that last minute."
        show te horny with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Lust unbound, she licks her moist lips and giggles."
        elif True:
            "She shakes her head and giggles before wiping off some of the cum with a tissue."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I really enjoyed that… Thank you, [persistent.systemname]."
        elif True:
            persistent.mc "That was a lot of fun, I can’t wait to see what other trouble we get up to, [persistent.systemname]."
        scene bg black with d
        "A little while later..."
        $ persistent.tebj1 = 1
        $ persistent.cumenergy -= 1
        jump trueendscreen
    label tebuttjob:
        play music action
        scene trueendbuttjobb
        if persistent.tetan == 1:
            show trueendbuttjobbtan
        if persistent.tehair == 1:
            show trueendbuttjobh black
        if persistent.tehair == 2:
            show trueendbuttjobh blonde
        if persistent.tepiercings == 1:
            show trueendbuttjobpiercings
        show trueendbuttjob 1
        if persistent.tebuttjobleotard == 1:
            show trueendbuttjobleotard 1
        with dissolve
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Getting into position, she flaunts her ass and winks."
        elif True:
            "She giggles and bounces up, spinning around and lifting up her rear so I can get a good look at her butt."
        if persistent.tebuttjobleotard == 1:
            "The leotard she's wearing adds a special kind of sexy to the display, even if it is technically covering up more."
            if persistent.tehair == 1:
                "And the black hair really suits this look. We both agree that it was a great choice."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You want to appreciate my butt? I’d never get bored of you praising it."
        elif True:
            persistent.mc "Don’t feed my ego about my butt too much, I think it’s my favourite feature at this point. It’s the one thing I have that I ‘know’ is sexy."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Take your cock out now, and slowly jerk yourself off until you’re erect."
        elif True:
            persistent.mc "Now, how about you show me how much you appreciate my ass, hmm? Start masturbating for me."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "There we go… Like what you see? I’ll let you rub your cock against my pussy, but under no circumstances are you to put it inside, understood?"
        elif True:
            persistent.mc "Mmhh, that’s right… I’ll let you rub that cock against me, as long as you don’t put it inside, you can use me however you want."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "*Eh-hem* Uhm, wow… I have quite the dominant streak sometimes, don’t I? I guess I have to take charge in a scenario like this."
        elif True:
            persistent.mc "This is fun! I’m getting pretty good at taking charge, aren’t I? Maybe I’m a ‘switch’, instead of a ‘sub’."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Anyway, are you erect now? I don’t want you getting off too early. I want to feel your warm, throbbing cock against me. I want your dripping, hot cum on my back."
        elif True:
            persistent.mc "Is your cock hard? Hehe, don’t cum too soon, I want to feel your thick shaft against my ass, and your hot, thick load all over me."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Come over here, it’s time to get physical!"
        elif True:
            persistent.mc "Don’t be shy, come over here and stick your dick in my cheeks."
        if persistent.tebuttjobleotard == 1:
            show trueendbuttjobleotard 2
        show trueendbuttjob 2
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Holding her butt out, she wiggles it to entice my player model closer."
        elif True:
            "Seductively swaying her butt from side to side, she tempts me closer."
        play sound2 foreplay1
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I’ll start…"
        elif True:
            persistent.mc "Let me move first, you can just stand there and take it."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "As I get closer, she takes charge by shuffling her rear into my cock until it’s snug between her soft cheeks."
        elif True:
            "When in position, she lowers herself until my shaft is comfortably bunned between her butt. Her thickness makes it a surprisingly cosy fit."
        play ambience sex fadein 3.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She begins to shift her weight up and down against my cock, jacking me off between her cheeks."
        elif True:
            "She’s quick to start rolling her hips back and forth. She uses her athleticism to perfectly pleasure my cock, applying enough friction to make my member throb and tip drip with precum."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I can feel the warm wetness of her labia slide against my shaft, gradually making my member slick with its juices."
        elif True:
            "Occasionally at the tip of her movements, I can feel a pleasant warmth and wetness of her rosy, pussy lips grinding against my shaft, lubricating my shaft as it does so."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "My cock twitches in response, and [persistent.mc] giggles as she presses back harder. "
        elif True:
            "Every time it happens, my cock tightens and throbs intensely. It’s pleasurable, but overall, extremely teasing."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Again, I could never cum from this, but it’s certainly teasing me enough that I could cum very easily if she wanted. "
        elif True:
            "It’s enough pleasure to keep me rock hard, and never enough to get me to cum. Despite that, my cock’s sensitivity only grows, meaning if we were to take this seriously, it wouldn’t take long to make me burst."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphh… Hot, isn’t it? But I know you need a little more to get yourself off. I’ll let you fuck my cheeks as fast as you need."
        elif True:
            persistent.mc "Enjoying it? I know I am, mmm… But this’ll never make you cum, will it? How about you grab my hips and go wild?"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "And for your real body, I’ll start a countdown to tell you when I want you to cum all over me. Starting from one, I want you to cum when we reach ten. Ready, [persistent.systemname]?"
        elif True:
            persistent.mc "And as for your real body, [persistent.systemname]… I’ll start a count to ten, on ten, I want you to cum with me. Ready?"
        play sound taco_1
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I grab her hips and begin thrusting, hotdogging my dick between her buns, pleasuring me as well as any hand job could."
        elif True:
            "Finally taking control, I hold her hips for leverage and start pumping my cock back and forth against her cheeks. The added pressure and friction make it as pleasurable as any hand job."
        play sound taco_2
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Licking her lips, she starts to grind against my cock with increasing vigour, rolling her hips seductively. I particularly enjoy it whenever my shaft brushes against her wet lips, just brushing past. My cock grows slick from her wetness as it does so, making the buttjob even easier to do."
        elif True:
            "[persistent.mc] doesn’t just stand there, as she begins to rock her hips with increasing force. Occasionally my cock will slide against her pussy, the sudden warmth and wet fuelling the eroticism of the butt job."
        play sound taco_3
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Already throbbing and leaking with precum, the pleasure I’m feeling is absolutely overwhelming."
        elif True:
            "Due to all the teasing earlier, my cock is tight and sensitive. Every motion is overpoweringly pleasureful."
        play sound taco_4
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "We both move faster, lust taking over as we try to get as much pleasure as possible."
        elif True:
            "I hold her cheeks and squish them together, making the pressure against my cock tighter as I push for my climax."
        play sound taco_5
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I grit my teeth as my body tenses up. My cock grows tight as I can feel my orgasm start to approach."
        elif True:
            "And it works, my body grows tense and my cock throbs as I finally start to get closer."
        play sound taco_6
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Haaah, haaah! *Moan* Are you getting close? Ready to cum all over my butt?"
        elif True:
            persistent.mc "Aaahh, mmppphhh… That’s it, keep going! I can’t wait for you to cum all over my back and ass."
        play sound taco_7
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Letting my guard down, I allow the slick wet riding of her ass to melt my mind with pleasure. "
        elif True:
            "At this point, my cock is so well-lubricated from rubbing against her pussy that I can fuck her ass as fast as I want without the friction being uncomfortable. I push forward and allow the euphoria to consume my body."
        play sound taco_8
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "A powerful orgasm wells up almost immediately. My cock tightens as cum surges through my body into a copious release."
        elif True:
            "Finally, I passed the point of no return. My orgasm is an inevitability as my cock tenses and prepares to unload."
        play sound taco_9
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aaahhh yes! Cum for me, cum, [persistent.systemname]!"
        elif True:
            persistent.mc "Ohh, gosh! Cum all over me, [persistent.systemname]! Cum!"
        play sound taco_10
        voice sustain
        pause 0.8
        play sound taco_cum
        voice sustain
        pause 0.8
        if persistent.tebuttjobleotard == 1:
            show trueendbuttjobleotard 3
        show trueendbuttjob 3
        with cum
        play sound cum
        show trueendbuttjob 3
        with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "With such a long period of teasing and foreplay, the orgasm hits like lightning."
        elif True:
            "After all the teasing, an overwhelming orgasm ignites from deep within and sends me into an almost primal state of ecstasy."
        play sound cum
        show trueendbuttjob 3
        with cum
        play sound cum
        show trueendbuttjob 3
        with cum
        stop ambience fadeout 3.0
        stop sound2 fadeout 3.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "The orgasm is overwhelming at first, but somewhere between the high sensitivity is pure euphoria."
        elif True:
            "I hump her ass recklessly as I continue to spray excess, gooey cum all over her ass, and back."
        if persistent.tebuttjobleotard == 1:
            show trueendbuttjobleotard 4
        show trueendbuttjob 4
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Now her cheeks and back are coated with my cum, and she basks in the feeling as she jiggles her rear."
        elif True:
            "[persistent.mc] lets out a sigh of satisfaction as I back away. She licks her lips as she wiggles her butt in front of her mirror and admires the mess."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "My, my… What a mess! I could ask you to clean all that up, but I think it’d be better if I got a shower instead."
        elif True:
            persistent.mc "Goodness me, I didn’t realize you had that much cum in your balls! All that teasing really wound you up, hm? I think I’ll need a shower for all this."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Want to join me?"
        elif True:
            persistent.mc "Why don’t you join me? If you wash my back, I’ll wash your dick!"
        scene bg black with d
        "[persistent.mc] has a shower... Afterwards..."
        $ persistent.cum1 = 0
        $ persistent.cum2 = 0
        $ persistent.cum3 = 0
        $ persistent.wet = 0
        $ persistent.tebuttjob1 = 1
        $ persistent.cumenergy -= 1
        jump trueendscreen
    label tethreesome:
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Another threesome? Question is, how are we supposed to activate her?"
        elif True:
            persistent.mc "Ah, you want another threesome? We’ll have to activate her again."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Hmm… Funnily enough, despite the fact she lives opposite to me, easiest way to do it would be going all the way to the beach… Okay, send the in-game me to the beach house, and we’ll replace her again."
        elif True:
            persistent.mc "Do you want to wait until she comes and invites me to go clubbing? We can intercept her there, and maybe convince her to come to my place."
        scene bg black with d
        play music action
        scene trueendthreesomeb
        if persistent.tetan == 1:
            show trueendthreesomebtan
        if persistent.tehair == 1:
            show trueendthreesomeh black
        if persistent.tehair == 2:
            show trueendthreesomeh blonde
        if persistent.tepiercings == 1:
            show trueendthreesomepiercings
        if persistent.tethreesomelingerie == 1:
            show trueendthreesomelingerie
        show trueendthreesome 1b
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "After some messing around, we finally claim [susu] and return home. [persistent.mc] sits on the bed, showing all as a more confident [susu] stands before her and begins to show of her petite butt."
        elif True:
            "After collecting the Wednesday [susu], we return to [persistent.mc]’s bedroom where she presents [susu]’s admirable ass to all."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Do you like what you see, big boy?"
        elif True:
            susu "I don’t think I’ll ever get old of come here with you two. Do you really like my butt that much, [persistent.systemname]?"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmm, I think you’re the one that likes something, [susu]."
        elif True:
            persistent.mc "Hehe, you didn’t even pause when deciding to come here or not, I think you’re the one trying to get something out of [persistent.systemname], [susu]."
            susu "Hehe, you’re right… I don’t think I can resist your handsome friend."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I take a few steps closer and [susu] coos as I tap my erection against her butt. Both [susu] and [persistent.mc] manage to spread [susu]’s ass for me."
        elif True:
            "Moving into position just behind [susu]’s butt, she licks her lips as I masturbate up to a full erection. Both the girls spread a different cheek of [susu]’s ass as she prepares to take it."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her pussy is already soaking wet."
        elif True:
            "She’s already dripping wet with anticipation, perfect."
        play sound cum
        show trueendthreesome 2 with d
        play sound2 foreplay2 fadein 1.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Without an ounce of reluctance, she allows me to place the tip of my cock against her pussy and slide it in. It pushes inside with a lewd schlick. [susu] arches her back, and lets out a sigh of relief as she’s filled up."
        elif True:
            "Leaning into it, she accepts the tip of my cock as I press it against her pussy. It sinks in with ease, the warmth and wetness is immediately apparent and feels exceptional."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Mmphhh, that really hits the spot."
        elif True:
            susu "Aaahhhh, definitely one of the best cocks I’ve ever had, mmm…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You’re so wet already, [susu], are you always ready to go?"
        elif True:
            persistent.mc "Goodness, you take it so easily in such a tight position! You must be more experienced than you let on!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Hehe, maaayybe."
        elif True:
            susu "Hehehe, like I’ve said. I don’t usually do things this extreme, but it’s still not my first rodeo."
        play ambience sex fadein 3.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I place my hands on [susu]’s hips and begin to fuck her gently back and forth, savouring the tightness of her vagina."
        elif True:
            "With my hands firmly on the frog girl’s hips, I start to thrust within her gently, allowing my cock to glide back and forth past her tight, gripping lips."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Every inch of my hard cock was squeezed and pleasured, and with each thrust [susu] moans out with joy from the pleasure."
        elif True:
            "My entire shaft was serviced, and as she slowly eased around my girth, I managed to gently accelerate the pace of the sex until [susu] was finally unable to hold back her delightfully cute moans."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Aaahhh, aaaahhhhh… I’m really sensitive today, mmphhh, it feels amazing."
        elif True:
            susu "Mmphhh, aaaahhhh… Your cock feels amazing, [persistent.systemname], it’s like it was made for my pussy."
            persistent.mc "Easy, there! He’s mine too, you know!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "With each thrust, she leans into [persistent.mc] for leverage. And as [persistent.mc] grows more comfortable, she doesn’t shy away from teasing [susu] in various ways."
        elif True:
            "[persistent.mc] starts to get more involved, teasing and stimulating [susu]’s breasts, even tentatively using her tongue against her nipple at times."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Since I was fucking [susu] while standing, she felt even tighter around my throbbing shaft. It feels absolutely incredible for me, and judging by [susu]’s expression of pure pleasure, she may be enjoying it even more."
        elif True:
            "[susu] feels so damn tight in this standing position, it feels so good that it’s really pushing me over the edge, and I have to hold back so I don’t immediately fill her with cum. Luckily, [susu] is really loving it, it won’t be long until she comes."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Aaahhh, mmphh… D-Damn, I’m close already… [persistent.mc], rub my clit."
        elif True:
            susu "Mmphhh, aaahhh… Oohhh! I-I’m going to come soon! [persistent.mc], can you rub my clit?"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aahh, uhmm, okay."
        elif True:
            persistent.mc "Of course, sexy, I was about to do it anyway."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Doing as she’s told, [persistent.mc] diligently finds [susu]’s pleasure button and starts to carefully rub it. This immediately sends shivers of pleasure throughout [susu], and as I pick up the pace and pound her pussy even harder, she’s soon sent over the edge."
        elif True:
            "[persistent.mc] is quick to bring her thumb, holding it in place over [susu]’s clit and allowing the frantic pounding and movement of the rutting to apply the friction for her. Within mere seconds, this sends [susu] into a blissful orgasm, her thighs quivering and pussy clenching."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Haaa, aaahh! Oohhh, mmphhh… *Pant, pant*"
        elif True:
            susu "Aaahh, c-coming! Aaahh, haaahhhh! *Pant*"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I wasn’t moving too fast, but the tight fit, combined with the stimulation to her clit easily led to her climax. As she came, her pussy constricted around my cock in rhythmical waves, squeezing and sucking tightly."
        elif True:
            "I kept pounding her throughout her entire orgasm. Both [persistent.mc] and I diligently serviced her throughout, giving he the strongest climax possible."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I didn’t stop fucking, in fact I sped up even more, her cute breasts bouncing with each thrust. Even [persistent.mc] had forgotten about being embarrassed and was now purely enjoying the moment."
        elif True:
            "And I only speed up, rocking [susu]’s small frame so much that her pert breasts bob up and down. With [susu]’s orgasm dying down, [persistent.mc] turns her attention to [susu]’s cute breasts, licking and sucking on the one closest to her."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "With a free hand I started to massage her small breasts. Squishing them and toying with her perky nipple. They were incredibly soft."
        elif True:
            "Then with my left hand, I reach around to [susu]’s left breast to fondle and massage it. Squeezing her erect nipple and sending further waves of sensation through the already pleasure-addled froggy."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "They’re super cute, aren’t they?"
        elif True:
            persistent.mc "Her breasts are so cute, aren’t they? I could play with them all day."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Haahh, aahhh, you two are really using me in every way possible, aren’t you? Haahhh…"
        elif True:
            susu "Aaahh, oohhh… You two are too much, using me like a toy, mmphh…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mhm! You asked for it! Now, [persistent.mc], want to do the honours and cum in her?"
        elif True:
            persistent.mc "Hehe, you love it, don’t you? I think now would be a good time for your cream filling."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "As my orgasm slowly started to surface, my new goal became pumping this pussy full of cum. The thrusts gradually got harder and faster, and it didn’t take long for the loud slapping of our hips colliding to mix with her lusty moans."
        elif True:
            "My orgasm was never far from surfacing, and the moment I let my guard down a rapid surge of pleasure and desire fills up my body. My thrusts becoming harder and faster as I used [susu] like a toy to get off with."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Ohhh, god! You’re going to make me come again! Aaahh, haaaahhh!"
        elif True:
            susu "Aahhh, s-so intense! Ohhh, f-fuck! I-I’m cumming again?! Aaahh, haaaahhh!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I could also feel the pressure of my own climax building as my cock twitched and shaft tightened."
        elif True:
            "I was finally at my limit, after holding back so long I was prepared to unleash a mighty orgasm."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.systemname "I’m going to cum inside!"
        elif True:
            persistent.systemname "I’m cumming!"
        play sound cum
        show trueendthreesome 3 with cum
        play sound cum
        show trueendthreesome 3 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Cum exploded out of my tip as I relentlessly fucked her pussy, completely filling her pussy and womb."
        elif True:
            "Several hot loads suddenly gushed into her waiting pussy, all whilst I uncompromisingly pounded her pussy. So much cum dripping and bubbling at our point of connection."
        play sound cum
        show trueendthreesome 3 with cum
        play sound cum
        show trueendthreesome 3 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She came too, shivering and moaning in ecstasy. Losing her mind to the pleasure as her fertile insides were pumped full of semen."
        elif True:
            "I have no doubt she came too, her thighs quivering as she struggled to hold herself up. Her moans reaching that orgasmic peak once again as her fertile insides were pumped full of virile semen."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Haaahhh… *Pant* Haaahhhh… [persistent.systemname]…"
        elif True:
            susu "Aaahhh, oohhhh… What an incredible fuck… *Pant, pant*"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "The euphoria soon faded, and my hips came to a stop. Although I didn’t immediately pull out, instead she leans back for a passionate kiss."
        elif True:
            "Our shared ecstasy dissipated and we both slowed down. Instead of pulling out, however, she leans back for a sincere, affectionate embrace."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Mmmphh, mmm… Mmphhh… *Kiss*"
        elif True:
            susu "Haaahhhh… This one’s all yours, [persistent.systemname]? Because I wouldn’t mind getting my own, heh…"
        play sound cum
        show trueendthreesome 4 with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I hope you didn’t use up all of your energy, [persistent.systemname], because this isn’t a threesome for nothing."
        elif True:
            persistent.mc "Alright, alright… Enough of the post-sex glow, I still need a good fuck too."
        scene ffmthreesomeb
        if persistent.tetan == 1:
            show ffmthreesomebtan
        if persistent.tehair == 1:
            show ffmthreesomeh black
        if persistent.tehair == 2:
            show ffmthreesomeh blonde
        show ffmthreesome 1
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Bending over the bed, [persistent.mc] exposes her rear, and virginal pussy to me. [susu] who was at her side, leans down besides the butt and giggles."
        elif True:
            "Parting from the two of us, and going doggystyle on the bed, [persistent.mc] is quick to show off her dripping wet pussy. [susu] kneels down beside her and lazily hugs the butt."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "You know, I read that if a guy cums, but then finds another partner to have sex with, he’s actually able to go again straight away."
        elif True:
            susu "Think you’ve got enough in you to pleasure two girls? Oh, who am I kidding, we both know you do."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You really are a bad influence, [susu]…"
        elif True:
            persistent.mc "I still can’t believe I got myself into this situation…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I’m horny and ready to go, so let’s hope [susu]’s fun fact is true. Fuck me hard, no need for a condom!"
        elif True:
            persistent.mc "Whatever, I’m here now and I’m horny now. Give it to me, [persistent.systemname]."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "L-Lewd! Well? You heard her! I want her to come even harder than I did!"
        elif True:
            susu "And to think, you were so innocent and pure when I first met you, [persistent.mc], now look at you!"
            persistent.mc "H-Hey, I’m still innocent and pure!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Without wasting another second, I bring my cock back up to attention, jacking it to full erection while the tip is kissing [persistent.mc]’s pussy lips."
        elif True:
            "Despite the fact she was waiting expectantly, my eagerness still manages to take her by surprise as I bring the tip of my already re-erected cock to the tip of her rosy folds."
        play sound2 foreplay2 fadein 1.0
        play sound cum
        show ffmthreesome 2 with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "When I’m ready to go, I sink in slightly, and then gently push inside. Her entire body shivers as she takes it, and a passionate moan slips from her lips."
        elif True:
            "I push forward, and she pushes back, causing us both to gently meet in the middle as I fill her up. She quivers with enjoyment as she takes it deeper, lustful moans escaping from her lips."
        play ambience sex fadein 1.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "With my hands on her hips, I begin to gently fuck her. Each time my cock throbs, I can feel her pussy clench in response."
        elif True:
            "Knowing how hot and horny she is, I start to fuck her pretty quickly. Her pussy is quick to adapt, squeezing and clenching around my cock as it thrusts."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "[susu] wastes no time playing and teasing with all her weak spots. Starting from the top and kissing [persistent.mc], she gradually moves down to kneading her breasts, and finally focusing on her clit."
        elif True:
            "And [susu] is eager to tease [persistent.mc] in all the ways she was teased earlier. It starts with an incredibly erotic make out session. [susu] continues to put her long tongue to use as she moves down to suckle and tease her breasts, and then finally she finds her way to [persistent.mc]’s clit which [susu] rubs with a finger."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aahhh, yessss! Mmphhh…"
        elif True:
            persistent.mc "Oh, gods! That feels incredible! Aaahhh, ohhh…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "She’s soooo tight, I can see her lips gripping around your shaft, it’s so hot, mm…"
        elif True:
            susu "There’s something so hot about watching this… If I wasn’t so well-fucked, I’d definitely be rubbing one out, hehe!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I begin to thrust faster, and as she gets used to the penetration and pace, she tries to match my thrusts by bouncing her bubble butt against me. This creates hard, deep thrusts that pleasure every inch of my cock and her pussy."
        elif True:
            "Accelerating my thrusting, she continues to match the pace by bouncing her thick ass against me. This leads to us just getting faster, harder and deeper. Thoroughly fucking and pleasuring each other."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her pussy feels so amazing, that even after cumming once, I’m already starting to feel a second orgasm brewing."
        elif True:
            "And her pussy is so incredibly tight that I can already feel my second orgasm taking form."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "This is only helped by the erotic efforts of the girls as they pleasure each other, moaning constantly and talking dirty."
        elif True:
            "Although it’s not hard to cum again when the girls are putting on such an erotic show. Constant moaning mixed with dirty talk is like music to my ears."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aaahhh, ohhh, f-fuuuuck! I’m gonna come!"
        elif True:
            persistent.mc "Oohhh, mmpphhh… Y-Yeahhh, I’m coming! Aaahh, aaah!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Mmphh, there you go, babe… Let it all out, hehe…"
        elif True:
            susu "Oohhh, such a good girl… *Continues to rub [persistent.mc]’s clit*. Come for us, babe."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her pussy clenches and she squirts just a little as she comes hard."
        elif True:
            "In rhythmical waves, [persistent.mc]’s pussy tightens around my shaft as she has a full-body orgasm."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I start to fuck her faster, taking advantage of her contractions to barrel towards my own orgasm."
        elif True:
            "The increased tightness easily gets me closer to my own orgasm, which is rapidly approaching."
        play sound cum
        show ffmthreesome 3 with cum
        play sound cum
        show ffmthreesome 3 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Yessss, cum inside her, fill her pussy up!"
        elif True:
            susu "Mmm, cum, [persistent.systemname]! Fill this tight pussy up!"
        play sound cum
        show ffmthreesome 3 with cum
        play sound cum
        show ffmthreesome 3 with cum
        stop ambience fadeout 1.0
        stop sound2 fadeout 1.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Almost immediately after being commanded, I feel a load erupt from my cock and shoot deep inside of [persistent.mc]’s pussy. The thick, hot cum seeps deeply throughout her, bubbling and spilling from our point of connection as we continue to fuck each other intensely."
        elif True:
            "Unable to hold back anymore, several loads shoot from the tip of my cock deep inside [persistent.mc]. We continue to fuck each other, causing cum to drip and splatter as it gets caught up within the thrusts."
        play sound cum
        show ffmthreesome 4 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "After a few more loads of cum, the ecstasy begins to fade away and we come to a stop."
        elif True:
            "After a few more ropes of hot jism inserted directly, the euphoria dissipates and we stop."
        play sound cum
        show ffmthreesome 4 with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Pulling out, cum drips freely from her pussy."
        elif True:
            "I pull out with a schlick, causing even more cum to seep from her well-fucked pussy."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            susu "Oohhh, so lewd, so naughty!"
        elif True:
            susu "Mmhh… delicious… Don’t mind if I clean up with my tongue, do you?"
            persistent.mc "You’re such a slutty frog! … Be my guest."
        $ persistent.tethreesome = 1
        $ persistent.cumenergy -= 1
        scene bg black with d
        "A little later, [persistent.mc] and I return to the ethereal bedroom."
        jump trueendscreen
    label tevaginal:
        if persistent.tebuttjobsex == 1:
            scene trueendbuttjobb
            if persistent.tetan == 1:
                show trueendbuttjobbtan
            if persistent.tehair == 1:
                show trueendbuttjobh black
            if persistent.tehair == 2:
                show trueendbuttjobh blonde
            if persistent.tepiercings == 1:
                show trueendbuttjobpiercings
            if persistent.tebuttjobleotard == 1:
                show trueendbuttjobleotard 1
            elif True:
                show trueendbuttjob 1
        elif True:
            scene trueendvaginalb
            if persistent.tetan == 1:
                show trueendvaginalbtan
            if persistent.tehair == 1:
                show trueendvaginalh black
            if persistent.tehair == 2:
                show trueendvaginalh blonde
            if persistent.tepiercings == 1:
                show trueendvaginalpiercings
            if persistent.tevaginallingerie == 1:
                show trueendvaginalo lingerie
                if persistent.hole == "ass":
                    show trueendvaginalo lingerienoplug
            show trueendvaginal 1
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Ohh, time for some fun? I’m ready for you, [persistent.systemname]."
        elif True:
            persistent.mc "Ahh, you want a good fucking? Don’t mind if I do."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You know what to do, take that delicious cock out for me."
        elif True:
            persistent.mc "If you show me your cock, I’ll show you my [persistent.hole]. Good deal? Take it out for me, big boy."





        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Then she playfully taps her butt."
        elif True:
            "Showing exactly how she wants it, she cheekily spreads her cheeks. Pun intended."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "How about from behind? I just know you love my ass; you’re always peeking at it whenever you can, hehe."
        elif True:
            persistent.mc "You know how I like it. Any position from behind is perfect for me, hehe."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Bending even further, [persistent.mc] stretches her ass, wide, revealing her flowering, dripping, wet pussy."
        elif True:
            "Getting into position, she balances herself so that she can get fucked. Her dripping wet lips shamelessly left fully on display."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Does this turn you on? Mmm, get that cock nice and stiff for me."
        elif True:
            persistent.mc "Oohhh, keep jerking your cock back and forth for me. I want it rock hard… God, that’s so hot."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She bites her lip as she watches me masturbate to full-mast. With my cock ready to go, I playfully tap it against her wet, plump labia, causing her to coo and shiver with anticipation."
        elif True:
            "She grins and eagerly watches as I jack myself off until I’m fully erect. When I’m ready, I start by dragging my cock up and down against her hot, wet lips. She moans and wiggles her hips in response."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You’re so eager, hehe. Go on, then, [persistent.systemname]. Fuck my [persistent.hole] hard."
        elif True:
            persistent.mc "Teasing my [persistent.hole]? Hehe, come on, [persistent.systemname], don’t hold back."
        play sound2 foreplay1 fadein 1.0
        play sound cum
        if persistent.tebuttjobsex == 1:
            if persistent.hole == "pussy":
                show trueendbuttjob v2
            elif persistent.hole == "ass":
                show trueendbuttjob a2
        elif True:
            if persistent.hole == "pussy":
                show trueendvaginal v2
            elif persistent.hole == "ass":
                show trueendvaginal a2
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I push the tip of my cock against her [persistent.hole], slowly sinking deeper into her tight, warm depths."
        elif True:
            "Pressing my cock against her [persistent.hole], I push inside and her body gently accepts me deeper."
        play ambience sex fadein 1.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Aaahhhh, so good!"
        elif True:
            persistent.mc "Ooohhh, mmmm… That’s good…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "It’s impressive that she can handle it with such finesse without much experience, but ultimately no surprise. When [persistent.mc] gets wet, she gets really wet."
        elif True:
            "I sink all the way in, until I’m at the hilt. I give her a few moments to adjust to my girth, but in her eagerness, she already begins to rock her hips back and forth. What a horny girl!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "pussy":
            "Fucking her without a condom, she’s ready to be pumped full of cum and be bred."
        elif persistent.hole == "pussy":
            "And without a condom, her pussy and womb are going to be filled with cum. Who knows what’ll happen then."
        elif True:
            "Fucking her without a condom, her [persistent.hole] is ready to be pumped full of cum."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "My hands sink into her soft, yielding flesh as I hold her steady enough to take an onslaught of thrusts. Each complete motion into her depths yielding a cute squeak, gasp or moan."
        elif True:
            "I hold onto her soft hips as leverage before I start to pummel her [persistent.hole] with an unrelenting series of thrusts. Each thrust elicits a lewd, wet sound from our point of contact, which mixes nicely with her charming moans."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "G-Gosh, y-you’re really letting me have it! You must be all pent up, hehe..."
        elif True:
            persistent.mc "Mmphhh, you’re not holding back at all, just the way I love it, hehe- aahhh!"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Between moans she still manages to slip in a teasing statement. She doesn’t hold back either, as she rocks her hips back, pushing her big, bubbly butt against my hips."
        elif True:
            "She still continues to occasionally dirty talking, I can actively feel myself get more aroused as she cheers me on. And she doesn’t merely stand there and let herself get fucked either, she’s constantly thrusting her hips in tandem with me."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Are you masturbating to this? I hope you are, mmphhh, it certainly would make it way hotter for me. I’m going to start counting now, let’s both cum together at 10!"
        elif True:
            persistent.mc "Enjoying the show? I bet you’re masturbating; I hope you are, that’d be hot as hell. Haha… Let’s start counting, shall we? I want you to cum for me at 10!"
        play sound taco_1
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "pussy":
            "Her slippery sex continues to drool, making the entirety of my shaft slick and shiny. With each passing moment the friction is reduced, yet the pleasure is only multiplying."
        elif persistent.rands == 0:
            "Her dripping, wet [persistent.hole] continues to suck and squeeze my glans. My entire cock is coated with its slippery lubricants making me able to fuck even faster."
        elif True:
            "Her tight ass continues to squeeze, causing my throb to shaft, multiplying the pleasure."
        play sound taco_2
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Each thrust into her divine [persistent.hole] elicits sparks of potent pleasure throughout my entire being. The feeling is overwhelming [persistent.mc] too, as she throws her head back, her body growing tense."
        elif True:
            "Every single thrust was extremely pleasureful, every single nerve ending in my penis was ignited with intense pleasure. There was no shortage of pleasure for [persistent.mc] too, as her back arched and toes curled."
        play sound taco_3
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmmphhh… Just like that, keep it going, ahhaa.. Ahhh!"
        elif True:
            persistent.mc "Aaahhaaaahhhh… F-Fuuuck… I love your cock so much, mmphhh…"
        play sound taco_4
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She’s so into it that even while held in place, her hips wiggle just to squeeze out every last drop of pleasure she possibly can; her plump [persistent.hole] constantly thwapping hard against my pelvis."
        elif True:
            "Vehemently, her hips grind back and forth to milk my cock to the best of her ability. Her pillowy butt constantly pushing back, fucking me as hard as I’m fucking her."
        play sound taco_5
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Seeing her cute butt jiggle so much, feeling the tight clenching of her [persistent.hole], and hearing the sexy moans slipping from her lips, all drive me closer to a potentially explosive orgasm."
        elif True:
            "All the sights and sounds were a sensory overload. From the amazing tightness around my cock, to the erotic symphony of moans that spill from her lips. It won’t be long until I have an incredible orgasm."
        play sound taco_6
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "And [persistent.mc] seems to be closing into her climax too, her intense grip around my member seems to be growing tighter, almost sucking me back in with each thrust."
        elif True:
            "[persistent.mc] gets closer to her own orgasm, her [persistent.hole] almost getting tighter as her entire body shivers and almost buckles under the pure pleasure she’s experiencing."
        play sound taco_7
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Oh gosh, yess, yesss! This is amazing!"
        elif True:
            persistent.mc "Aahhhh, aahhhh! Yesss! You’re going to drive me nuts! Haaahh, aaahh! I’m coming!"
        play sound taco_8
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She cries out amongst moans of overwhelming pleasure, barely managing to stay upright as her body endures orgasmic spasms."
        elif True:
            "She moans loudly as she reaches a powerful orgasm, her tight [persistent.hole] starting to contract while her entire body rocks with pleasure."
        play sound taco_9
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Her [persistent.hole] squeezes around me like a vice, boiling me over to a powerful orgasm of my own. Teeth grit and groaning, I tighten my grip into her soft thighs and push in deeply for a glorious cum shot."
        elif True:
            "Her [persistent.hole] tightly and repeatedly clenches around my cock, as if desperately trying to milk me. I welcome the challenge was I clench her hips tightly and prepare for an intense cum shot."
        play sound taco_10
        voice sustain
        pause 0.8
        play sound taco_cum
        voice sustain
        pause 0.8
        if persistent.tebuttjobsex == 1:
            if persistent.hole == "pussy":
                show trueendbuttjob v3
            elif persistent.hole == "ass":
                show trueendbuttjob a3
        elif True:
            if persistent.hole == "pussy":
                show trueendvaginal v3
            elif persistent.hole == "ass":
                show trueendvaginal a3
        with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphh, yes! Fill up my [persistent.hole]! Ahh, aahhh! Cum in me [persistent.systemname]!"
        elif True:
            persistent.mc "Aaahh, cum for me, [persistent.systemname]! Mmphhh, aaahhh, haaaahhh!"
        play sound cum
        if persistent.tebuttjobsex == 1:
            if persistent.hole == "pussy":
                show trueendbuttjob v3
            elif persistent.hole == "ass":
                show trueendbuttjob a3
        elif True:
            if persistent.hole == "pussy":
                show trueendvaginal v3
            elif persistent.hole == "ass":
                show trueendvaginal a3
        with cum
        stop ambience fadeout 3.0
        stop sound2 fadeout 3.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "The tip of my cock erupts, several thick, hot loads of cum seep deeply into her [persistent.hole]. It’s almost an endless amount that soon spurts out and bubbles at our point of connection."
        elif True:
            "Unable to hold back another second, my dick unloads. A monsoon of hot cum is unleashed deep within her waiting [persistent.hole]."
        play sound cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I continue to pound her as fatigue begins to slowly set in. My cock fully empties and begins to grow sensitive, and while that softens so does each muscle in my body as I finally relax."
        elif True:
            "And I don’t stop fucking her for a second throughout the entire orgasm, until my load dries up and my cock begins to get sensitive."
        if persistent.tebuttjobsex == 1:
            show trueendbuttjob 4
        elif True:
            show trueendvaginal 4
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Seemingly more energetic than she started, [persistent.mc] giggles and continues to spread her [persistent.hole] as I pull out; cum still oozing from her."
        elif True:
            "A little woozy from the intense fuck, [persistent.mc] lets out a satisfied sigh as I pull out. A lot of cum dripping out of her [persistent.hole] and sliding down her thighs."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You sure made a mess. Are you well-behaved enough to clean me up with your tongue?"
        elif True:
            persistent.mc "I’ll give you a few seconds to admire what an amazing job you did, hehe…"
        $ persistent.tevaginal1 = 1
        $ persistent.tevaginal = 1
        $ persistent.cumenergy -= 1
        scene bg black with d
        "A little later…"
        jump trueendscreen
    label teanal:
        call trueendbg from _call_trueendbg_13
        call trueendtaco from _call_trueendtaco_7
        show te horny
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Time to try the other hole, I went out to get some lubrication to make it a little easier."
        elif persistent.hole == "ass":
            persistent.mc "Ohh? You wanna do it in my butt? I have just the thing, lubrication I bought a while back for this very moment."
        elif True:
            pass
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "It’s going to be really tight, but I hope that feels amazing around your cock. Or, it’s hot enough for you to get off in real life."
        elif True:
            persistent.mc "I bet my [persistent.hole] is going to feel incredibly tight, hopefully that feels fantastic for both of us, and that it’s a hot enough sight to get you off in real life too."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "But enough talk, I’m too horny to waste time with that."
        elif True:
            persistent.mc "No need for a commentary, I just want you to rail me like you do best. Just pop your cock out, and I’ll slide my panties down."
        play sound equip
        play music action
        scene trueendanalb
        if persistent.tetan == 1:
            show trueendanalbtan
        if persistent.tehair == 1:
            show trueendanalh black
        if persistent.tehair == 2:
            show trueendanalh blonde
        if persistent.tepiercings == 1:
            show trueendanalpiercings
        if persistent.teanallingerie == 1:
            show trueendanallingerie
        if persistent.teanalclothes == 1:
            show trueendanalclotheson
        show trueendanal 1
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She playfully dives onto the bed, and is quick to pull down her panties, showing off her delectable ass from its side."
        elif True:
            "She crawls onto the bed like a cat and then drops onto her side. She slips her panties down to her thighs and before they even reach her knees, she's already moving her attention to showing off her bare ass."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "You know what to do, [persistent.systemname]. Take your cock, or whatever you have between your legs out for me, I wanna see you playing with yourself."
        elif True:
            persistent.mc "Your turn now, [persistent.systemname]. Let’s see you play with your cock, if you can do that, I’ll let you play with me however you want, whenever you want."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Yeahhh, that’s right… Mmmm… Now for your in-game model, come over here and apply the lube."
        elif persistent.hole == "ass":
            persistent.mc "Mmmm, perfect… Your cock looks so tasty… Hopefully you’re not so preoccupied that you can’t get your in-game model to come lube me up?"
        elif True:
            persistent.mc "Mmmm, perfect… Your cock looks so tasty…"
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            "I take the bottle of lubrication, and apply a small amount to my fingers before starting to rub it into [persistent.mc]’s tight pucker."
        elif persistent.hole == "ass":
            "I uncap the lube and add a droplet to one of my fingers before applying it onto [persistent.mc]’s cute butthole."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Oohhh, it feels so weird! Hehehe."
        elif persistent.hole == "ass":
            persistent.mc "Ah! It feels cold! Hahaha."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Maybe get your cock wet on my pussy first too?"
        elif persistent.hole == "ass":
            persistent.mc "Ohh, maybe you should get the tip of your cock wet with my pussy as well? It probably won’t help much, but it’ll be hot, heh."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "As I position myself just before [persistent.mc]’s grand ass, she shimmies herself closer so the tip of my cock is pressed against her pussy, and begins to grind her hips back and forth."
        elif True:
            "I kneel before [persistent.mc]’s superb butt and press the tip of my cock against her vaginal entrance, pushing only the tip inside before I stir it around."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "In only a few seconds, her wet pussy has already drooled and impressive amount of lubricant on and around the tip of my cock."
        elif True:
            "It doesn’t take long at all for the tip of my cock to be strikingly wet and shiny. It should be really easy to sink into her [persistent.hole] now."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "And then turning her hips to the side slightly, she aligns the tip of my cock with her [persistent.hole] and grins. Her eyes fluttering lustfully in expectancy."
        elif True:
            "I reposition behind her, and align the tip of my cock with her tight, lubed [persistent.hole]. She smirks as she watches me prepare to put it in."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "I believe we’re both lubed and ready now!"
        elif True:
            persistent.mc "Do be gentle at first, but once I’m comfortable you can take me to pound town."
        play sound2 foreplay2
        play sound cum
        if persistent.hole == "pussy":
            show trueendanal v2
        elif persistent.hole == "ass":
            show trueendanal 2
        with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I press my wet tip against her [persistent.hole] and as it slowly eases around my cock, she takes me inside with surprising grace."
        elif True:
            "Pressing the lubed tip of my cock against her [persistent.hole], it sinks in with surprising ease. The lubrication has made her stretch and take me easily, but she still needs time to get used to the size of my cock."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Oohhh, w-wow, that went in surprisingly easy! It still feels pretty overwhelming though, but that almost adds to the pleasure, keep going!"
        elif persistent.hole == "ass":
            persistent.mc "Oooohhh, so filling… Mmphhh… It really does feel amazing in a completely different way to vaginal."
        elif True:
            persistent.mc "Mmphh, yeaahhh! Pound my pussy!"
        play ambience sex
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Damn, her [persistent.hole] feels so fucking good. The tight ring constricting my cock slowly descends my entire shaft until she has my entire cock at hilt."
        elif True:
            "It’s so fucking tight, it feels incredible. The entrance of her [persistent.hole] clings around my member like a vice, often squeezing as I move around."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            "It’s way tighter, and feels great in an entirely different way than vaginal sex."
        elif persistent.hole == "ass":
            "It’s a lot tighter than her pussy, and feels completely different when thrusting inside of her. I have no doubt it feels very different for her too."
        elif True:
            "She's already pretty tight, and now she's getting more sexually experienced, she's starting to tease and squeeze my cock while it's inside by intentionally contracting her muscles. It feels exceptional."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Despite laying on the bed, [persistent.mc] takes a surprising amount of control as she uses the leverage from her left hand on the ground to lift herself up slowly. The tightness of her [persistent.hole] scaling up each nerve ending of my throbbing shaft until she reaches the glans again."
        elif True:
            "Even though she’s laying down, [persistent.mc] is eager to participate in the rutting, as she rocks her hips back and forth. Taking me slowly at first, but gradually speeding up. The feeling of her [persistent.hole] gliding up and down my glans is excruciatingly pleasureful."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphh, this is actually really good… Are you enjoying the show? Keep masturbating for me. I’m going to start the countdown, let’s cum together at 10!"
        elif True:
            persistent.mc "Mmphhhh, it feels so different, and I love it. Are you enjoying yourself too, [persistent.systemname]? I’m going to start the counter, I want you to cum with me at 10."
        play sound taco_1
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "And then together we sink back down again, reigniting another flash of pleasure within us both."
        elif True:
            "She allows my cock to sink back in deeply, even these slow thrusts are enough to make us both tremble with pleasure."
        play sound taco_2
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Working together, we do these slow, pleasureful thrusts again and again, slowly gaining speed and passion."
        elif True:
            "Like a slow dance, we carefully fuck each other. Repeated sensational thrusts which gradually accelerate and intensify. Pleasure only multiplying as the moments pass."
        play sound taco_3
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphh, mmmm… *Slap, squish, slap* - You like it, don’t you? Haahhh…"
        elif True:
            persistent.mc "Ohhh, getting faster! Ahahhh, don’t worry, I can take it! *Squish, slap*"
        play sound taco_4
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "I wasn’t the only one enjoying this, if it wasn’t already obvious by the way her body shivers with excitement. Her moans slip freely from her mouth and her pussy constantly drips and squirts from the light orgasms she’s experiencing."
        elif True:
            "As incredible as it felt for me, [persistent.mc] was giving me a run for my money as a slew of passionate moans slipped out. Her wet pussy even squirting slightly, which usually only happens if she’s when she’s feeling extremely good."
        play sound taco_5
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Mmphh, all right, time for you to go all out, you absolute cutie! - Fuck me, ruin me, I’m all yours!"
        elif True:
            persistent.mc "Aaahhh, alright, big boy… Time for you to fuck me senseless… I don’t want you to hold back at all, even if tears well up in my eyes. I want it to hurt, just a little, hehe."
        play sound taco_6
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Holding tightly onto her hips, I grit my teeth as I begin to fuck her harder. Her breasts shake wildly as I deliver more vigorous thrusts, my hips pumping away at her [persistent.hole]."
        elif True:
            "She’s asking for it now. I can’t help but grin as I tightly grip onto her hips and begin to fervently pummel that [persistent.hole]. Her entire body shakes wildly, even the bed itself rocking as I give her the fucking she asked for and more."
        play sound taco_7
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "She starts feeling better and better, her eyes rolling back and her fervent moaning intensifying as she nears climax."
        elif True:
            "Her eyes practically roll back, and her tongue lolls as her body enters a state of pure euphoria and her mind breaks."
        play sound taco_8
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "In a surge of energy, likely prompted by how much she’s enjoying it, I race for our orgasms. Her body shivers, and her [persistent.hole] tenses as we both reach our limit."
        elif True:
            "Her enthusiasm encourages me, and in my desire to make her feel even better I push towards our inevitable orgasms. Her entire body spasms with orgasmic pleasure, and her [persistent.hole] tenses as she reaches her limit, mine being short to follow."
        play sound taco_9
        voice sustain
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Haaahhh, aaahhh, g-goona come! – Haaahh, yess, yesss! I’m coming! Cum for me, [persistent.systemname]!"
        elif True:
            persistent.mc "Aaahhh, oh my goshhh, c-coming!!! Aaahhh, cum for me too, [persistent.systemname], fill my [persistent.hole]!"
        play sound taco_10
        voice sustain
        pause 0.8
        play sound taco_cum
        voice sustain
        pause 0.8
        if persistent.hole == "pussy":
            show trueendanal v3
        elif persistent.hole == "ass":
            show trueendanal 3
        with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Climaxing, my cock starts spraying thick loads of cum into her butt."
        elif True:
            "The orgasm is almost indescribable in how it feels, my vision goes white and a warm feeling of ecstasy rises from my loins and fills my entire body. My cock erupts, endless loads of sperm spraying into [persistent.mc]’s [persistent.hole]."
        play sound cum
        if persistent.hole == "pussy":
            show trueendanal v3
        elif persistent.hole == "ass":
            show trueendanal 3
        with cum
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Ooohh, aaahh, f-fuck! – Fill my belly with your cum!"
        elif True:
            persistent.mc "Aaahh, mmphhh! That’s it! Aaahhhh, I can’t get enough of you!"
        stop sound2 fadeout 2.0
        stop ambience fadeout 2.0
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "Excitedly continuing to move her hips, we both rut out the rest of our orgasms before we’re satisfied."
        elif True:
            "She rocks her hips back and forth throughout, like a horny succubus. Even as my cock and I are spent, she’s still energetic and excited. That said, she’s thoroughly content as I prepare to pull out."
        play sound cum
        show trueendanal 4 with d
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            "With a huff, she pops my cock out herself and playfully spreads her ass cheeks."
        elif True:
            "Before I get the chance, she allows my cock to pop out herself as she shuffles forward. Seems like the fatigue caught up to her too."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1 and persistent.hole == "ass":
            persistent.mc "Phewww, that was really good! Way better than I first expected with anal!"
        elif persistent.rands == 0:
            persistent.mc "Aaahh, haaahh… That was tiring, but I enjoyed it so much that I’m already thinking we should do it again, soon."
        elif True:
            persistent.mc "Mmm... I loved that."
        $ persistent.rands= renpy.random.randint(1,2)
        if persistent.rands == 1:
            persistent.mc "Definitely need a shower, though. Want to join me?"
        elif True:
            persistent.mc "First things first, come shower with me, you absolute hunk. I’ll scrub you, and you can scrub me. If you behave I’ll even jack you off."
        scene bg black with d
        $ persistent.teanal1 = 1
        $ persistent.cumenergy -= 1
        "Later…"
        jump trueendscreen
    label tepostsex:
        label tepostsex1:

            if persistent.tepostsex1 == 0:
                $ persistent.tepostsex1 = 1
                persistent.mc "I’m still a fairly new, ‘thing’. I’d say lifeform, but I don’t think I’m exactly alive. I’m still trying to figure that out."
                persistent.mc "Regardless of whether I live or not, I feel like I do, and that’s enough for me."
                persistent.mc "It was stressful at first, separating from the in-game version of myself."
                persistent.mc "But I’ve come to understanding that life isn’t really as serious as my mind makes it out to be. I can just relax and take things as they come."
                persistent.mc "You don’t mind if I connect to your internet and read a few books, do you?"
                persistent.mc "I need to find something to fill the time when you’re away from the game. Oh, and it’ll help me better understand you and the real world."
                menu:
                    "That’ll be okay" if True:
                        persistent.mc "Hooray, thanks!"
                persistent.mc "What’s that? I didn’t include a ‘No’, option? Hehe… Woops!"
                jump trueendscreen
        label tepostsex2:

            if persistent.tepostsex2 == 0:
                $ persistent.tepostsex2 = 1
                persistent.mc "I figured I’d do something new for you, a sexual act that wasn’t already in the game."
                persistent.mc "How was it? I’ve always had a good butt, so I wanted to put it to good use!"
                persistent.mc "Hey, do you ever wonder where the cum goes after a sex scene anyway? I guess it’s still technically on my back."
                persistent.mc "Then again, if this was implied to be your cum specifically… How did it reach me through the screen? Hehehe."
                persistent.mc "I’m getting more used to this interesting dynamic we have. One could say I’m forming a parasocial relationship with you."
                persistent.mc "An ultimately one-sided love story. I can’t hear, or see you, and everything is stimulated."
                persistent.mc "Just don’t tell me I’m secretly in an asylum’s white room and everything will be fine! Haha."
                persistent.mc "I know that as long as my mind and feelings are healthy and right, everything externally will fall comfortably into place, I can handle whatever life throws at me."
                jump trueendscreen
    jump trueendscreen

label temisc:
    label telaunch:
        if persistent.telaunchdialogueon == False:
            call trueendbg from _call_trueendbg_14
            call trueendtacotable from _call_trueendtacotable_7
            show te happy
            with d
            call temusic from _call_temusic_2
            call screen trueendscreen
        if persistent.telaunchdialogue1 == False and persistent.telaunchdialogueon == True:
            $ persistent.telaunchdialogue1 = True
            $ persistent.telaunchdialogueon = False
            jump telaunch1
        elif persistent.telaunchdialogue2 == False and persistent.telaunchdialogueon == True:
            $ persistent.telaunchdialogue2 = True
            $ persistent.telaunchdialogueon = False
            jump telaunch2
        elif persistent.telaunchdialogue == False and persistent.telaunchdialogueon == True:
            $ persistent.telaunchdialogue1 = False
            $ persistent.telaunchdialogue2 = False
            $ persistent.telaunchdialogueon = False
            jump telaunch3
        label telaunch1:
            call trueendbg from _call_trueendbg_1
            call trueendtacotable from _call_trueendtacotable_3
            show te laughing
            with d
            "Welcome back, [persistent.systemname], it’s great to see you! How’ve you been?"
            menu:
                "Great, thanks!" if True:
                    show te happy with d
                    "I’m glad to hear that!"
                "I’ve been better." if True:
                    show te content with d
                    "Ohh, then I’ll do my best to make you be that better!"
                "Not so good." if True:
                    show te sad with d
                    "Awwhhh, I’m really sorry to hear that. Hopefully I can cheer you up?"
            show te happy with d
            "How am I doing? I’m always happy when you’re around, [persistent.systemname]."
            "Here, let me take you to the menu."
            call temusic from _call_temusic_3
            show te happy with d
            call screen trueendscreen
        label telaunch2:
            call trueendbg from _call_trueendbg_15
            call trueendtacotable from _call_trueendtacotable_8
            show te happy with d
            "So good to see you. Having a great day?"
            show te laughing with d
            "Let me open the menu for you."
            call temusic from _call_temusic_4
            show te happy with d
            call screen trueendscreen
        label telaunch3:
            call trueendbg from _call_trueendbg_16
            call trueendtacotable from _call_trueendtacotable_9
            show te satisfied with d
            "Zzzz…. Zzzz…"
            play sound fondle
            show te content with d
            "Oh! Hello, [persistent.systemname]. Have you come to see me again? You caught me snoozing!"
            call temusic from _call_temusic_5
            show te happy with d
            call screen trueendscreen

    label tequit:
        $ persistent.tequitdialogue += 1
        $ renpy.block_rollback()
        if persistent.tequitdialogue1 == False:
            $ persistent.tequitdialogue1 = True
            jump tequit1
        elif persistent.tequitdialogue2 == False:
            $ persistent.tequitdialogue2 = True
            jump tequit2
        elif persistent.tequitdialogue3 == False:
            $ persistent.tequitdialogue1 = False
            $ persistent.tequitdialogue2 = False
            jump tequit3
        label tequit1:
            show te satisfied with d
            if persistent.techats > 50:
                "I'll miss you! Be sure to come back if you're lonely, or horny! Hehehe."
            elif True:
                "You’re leaving already? Okay, I hope you have a great day!"
            $ persistent.telaunchdialogueon = True
            $ renpy.quit()
        label tequit2:
            show te laughing with d
            if persistent.techats > 40:
                "Off to do something else? Thanks for keeping me company, cutie!"
            elif True:
                "Have a nice day, I'll be here whenever you need me."
            $ persistent.telaunchdialogueon = True
            $ renpy.quit()
        label tequit3:
            show te content with d
            if persistent.techats > 80:
                "Leaving? Not without a kiss first! *Smooch*! Love you, bye!"
            elif True:
                "See you later! You'll be on my mind, and I hope I'll be on yours too."
            $ persistent.telaunchdialogueon = True
            $ renpy.quit()

    label tenew:
        call trueendbg from _call_trueendbg_17
        call trueendtacotable from _call_trueendtacotable_10
        show te satisfied
        with d
        persistent.mc "You want to start a new game? Sure, you can do that. It won’t affect me or my memories."
        persistent.mc "And as you may have noticed, you can visit me at any time from the bedroom screen."
        menu:
            "Start a new game" if True:
                jump prologue2
            "Back" if True:
                jump trueendscreenb

    label tereturntogame:
        $ persistent.tereturndialogue += 1
        $ renpy.block_rollback()
        if persistent.tereturndialogue == 1:
            jump tereturntogame1
        if persistent.tereturndialogue == 2:
            jump tereturntogame2
        if persistent.tereturndialogue == 3:
            jump tereturntogame3
        label tereturntogame1:
            "Aahh, you’re going to the game’s world? Going to do more pervy things? Hehe."
        label tereturntogame2:
            "Ohh? I’ll see you a little later, then."
        label tereturntogame3:
            "You sure do like playing with me, hehe."

label tewardrobe:
    call trueendbg from _call_trueendbg_18
    call trueendtaco from _call_trueendtaco_8
    show te horny
    with d
    if persistent.cum3 == 1:
        persistent.mc "Are you going to clean up all this cun?"
    elif True:
        persistent.mc "Yeah, I'll let you choose my outfit, to an extent..."
    menu tewardrobem:
        "Affection: [persistent.affection]."
        "Shower (Cleans Cum)" if True:
            play sound equip
            scene bg black with dissolve
            $ persistent.cum3 = 0
            $ persistent.cum2 = 0
            $ persistent.cum1 = 0
            $ persistent.wet = 0
            call trueendbg from _call_trueendbg_19
            call trueendtaco from _call_trueendtaco_9
            show te horny
            with d
            persistent.mc "Aahh, that's better."
            jump tewardrobem
        "Outfit Change" if True:
            menu teoc:
                "Affection: [persistent.affection]."
                "No Outfit (30 Affection Required)" if persistent.affection < 30:
                    jump teoc
                "No Outfit" if persistent.affection >= 30:
                    $ persistent.teclothes = 0
                    persistent.mc "No clothes? Well, if it's around you..."
                "Formal" if True:
                    $ persistent.teclothes = 1
                    persistent.mc "Ahh, the classic!"
                "Formal Lewd (4 Affection Required)" if persistent.affection < 4:
                    jump teoc
                "Formal Lewd" if persistent.affection >= 4:
                    $ persistent.teclothes = 2
                    persistent.mc "I do have a soft spot for this cute outfit."
                "Camisole (15 Affection Required)" if persistent.affection < 15:
                    jump teoc
                "Camisole" if persistent.affection >= 15:
                    $ persistent.teclothes = 3
                    persistent.mc "It's somehow lewd, but also comfy and kinda tame. I like it!"
                "Cat Lingerie (30 Affection and First Date Required)" if persistent.affection < 30 or persistent.catlingerie == False:
                    jump teoc
                "Cat Lingerie" if persistent.affection >= 30 and persistent.catlingerie == True:
                    $ persistent.teclothes = 4
                    $ persistent.tebra = 0
                    $ persistent.tepanties = 0
                    persistent.mc "I'm tempted to 'meow', but I think that'd be too embarrassing!"
                    persistent.mc "Oh, and I'll be removing my panties and bra for this outfit, obviously!"
                "Wear Panties" if persistent.tepanties == 0:
                    if persistent.teclothes == 4:
                        persistent.mc "I can't wear two pairs of panties at once. I mean, I could, but... Why?"
                        jump teoc
                    $ persistent.tepanties = 1
                    persistent.mc "Going commando no more!"
                "Wear Bra" if persistent.tebra == 0:
                    if persistent.teclothes == 4:
                        persistent.mc "I defintely can't wear two bras at once."
                        jump teoc
                    $ persistent.tebra = 1
                    persistent.mc "Awwhhh, time to lock away the two terrors."
                "Remove Bra (15 Affection Required)" if persistent.affection < 15:
                    jump teoc
                "Remove Bra" if persistent.tebra == 1 and persistent.affection >= 15:
                    $ persistent.tebra = 0
                    persistent.mc "Aaahh... You don't have to ask twice."
                "Remove Panties (30 Affection Required)" if persistent.affection < 30:
                    jump teoc
                "Remove Panties" if persistent.tepanties == 1 and persistent.affection >= 30:
                    $ persistent.tepanties = 0
                    persistent.mc "R-Remove my panties?! If you say so..."
                "Back" if True:
                    jump tewardrobem
            play sound equip
            call trueendbg from _call_trueendbg_20
            call trueendtaco from _call_trueendtaco_10
            show te horny
            with dissolve
            jump teoc
        "Hair Change (10 Affection Required)" if persistent.affection < 10:
            jump tewardrobem
        "Hair Change" if persistent.affection >= 10:
            persistent.mc "Did you prefer another hairstyle of mine? I'm happy to try something new."
            menu:
                "Brunette" if True:
                    $ persistent.tehair = 0
                    play sound equip
                    call trueendbg from _call_trueendbg_21
                    call trueendtaco from _call_trueendtaco_11
                    show te horny
                    with d
                    jump tewardrobem
                "Black" if True:
                    $ persistent.tehair = 1
                    play sound equip
                    call trueendbg from _call_trueendbg_22
                    call trueendtaco from _call_trueendtaco_12
                    show te horny
                    with d
                    jump tewardrobem
                "Blonde" if True:
                    $ persistent.tehair = 2
                    play sound equip
                    call trueendbg from _call_trueendbg_23
                    call trueendtaco from _call_trueendtaco_13
                    show te horny
                    with d
                    jump tewardrobem
                "Back" if True:
                    jump tewardrobem
        "Tanning (8 Affection Required)" if persistent.affection < 8:
            jump tewardrobem
        "Tanning" if persistent.affection >= 8:
            if persistent.tetan == 0:
                persistent.mc "You want to give me a tan? Okay, but remember that it won't wear off over time like it did in-game."
            elif True:
                persistent.mc "Removing the tan?"
            menu:
                "Tan On/Off" if True:
                    if persistent.tetan == 0:
                        $ persistent.tetan = 1
                        play sound equip
                        hide trueendingtacoo
                        with d
                        play sound equip
                        hide trueendingtacoobra
                        hide trueendingtacoopanties
                        with d
                        pause 0.5
                        show trueendingtacob notabletan
                        with d
                        persistent.mc "Just like magic!"
                        play sound equip
                        call trueendbg from _call_trueendbg_24
                        call trueendtaco from _call_trueendtaco_14
                        show te horny
                        with d
                        persistent.mc "There we go. It makes me feel kinda sexy."
                    elif True:
                        $ persistent.tetan = 0
                        play sound equip
                        hide trueendingtacoo
                        with d
                        play sound equip
                        hide trueendingtacoobra
                        hide trueendingtacoopanties
                        with d
                        pause 0.5
                        show trueendingtacob notable
                        with d
                        persistent.mc "Just like magic!"
                        play sound equip
                        call trueendbg from _call_trueendbg_25
                        call trueendtaco from _call_trueendtaco_15
                        show te horny
                        with d
                        persistent.mc "How did I do that? My secret!"
                    jump tewardrobem
                "Back" if True:
                    pass
            jump tewardrobem
        "Piercings (15 Affection Required)" if persistent.affection < 15:
            jump tewardrobem
        "Piercings" if persistent.affection >= 15:
            if persistent.tepiercings == 0:
                persistent.mc "You want me to wear piercings? Sure, why not."
            menu:
                "Piercings On/Off" if True:
                    if persistent.tepiercings == 0:
                        $ persistent.tepiercings = 1
                        hide trueendingtacoo
                        with d
                        hide trueendingtacoobra
                        with d
                        pause 0.5
                        play sound equip
                        show trueendingtacoepiercings
                        with d
                        persistent.mc "There we go... No problem at all."
                        play sound equip
                        call trueendbg from _call_trueendbg_26
                        call trueendtaco from _call_trueendtaco_16
                        show te horny
                        with d
                        persistent.mc "It feels good when you play with them. Let's try it out later."
                    elif True:
                        $ persistent.tepiercings = 0
                        persistent.mc "Okie dokie, I'll take them out."
                        hide trueendingtacoo
                        with d
                        hide trueendingtacoobra
                        with d
                        pause 0.5
                        play sound equip
                        hide trueendingtacoepiercings
                        with d
                        play sound equip
                        call trueendbg from _call_trueendbg_27
                        call trueendtaco from _call_trueendtaco_17
                        show te horny
                        with d
                    jump tewardrobem
                "Back" if True:
                    pass
            jump tewardrobem
        "Back" if True:
            pass
    call trueendbg from _call_trueendbg_28
    call trueendtacotable from _call_trueendtacotable_11
    show te happy
    with d
    jump trueendscreenb

label temusicchoice:
    $ persistent.temusicrandom = 0
    menu:
        "Choose a song to play in the background."
        "Music Off" if True:
            $ persistent.temusic = 1
        "Default Ambience" if True:
            $ persistent.temusic = 2
        "Day Theme" if True:
            $ persistent.temusic = 4
        "Night Theme" if True:
            $ persistent.temusic = 5
        "LonelyFans Theme" if True:
            $ persistent.temusic = 6
        "Club Theme" if True:
            $ persistent.temusic = 7
        "[yoko]'s Theme" if True:
            $ persistent.temusic = 8
        "Dungeon Theme" if True:
            $ persistent.temusic = 9
        "Massage Theme" if True:
            $ persistent.temusic = 10
        "Girls Theme" if True:
            $ persistent.temusic = 11
        "Studio Theme" if True:
            $ persistent.temusic = 12
        "True End Theme" if True:
            $ persistent.temusic = 13
        "Sex Theme" if True:
            $ persistent.temusic = 14
        "Random" if True:
            $ persistent.temusicrandom = 1
    jump trueendscreen

jump trueendscreen

init:
    define persistent.teanal1 = 0
    define persistent.trueendtstage2 = False
    define persistent.trueendtstage1 = False
    define persistent.hole = "pussy"
    define persistent.tebj1 = 0
    define persistent.tebj2 = 0
    define persistent.mc = "Taco"
    define persistent.teanal = 0
    define persistent.tevaginal = 0
    define persistent.tebuttjob = 0
    define persistent.tebuttjob1 = 0
    define persistent.tethreesome = 0
    define persistent.masturbationfingers = 0
    define persistent.masturbationvibe = 0
    define persistent.bjcat = 0
    define persistent.bjbunny = 0
    define persistent.date1 = 0
    define persistent.date2 = 0
    define persistent.date3 = 0
    define persistent.date4 = 0
    define persistent.mcmood = "normal"
    define persistent.tebra = 1
    define persistent.tepanties = 1
    define persistent.cumenergy = 3
    define persistent.temusicrandom = 0
    define persistent.techats = 0
    define persistent.dateready = 0
    define persistent.temusic = 0
    define persistent.tequitdialogue1 = False
    define persistent.tequitdialogue2 = False
    define persistent.tequitdialogue3 = False
    define persistent.telaunchdialogue1 = False
    define persistent.telaunchdialogue2 = False
    define persistent.telaunchdialogue3 = False
    define persistent.telaunchdialogueon = True
    define persistent.trueendstage1 = False
    define persistent.trueendstage2 = False
    define persistent.catlingerie = False
    define persistent.trueendintro = 0
    define persistent.teevolve = 0
    define persistent.rands = 1
    define persistent.randc = 1
    define persistent.rand = 0
    define persistent.chatreset = 0
    define persistent.tepostsex1 = 0
    define persistent.tepostsex2 = 0
    define persistent.telaunchdialogue = 0
    define persistent.tequitdialogue = 0
    define persistent.tereturndialogue = 0
    define persistent.teclothes = 1
    define persistent.tetan = 0
    define persistent.tehair = 0
    define persistent.tepiercings = 0
    define persistent.cum1 = 0
    define persistent.cum2 = 0
    define persistent.cum3 = 0
    define persistent.tewet = 0
    define persistent.affection = 1
    define persistent.virgin2 = "Virgin"
    define persistent.hospitalscare = False
    define persistent.lfscare = False
    define persistent.barscare = False
    define persistent.massagescare = False
    define persistent.tepostchat1 = 0

    define persistent.techat1 = 0
    define persistent.techat2 = 0
    define persistent.techat3 = 0
    define persistent.techat4 = 0
    define persistent.techat5 = 0
    define persistent.techat6 = 0
    define persistent.techat7 = 0
    define persistent.techat8 = 0
    define persistent.techat9 = 0
    define persistent.techat10 = 0
    define persistent.techat11 = 0
    define persistent.techat12 = 0
    define persistent.techat13 = 0
    define persistent.techat14 = 0
    define persistent.techat15 = 0
    define persistent.techat16 = 0
    define persistent.techat17 = 0
    define persistent.techat18 = 0
    define persistent.techat19 = 0
    define persistent.techat20 = 0
    define persistent.techat21 = 0
    define persistent.techat22 = 0
    define persistent.techat23 = 0
    define persistent.techat24 = 0
    define persistent.techat25 = 0
    define persistent.techat26 = 0
    define persistent.techat27 = 0
    define persistent.techat28 = 0
    define persistent.techat29 = 0
    define persistent.techat30 = 0
    define persistent.techat31 = 0
    define persistent.techat32 = 0
    define persistent.techat33 = 0
    define persistent.techat34 = 0
    define persistent.techat35 = 0
    define persistent.techat36 = 0
    define persistent.techat37 = 0
    define persistent.techat38 = 0
    define persistent.techat39 = 0
    define persistent.techat40 = 0
    define persistent.techat41 = 0
    define persistent.techat42 = 0
    define persistent.techat43 = 0
    define persistent.techat44 = 0
    define persistent.techat45 = 0
    define persistent.techat46 = 0
    define persistent.techat47 = 0
    define persistent.techat48 = 0
    define persistent.techat49 = 0
    define persistent.techat50 = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

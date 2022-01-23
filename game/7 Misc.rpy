
label shops:
    scene bg shops
    if morning == 1:
        scene bg shopsday
    call clothes from _call_clothes_70
    show mce happy
    if nude == 1 or lewdoutfit == 1:
        show mce horny
    with d
    if shoppingintro == 0:
        $ shoppingintro = 1
        "Let's do some shopping!"
        "Thanks to modern technological advancements, deliveries are now instant! They just magically warp into my room!"
        "I have no idea how..."
    if nude == 1:
        "Being completely nude, I get so many people looking at me it's ridiculous. It makes me so wet."
    elif lewdoutfit == 1:
        "Wearing a lewd outfit, I get several stares. It's enough to make my panties a little damp."
    menu shoppingmenu:
        "You currently have $[money]."
        "General Store" if True:
            menu:
                "You currently have $[money]. Sexual Desire: [sd], Shame: [shame], Smarts: [smarts]."
                "Pornographic Magazine ($20)" if True:
                    if money < 20:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "A lewd magazine... Well, I get horny too!"
                    if sd < 50:
                        "(If you have less than 50 sexual desire, a pornographic magazine will increase it by 2 points!)"
                    elif True:
                        "(Since you have over 50 sexual desire, the book is a far less effective and will only increase it by 0.5 points."
                    menu:
                        "Buy!" if True:
                            $ money -= 20
                            if sd < 50:
                                "Feeling a little naughty, I buy a pornographic magazine for 'research' purposes."
                                play sound success
                                $ sd += 2
                                "(+2 Sexual Desire)"
                            elif True:
                                "This'll be some fun for later."
                                play sound success
                                $ sd += 0.5
                                "(+0.5 Sexual Desire)"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "'Get Rich Quick' Magazine ($25)" if True:
                    if money < 25:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    if shame < 50:
                        "Hmm... Money making methods... Let's try a few of them!"
                    elif True:
                        "I don't need a magazine for this anymore. I should be out there putting what I know to use."
                        jump shoppingmenu
                    if sd < 50:
                        "(If you have more than 50 Shame, a 'Get Rich Quick' magazine will decrease it by 2 points!)"
                    elif True:
                        "(Since you have over 50 Shame, the 'Get Rich Quick' magazine is a far less effective and will only decrease it by 0.5 points.)"
                    menu:
                        "Buy!" if True:
                            $ money -= 25
                            if shame < 50:
                                "Feeling a little naughty, I buy a pornographic magazine for 'research' purposes."
                                play sound success
                                $ shame -= 2
                                "(-2 Shame)"
                            elif True:
                                "This might give me some ideas later."
                                play sound success
                                $ sd += 0.5
                                "(-0.5 Shame)"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Study Books ($25)" if True:
                    if money < 25:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "A studying book will really help me in class, and when tutoring."
                    if smarts < 50:
                        "(If you have less than 50 smarts, a study book will increase it by 2 points.)"
                    elif True:
                        "(You have over 50 smarts, so the study book will only increase your smarts by 0.5.)"
                    menu:
                        "Buy!" if True:
                            $ money -= 25
                            if smarts < 50:
                                "Ohh, this is perfect, it's full of stuff my class hasn't even covered yet."
                                play sound success
                                $ smarts += 2
                                "(+2 Smarts)"
                            elif True:
                                "I know most of what's in here, but it never hurts to revise."
                                play sound success
                                $ smarts = 0.5
                                "(+0.5 Smarts)"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Pregnancy Test ($10)" if True:
                    if money < 10:
                        "Hmm... I don't have enough money for that. Considering it only costs $5, that kinda sucks."
                        jump shoppingmenu
                    "(This'll instantly confirm whether you're pregnant or not, and even tell you how far along you are.)"
                    menu:
                        "Buy!" if True:
                            "This special test only needs some DNA from my tongue... So let's see here."
                            $ money -= 10
                            "Okay, let's see here..."
                            if pregnant == 1:
                                "Pregnant: Yes, Days Pregnant: [pregnancyterm]/240."
                            elif True:
                                "Pregnant: No, Days Pregnant: 0."
                            if pregnant == 1 and pregnancyshowing == 0:
                                "W-Woah, I'm pregnant!"
                            elif True:
                                "Ahh, nothing surprising."
                        "Nah..." if True:
                            jump shoppingmenu
                "Pepper Spray ($50)" if pepperspray == 0:
                    if money < 50:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "(Permanently prevents perverts from groping you in public.)"
                    menu:
                        "Buy!" if True:
                            $ money -= 50
                            $ pepperspray = 1
                            "Perfect, I can't believe just how perverted this city was."
                            "(You can turn Pepper Spray on/off from the bedroom's inventory menu.)"
                            "(Would you like to turn pepper spray on now?)"
                            menu:
                                "Pepper Spray On" if True:
                                    $ peppersprayon = 1
                                "Pepper Spray Off" if True:
                                    $ peppersprayon = 0
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Back" if True:
                    jump shoppingmenu
        "Pharmaceuticals" if True:
            menu:
                "You currently have $[money]."
                "Female Condoms ($5 each)" if True:
                    if money < 5:
                        "Hmm... I don't have enough money for that. Considering it only costs $4, that's a really sad state of affairs..."
                    elif pregnant == 1:
                        "I'm already pregnant, so I don't need these anymore..."
                        jump shoppingmenu
                    if sd < 10:
                        "Condoms, huh? I-I guess I am that age now... I should have some, just in case."
                    elif True:
                        "I'll definitely need these if I'm going to get through college."
                    "(Condoms can be used before certain sex scenes to prevent you from getting pregnant.)"
                    "(They're one use, but multiple can be bought at once.)"
                    "(Oh, and these are female condoms! That means we can still have messy 'creampies', hooray! (Except sex scenes with your [crush], he has male condoms.))"
                    menu condommenu:
                        "Buy 1 ($5)" if True:
                            if money < 5:
                                "Ah, whoops. I don't have that much money. That's right, I don't even have $4. Sadge."
                                jump condommenu
                            $ money -= 5
                            $ condoms += 1
                        "Buy 3 ($15)" if True:
                            if money < 15:
                                "Ah, whoops. I don't have that much money."
                                jump condommenu
                            $ money -= 15
                            $ condoms += 3
                        "Buy 6 ($30)" if True:
                            if money < 30:
                                "Ah, whoops. I don't have that much money."
                                jump condommenu
                            $ money -= 30
                            $ condoms += 6
                        "Nah..." if True:
                            jump shoppingmenu
                    if sd < 20:
                        "Just in case, right...?"
                    elif True:
                        "Better safe than sorry!"
                    jump shoppingmenu
                "The Pill ($40)" if True:
                    if money < 40:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    elif pregnant == 1:
                        "I'm already pregnant, so I don't need these anymore..."
                        jump shoppingmenu
                    "(Once bought, the pill will prevent you from getting pregnant. You can revert this at any time in the inventory. It doesn't stop you from being pregnant if you've already been impregnated, though.)"
                    menu:
                        "Buy!" if True:
                            $ money -= 40
                            "Just in case, right? I hear they help regulate periods too."
                            "(You are now on the pill.)"
                            $ onpill = 1
                            $ pill = 1
                        "Nah..." if True:
                            jump shoppingmenu
                "Fertility+ ($50)" if True:
                    if money < 50:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "(Using Fertility+ gives you an extremely high chance to get pregnant for the entire day!)"
                    "(The effects are so strong, it bypasses the pill, but it won't bypass a condom."
                    menu:
                        "Buy!" if True:
                            $ money -= 50
                            "Huh? Why am I buying this?"
                            $ fertilityplus += 1
                        "Nah..." if True:
                            jump shoppingmenu
                "Aphrodisiac ($60)" if True:
                    if money < 60:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    if shame > 75:
                        "Why would I buy something like this?"
                    elif True:
                        "It's expensive, but I imagine this'll make earning money easier..."
                    "(Aphrodisiac is a single-use item that can be used to temporarily increase sexual desire by 20 points while lowering shame by 10 for the evening.)"

                    menu:
                        "Buy!" if True:
                            $ money -= 60
                            $ aphrodisiac += 1
                            if shame > 75:
                                "Pfft... I feel stupid buying this..."
                            elif True:
                                "This is gonna be good."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Plan C ($30)" if True:
                    if money < 30:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    if pregnancyshowing == 1:
                        "I'm already super pregnant. I'd need a Plan Z at this point."
                        jump shoppingmenu
                    "(Plan C can be used to prevent pregnancies within the first five days of being inseminated.)"
                    "(If you're not pregnant, or the egg has already been fertilized, this pill does nothing.)"
                    menu:
                        "Buy!" if True:
                            $ money -= 30
                            if pregnant == 1 and pregnancyterm <= 5:
                                $ pregnant = 0
                                $ pregnancyterm = 0
                            "I swallow the pill. Better to be safer than sorry."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Back" if True:
                    jump shoppingmenu
        "Beauty Store" if True:
            menu:
                "You currently have $[money]."
                "Hair Makeover ($50)" if True:
                    if money < 50:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    menu:
                        "(Sexual Desire: [sd], Shame: [shame])"
                        "Blonde Bimbo Style (30 Sexual Desire)" if hair == 0 or hair == 1:
                            if sd < 30:
                                "Blonde is a bit too extreme for me, I think!"
                                jump shoppingmenu
                            $ money -= 50
                            scene bg black with d
                            play sound success
                            $ hair = 2
                            scene bg shops
                            if morning == 1:
                                scene bg shopsday
                            call clothes from _call_clothes_71
                            show mce happy2
                            with d
                            "Wow, I'll definitely reel in the guys looking like this!"
                            jump shoppingmenu
                        "Goth GF Style (<70 Shame)" if hair == 2 or hair == 0:
                            if shame > 70:
                                "Black hair? Aren't I a little old for a goth phase?"
                                jump shoppingmenu
                            $ money -= 50
                            scene bg black with d
                            $ hair = 1
                            scene bg shops
                            if morning == 1:
                                scene bg shopsday
                            call clothes from _call_clothes_72
                            show mce happy2
                            with d
                            "I look totally cool."
                            jump shoppingmenu
                        "Brunette Beauty (Default)" if hair == 2 or hair == 1:
                            $ money -= 50
                            scene bg black with d
                            $ hair = 0
                            scene bg shops
                            if morning == 1:
                                scene bg shopsday
                            call clothes from _call_clothes_73
                            show mce happy2
                            with d
                            "I feel myself again!"
                            jump shoppingmenu
                        "Back" if True:
                            jump shoppingmenu
                "Fake Tan ($15)" if True:
                    if money < 15:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    menu:
                        "A fake tan will last two weeks, twice as long as a natural tan."
                        "Yes" if True:
                            $ tan = 1
                            $ tantime += 14
                            $ money -= 15
                            scene bg black with dissolve
                            play sound success
                            scene bg massage
                            call clothesbeach from _call_clothesbeach_23
                            show mce happy
                            with dissolve
                            pause 0.1
                            scene bg black with dissolve
                            scene bg shops
                            if morning == 1:
                                scene bg shopsday
                            call clothes from _call_clothes_74
                            show mce laughing
                            with d
                            "Heheh, sexy!"
                            jump shoppingmenu
                        "Back" if True:
                            jump shoppingmenu
                "Nipple Piercings ($75) (40 Sexual Desire, <80 Shame)" if piercings == 0:
                    if money < 75:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    elif sd < 40 or shame > 80:
                        "Nipple piercings? Why would I ever get those?"
                        jump shoppingmenu
                    $ piercings = 1
                    $ piercingson = 1
                    $ money -= 75
                    scene bg black with dissolve
                    play sound success
                    scene bg massage
                    call clothesnude from _call_clothesnude_28
                    show mce happy
                    with dissolve
                    pause 0.1
                    scene bg black with dissolve
                    scene bg shops
                    if morning == 1:
                        scene bg shopsday
                    call clothes from _call_clothes_75
                    show mce laughing
                    with d
                    "Heheh, sexy!"
                    jump shoppingmenu
                "Back" if True:
                    jump shoppingmenu
        "Clothing Store" if True:
            menu:
                "You currently have $[money]."
                "Cat Ears ($50)" if catears == 0:
                    if money < 50:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "These are cute, if not a little embarrassing to wear!"
                    menu:
                        "Buy!" if True:
                            $ catears = 1
                            $ money -= 50
                            "Hehe, I'm not wearing these to college!"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Camisole Lingerie ($200)" if cami == 0:
                    if money < 200:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "This is cute! A little expensive though..."
                    menu:
                        "Buy!" if True:
                            $ cami = 1
                            $ money -= 200
                            "Alright! Only question is, who's going to see it first?"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Swimsuit ($200)" if swimsuit == 0:
                    if money < 200:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "This is cute! A little expensive though..."
                    menu:
                        "Buy!" if True:
                            $ swimsuit = 1
                            $ money -= 200
                            "Alright! Time to visit the beach and swimming pool."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Bunny Suit ($500)" if bs == 0:
                    if money < 500:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "Wow! This would get me some tips at the bar."
                    menu:
                        "Buy!" if True:
                            $ bs = 1
                            $ money -= 500
                            "Phew, will I have the courage to wear something like this?"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Cat Keyhole Lingerie ($1000)" if cgl == 0:
                    if money < 1000:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "So lewd, yet cute! I honestly wouldn't mind having this for myself."
                    menu:
                        "Buy!" if True:
                            $ cgl = 1
                            $ money -= 1000
                            "So expensive... I wonder if I could get some money back selling photos?"
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Back" if True:
                    jump shoppingmenu
        "Sex Toy Store" if True:
            menu:
                "You currently have $[money]."
                "Vibrator ($50)" if vibrator == 0:
                    if money < 50:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "Seems like a fun toy to make my nights more 'eventful', hehe."
                    menu:
                        "Buy!" if True:
                            $ vibrator = 1
                            $ money -= 50
                            "A little pricy, but imagine the stress relief."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Dildo ($200)" if dildo == 0:
                    if money < 200:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "Gulp, the thought of owning something like this is rather arousing."
                    menu:
                        "Buy!" if True:
                            $ dildo = 1
                            $ money -= 200
                            "For this price, I best get some use out of it."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Jewelled Buttplug ($300)" if plug == 0:
                    if money < 300:
                        "Hmm... I don't have enough money for that."
                        jump shoppingmenu
                    "Gulp, the thought of owning something like this is rather arousing."
                    menu:
                        "Buy!" if True:
                            $ plug = 1
                            $ money -= 300
                            "It's so cuuute! I'll definitely be getting some use out of this."
                            jump shoppingmenu
                        "Nah..." if True:
                            jump shoppingmenu
                "Back" if True:
                    jump shoppingmenu
        "(Smooth Operator) Steal Attempt (Once Per Day)" if personality == 3 and gssa == 0:
            $ gssa = 1
            "I wait for a calm opportunity to steal something from the general store..."
            "Not one to risk getting caught, I play it cool and open myself to the opportunity of not taking anything at all."
            $ rand = renpy.random.randint(1,5)
            if rand == 1 or rand == 2:
                show mce happy2 with d
                play sound success
                "I manage to steal a porno mag!"
                $ sdgain = 2
                call sdgain from _call_sdgain_50
                "(Sexual Desire +2!)"
            elif rand == 3:
                show mce happy2 with d
                "I snagged a study book!"
                play sound success
                $ smartsgain = 2
                call smartsgain from _call_smartsgain_3
                "(Smarts +2!)"
            elif True:
                show mce neutral with d
                "With no clear opportunity, I end up leaving after a while to avoid suspicion."
                play sound success
                $ shameloss = 1
                call shameloss from _call_shameloss_28
                "(-1 Shame)"
                jump shoppingmenu
        "Back" if True:
            jump worldmap2
jump shoppingmenu



label clubbing:
    stop music fadeout 1.0
    scene bg black with d
    "Accepting [susu]'s proposition, I wait at home until night before meeting with her at a bar."
    play music club
    scene bg bar with d
    call clothesclub from _call_clothesclub_1
    show mce happy
    show susub:
        xpos 1200
    show susuo uniform:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "We start at the college bar because the drinks are cheaper."
    if pregnancyshowing == 1:
        "Although, since I'm pregnant I won't be having any alcoholic drinks."
    menu:
        "Order a soft drink." if True:
            "I start with a soft drink. [susu] orders alcohol."
        "Order an alcoholic drink. (+5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ sd += 5
            $ shame -= 5
            play sound alcohol
            "I start with an alcoholic drink. It gives me a slight buzz."
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
                "(Lightweight) Due to being a lightweight, you feel the effects twice as much!"
            $ drunk += 1
    scene bg bar2 with d
    call clothesclub from _call_clothesclub_2
    show mce happy
    show susub:
        xpos 1200
    show susuo uniform:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "Going to a cocktail bar, [susu] and I chat about trivial things as we order another drink."
    menu:
        "Order a soft drink." if True:
            "The drinks do seem quite expensive here... Let's just buy a soft drink."
        "Order a cocktail. (+5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ sd += 5
            $ shame -= 5
            play sound alcohol
            "[susu] and I go two for one on a cocktail, saving me some money."
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
                "(Lightweight) Due to being a lightweight, you feel the effects twice as much!"
            $ drunk += 1
            if drunk == 2:
                "I'm starting to feel tipsy; it feels good."
            elif True:
                "The cocktail gives me a slight buzz."
    scene bg black with d
    scene bg club with d
    call clothesclub from _call_clothesclub_3
    show mce happy
    show susub:
        xpos 1200
    show susuo uniform:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "Final stop of the night, the nightclub itself!"
    menu:
        "Just go and dance already!" if True:
            pass
        "Order a shot. (+5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ sd += 5
            $ shame -= 5
            play sound alcohol
            "One last chance to buy booze. Not wanting to waste this opportunity, I buy something strong."
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
                "(Lightweight) Due to being a lightweight, you feel the effects twice as much!"
            $ drunk += 1
            if drunk == 3:
                "I'm totally drunk now. Even walking is a challenge. But it feels great!"
            elif drunk == 2:
                "I'm starting to feel tipsy; it feels good."
            elif True:
                "The drink gives me a slight buzz."
    scene bg black with d
    scene bg club with d
    call clothesclub from _call_clothesclub_4
    show mce happy
    show susub:
        xpos 1200
    show susuo uniform:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "[susu] and I dance at the nightclub."
    "It doesn't take too long for a male student we recognize from another class joins us."
    show student3 with d:
        xpos 50
    show mce laughing
    "Sheesh! He's kind of a hunk."
    "And [susu] seems particularly 'interested' in this student."
    if sd > 40:
        "And I'm horny enough to be interested too..."
    elif drunk == 2 and sd > 15:
        "And I'm just drunk and horny enough to be kinda interested too..."
    elif drunk == 3:
        "And three drinks in, my inhibitions are just low enough that I'm totally interested too..."
    if personality == 2 and sd > 15:
        "(Always Horny) Mmphh... I should do something to him."
    menu clubmenu:
        "Sexual Desire: [sd], Shame: [shame]"
        "Just dance!" if True:
            if personality ==2 and sd > 15:
                "(Always Horny) I'm not giving up this opportunity."
                jump clubmenu
            show mce sad
            "[susu] talks a lot with the male student, and eventually they start making out right infront of me."
            "It doesn't go any further than that."
            show mce happy
            hide student3 with d
            if drunk > 1 or sd > 10:
                "But a part of me was aroused watching."
                play sound success
                $ sdgain = 1
                call sdgain from _call_sdgain_82
                "(+[fsd] Sexual Desire!)"
        "Flirt with the student. (Sexual Desire 15)" if True:
            if sd < 15:
                "Aahh... I guess I'm not that interested."
                jump clubmenu
            scene bg club
            show susub:
                xpos 1200
            show susuo uniform:
                xpos 1200
            show susue happy:
                xpos 1200
            with d
            "The student and I flirt back and forth multiple times. Eventually we end up making out right infront of [susu]."
            call clothesclub from _call_clothesclub_5
            show mce horny
            with d
            $ groped += 1
            "I think he even grabbed my butt. My panties definitely got a little wet after that."
            play sound success
            $ sdgain = 2
            $ kisses += 1
            call sdgain from _call_sdgain_83
            "(+[fsd] Sexual Desire!)"
        "Give him a blowjob in a bathroom stall. (Sexual Desire 65, Shame <70)" if True:
            if sd < 65 or shame > 70:
                "A most degenerate thought crosses my mind, but it's a thought no less... I'd never do anything like that."
                jump clubmenu
            show mce happy with d
            "Yep, I'm gonna do it."
            "I want him all to myself, and I want him now."
            "Whispering into his ear, I manage to convince him to come with me."
            hide susu with d
            "Subtly too, [susu] just thinks we're both going to separate toilets, she doesn't suspect a thing."
            "In one of the most daring moves of my life I go into the men's bathroom with him."
            scene bg toilets with d
            "It's not empty... But fortunately my hunk and I successfully slip into the closest toilet stall before I get the attention of more than one guy."
            show bg toiletstall with d
            "The toilet stall locks with a clunk, and I feel my courage build up as I turn towards my partner."
            show student3 with d
            "I gulp momentarily before getting on my knees and getting to work. I'm eager, and the daring situation is making my heart race."
            "I unbuckle his belt and take out his delicious cock, it's everything I'd imagined it'd be and more."
            hide student3
            show povblowjobb
            if tan == 1:
                show povblowjobbtan
            if piercingson == 1:
                show povblowjobpiercings
            if hair == 1:
                show povblowjobh black
            if hair == 2:
                show povblowjobh blonde
            show povblowjob 1
            with d
            play ambience blowjob
            "Wasting no time, I pull back the foreskin and wrap my tongue around its tip."
            "I allow its taste, smell and feel to overwhelm my senses as I fully indulge in this slutty and depraved act with a lustful pride."
            mc "Mmphhh... Your cock is so biiggg..."
            "Causing my lover to stifle a laugh, he jokingly tells me off for making too much noise. In reality, no one would be able to hear me over the music."
            "The stud strokes my hair as I take his cock deeper while swirling my tongue around his sensitive glans."
            "In my horny stupor, the hand I'm not jacking him off with finds itself unbuttoning my jeans and rubbing my damp panties."
            "The pleasure I feel from just unfocused rubbing is electrifying, showing just how aroused I am right now."
            "I muffle a few moans into the blowjob as I increase my effort."
            "The combination of my hand, mouth and tongue should be able to get him off quickly, and while I do want to savour the moment, I'm equally as eager to guzzle on his hot cum."
            "It doesn't take long for his cock to begin to throb and swell up, ejaculation was imminent, so I took his cock deeper and deeper."
            "Almost deepthroating him on occasion, I fuck his cock with my mouth, creating the most lecherous, sloppy wet noises possible."
            play sound cum
            show povblowjob 2 with cum
            play sound cum
            show povblowjob 2 with cum
            "The orgasm came quick and strong, taking me by surprise. Immediately, several loads of thick cum coated the back at my throat."
            play sound cum
            show povblowjob 2 with cum
            play sound cum
            show povblowjob 2 with cum
            stop ambience fadeout 3.0
            "It was an excessive amount, and since it caught me off guard a lot of it spilled out from my mouth and in one instance where I pull back, I get several loads on my face."
            "I swallow each drop that I'm able. It doesn't taste great, but the pure erotic stimulation literally makes me climax as I finally rub myself off just as he finishes."
            scene bg toiletstall with d
            show student3
            with d
            "Pulling his deflating cock away, he hoists it back into his pants and does his belt back up as I sheepishly peer at him from below with a face covered in cum."
            stu "You best get yourself cleaned up before you go back out."
            "He pats my head one last time before... he leaves! He's just leaving me in here!"
            hide student3 with d
            "Unlocking the stall door, he walks out causing me to panic and quickly lock it again to the confusion of another dude outside the stall."
            scene bg toilets with d
            "I spend a few moments using toilet paper to wipe the semen off my face before I head back out through the male's bathroom, under some all-to-knowing gazes."
            scene bg club with d
            "I feel like such a slut."
            "And it feels great..."
            play sound success
            $ sdgain = 2
            call sdgain from _call_sdgain_84
            $ shameloss = 1
            call shameloss from _call_shameloss_59
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
            if qsecretlydepraved == 1:
                "The enjoyment of the depraved act causes you to gain an additional [fsd] sexual desire!"
                call sdgain from _call_sdgain_85
            $ blowjobs += 1
        "Orchestrate a threesome. (Sexual Desire 100, Shame <75)" if True:
            if sd < 100 or shame > 75:
                "If we're both interested, maybe we could... Ah, no, no... Too perverted of an idea."
                jump clubmenu
            $ event3complete = 1
            "There's no way I'd be able to bring him to my place without [susu] knowing, we live on the same corridor!"
            "And there's always 'bros before hoes'... Or sisters in this case?"
            "But what about bros and hoes? I think there's a way for both [susu] and I to get something out of this."
            show mce happy with d
            mc "Psst, [susu]... Wanna bring him over to the dorms?"
            susu "Both of us? At the same time?"
            mc "Yeah, how about it?"
            susu "Hehe, you're outrageous, [mc]... Okay, let's do it!"
            scene bg black with d
            "Through expert seduction tactics..."
            "Such as, 'simply asking if he wants a threesome', we manage to get him to [susu]'s dorm."
            scene bg bedroomnight with d
            play music action fadein 3.0
            call clothesnude from _call_clothesnude_29
            show mce happy
            show susub:
                xpos 1200
            show susuo uniform:
                xpos 1200
            show susue happy:
                xpos 1200
            show student3:
                xpos 50
            with d
            "Well, that was easy."
            scene bg bed
            show ffmthreesomeb
            if tan == 1:
                show ffmthreesomebtan
            if hair == 1:
                show ffmthreesomeh black
            if hair == 2:
                show ffmthreesomeh blonde
            show ffmthreesome 1
            with d
            "Both completetly nude, [susu] and I take control of the situation to tease and toy with the boy."
            susu "Ohh, you're dripping wet, [mc]! So naughty!"
            mc "Ahhh, I think I'm ready for your big cock! Fuck me hard!"
            $ condomon = 0
            if pregnancyshowing == 0:
                if condoms > 0:
                    menu:
                        "Condoms: [condoms]. [fertilityrate]."
                        "Wear a condom" if True:
                            $ condomon = 1
                            $ condoms -= 1
                        "Bareback!" if True:
                            $ condomon = 0
            play sound cum
            show ffmthreesome 2
            with d
            play ambience sex fadein 3.0
            "Without messing around, he brings the tip of his cock to my pussy and slowly slides inside. It's so thick that mere penetration causes me to shiver and moan loudly."
            if virgin == 0:
                call virgin from _call_virgin_1
            "With his hands on my hips, he begins vigorously fucking me as his cock throbs and my pussy clenches."
            "I absolutely needed this, there's something fantastical about finally having sex after a long buildup; I've been aroused and anticipating this ever since we were in the club."
            mc "Aahhh, yesss! Mmmmhh..."
            susu "Ooohhh, you're really filling her up! I can see her lips tightly gripping around your shaft."
            "The thrusts start to come faster, and in my enthusiasm I try to match the thrusts by bouncing my butt against him. This results in hard, deep thrusts that pleasure every inch of my insides."
            "At this speed I'm really starting to get pushed over the edge, my muscles tense up and my pussy tightens as my orgasm rises."
            mc "Aaahhh, f-fuuuckk! I-I'm gonna come!"
            susu "Oohh, yesss... Cum inside her, fill her pussy up!"
            "He starts to fuck my pussy as fast as he can, easily pushing me to a climax as he barrels towards his."
            mc "Y-Yes! I'm coming! Ahhh, aahhh"
            play sound cum
            show ffmthreesome 3 with cum
            play sound cum
            show ffmthreesome 3 with cum
            "Almost immediately as I moan, I feel a load shooting deep inside my pussy. The thick, hot cum seeps throughout me as we continue to fuck each other intensely."
            play sound cum
            show ffmthreesome 3 with cum
            play sound cum
            show ffmthreesome 3 with cum
            stop ambience fadeout 3.0
            "After a few more loads of cum, the euphoria dissipates and we come to a stop."
            mc "*Pant, pant* That was so good, haaahh..."
            show ffmthreesome 4 with d
            "Pulling out, cum freely drips from my pussy."
            susu "Ooohhh, so lewd, so naughty!"
            susu "My turn next, right? Hehe."
            scene bg black with d
            play sound success
            if condomon == 0:
                call pregnancyroll from _call_pregnancyroll_3
            $ sdgain = 2
            call sdgain from _call_sdgain_86
            $ shameloss = 1
            call shameloss from _call_shameloss_60
            $ status += 2
            $ vaginalsexes += 1
            $ groupsexes += 1
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            jump genericsleep
label postclub:
    stop music fadeout 1.0
    scene bg black with d
    scene bg bedroomnight with d
    "Eventually, at some arbitary, absurdly late time, I find myself stumbling back into my room."
    if drunk > 2:
        $ masturbations += 1
        scene masturbationb
        if tan == 1:
            show masturbationbtan
            if pregnancyshowing == 1:
                show masturbationbtanp
        if hair == 1:
            show masturbationh black
        if hair == 2:
            show masturbationh blonde
        if piercingson == 1:
            show masturbationpiercings
        show masturbation 1b
        if pregnancyshowing == 1:
            show masturbatione pregnant
        with d
        "Feeling very aroused, I end up masturbating before sleeping."
        "Dirty thoughts of hooksups and one-night stands swirling through my drunken head."
        if sd < 20:
            "Of course... I'd never do that... I'm just masturbating at the idea of it, right?"
        elif sd < 40:
            "I imagine what it'd be like having that male student railing me at this very moment."
        elif True:
            "I should have fucked that guy when I had the chance. Next time I won't let him escape."
        play sound cum
        show masturbation 1b with cum
        play sound cum
        show masturbation 1b with cum
        "One strong orgasm later, and I practically fall asleep immediately."
    scene bg black with d
    jump morning
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

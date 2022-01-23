label endings:
    if endingsunlocked == 0 and endingoverride == 0:
        show mce neutral with d
        "*Ah choo!*"
        show mce laughing with d
        "Phew, sorry!"
        show mce happy with d
        jump maptobedroom
    elif True:
        label endingm:
            if vie == 1 and lge == 1 and yge == 1 and de == 1 and yye == 1 and ege == 1 and dae == 1 and sae == 1 and pe == 1 and sge == 1:
                $ endingsseen = 11
            stop ambience fadeout 1.0
            play music ending
            scene bg crystalball
        menu unseenendings:
            "Virgin Ending (Pay off your Tuition)" if vie == 0:
                if tuition > 0 and endingoverride == 0:
                    "I still have $[tuition] remaining."
                    jump unseenendings
                $ endingsseen += 1
                jump virginending
            "Loyal Girlfriend Ending (Reach 6 [crush] Affection)" if lge == 0:
                if ca < 5 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump loyalgirlfriendending
            "[yomo]'s Girlfriend Ending (Complete [yomo]'s Route)" if yge == 0:
                if yomoroutecomplete == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump yomogfending
            "Dominatrix Ending (Complete the Dungeon Route)" if de == 0:
                if dungeonroute3 == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump dominatrixending
            "Yandere Ending (Complete [yoko]'s Route)" if yye == 0:
                if yokosex4 == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump yokoending
            "E-Girl Empress Ending (Complete LonelyFans, ChatFap and Reach 2,000 Followers)" if ege == 0:
                if endingoverride == 1:
                    $ endingsseen += 1
                    jump egirlending
                elif fol < 2000 or lonelyfans21 == 0 or chatfaproute6 == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump egirlending
            "Professional Masseuse (Complete the Massage Parlour)" if mpe == 0:
                if massageroute5 == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump massageparlourending
            "Drug Addict Ending (Complete the Studio Route)" if dae == 0:
                if studioroute5 == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump drugaddictending
            "Sex Addict Ending (Reach 200 Sexual Desire)" if sae == 0:
                if sd < 200 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump sexaddictending
            "Prostitute Ending (Sell Sex in Every Location)" if pe == 0:
                if endingoverride == 1:
                    $ endingsseen += 1
                    jump prostituteending
                elif clubsex == 0 or mdsex == 0 or gloryholesex == 0:
                    if clubsex == 0:
                        "I still need to sell sex at the clubs."
                    if mdsex == 0:
                        "I still need to sell sex at the male dorms."
                    if gloryholesex == 0:
                        "I still need to sell sex at the gloryholes."
                    jump unseenendings
                $ endingsseen += 1
                jump prostituteending
            "Slime Girl (Adopt Mr. Slime)" if sge == 0:
                if mrslime == 0 and endingoverride == 0:
                    "I haven't unlocked this ending."
                    jump unseenendings
                $ endingsseen += 1
                jump slimegirlending
            "{size=+25}{k=2.5}{color=#8ac4ff}{b}True Ending{/b}{/color}{/k}{/size}" if endingsseen == 11 and persistent.trueendstage1 == False or endingoverride == 1 and persistent.trueendstage1 == False:
                menu btem:
                    "Warning, beginning this ending will cause you to lose unsaved progress."
                    "Save" if True:
                        call screen save
                        jump btem
                    "Continue" if True:
                        jump trueending
                    "Back" if True:
                        jump endingm
            "View Seen Endings" if True:
                jump seenendings
            "Back" if True:
                jump maptobedroom
        jump endingm
        menu seenendings:
            "Virgin Ending" if vie == 1:
                jump virginending
            "Loyal Girlfriend Ending" if lge == 1:
                jump loyalgirlfriendending
            "[yomo]'s Girlfriend Ending" if yge == 1:
                jump yomogfending
            "Dominatrix Ending" if de == 1:
                jump dominatrixending
            "Yandere Ending" if yye == 1:
                jump yokoending
            "E-Girl Empress Ending" if ege == 1:
                jump egirlending
            "Professional Masseuse" if mpe == 1:
                jump massageparlourending
            "Drug Addict Ending" if dae == 1:
                jump drugaddictending
            "Sex Addict Ending" if sae == 1:
                jump sexaddictending
            "Prostitute Ending" if pe == 1:
                jump prostituteending
            "Slime Girl" if sge == 1:
                jump slimegirlending
            "Back" if True:
                jump unseenendings

label drugaddictending:
    $ dae = 1
    stop music fadeout 1.0
    scene bg black with d
    "A few days later…"
    play music intro
    show bg bedroomday
    call clothes from _call_clothes_110
    show mce neutral
    with d
    "Hmm… Where shall I go today?"
    "I know I have college, but… I itch my arm slightly. I can’t help but think about visiting the Studio again."
    "It sounds strange, but I’ve been thinking a lot about taking some of the stuff they’ve got there. The drugs…"
    "I know they’re bad, however, I’ve only taken it once. It’s not like I’m an addict."
    "It’ll be fine. I’ll go there, take something light, have a laugh and earn some money filming a video."
    "What’s the worst that could happen?"
    stop music
    play sound glasssmash
    show brokenglass
    pause(0.5)
    "Three years later…"
    scene bg black with dissolve
    play music toko
    scene bg studio
    show black:
        alpha 0.5
    with dissolve
    show stranger1:
        xpos 1200
    with dissolve
    dire "Tch, your shitty videos aren’t making enough money anymore."
    show mc tan
    show mco bar2
    show mch blonde
    show mce neutral
    with dissolve
    mc "You can’t blame me for this. No one could have predicted that our dealer would get arrested by a pro hero."
    dire "Fucking hell. Did you at least get some money from that freak you sucked dry?"
    mc "Yeah, he paid $50, b-but, I only want to be with you, babe…"
    dire "$50? Fucking hell… What about the other customer?"
    mc "He cancelled on me… I’m sorry, babe…"
    dire "Great, so we’ve got $50. That won’t cover our rent, let alone the blow you snort in a day."
    show mce sad with d
    mc "I’m sorry! I-I’ll go figure something out."
    dire "Whatever, you know how much money you need to make. I don't even know why you'd bother showing up without it."
    dire "Go out and get another $100. Last chance, you either bring the dough or you fuck off, I can’t afford to support a deadweight whore."
    mc "Right, understood, I’ll come back with the money right away, babe."
    scene bg black with dissolve
    play ambience rain
    show bg shops
    show rain1:
        alpha 0
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0
        repeat
    show rain2:
        alpha 0.5
        linear 0.5 alpha 0
        linear 0.5 alpha 0.5
        repeat
    with dissolve
    show mc tan
    show mco bar2
    show mch blonde
    show mce sad
    with dissolve
    "I hurry out of the run-down studio and quickly pull my phone out."
    "Fuck… I can’t let him down, not again… He’s relying on me to earn money. Why is it always about money? Damnit."
    "I’m so stupid, what do I do? …"
    "Guess, my pimp, ‘Guru’ is my only option."
    scene bg black with d
    play ambience rain volume 0.2
    play music toko volume 0.3
    scene bg booth
    show stranger2:
        xpos 1200
    with d
    guru "You know I can’t just give you money because you’re in a tight spot, girl."
    show mc tan
    show mco bar2
    show mch blonde
    show mce neutral
    with d
    mc "I-I know, so…"
    guru "Heh, so you’re looking to earn it, hm?"
    show mce horny with d
    mc "That’s right. A-Are you interested?"
    "He’s just my pimp, it doesn’t matter if I fuck him… Babe’s the only one for me."
    guru "Well, I ain’t never fucked and paid you like this before, but I can make an exception."
    show mce happy2 with d
    "He takes out two $50 notes. An already high bar for what I typically earn with a client."
    guru "Or, alternatively…"
    show mce neutral with d
    "He takes out a bag of blue, easily around $80, and I freeze up, goosebumps forming all over my body as my mouth salivates slightly."
    mc "H-Huh? Blue…"
    guru "Up to you, [mc]. How’d you rather get paid? You need the money, or the drugs?"
    "Come on, [mc]… The $100 will pay your half of this month’s rent immediately…"
    "But… Just as my hand is over the cash, I waver…"
    play sound glasssmash
    show brokenglass
    stop music
    stop ambience
    play sound2 foreplay2
    play ambience sex
    scene addictendb
    show addictend 2
    show blue:
        alpha 0.1
        linear 2 alpha 0.2
        linear 2 alpha 0.1
        repeat
    "A euphoric blue glaze clouds my eyes as my head swirls in endless clouds."
    mc "Oohhhh, you two! Y-Yes! Hoooh!"
    "Both Guru and his bodyguard were utterly toying with me. Both my ass and pussy filled and pounded relentlessly. But the blue had left my body so numb it barely mattered."
    "My own hips spasmed as they rocked back and forth. Both my holes squeezing and clenching in response to the rigorous bouncing of cocks."
    "All these sensations are overwhelming. I feel like a puddle of pure pleasure. Beyond ecstasy."
    guru "God damn, she still has the best pussy of my whores, no matter how much she gets fucked."
    mc "Guhhh, hoooohhh… So-sooo biig…. Aaahh, ohhh…"
    "Their cocks were as hard as could be, and my pussy and ass were only made tighter by the position and double penetration."
    "And at their consistent, pounding pace, I was easily sent over the edge. My insides constricting in rhythmical waves, tightening around the bases of their cocks, squeezing and sucking."
    "My entire body reacts with elation, my hips desperately moving back and forth to derive as much pleasure as possible."
    guru "You sure you should be taking the drugs? You’ll never save up money if you keep blowing it like this."
    show addictend 2b with d
    mc "Mmphh, mm… *Gulp* Aahahh, y-yeah… This is amazing!"
    "Their thrusting accelerates, and soon the sound of wet bodies smacking into each other echoes throughout the room. That combined with the lewdest wet noises from our point of contact spurs us on even more."
    show addictend 2 with d
    mc "Aahh, ohhh… I’m gonna cum again!"
    guard "Damn, this bitch really goes wild when she’s high."
    guru "She’s a pain in the ass because she’s a complete addict, but yeah, she’s probably the best fuck we have."
    "Their admonishing is almost like dirty talk to me. I’ve become such a degenerate that the simple acknowledgement that I’m a drug-addled failure is enough to get me off."
    "And within moments I’m coming again, my pussy and ass squeezing tightly around their throbbing cocks, which are both on the precipice of cumming."
    play sound cum
    show addictend 3 with cum
    play sound cum
    show addictend 3 with cum
    "Cum explodes from their tips as they fervently piston in and out my holes."
    play sound cum
    show addictend 3 with cum
    play sound cum
    show addictend 3 with cum
    "This orgasm hits even harder than the last, causing me to shiver and moan as my insides are pumped full of semen."
    stop ambience fadeout 1.0
    stop sound2 fadeout 1.0
    play sound cum
    show addictend 4 with d
    "As they come down, I’m still shaking from my orgasmic and drugged high. They pull out and leave me to recompose on the bed."
    show black:
        alpha 0.1
        linear 2 alpha 0.2
        linear 2 alpha 0.1
        repeat
    with d
    mc "Aaahh, haaahhh… *Pant, pant*…"
    guru "You have five minutes, then I want you out."
    mc "Yeahh… Haahhh… Thanks…"
    play ambience rain volume 0.1
    scene bg booth
    show mc tan
    show mch blonde
    show mce neutral
    show blue:
        alpha 0.1
        linear 2 alpha 0.2
        linear 2 alpha 0.1
        repeat
    with d
    "A few minutes after they leave, I uneasily stand back up."
    "Fuck… What do I do? I really needed that hit, it’s been days since my last, but… Babe told me not to come back without money."
    "Aahh, but I still have more blue in my bag. Maybe if he sees this, he’ll change his mind?"
    scene bg black with dissolve
    scene bg studio
    show black:
        alpha 0.5
    with dissolve
    "I return to the worn-down studio, where I find babe playing one of his video games."
    show stranger1:
        xpos 1200
    with dissolve
    dire "Since you’re back, I’m expecting the rest of your rent."
    show mc tan
    show mco bar2
    show mch blonde
    show mce horny
    with d
    mc "Uhh, uhmm… I don’t have it, but maybe what I do have is even better, hmm?"
    "I open my handbag and dangle the little baggie of blue. About 3/4ths of it still left."
    dire "What is this shit? More drugs? Is this where all my money is going these days?"
    show mce neutral with d
    mc "Wha? B-But I really needed the hit."
    dire "You fucking junkie whore! You just want to get high!"
    show mce sad with d
    mc "I’m sorry, babe! I could still-"
    dire "No, you’re done. Get the fuck out of here, you bitch. Go become someone else’s problem instead."
    play sound spank
    "Somewhat aggressively, he grabs me and drags me back outside."
    mc "Babe, b-babe! I’m sorry! I can change, I-I can quit!"
    play sound equip
    play ambience rain
    scene bg shops
    show rain1:
        alpha 0
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0
        repeat
    show rain2:
        alpha 0.5
        linear 0.5 alpha 0
        linear 0.5 alpha 0.5
        repeat
    with dissolve
    show mc tan:
        ypos 400
    show mco bar2:
        ypos 400
    show mch blonde:
        ypos 400
    show mce sad:
        ypos 400
    with dissolve
    play sound door1
    "Thrown outside, he slams the door to the studio I had once entered innocently."
    "I stumble back onto my ass, wiping the tears from my face as I remember that first day."
    scene bg shopsday
    show mc nude
    show mco uniform
    show mce happy2
    with d
    "What I was wearing, what I had looked like, and who I had become."
    "What do I do now? I gave everything up for that toxic lifestyle."
    scene bg shops
    show rain1:
        alpha 0
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0
        repeat
    show rain2:
        alpha 0.5
        linear 0.5 alpha 0
        linear 0.5 alpha 0.5
        repeat
    show mc tan
    show mco bar2
    show mch blonde
    show mce sad
    with dissolve
    "Dropped out of college."
    "Cut contact with my parents because he asked me to."
    "I’ve got nowhere to go, and no money…"
    "I scratch my arm again and look back at my handbag… I still have a bag of blue."
    "I need a hit."
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    jump endings
label loyalgirlfriendending:
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    $ lge =  1
    play music intro
    scene bg black with d
    "A couple of years after I started dating [crush], and our last year of Hero College…"
    show bg date
    call clothesclub from _call_clothesclub_6
    show mce laughing
    show crushb:
        xpos 1200
    show crushe laughing:
        xpos 1200
    with d
    "[crush] had taken me on an amazing date. We’ve been partners for so long, and while I may have had some money related complications at the start of our relationship, I’ve been committed and loyal to him ever since."
    "I do have a guilty pit in my stomach whenever I remember the things I did for money before I dated [crush]. The lewd photosets, the ‘massages’, or dances at the strip club. That among other things… But I paid my debt, and quit that life."
    "Now I just want to have a normal, loving life with my boyfriend."
    "[crush] had taken me out on a romantic date. A delicious restaurant. He’s really sweet, his work ethic and determination to do the best he can really enraptures me."
    "We definitely bring out the best of each other, because we’re always there to lift each other up when we’re down, and give the encouragement required to make it through some of the hardest parts of life."
    "Our super powers also really compliment each other. I’m looking forward to working with him in an official capacity when we both graduate in a few months."
    "We finish up our meals, and prepare to return to his place. I had already prepared a sexy surprise under my clothes for him."
    "Bless him, he’s not the most exciting in bed, so I put in a little more effort to spice things up. I never thought I’d be the top, and I’d prefer to be someone’s bottom, but I suppose it’s hard to live up to some of the sexual experiences I’ve been through."
    stop music fadeout 1.0
    scene bg shopsday
    call clothesclub from _call_clothesclub_7
    show mce horny
    "I step outside, and [crush] briefly excuses himself to go to the toilets. It’s been a week since we last had sex, I’m ready for a good, loving fuck. Heh, I should get my head out of the clouds, when did I become such a pervert?"
    play music dungeon
    show student3:
        xpos 50
    with d
    bacucko "Hey, [mc]. Haven’t seen you around in ages."
    show mce neutral with d
    "I freeze up slightly as this particular student greets me. He’s not just anyone, he was a childhood friend of [crush], and perhaps my most regrettable fuck with how my life has developed with [crush]."
    "When I started university, this guy was one of very few men I fucked for cash. I had no idea he and [crush] were so close at the time! I can’t let [crush] find out."
    show mce happy with d
    mc "H-Hey! It has been a while."
    bacucko "Still dating that dork?"
    show mce angry with d
    mc "He’s not a dork… I love him very much."
    student "Heh, never quite knew what you saw in him. I mean this respectfully when I say that guy has always been more interested in ‘things’, than people. His dream will always come first."
    show mce happy with d
    mc "Yeahh, I know… But that’s a pretty healthy thing too, having a life outside of your relationship."
    student "Pfft, you certainly had one hell of a life outside of yours. I’m just saying that I don’t think he can give you the attention and excitement you need."
    show mce neutral with d
    mc "I… I suppose he doesn’t, no."
    bacucko "I think you and I would make a better pair. How about you come back to my place for some fun? I haven’t had a fuck as good as you since you shackled up with him."
    mc "Uuhh, I…"
    "Awkwardly I look away as I sway back and forth. Naturally my mind is racing with memories of the last time I fucked this guy. It was really, really good…"
    "And as much as I hate to admit it, my wandering mind was no stranger to imagining him while I masturbated."
    "There was always something particularly spicy and taboo about the memory, especially since he was a close friend of my [crush]…"
    "Is that the kind of person I am? A thrill seeker that wants naughty experiences? Or am I the good girl that loves and dotes upon my boyfriend?"
    bacucko "I knew it. You’re actually conflicted. Is he really that bad in bed?"
    "I nonchalantly shrug, lacking the self-assurance to lie and say he is good in bed, but without the confidence to confirm his belief."
    show mce angry with d
    "This is the worst. Even if I make a bad choice, I’d rather make a choice, not sit in this awkward middle ground."
    "Yes, I love [crush], but every so often I just want a taste of that sex life I had before we started seriously dating."
    "Just a taste…"
    show mce happy
    show crushb:
        xpos 1200
    show crushe happy:
        xpos 1200
    with d
    crush "Ohh, hey you two! Thanks for keeping [mc] company. We were just returning to the dorms."
    bacucko "Really? Me too! How about we all go back together?"
    mc "*Gulp* S-Sure!"
    scene bg black with d
    "I’m quiet as we walk back to the dorms, I stand between the two men, holding hands with my boyfriend, physically bonding with him, yet mentally wandering to his opposition."
    show bg maledorms with d
    call clothesclub from _call_clothesclub_8
    show mce neutral
    show crushb:
        xpos 1000
    show crushe happy:
        xpos 1000
    show student3:
        xpos 50
    with d
    "It’s time to make a choice."
    "Whose bedroom will I be waking up in tomorrow morning?"
    menu:
        "Stay Loyal" if True:
            stop music fadeout 3.0
            jump loyalending
        "Cheat" if True:
            stop music fadeout 3.0
            jump cheatending
    label loyalending:
        "Damnit, why is this even a choice? I’ve been loyal for years and that’s not about to change anytime soon."
        show mce happy with d
        mc "Have a goodnight!"
        bacucko "You too, guys! Don’t keep us all up too late."
        crush "Haha, we won’t!"
        "I hope we do; you jerk!"
        scene bg black with d
        "A little later, in [crush]'s bedroom..."
        "While he’s moderately distracted, I undress and tie my hair back as I prepare to seduce the ever-living heck out of my boyfriend."
        "All that pent up sexual frustration is going into this one."
        play sound equip
        play music action
        scene loyalgfendb
        if tan == 1:
            show loyalgfendbtan
        if hair == 1:
            show loyalgfendh black
        if hair == 2:
            show loyalgfendh blonde
        if piercingson == 1:
            show loyalgfendpiercings
        show loyalgfend 1
        with d
        mc "Ohh, [crush]…"
        crush "W-Woah! [mc]! Y-You look so gorgeous!"
        mc "Thank you, cutie, and I’m all yours."
        crush "Ohh, you even have one of those butt things."
        mc "Mhhmm, I should feel even tighter than usual."
        "He quickly undresses, and kneels down on the couch beside me. His impressive cock growing in size as he brings his face level with my pussy and immediately begins assaulting my clit with his tongue."
        mc "Ohhhh, mmppphhhh… That’s it!"
        "This is actually a rarity for him, it was more something I had suggested he do more often recently. Even if [crush] isn’t the best in bed right now, he definitely isn’t beyond training!"
        "I enjoy every movement of his tongue, while happily watching him gently stroke his cock to a full erection."
        mc "Aahhhh, you’re really good at that! Focusing exactly on my clit like I said… You could get me off easily if you kept going. But… I’d much rather…"
        crush "My cock? Don’t worry, I think I’m getting better at knowing what you like."
        "He comes up and lines his cock up with my pussy, and at the perfect height to slide right inside. He holds my right thigh steady as he guides himself inside."
        play sound2 foreplay2 fadein 3.0
        play sound cum
        show loyalgfend 2 with d
        "As he parts my dripping, wet lips, I moan and shiver with pleasure as he pushes as deep as my tight pussy allows."
        mc "Oohhhh, that feeling of getting filled up for the first time never gets old."
        play ambience sex fadeout 1.0
        "He wraps his other hand around my left thigh and holds me in place as he begins to gently make love to me."
        "At the peak of each thrust, I can’t help but let a cute moan slip, my body shivering with excitement."
        "I was such a fool to not immediately shut down his friend. Not exciting enough for me? Utter nonsense. [crush] has one thing so few lovers have, and that’s a strength and speed boosting power."
        crush "It feels so good. Think I can speed up?"
        mc "Mhhmmm, give it to me hard. Why don’t you, hmmm… Use your power?"
        crush "My power? That’s a first."
        mc "Heh, you know I’m almost as fast and tough as you, I can take it."
        crush "Oookayy, you asked for it… Full-Cock, 50%%!"
        "He squeezes tightly into my thighs and begins to pummel away. *Slap, slap slap*."
        "Each successful connect of our bodies rocks my world as he uses his enhanced power to fuck me silly."
        "He doesn’t stop there too, he graciously places his thumb against my clit, just holding it there and allowing the rocking of our bodies to create the friction."
        "The simultaneous pleasures shock me, causing my body tremble as sparks of bliss course through my nerves, getting me closer and closer to an explosive orgasm."
        "I can barely get a sentence out between moans, and within twenty seconds of this I’m easily brought to climax."
        "Swapping gears, he takes his finger away from my clit, and holds me tighter."
        crush "Here goes… Full-Cock, 65%%! Smaaaaaaaaassshh!"
        mc "Uwaaaahhhaaahhh!!!"
        play sound cum
        show loyalgfend 3 with cum
        play sound cum
        show loyalgfend 3 with cum
        "My mind is briefly lost in bliss as his cock explodes deep inside of me. (Not literally)"
        play sound cum
        show loyalgfend 3 with cum
        play sound cum
        show loyalgfend 3 with cum
        stop ambience fadeout 3.0
        "*Thrust, thrust, thrust* My tight pussy squeezes as much cum as it can during our seven seconds of heaven."
        "Before we gradually come back down to earth, and we both completely tap out."
        stop sound2 fadeout 1.0
        play sound cum
        show loyalgfend 4 with d
        "Oh my god, he fucked me beyond silly. I can’t even think straight, and my hair is a complete mess. Why did we never think to use his super power in bed before this?"
        play music intro
        scene bg black with d
        "And so…"
        show bg class
        call clothesformal from _call_clothesformal_35
        show mce happy2
        show crushb:
            xpos 1200
        show crushe happy:
            xpos 1200
        with d
        "We went onto to become a loving couple forevermore, and the sex ended up being so good, it was almost too much sometimes!"
        "I guess that’s just an advantage of marrying the no. 1 pro hero in the country, hehe."
        jump lgfee
    label cheatending:
        "If only I wasn’t dating [crush]… At least I know his friend can keep his mouth closed."
        "Maybe I can get the best of both worlds. Maybe this can just be a one-time lapse of judgement. I deserve to feel good too."
        show mce happy with d
        mc "Okay, boys, I think it’s about time I went back to my dorms. I’m feeling really tired, and want to get a bath and go to sleep."
        show crushe laughing with d
        crush "Oh? Aahh, alright, [mc]. I hope you have a pleasant sleep."
        "Damnit, [crush], why do you have to always be so understanding and sweet? I suppose that’s why despite fucking all these other people, you’re the one I fell in love with."
        "Still…"
        bacucko "Heh, see you in a bit, then."
        show mce neutral with d
        mc "Y-Yeah, goodnight."
        scene bg black with d
        "[crush] enters the male dorms, and Bacucko waits outside, browsing his phone."
        show bg maledorms
        call clothesclub from _call_clothesclub_9
        show mce neutral
        show student3:
            xpos 50
        with d
        "Needless to say, he was expecting me, and a part of me hates that, however, another part of me is excited."
        bacucko "I was going to give you five minutes, but you didn’t make me wait one."
        show mce angry with d
        mc "I’d rather keep everything we do outside quick, I wouldn’t want to get caught."
        scene bg black with d
        "He nods and leads me to his room. It’s on a different floor to [crush]’s, but I’ll probably still need to slip out early in the morning. The devil on my shoulder tells me ‘That makes it even more exciting’."
        "I enter the male bedroom, its walls notably blue instead of the pink from my dorm, and it’s a similar shade to the lingerie I had been wearing for [crush] under my clothes."
        play music action
        play sound equip
        show ntrendb
        if tan == 1:
            show ntrendbtan
        if hair == 1:
            show ntrendh black
        if hair == 2:
            show ntrendh blonde
        if piercingson == 1:
            show ntrendpiercings
        show ntrend 1
        with d
        "I strip piece by piece, and tie my hair back. I swirl around and show off how my ass looks in garters. There’s uncertainty in my eyes, but my pussy is aching with desire."
        mc "Well, what do you think?"
        bacucko "Unbelievable, you even put on sexy lingerie to surprise him, and yet you’re giving me that honour?"
        mc "He probably wouldn’t have appreciated it."
        bacucko "Heh, but I’ll appreciate it alright. I’ll appreciate every inch of you."
        "My body shivers with excitement as he nears me, his fingers lightly grazing around the smooth skin of my ass."
        bacucko "You’re really wet."
        mc "I have my needs… You better make it worth it."
        bacucko "Don’t you worry about that."
        "He slides his pants and underwear down and starts to jack his cock off until it’s perfectly solid. It’s an exciting sight, and my hips instinctively push out a little further beckoning it."
        play sound2 foreplay1
        play sound cum
        show ntrend 2 with d
        "He holds me by the hips as he gently eases it between the plush lips of my labia, sinking forward past my delicate folds and deep into my pussy."
        "The cock’s larger than my crush’s, but I still take it easily, all whilst cooing at the sensation of being filled up."
        mc "Aaahhhh, I’m so damn sensitive right now, heh…"
        play ambience sex fadein 2.0
        "He pulls out, sending another spark of pleasure throughout me, and then he thrusts back inside. He begins fucking me at a pace pleasant to both of us."
        "I already feel like he understands my body more already. He handles me with such confidence and grace."
        "Giving out as much as I take, my pussy purposely teases and squeezes around his member. I feel like I can fully let loose and be the slutty girl I became at the start of college."
        "Our hips both rock, meeting in the middle with each thrust, making it that little bit harder."
        mc "Mmphhh, I love your thick cock, still one of the best fucks I had. Aaahhh… Tighten it a little for me, won’t you?"
        "He tightens his cock slightly at my request, and in turn I tighten my pussy slightly."
        mc "Aaahh, aahhh.. So fucking good, haahh…"
        bacucko "Your pussy is even better than I remember it, I didn’t think it could get any tighter, but here we are!"
        mc "Nnhh, aahhh.. Sounds like challenge, hehehe."
        "Any thoughts of my boyfriend or guilt have completely left my mind. All that matters right now is getting a good fuck!"
        "I rhythmically clench my pussy around his cock, doing my best to milk him dry as he pounds into my sloppy, wet pussy."
        "At this rate, it wouldn’t take either of us long to come, but we move at a pace to savour every last drop of pleasure we can."
        "That is until I feel one of his hands move between my legs to rub my clit. This really gets me going, causing me to moan uncontrollably, and barely maintain my stance as pleasure overpowers me."
        "He holds me close, keeping me upright as he continues to pound me at an accelerating pace. I can feel his cock swell up and prepare to unload inside of me."
        play sound cum
        show ntrend 3 with cum
        play sound cum
        show ntrend 3 with cum
        "And before I know it, my tight, squeezing pussy coaxes his orgasm, as cum freely spills deep into me."
        play sound cum
        show ntrend 3 with cum
        play sound cum
        show ntrend 3 with cum
        stop sound2 fadeout 3.0
        "Several loads of ejaculate seep deeply into my pussy, enough to overflow and splatter down my thighs."
        mc "Haaahh, yeessss… This is exactly what I needed and more."
        stop ambience fadeout 1.0
        play sound cum
        show ntrend 4 with d
        "My legs wobble a little as he pulls out, more cum dripping as he does."
        bacucko "How about we watch a film, and go again in an hour?"
        mc "I appreciate the thought, but…"
        "I look down at my clothes and think for a few moments."
        mc "I really could use that bath and early night."
        bacucko "Ahahah, of course, I can’t blame you."
        bacucko "But hey, don’t be a stranger. If [crush] is ever letting you down, I know a thing or two."
        mc "Maybe I’ll take you up on that, we’ll have to be discreet, though."
        stop music fadeout 1.0
        scene bg black with d
        "And so…"
        play music intro
        show bg class
        call clothesformal from _call_clothesformal_40
        show mce happy2
        show crushb:
            xpos 1200
        show crushe happy:
            xpos 1200
        with d
        "I continued my relationship with [crush], it was a great relationship too."
        "You’d assume I’d be unsatisfied with it, but I found my satisfaction elsewhere as I’d cheat every so often."
        show student3:
            xpos 50
        show mce horny
        with d
        "I ended up fucking Bacucko a few more times, among others…"
        "It was easy to keep it hidden from [crush], because he’s so damn trusting and loving."
        hide student3
        show mce happy
        show bg bedroomnight
        with d
        "When we inevitably moved in together, I did stop the affairs. Especially since he became the no. 1 hero in the country. I didn’t want to get pulled into a scandal and have both our careers turn rocky."
        "And he did get better in bed eventually."
        "But I have to admit, I’d be lying if I didn’t crave excitement like my early college days every once in a while."
    label lgfee:
        pass
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings
label egirlending:
    $ ege = 1
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    play music intro
    scene lonelyfansb mirror
    show lonelyfans 1
    if hair == 1:
        show lonelyfans1h black
    if hair == 2:
        show lonelyfans1h blonde

    with d
    "A few years ago, I posted my first image set."
    "It was simply me posing in some comfy casual clothes in front of a mirror, with my head obscured."
    scene bg bedroomday
    show mc nude
    show mco catlingerie
    show mch pink
    show mce laughing
    with d
    "Today, marks me breaking a new landmark goal. $1,000,000."
    show mce horny with d
    "A month."
    "$1,000,000. A month."
    scene bg bedsex
    show camoutfitsb
    show camoutfitse catgirl
    show camoutfitsh pink
    show camoutfits 1
    show chatfapborder
    with d
    "Long gone are the days of me scrounging around to desperately earn a mere $72,000."
    "Through hard work and persistence, I’ve become one of the highest earning e-girls on the internet."
    "I’m no longer even ‘[mc]’ online either, I have my own identity. My own style."
    "I do cosplays, photosets, videos, porn and more."
    "Millions of people online eagerly consume every drop of media I put out."
    "And yeah, people recognize me all the time in person. Heck, I couldn’t hide this from any family member or friend. Fortunately, the world has become a lot more open to sex work, and they needn’t know the ‘details’ of what I do, unless they were so inclined to purchase a subscription."
    scene bg shops
    show mc nude
    show mco yokouniform
    show mch pink
    show mce laughing
    show stranger1:
        xpos 50
    show student7:
        xpos 1200
    with d
    "People recognizing me is a roll of the dice. Sometimes they’ll be a creep, other times they may be friendly and a joy to talk to."
    "As a frequent visitor of anime conventions, it was inevitable that I’d be recognize by… well, almost everyone."
    "I could do something fun with this…"
    scene bg massage2 with d
    play music action
    show xtubeborder
    with d
    "A great bid was enacted. Six people could have the opportunity to fuck me in one of the most prolific moments in e-girl history. Regular news outlets covered the story as people bid up to $100,000."
    "The highest bidder could choose whether to fuck my ass and pussy, second highest got the other option. Third and fourth will be serviced with my mouth. Fifth and sixth will get to play with my breasts and body as they jack off."
    "It went down as the most expensive act of prostitution in history and only served to boost my explosive popularity. Exactly me and my marketing team’s intent. (Oh yeah, I have a marketing team, hehe.)"
    "These men practically worshipped me."
    hide xtubeborder with dissolve
    pause (0.2)
    play sound2 foreplay1
    show egirlempressendb
    show egirlempressend 1
    with dissolve
    "I sat on my throne of man in the centre of the bed. One beneath me with his cock pressed between my cheeks, two behind me on either side, one in front of my pussy, and two more at either side of that."
    mc "Aha, look at you all. Rock hard and ready to go. Let’s start with the top bidder, you chose to fuck me ass, so let’s ease you in there."
    play sound cum
    show egirlempressend 2
    with dissolve
    "All lubed up, his tip pressed against my pucker and gently pushed inside. I’m already incredibly experienced with anal, and prepared by wearing a butt plug to the anime con, so it sinks deep inside with complete ease."
    mc "Nnn, that feels good… Once we get the other in my pussy, I’ll be ready to rock your world."
    "Excitement rose in the room as they all watched me. My two camera men ensuring they capture everything clearly with their 4K equipment."
    mc "I’ll take everything you’ve got, so get ready to blast me with everything you’ve stored up. And I do hope you’ve stored up a lot for me."
    "I grin and suggestively rub my cheek against the closest cock."
    mc "Aaahhh, so hot and eager… I can see your tip dripping with precum."
    "The second highest bidder stands before me, preparing his erection before my juicy pussy."
    mc "Ohhh! Hurry up and let me get a feel of that goliath! Phewww…"
    "Unable to contain my desire, I wiggle my hips a little closer, causing the cock in my ass to throb slightly."
    play sound cum
    show egirlempressend 3
    with dissolve
    "He excitedly smirks as he kneels down and places his cock against my labia. Then, slowly sinking deeper inside, his throbbing, hot cock fills me up inch by inch."
    mc "Aaahhh! So big! Mmphhh, I always feel so full taking it in both holes at once."
    "The thick member spreads me wide, but my pussy clings tightly, causing him to groan."
    "I begin to sway my hips, squirming and wriggling about as I fuck both the cock in my ass and pussy."
    play ambience sex
    "The men get the message and begin rocking the hips like pistons. Obscene fucking sounds fill the room as I shake my hips too."
    "Everyone finds their footing and gets faster, and faster. *Smack, smack, smack!*. It’s not long until I’m panting like a bitch in heat."
    mc "Mmphhh, aahhh, moooreee! Gimmie a cock to suck on too! Hehehe."
    "One of the men beside me takes their erection and brushes it against my cheek affectionately, precum dripping down my face. The others, unable to hold back their lust, jerk off furiously at all the sights."
    play sound cum
    show egirlempressend 4
    with dissolve
    "I sigh pleasantly as I nuzzle the cock, before turning my face and allowing it to slip into my mouth."
    "It pushes in deep, and my tongue sloppily rolls around its tip in response."
    "It’s so hard to maintain focus while I’m being fucked in three places at once. And that’s not all, as the men toy with my pert nipples, my feet and even my belly."
    "My pussy clamps down as I indulge in the occasional orgasm, my body spasming as pleasure surges through my nerves."
    "The tight squeezing excites my fuckers, as they excitedly moan and swing their hips faster."
    "Each impact rocked my body and mind, as I eventually completely lost focus and control and became a fuck toy for everyone."
    "I still tried to give as good as I got, as I eagerly sucked the cock and rocked my hips, but it was entirely primal and instinctive."
    play sound cum
    show egirlempressend 5 with cum
    "As I brushed my tongue against the tip in my mouth, it suddenly swelled up and a huge mouthful of hot semen blasted inside against my cheek."
    play sound cum
    show egirlempressend 5 with cum
    "I gulp down as much of this fresh cum as I could, but even as I drink this sticky semen down, the man continues to fuck my mouth and unload more."
    play sound cum
    show egirlempressend 6 with cum
    "The chaotic chain reaction of cum didn’t stop there, as a sudden burst of hot semen flooded into my ass. Totally unable to contain it, it became a nearly never-ending flow of cum that bubbled and oozed out of my well-fucked ass."
    play sound cum
    show egirlempressend 6 with cum
    "My pussy was next as I squeezed down tightly on the dicks shoved inside, another torrent of cum filling me to bursting point."
    play sound cum
    show egirlempressend 7 with cum
    mc "Mmphhh, yessss! Guhhh, mmphhhh!"
    play sound cum
    show egirlempressend 7 with cum
    "Long ropes of sticky jism splattered and coated my face, breasts, ass and thighs as all men came in roughly a one-minute span. I too indulged in a cheeky orgasm for about half that length."
    "In fact, I was so lost in pleasure that I didn’t stop wildly thrusting my hips, my tongue lolling as I was hungry for more."
    stop ambience fadeout 1.0
    stop sound2 fadeout 1.0
    play sound cum
    show egirlempressend 8 with d
    "The men had to unfortunately withdraw as their cocks grew sensitive and flaccid…"
    "Maybe, just maybe… We could go for seconds?"
    guy1 "What a woman…"
    guy2 "She’s like a succubus."
    guy3 "If she is a succubus, then I think she’s beguiled the entire world."
    play sound success
    "Pink Hair accessory unlocked. (Will not appear in sex scenes.)"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    jump endings
label virginending:
    $ vie = 1
    play music intro
    scene bg college
    show mc nude
    show mco uniform
    show mce happy
    with d
    mc "Finally! I’ve paid off my student loan!"
    "It wasn’t easy. I tutored many students, worked many days in that bar in the unruly, lewd costume."
    "Taken the occasional risqué photoshoot for my followers online."
    "But despite it all, my desire for money didn’t break me."
    "I never once lost myself in the pursuit of money."
    if virgin == 1:
        "And I definitely never sold my body for money, or exchanged sex for monetary gain."
        "Right?"
        show mce angry with d
        "Right…?"
    show mce happy2 with d
    "I’ll live a normal life from now on."
    "No more desperate jobs for money. I’ll become a full-time hero, fall in love with someone, marry someone, and have a normal life!"
    "I’m going to focus on graduating with the best grades possible, then I’ll ask [crush] if he wants to be my boyfriend if he hasn’t already made the first move."
    play sound success
    "(Congratulations on paying off your tuition while remaining a virgin!)"
    if virgin == 1:
        "(You did pay off your tuition while remaining a virgin, right?)"
        show mce horny with d
        "(Riiight…?)"
    elif True:
        "(But, why did you beat an entire porn game while avoiding the porn?)"
        play sound success
        "(Oh well, as a reward, you’ve unlocked every other ending in the game.)"
        $ endingoverride = 1
    jump endings
label massageparlourending:
    $ mpe = 1
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    play music intro
    scene bg college
    call clothesformal from _call_clothesformal_31
    show mce laughing
    with d
    "Four long years, and I’ve finally graduated from Hero Academy!"
    "However, despite being a capable and well-trained hero, I decided to only do it part-time, a little like my role-model, Bunny!"
    scene bg massage
    call clothescamisole from _call_clothescamisole_1
    show mce horny
    show bunny:
        xpos 1200
    with d
    "In fact, Bunny has helped me in a ton of ways as a top hero herself. I’m actually working with her as a assistant at the parlour and as a hero! Hehehe…"
    "So, just like my role model bunny, I save lives during the day, and sleep with people during the night. It’s a ton of fun."
    bunny "Congratulations on your graduation! We’re going to make an amazing duo out there on the field."
    bunny "My strength combined with your support, there’s no villain we can’t defeat, and no civilian we can’t save."
    show mce laughing with d
    mc "Yeah, I agree! Let’s do our best!"
    bunny "And let’s not forget that we also make an amazing duo in here, don’t we just? Hehehe."
    "We’ve started to get a reputation, Bunny’s popularity has only grown as a sex-positive hero in the modern age, and rumours of a fellow assistant also joining her at their parlour? Well, that’s definitely brought in the customers."
    bunny "Specifically… I have another customer that asked just for us two!"
    show mce horny with d
    mc "Again? That’s the third this week!"
    bunny "Hehe, but we can charge them more than double. Oh, and this is technically two customers, I guess it’ll be a foursome!"
    show mce happy with d
    mc "Ohh, that’s a first. How much are we getting?"
    bunny "$1,000!"
    bunny "Each…"
    show mce laughing with d
    mc "Phewww! We certainly are getting prolific, hehe, let’s do it!"
    stop music fadeout 1.0
    scene bg black with d
    "…"
    play music action
    scene bg massage
    show massageparlourthreesomeb
    if tan == 1:
        show massageparlourthreesomebtan
    if hair == 1:
        show massageparlourthreesomeh black
    if hair == 2:
        show massageparlourthreesomeh blonde
    show massageparlourthreesome 1
    bunny "Do you like what you see? This tight ass is aaalll yours…"
    "Bunny teasingly pats my butt as our customers undress and get into position behind us."
    mc "Eep! That’s right, my pussy is all ready to massage your cock."
    "Erections in hand, the two customers take their pick. Naturally they want to take turns fucking us both, but for now the one with a slightly smaller cock settles on me."
    "Bunny coos as she presents her utterly soaked pussy. Juices dripping down both our thighs as we’re so thoroughly ready for a good fuck."
    play sound2 foreplay2 fadein 3.0
    play sound cum
    show massageparlourthreesome 2
    "The tips of their cocks tease and prod against our entrances before they comfortably slip into a world of delightful warmth and tightness."
    bunny "Aaahhh, don’t hold back, lads, there’s nothing [mc] and I love more than a hard pounding."
    play ambience sex fadein 2.0
    "The cock inside me slides all the way into the hilt, before pulling back outside quickly and engaging in some rough pounding. With each thrust, the entirety of the shaft is pulled out, and then sunk back in as deep as it’ll go."
    mc "Mmphh, mmm, that’s really good!"
    "My experienced pussy intentionally tightens and milks the customer’s cock as even when bent over and receiving I do my best to provide exceptional service to the customer."
    "Bunny and I maintain lewd, joyous facial expressions. Soft, sensual moans, and enthusiastic body language."
    "But it wasn’t all acting. Maybe it was, at a time, but now, we’re enjoying every second of this to its fullest."
    "Every nerve ending in my pussy is stimulated wonderfully, euphorically, and this is an experience I get to consensually and happily enjoy every night for a living."
    "Bunny giggles as I space out, spanking my butt playfully as the passion of the moment approaches it climax."
    bunny "Come on, boys! Fill ‘em up good!"
    "Taking it as a challenge to speed up, the man fucking me really pushes me to my limit. I couldn’t even contain my enjoyment if I wanted to!"
    "As I approach my orgasm, my pussy starts to tighten around the customer’s swelling cock, it seems he’s at his limit too."
    play sound cum
    show massageparlourthreesome 3
    "The sudden tightness of my pussy seems to push them over the edge, as they suddenly start to unload deep inside me."
    play sound cum
    show massageparlourthreesome 3
    "And it’s not just me, Bunny too is filled up by a substantial amount of cum."
    stop ambience fadeout 2.0
    stop sound2 fadeout 2.5
    mc "Mmphhh, so good, aahhh…"
    bunny "Phew, that was a nice quickie to start with! Now what are we going to spend the next fifty-five minutes doing? Hehehe?"
    scene bg black with d
    "…"
    play music intro
    scene bg massage
    call clothesformal from _call_clothesformal_32
    show mce happy
    show bunny:
        xpos 1200
    "And so, I had a healthy and fun career for the rest of my life with Bunny."
    "I always had the goal of earning money, and helping people as a hero, and somewhere along the way I picked up a healthy sex drive too."
    hide bunny with d
    show mce laughing with d
    "After over a decade of this lifestyle, Bunny retired, and I took over as the owner of the massage parlour."
    show toko:
        xpos 1200
    "And that’s when a seemingly innocent student arrived at my door, asking if she could work here. I knew what I had to do!"
    "When it was time for me to retire? Heh, my assistant took over, of course!"
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings
label slimegirlending:
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene bg black with d
    "About a year later…"
    play music intro fadein 1.0
    scene bg bedroomday
    call clothesnude from _call_clothesnude_70
    show pinkbody
    show pinkhair
    show mce happy
    show pinkeyes
    with d
    mc "Yaaawwnn… Another day of college!"
    "My name’s [mc], and I’m a top student at Hero Academy."
    play sound equip
    show mco underwear with d
    "I’m one of the rarest examples of a super powered human, because not only do I have a slime mutant power, but I also have a gravity manipulation power."
    "99.99%%%% of people are only born with a single power, but for some reason, I was born with two!"
    "Yup, my entire body is gooey! If you try to punch me, your fist is likely to get absorbed into my body. And that's not even to mention the really powerful aphrodisiacs coating the slime. I have to be very careful not to touch anyone in daily life."
    play sound equip
    hide pinkhair
    show mco uniform
    show pinkhair
    with d
    "My parents were so shocked to find out that my slime power manifested so late, but how could I complain?"
    "Oh, and [tina] and I were easy BFFs, since we were both pink! Hehe."
    "In fact... just yesterday..."

    play music action
    play sound2 foreplay1
    show tinathreesomeb
    if tan == 1:
        show tinathreesomebtan
    if hair == 1:
        show tinathreesomeh black
    if hair == 2:
        show tinathreesomeh blonde
    show tinathreesomeslime
    show tinathreesome 1
    show tinathreesomepinkeyes
    with d
    "*Spread, squish*"
    tina "Ohoh, once you're done with this pretty, pink pussy, you'll get mine too!"
    "I look back expectantly as the man jacks his cock to full erection. Tina doesn’t just spread and toy with my pussy, but also wiggles my butt enthusiastically."
    play sound cum
    hide tinathreesomepinkeyes
    show tinathreesome 2b
    with d
    "With his cock ready to go, Thad positions it at my pussy and slowly pushes forward. Easily sinking inside, my lips grip and squeeze around every inch of the shaft."
    mc "Aaahhh, aahhh…"
    "My whole body reacts with a shiver of pleasure, culminating in a loud moan that escapes my mouth. My slimy pussy is absolutely throbbing with pleasure and desire."
    play ambience sex fadein 2.0
    tina "Oohh, I love your cute moans, [mc]."
    guy "Woah... This slime... You weren't kidding, it feels insane!"
    mc "Aahhh, yup, ahhh, that aphrodisiac will keep you going for a few times!"
    tina "Can you see why I love her so much? Hahaha."
    "We both speed up a lot. His cock feels astounding in my pussy right now, it’s overwhelming my senses."
    "He can't hold back much longer than a minute, as his thick cock begins to swell up as my mind and body are overwhelmed with orgasmic euphoria."
    play sound cum
    show tinathreesome 3b with cum
    "My vision turns white and my muscles grow tense as I reach the peak of my climax. The pleasure is indescribable."
    stop ambience fadeout 2.0
    stop sound2 fadeout 2.0
    tina "Damn, stud! Leave some for me, mmm…"
    play sound cum
    show tinathreesome 4
    show tinathreesomepinkeyes
    with d
    "Pulling out, copious amounts of cum oozes from my pussy, he must have really enjoyed it."
    tina "Mmphh, my turn! [mc], give me a hit of that aphrodisiac."
    mc "You got it!"
    play music intro
    scene bg street
    call clothesnude from _call_clothesnude_71
    show pinkbody
    show mco slimehero
    show pinkhair
    show mce happy2
    show pinkeyes
    with d
    "While out working as a hero, I can manipulate my body into many forms both offensively and defensively."
    "My go to, however, has always been fast gripping tentacles! The powerful aphrodisiac these things ooze can impair even the most fortuitous combatant, and swoon even the coldest lover."
    "My hero suit was modified to show even more skin than before. Although I still have to be careful, since my aphrodisiac affects allies as well as enemies."
    "I can’t remember the details around my power manifesting… But something about that aphrodisiac, and these tentacles reminds me of it…"
    "Not to mention it’s extraordinarily rare for a mutant power to not appear in my family tree previously, and no one else in my family has a power like mine. My mother knows telekinesis, and my father can float."
    scene bg bedroomnight
    call clothesnude from _call_clothesnude_72
    show pinkbody
    show mco pjs
    show pinkhair
    show mce neutral
    show pinkeyes
    with d
    "…There it is, again… This itch in the back of my head… Where the hell did I get this power from?"
    "A header in the news catches my attention, so I turn my focus to the television and listen up."
    "'NeoHero City Power Research and Development Lab Scandal’."
    "I walked past there once, right? Hmm…"
    "’A scientist has recently been under criticism for experimentation with seemingly living ‘slime’ substance.'"
    "An image shows one of the labs, and I get a strange feeling of déjà vu."
    "I’ve been in that lab, haven’t I? I recognize it completely… But, no, I’ve never been inside that building before. How strange…"
    "The broadcast continues: ’People have been outspoken on the cruelty of performing tests on what seem to be cute, and sentient slime creatures.’"
    "’However, the lab released this statement: These slimes are not living creatures, they’re the result of a power we’re researching. It is an invasive specimen would attack individuals, and attempt to assimilate with them.’"
    "’These slimes originate from a very special mutant Slime Girl.’"
    "’It is one of the first examples of a power existing long-term outside the body of the individual of origin. We even hypothesis that other individuals could adopt these powers temporarily. This is why it’s such an important avenue of research.’"
    mc "Huh…"
    "I momentarily raise my hand and stare at my gooey form. Was I attacked and assimilated?!"
    mc "…Naaahh, ahaha, I’d remember that… I’d remember…"
    scene bg shopsday
    call clothesnude from _call_clothesnude_73
    show pinkbody
    show mco slimehero
    show pinkhair
    show mce happy2
    show pinkeyes
    with d
    "Needless to say, I went on to be one of the most successful heroes in the country, taking full advantage of my gravity manipulation and slime body."
    "Before, I had to touch people to manipulate their gravity, now all I needed to do was shoot a hyper-fast tentacle and poke them once."
    "I was almost overpowered, and I became not only a symbol for peace, but also a symbol for others with mutant quirks."
    "But I never quite got over the anxiety of not knowing where my power came from. For me, it became a well-kept secret. If anyone asked? I was born like this."
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    if sge == 0:
        play sound success
        "Unlocked Crop-Top Hero Costume!"
        $ clothes = 14
    $ sge = 1
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endingm
label yomogfending:
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene bg black with d
    $ yge = 1
    "About a year later…"
    play music intro fadein 1.0
    scene bg house1
    call clothesformal from _call_clothesformal_36
    show mce happy
    show yomob:
        xpos 1200
    show yomoo uniform:
        xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    with d
    "[yomo] had asked me to be her girlfriend on fateful day. Of course, I said yes!"
    "Four long years later, my girlfriend and I finally graduated from Hero Academy together!"
    "[yomo] and I were inseparable. We’d sit together at class, get lunch together, then walk back to her estate and sometimes I’d even stay there."
    "From the moment we first met each other on the first day of class, to the days where we studied together and bonded like a wildfire."
    "It’s weird, right? How could she and I never get sick and tired of each other. Never once did we argue or grow weary of each other’s company."
    "It was mostly because of how tactful, and mature [yomo] is. Even when we had a serious disagreement, we had the ability to communicate calmly, and compromise."
    "I still remember our first sexual moment in detail, the way she touched me."
    show yomomakeout1
    show yomomakeout2
    with d
    "Our hands wrapping around each other, as she took charge and pulled me into the kiss."
    "Oh yes, I was an easy bottom for [yomo] as she took things a little further every single time."
    scene yomofingeringb
    if pregnancyshowing == 1:
        show yomofingeringe pregnant
    if tan == 1:
        show yomofingeringbtan
        if pregnancyshowing == 1:
            show yomofingeringbtanp
    if hair == 1:
        show yomofingeringh black
    if hair == 2:
        show yomofingeringh blonde
    if piercingson == 1:
        show yomofingeringpiercings
    show yomofingering 3
    with d
    "But she was only capable of that confidence because I brought out the best in her, and she brought out the best in me."
    "That’s more or less what the foundation of our relationship was always built on, strong communication, understanding and being there for each other through thick and thin."
    scene bg house1
    call clothes from _call_clothes_104
    show mce happy
    show yomob:
        xpos 1200
    show yomoo uniform:
        xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    "So, when she asked me to marry her…"
    show mce laughing
    show yomoe laughing
    with d
    "I said yes, of course!"
    scene bg black with d
    "Later, on the night of our wedding…"
    scene bg house1
    call clothesnude from _call_clothesnude_74
    show mce happy
    show yomob:
        xpos 1200
    show yomoe horny:
        xpos 1200
    with d
    yomo "I can only think of one more thing left to seal the deal, babe."
    mc "How about we kiss with another pair of lips? Hehe."
    yomo "Ohh, tribadism? Despite all our grinding and love-making, I don’t think we’ve ever done it quite like that."
    mc "It’s a special occasion, let’s give it a shot! It’ll either be memorable, or at least a laugh."
    play music action
    show yomoendingb
    if pregnancyshowing == 1:
        show yomoendingbp
    if tan == 1:
        show yomoendingbtan
        if pregnancyshowing == 1:
            show yomoendingbtanp
    if hair == 1:
        show yomoendingh black
    if hair == 2:
        show yomoendingh blonde
    if piercingson == 1:
        show yomoendingpiercings
    show yomoending 1
    with dissolve
    play sound2 foreplay1
    "Initially laying down, we lock our legs before hoisting ourselves up, leveraging each other by holding hands, supporting each other as our wet pussies finally smooched together."
    mc "Oohh, warm, wet and gooey!"
    yomo "Let me know if this angle is good for your clit."
    show yomoending 2 with d
    "She winks and instantly takes charge, rocking her hips back and forth, grinding our pussies together with a special focus on our swollen clits."
    "It immediately feels great, not to different from how I could hump a pillow to masturbate, with the benefit of having my smoking, hot wife being the one humping me."
    mc "Aaahh, aren’t you eager? Mmphh…"
    yomo "I can’t hold back with you, [mc], I’ve been wanting to ravage your body in unspeakable ways all day."
    mc "Aahaha, aaahhh, but you already did that last night!"
    yomo "Mmhhhmm, and I’ll do it tomorrow too!"
    "I start to rock my hips too, doubling the intensity and pleasure of our pussy make out session."
    "Understanding each other’s bodies through and through, we find a perfect angle and intensity, and keep at that pace. It wouldn’t take long for our orgasms to start brewing."
    "My wife’s moaning is music to my ears, and our longing eye contract is a big turn-on for this position. It’s pure love and love."
    "We both squirm and spasm with pleasure as the tension keeps rising and rising… Our moans keep getting louder, finally overpowering the squishing sound of our wet pussies. I can feel my orgasm getting really close!"
    play sound cum
    show yomoending 3 with d
    "It’s [yomo] that’s pushed over the edge first, you really can’t miss her orgasms, as her entire body buckles and it’s often accompanied by a delightful orgasmic moan."
    play sound cum
    stop music fadeout 5.0
    stop sound2 fadeout 3.0
    "And it’s not too similar from my reaction as I’m shaken to the core with euphoria."
    mc "Oohhh, [yomo]! I love you! Aaahhhh!"
    yoko "I love you too, [mc]! Let’s be together, forever! Aahh, mmphh…"
    "The climaxes were strong, marking the culmination of our wedding day. But despite the tiring day, I certainly imagine they won’t be our last orgasms tonight."
    play music intro
    scene bg black with d
    "…"
    scene bg shopsday
    call clotheshero from _call_clotheshero_1
    show mce happy
    show yomob:
        xpos 1200
    show yomoo hero:
        xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    "[yomo] and I were not only an inseparable couple, but we naturally, we worked together as heroes."
    "Initially we started working in an agency as we got our name."
    "Eventually, we got that name, and as [yomo] was always an ambitious genius, and this rubbed off on me. Always wanting to pursue something greater, we had decided to run our own agency to great success."
    "It certainly helped our image in hero celebrity culture that we were an openly lesbian hero couple."
    "And as we both managed to find ourselves in the country’s top ten heroes list, that popularity and success only soared."
    "We lived long, happy lives, and we were together the entire time."
    scene bg black with d
    "The End..."
    stop music fadeout 1.0
    "Or... is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endingm
label dominatrixending:
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    play music intro
    scene bg dungeon
    show mikab:
        xpos 1200
    show mikao dom:
        xpos 1200
    show mikae horny:
        xpos 1200
    with d
    "What’s better than one sexy, assertive dominatrix?"
    call clothesdom from _call_clothesdom
    show mce horny
    with d
    "Two of them!"
    show mce laughing with d
    "After becoming best friends with [mika] during my college years, I seem to have picked up one or two kinks."
    "And now, I’ve risen to become a dominatrix, just like her."
    scene bg dungeon
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
    "The dungeon is a lot more popular than before, finally opening up from a private club to an open fetish club for college students."
    "Surprisingly this resulted in tons of girls joining, most of them bottoms. This led to me, a more experienced member of the club, often being involved with teaching and show people how to tie rope."
    scene bg dungeon
    call clothesdom from _call_clothesdom_1
    show mce happy2
    with d
    "And I loved it. It wasn’t long until I became a dedicated top in a lot of situations, with the ladies and gents."
    stop music fadeout 2.0
    scene bg black with d
    "This is one such event."
    menu:
        "Choose a Sex Partner"
        "Female" if True:
            play music action
            show dominatrixendb
            if tan == 1:
                show dominatrixendbtan
            if hair == 1:
                show dominatrixendh black
            if hair == 2:
                show dominatrixendh blonde
            if piercingson == 1:
                show dominatrixendpiercings
            show dominatrixendcollar
            show dominatrixenddom 1
            show dominatrixend f1
            with d
            mc "Aaahhh, your pussy is so wet already… Tchh, all I did was sit on you."
            "I use the leash to tug the collar of the girl I’m toying with today. She’s fresh meat, and there’s nothing more I enjoy than playing with them as they’re indoctrinated into the club."
            "It’s not too different from when I was indoctrinated. They get to choose their punishment, and then how they get fucked. This girl’s more lesbian inclined, so she hand-picked me!"
            "In addition, she chose a gag, a collar, and for me to ravage her with some pussy on pussy action."
            mc "Ohh, don’t think I didn’t notice your hips subtly grinding. Does that mean you want more?"
            "The poor sap nods as she ogles my body, taking a particular interest in my breasts."
            mc "Ohh? You like my big milkies? If you behave, I’ll let you see them."
            "She obediently nods again; I can actively feel her submission turn me on as my clit grows more sensitive and needy."
            play sound equip
            show dominatrixenddom 2 with d
            "I unstrap my bra, letting it fall onto my partner as my breasts sway freely. As she watches, her nipples naturally stiffen with arousal before my eyes."
            mc "Hehe, if I tease you anymore, you might orgasm before me. So, let’s begin, shall we?"
            play sound cum
            show dominatrixend f2 with d
            play sound2 foreplay1
            "I lift myself up and adjust myself until our pussies are kissing. Then with our clits roughly touching I start to rock back and forth, taking us both to the depths of pleasure."
            mc "Mmmmphhh, you have such a cute pussy, you know? You’ll fit in nicely."
            "I grind back and forth, the friction applied against my clit sends shocks of intense pleasure throughout my body. She doesn’t hold back either as she starts to thrust her hips up and down."
            "To maintain my dominating composure, I hold back my moans of pleasure, and maintain a sultry, erotic eye-contract."
            "The pleasure is undeniable though, and eventually our practiced motions of sex become primal, lustful humping as we lose ourselves to the passion."
            mc "Ohhh, mmmphhh! Do you like my pussy? Mmphhh, I really want you to come with me."
            "I don’t forget to whisper dirty things every so often, my saccharine words are perhaps more powerful than any physical sexual stimulant."
            mc "Yeaahh, yeahhh… I’m close! Come for me, babe!"
            "I keep going, fucking even harder, working my hips like a dancer to push us both over the edge."
            play sound cum
            show dominatrixend f3 with d
            "Finally, we both pass the point of no return. My vision goes white as I’m filled with orgasmic pleasure, whilst below, my partner squirts slightly as she too climaxes."
            play sound cum
            stop sound2 fadeout 3.0
            "The two of us remain entwined in euphoria. Several waves of intense pleasure rushing through my nervous system as I continue to ride her as hard as I can."
            "After a few remaining moments of heated passion, we finish and relax. Letting my guard down slightly, I remain cuddled on-top of her for a few moments before rising again."
        "Male" if True:
            play music action
            show dominatrixendb
            if tan == 1:
                show dominatrixendbtan
            if hair == 1:
                show dominatrixendh black
            if hair == 2:
                show dominatrixendh blonde
            if piercingson == 1:
                show dominatrixendpiercings
            show dominatrixendcollar
            show dominatrixenddom 1
            show dominatrixend 1
            with d
            mc "Aaahhh, I can feel your hard cock already pressing up against my butt. Tchh, all I did was sit on you."
            "I use the leash to tug the collar of the man I’m toying with today. He’s fresh meat, and there’s nothing more I enjoy than playing with them as they’re indoctrinated into the club."
            "It’s not too different from when I was indoctrinated. They get to choose their punishment, and then how they get fucked."
            "This guy chose a gag, a collar, and for me to ravage his cock with my pussy."
            mc "Ohh, I can feel you twitching against my ass. Does that mean you want more? Do you want me to slide it into my slippery wet pussy?"
            "The poor sap nods as he ogles my body, taking a particular interest in my breasts."
            mc "Ohh? You like my big milkies? If you behave, I’ll let you see them."
            "He obediently nods again; I can actively feel his submission turn me on as my clit grows more sensitive and needy."
            play sound equip
            show dominatrixenddom 2
            with d
            "I unstrap my bra, letting it fall onto my partner as my breasts sway freely. As he watches, I can feel his cock throb enthusiastically."
            mc "Hehe, if I tease you anymore, you might cum before I’m satisfied. So, let’s begin, shall we?"
            play sound cum
            show dominatrixend v2 with d
            "I lift myself up, allowing his tip to press and prod against my pussy. Then, I sink down in a single, practiced motion, taking him to the depths of pleasure."
            play ambience sex
            play sound2 foreplay1
            "Wasting no time, I start to rock my hips back and forth. My pussy tightens and teases each inch of his shaft with each motion."
            mc "Mmmmphhh, what a nice cock… You’ll fit in nicely."
            "I grind back and forth, ensuring his cock hits all the deep pleasurable spots within me. He doesn’t hold back either as he starts to thrust his hips up and down."
            "To maintain my dominating composure, I hold back my moans of pleasure, and maintain a sultry, erotic eye-contract."
            "The pleasure is undeniable though, and eventually our practiced motions of sex become primal, lustful pounding as we lose ourselves to the passion."
            mc "Ohhh, mmmphhh! Do you like my pussy? Mmphhh, I really want you to fill it up."
            "I don’t forget to whisper dirty things every so often, my saccharine words are perhaps more powerful than any physical sexual stimulant."
            mc "Yeaahh, yeahhh… I really want you to cum for me."
            "I keep going, fucking even harder, working my hips like a dancer to push us both over the edge."
            play sound cum
            show dominatrixend v3 with cum
            play sound cum
            show dominatrixend v3 with cum
            "Finally, we both pass the point of no return. My vision goes white as I’m filled with orgasmic pleasure, whilst below, my partner lets loose a torrent of thick cum."
            play sound cum
            show dominatrixend v3 with cum
            play sound cum
            show dominatrixend v3 with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 3.0
            "The two of us remain entwined in euphoria as I’m filled up. Several streams of hot cum guzzling deeply into my waiting room as I continue to ride him as hard as I can."
            "After a few remaining moments of heated passion, we finish and relax. Letting my guard down slightly, I remain cuddled on-top of him for a few moments before rising again."
    play sound equip
    scene bg dungeon with d
    call clothesdom from _call_clothesdom_2
    show mce horny
    with d
    mc "Not bad, meat. Welcome to the club!"
    "And so, I was a kinky top for the rest of my life."
    "Funny how the smallest decisions can dictate the future like that."
    play sound success
    if de == 0:
        $ de = 1
        "Dominatrix Outfit unlocked!"
    scene bg black with d
    "The End…"
    stop music fadeout 1.0
    "Or… is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings
label yokoending:
    $ yye = 1
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    scene bg black with d
    play music toko fadein 20.0
    "About one year later…"
    play sound2 foreplay2
    play ambience sex
    scene bg bedsex
    show yokoselfcestb
    if tan == 1:
        show yokoselfcestbtan
    if pregnancyshowing == 1:
        show yokoselfcestbp
        if tan == 1:
            show yokoselfcestbtanp
    if hair == 1:
        show yokoselfcesth black
    if hair == 2:
        show yokoselfcesth blonde
    show yokoselfcest alt1
    with d
    "Here I am, my best friend and often fuckbuddy licking out my pussy."
    "Whilst [crush]'s cock pushes inside of her pussy, his balls on my face."
    "You’re probably wondering how I ended up in this situation, aren’t you?"
    "Well…"
    stop sound2 fadeout 3.0
    stop ambience fadeout 3.0
    scene bg class with d
    show yokob:
        xpos 1200
    show yokoo uniform:
        xpos 1200
    show yokoe happy:
        xpos 1200
    call clothesformal from _call_clothesformal_37
    show mce happy
    with d
    yoko "[mc], [mc], heeyyyy!"
    mc "[yoko]! Why don’t you come eat some lunch with me?"
    "[yoko], the girl I had fatefully ran into at a club, had now become a NeoHero Student in the year below me."
    "This is no small feat. NeoHero Student is the best college in the country for a reason, and for [yoko] to pass the assessment to join means she has potential to be an excellent hero."
    "Although part of that is attributed to the fact, she has one of the most powerful super powers I’ve ever seen."
    "By simply digesting the body fluids of any other individual, she’s capable of not only transforming into them, but completely mimicking their powers."
    show mce neutral with d
    "Yeah… Body fluids… You’re probably wondering how that happens, right?"
    show mce happy2
    show crushb:
        xpos 50
    show crushe happy:
        xpos 50
    show yokoe horny
    with d
    "You’re probably aware that I have a crush, called [crush]. While I have actually had sex with him, I was never brave enough to ask them to be my boyfriend. [yoko] was instantly smitten by him the same way I was."
    "And [yoko] isn’t stupid! She could tell I liked him too, and she knew his strength power would be perfect for passing the test."
    hide crush with d
    "So, [yoko] set a plan in motion. I wasn’t entirely comfortable with the idea, but I couldn’t resist her puppy-dog eyes and ended up relenting."
    scene bg black with d
    show bg bedroomnight
    call clothesformal from _call_clothesformal_38
    show mce neutral
    show yokob:
        xpos 1200
    show yokoo uniform:
        xpos 1200
    show yokoe laughing:
        xpos 1200
    with d
    "Step 1. Make out with [yoko], mixing saliva and enabling her to turn into me."
    "Step 2. Invite [crush] to my dorm under a fairly innocent guise."
    "Step 3. [crush] walks in and sees two of me, and we both seduce him."
    "Step 4. [yoko] gets a messy creampie, we make sure to collect some of the cum, and then she transform into [crush] for the test."
    scene bg black with d
    "..."
    scene bg bedroomnight
    call clothesformal from _call_clothesformal_39
    show mce horny
    show yokomcdisguise:
        xpos 1200
    show crushb:
        xpos 50
    show crushe neutral:
        xpos 50
    with d
    crush "T-There’s two of you?!"
    mc "Yep! I used a friend of mine’s powers to temporarily clone myself so I could surprise you!"
    yoko "Hello, I’m the clone! We’re going to have lots of fun smashing today, hehehe."
    crush "Woah, I don’t know what to say… Doesn’t three players make smashing pretty hard to balance, though?"
    yoko "No, you dolt, we’re going to fuck you!"
    show crushe laughing with d
    crush "O-Oh!"
    play sound2 foreplay2 fadein 3.0
    scene bg bedsex
    show yokoselfcestb
    if tan == 1:
        show yokoselfcestbtan
    if pregnancyshowing == 1:
        show yokoselfcestbp
        if tan == 1:
            show yokoselfcestbtanp
    if hair == 1:
        show yokoselfcesth black
    if hair == 2:
        show yokoselfcesth blonde
    show yokoselfcest alt1
    with d
    "Here I am, my best friend and often fuckbuddy licking out my pussy."
    "Whilst [crush]'s cock pushes inside of her pussy."
    "I’m pretty sure she was a virgin, yet she takes it like a champ, cooing as her slippery pussy is filled up."
    play ambience sex
    "I do my best to playfully add to the sensation by licking at [yoko]’s clit, my tongue indirectly grazing [crush]’s cock as he slides it back and forth."
    yoko "Aaahhh, wow! I can’t believe your cock is inside of me, [crush]!"
    "I’m not {i}that{/i} jealous, considering I probably love [yoko] more than I love [crush]. But then again, it’s not just that I’m watching [crush] fuck [yoko], it’s also that I’m watching [yoko] fuck [crush]…"
    "Maybe I’d feel a bit better if I was getting fucked too. Maybe I should afterwards!"
    "With some vigor renewed, I slide my tongue up and down [crush]’s thrusting cock. The view is amazing from down here, I love watching [yoko]’s bubble butt jiggle at the apex of each thrust."
    "And she doesn’t simply let herself be fucked, she wiggles her hips back and forth, making each thrust a little harder."
    "Diligently she maintains her flicking tongue against my clit, and that pleasure never stops building as my back arches and my toes curl. I’m starting to enjoy this more and more."
    mc "Aaahhh, yes! Fuck my clone’s pussy, [crush]! Aaahhh!"
    yoko "Mmphh, yeah! This is so fucking good, haaahh… haaahhh. *Lick, slurp*"
    crush "I didn’t realize your wonderful pussy could get any tighter, [mc]."
    "H-Hey, I don’t know whether I should be offended by that or not."
    "At any rate, we all seemed to be close to coming. [yoko]’s pussy rhythmically clenched around his cock, as she does her best to milk him dry as he pounds into her sloppy, wet puss."
    "She’s really starting to moan now, her tongue work slowing down slightly as she’s overwhelmed with pleasure. I keep up my tongue against her clit, and soon she’s unable to hold back as she comes."
    yoko "Aaahh, aaahhhh… Y-Your tongue, and the cock… Being completely used by the two people I love so much! Aaahhh, I-I can’t stop from coming!"
    "[yoko] gets off way before I do, setting off a long full-body orgasm as my own creeps ever closer."
    "[crush] continues to pound [yoko], accelerating as his cock swells up and prepares to unload."
    play sound cum
    show yokoselfcest alt2 with cum
    play sound cum
    show yokoselfcest alt2 with cum
    "And before I know it, her tight, squeezing cunt robs his orgasm and cum spills freely into her."
    play sound cum
    show yokoselfcest alt2 with cum
    play sound cum
    show yokoselfcest alt2 with cum
    stop ambience fadeout 2.0
    stop sound2 fadeout 2.0
    "Several loads of ejaculate seep directly into her, whilst many overflow and spray onto her ass and my face."
    yoko "Haaahh, god yes! That’s exactly what I needed! Mmphhh…"
    play sound cum
    show yokoselfcest alt3 with d
    "After almost thirty whole seconds of sustained peak-pleasure sex, [crush] inevitably pulls out and causes even more cum to dribble down my face, all seeping out of [yoko]’s well-fucked pussy."
    "I don’t even know how I feel about this anymore. I just know a part of me wants a slice of pie too."
    scene bg black with d
    "…"
    show yokoending with dissolve
    "And so, with [crush]’s body combined with overwhelming power, [yoko] easily beat the assessment."
    "What became of us all after that?"
    "I thought it was only natural for me to try and start seriously dating [crush]."
    "After all, [yoko]’s little trick had worked well to get us closer than ever, and it may have just been the push I needed to officially ask him to be my boyfriend."
    "Unfortunately… [yoko] didn’t appreciate being left out."
    "At every turn, [yoko] seemed to be there to hinder our interactions."
    "I even had sex with him once, only for it to have been [yoko] the entire time!"
    "She was getting beyond obsessive. The prospect of [crush] and I dating and leaving her alone haunted her to the core."
    "It got worse than that too. I’d go clubbing with friends, and she’d be there. I’d go shopping, and run into her."
    show red:
        alpha 0
        linear 5 alpha 0.5
    "I'd return home."
    "She"
    "was"
    "there."
    yoko "Hehehe, hehehehehe... You'll date me, won't you, [mc]? After all, I can be everything and everyone you could ever want."
    "I didn’t really know what to do."
    "I guess dating [yoko] can’t be that bad, right?"
    "At least I had a safeword."
    scene bg black with d
    "The end…"
    stop music fadeout 1.0
    "Or… is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings
label sexaddictending:
    $ sae = 1
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    play music intro
    scene bg class
    show mc:
        xpos 300 ypos 300
    show pinkbody 0:
        xpos 300 ypos 300
    show mcpiercings blank:
        xpos 300 ypos 300
    show mccatears blank:
        xpos 300 ypos 300
    show mch:
        xpos 300 ypos 300
    show mco:
        xpos 300 ypos 300
    show pinkhair 0:
        xpos 300 ypos 300
    call clothesuniform from _call_clothesuniform_2
    show mce horny:
        xpos 300 ypos 300
    with d
    mc "Haha, ahaha, haha…"
    "Standing in class, I recite the line from the textbook as my tutor had requested."
    show supervisor:
        xpos 1200
    "The tutor I had fucked last night, and allowed to have a fresh creampie in my pussy. I still remember the way it felt."
    play sound equip
    scene bg class
    show mc:
        xpos 300
    show pinkbody 0:
        xpos 300
    show mcpiercings blank:
        xpos 300
    show mccatears blank:
        xpos 300
    show mch:
        xpos 300
    show mco:
        xpos 300
    show pinkhair 0:
        xpos 300
    call clothesuniform from _call_clothesuniform_3
    show mce horny:
        xpos 300
    with d
    "As I stood and repeated what was asked of me, I could feel a buzz between my legs. Hehe, the vibrator inside my pussy was slowly getting faster."
    "That was [hana]’s doing, I’m sure! That sneaky, invisible slut."
    scene bg class
    show mc:
        xpos 300 ypos 300
    show pinkbody 0:
        xpos 300 ypos 300
    show mcpiercings blank:
        xpos 300 ypos 300
    show mccatears blank:
        xpos 300 ypos 300
    show mch:
        xpos 300 ypos 300
    show mco:
        xpos 300 ypos 300
    show pinkhair 0:
        xpos 300 ypos 300
    call clothesuniform from _call_clothesuniform_4
    show mce horny:
        xpos 300 ypos 300
    show upskirt
    with d
    "My soaked panties drip as I finish reading and return to my seat."
    "Dressed in my slutty formal wear, the only reason I wear panties at all is because I have a slight panty fetish, otherwise I’d be tempted to go commando in this short skirt and constantly tempt fate with an upskirt flash."
    "I keep my legs partially open as I sit down, so if anyone were to turn back, they’d get a glimpse between my legs anyway. [tina] does so briefly, and sticks her tongue out playfully. I’ll probably join her and Thad later for a threesome."
    "Unless [susu] wants to go clubbing, it is Wednesday after all."
    "Haaahh, I lean back at my desk and sigh… I’m so damn horny all the time…"
    "Almost everything I think about these days is sexual, or sex related."
    if qsexuallyexperienced == 0:
        "My body count is probably in the 100s at this point. Hard to believe I was a virgin before college."
    elif True:
        "My body count is probably in the 100s at this point. Hard to believe it was only a few before college."
    "Fortunately, it’s almost lunchtime…"
    stop music fadeout 3.0
    scene bg black with d
    scene bg class with d
    show student1:
        xpos 50
    show student2
    show student3:
        xpos 1200
    with d
    stua "What’s so special about lunchtime at Hero Academy?"
    stub "Well… Rumour has it, in the male toilets, there’s a girl in one of the stalls who will fuck anyone…"
    stua "Pfft, and you believe that rumour?"
    stuc "Why don’t we just check?"
    scene bg black with d
    "…"
    play ambience sex fadein 2.0
    play sound2 foreplay2 fadein 5.0
    show sexaddictendingb
    if tan == 1:
        show sexaddictendingbtan
    if hair == 1:
        show sexaddictendingh black
    if hair == 2:
        show sexaddictendingh blonde
    if piercingson == 1:
        show sexaddictendingpiercings
    show sexaddictending 1
    with d
    "For a while now, a female student can be heard moaning from the third floor’s male toilets. What was once the quietest part of the entire building, was now a place where male students would frequent."
    "Somehow, not a single person involved reported this. This is likely due to the high-quality service offered by the student…"
    mc "Aahhh, mphhh, haaahhh… These are some really nice cocks today! Aahhh, and you, inside me, you’re a new one aren’t you!"
    "The student does not reply, but his cock throbs and that’s all I care about in the end."
    "My hands rapidly jerk off the two guys at the side at roughly the same speed as the guy pounding my pussy. My goal is to try and get all three of them to shower me in their hot cum simultaneously."
    mc "Mmphh, god I’m so wet… Does my pussy feel good, hmm?"
    stua "Yeah, it’s amazing."
    stub "I can’t believe this slut is real."
    stuc "Don’t jinx it, she might vanish and it turns out we were all just circle jerking."
    stua "Hey, don’t say that, I’m trying to fuck her over here."
    mc "Hehehe, oh boys, don’t fight. Each of you can have a turn with my pussy if you can last long enough."
    "The cock within me tightens and throbs, eliciting excitement from my pussy as it squeezes and sucks in response."
    "All three of them were pretty unsure and nervous at first, but that chat seems to have emboldened them. The one fucking me starts to rock his hips faster, plapping and slapping against my pussy with vigor."
    mc "Aaahh, yesss! Fuck this slutty pussy, she can’t get enough!"
    "Getting fucked while jacking off two cocks never fails to get me off. The pleasure is always so overwhelming, and exciting, especially when I manage to get a new face to fuck me."
    "Ohh, fuck! I’m getting really close now. My hips rock back and forth, eagerly trying to suck as much pleasure out of my partner as possible, my pussy tightly squeezing around his throbbing member."
    mc "Ohhh, f-fuck! I-I’m gonna-"
    play sound cum
    show sexaddictending 2 with cum
    play sound cum
    show sexaddictending 2 with cum
    play sound cum
    show sexaddictending 2 with cum
    "To my surprise, he cums almost exactly as I do! And my handjobs shortly reach their peak too, as I’m doused in hot cum from my right and then my left."
    play sound cum
    show sexaddictending 2 with cum
    play sound cum
    show sexaddictending 2 with cum
    play sound cum
    show sexaddictending 2 with cum
    stop ambience fadeout 2.0
    stop sound2 fadeout 2.0
    "Load after load, I’m showered in sticky white. The feeling of pure bliss is overwhelming as we all orgasm together."
    "My fervent hips don’t stop grinding for a second throughout, and just as his cock grows sensitive and withdraws…"
    mc "Okay, who’s next?"
    "I’m ready for more."
    "No, actually… I need more. I’m not satisfied yet."
    "I will never, ever, be satisfied."
    if persistent.bathroomscare == False:
        $ persistent.bathroomscare = True
        play sound rip
        show sexaddictendingbathroom
        pause 0.05
        scene bg black
    elif True:
        scene bg black with d
    "The End…"
    stop music fadeout 1.0
    "Or… is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings
label prostituteending:
    $ pe = 1
    if pregnancyshowing == 1:
        $ pregnancyshowing = 0
    scene bg black with d
    play music intro
    "It all started with a need for money."
    "$72,000."
    scene bg street
    show flashing
    if pregnancyshowing == 1:
        show flashing p
    if tan == 1:
        show flashingtan
        if pregnancyshowing == 1:
            show flashingtanp
    if piercingson == 1:
        show flashingpiercings
    if hair == 1:
        show flashingh black
    if hair == 2:
        show flashingh blonde
    with d
    "Flashing my breasts for $20."
    scene bg bar
    show bar2a
    with d
    "Letting someone grope my ass for $30."
    scene bg bed with d
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
    "Sucking someone’s cock for $40."
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
    "Letting someone fuck me for $80."
    scene bg black with d
    "Slowly, but surely, I built myself up to do more degenerative actions for a higher pay out."
    "However, there was an unspoken reason behind this development in my character."
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
    show analbukkake 1
    with d
    "The truth is, I adored the sex, the attention, and the money."
    "When I was an innocent virgin, I hadn’t even realized that my personality would essentially make me love being a prostitute."
    "I can’t get enough. The empowering thrill of enticing a man with my body, collecting their hard-earned cash, and enjoying every moment of the act."
    "It’s hilarious in a twisted sense. I’m getting just as much enjoyment and pleasure as they are, maybe even more. Why am I the one getting paid? Hehehe, ahahaha."
    scene bg shopsday with d
    "I fucked my way throughout college and become incredibly wealthy as a result. Almost every single night, I’d scope out the male dorms, or the shopping centre."
    scene bg maledormsnight with d
    call clothesbar from _call_clothesbar_14
    show mce horny
    with d
    "It was addicting. I’d sit around at home twiddling my thumbs. Masturbation wasn’t really satisfying me enough, so I’d put on a sexy outfit, go outside and simply find a man."
    show student3 with d:
        xpos 1200
    "Didn’t really care what they looked like. Sure, I like fucking the hot ones, but in an erotic, degrading sense, letting the less than average men fuck me got me off just as much."
    scene sidewayssexb
    if pregnancyshowing == 1:
        show sidewayssexe pregnant
    if tan == 1:
        show sidewayssexbtan
        if pregnancyshowing == 1:
            show sidewayssexbtanp
    if hair == 1:
        show sidewayssexh black
    if hair == 2:
        show sidewayssexh blonde
    if piercingson == 1:
        show sidewayssexpiercings
    show sidewayssex 1
    show sidewayssex 1
    if pregnancyshowing == 1:
        show sidewayssexe pregnant
    with d
    "I ended up making over $100k, in addition to paying off my student debt."
    scene bg gloryholes with d
    "Despite my graduation, I decided to not become a hero in the end. I became a full-time prostitute instead, hiring out a small studio to conduct myself."
    "My business was pretty innovative. Here’s how it worked:"
    scene prostituteendb
    if tan == 1:
        show prostituteendbtan
    if hair == 1:
        show prostituteendh black
    if hair == 2:
        show prostituteendh blonde
    if piercingson == 1:
        show prostituteendpiercings
    show prostituteend 1
    show prostituteendjar 1
    with d
    "Pay a flat $50 for entry. When you enter, I’ll either be in one of two gloryholes, or I’ll be at the table ready to be used."
    "You don’t have to say a single thing, it’s complete free-use. Just come in and use me."
    "The hole at the back lets you fuck my pussy, and I can give blowjobs from the front."
    "If there are a few customers, sometimes I come out and let people spit roast me on the table."
    "This type of simple, low communication prostitution proved to be extremely popular."
    "It wasn’t long before I started to hire out other girls."
    scene holeb
    show holetina
    with d
    "What you’d see when you walked in would have looked like paradise."
    "A line of pussies, and you can pick and choose any one of them."
    play sound cum
    show hole cum with cum
    "You could take some doggy, maybe missionary, or maybe you’d rather get your cock sucked?"
    play sound cum
    show hole cum with cum
    "No matter what, though, despite owning the place, I was always there to get a good fucking too."
    scene bg black with d
    "Like… this one!"
    play music action
    play sound2 foreplay1
    play ambience sex
    scene prostituteendb
    if tan == 1:
        show prostituteendbtan
    if hair == 1:
        show prostituteendh black
    if hair == 2:
        show prostituteendh blonde
    if piercingson == 1:
        show prostituteendpiercings
    show prostituteendjar 2
    show prostituteend 2
    if tan == 1:
        show prostituteendclip 1
    show prostituteendborder
    with d
    mc "Aaahhh, mphhh, mmhh!"
    "With a cock pounding my pussy, and a cock in my mouth that I diligently service, I’m completely spit roasted in the centre of my studio."
    "This was one of my earlier fucks, I fondly remember the two taking turns, tossing in $50 after $50 to use me like a ragdoll."
    "It turned me on so much. The sex was so raw, so wet, and all three of us relish it."
    "Despite the two boys seeming to have all the power over me, though, my extremely high amount of sexual experience shines through."
    "The way I roll my hips, tense my muscles, and swirl my tongue. I’m getting 110%%%% out of me and the customers."
    "That said, my body spasms constantly with pleasure, and every so often I lose myself in the indulgence of a powerful orgasm."
    mc "Mmphhh, aaahhhh- mmm!"
    "My pussy clenches tightly, sucking the customer’s throbbing cock in a needy attempt at coaxing an intense orgasm. Whilst the cock in my mouth swells up and prepares to explode."
    play sound cum
    if tan == 1:
        show prostituteendclip 2
    show prostituteend 3 with cum
    play sound cum
    show prostituteend 3 with cum
    "Copious amounts of cum shoot into my pussy and the back of my throat. So hot and messy, I take it all as the three of us continue to fuck at a relentless pace."
    play sound cum
    show prostituteend 3 with cum
    play sound cum
    show prostituteend 3 with cum
    "We keep going into they’re both sensitive and flaccid. I’d managed to squeeze every drop of pleasure out that as possible, even coming. It’s a wonder that I’m not paying them."
    "And yet… another two $50s are dropped as the men swap."
    guy1 "Time for me to get a piece of that ass."
    guy2 "Let’s see if this tongue work is all its hyped up to be."
    mc "Be my guest, boys, I’ll happily fuck you as long as you keep that jar nice and full."
    play sound cum
    if tan == 1:
        show prostituteendclip 3
    show prostituteend 4 with d
    "And then I was fucked again."
    "And again."
    "I don’t even know if I do it for the money or sex anymore."
    stop ambience fadeout 3.0
    stop sound2 fadeout 3.0
    scene bg black with d
    "The End…"
    stop music fadeout 1.0
    "Or… is it?"
    if pregnant == 1 or bloated == 1:
        $ pregnancyshowing = 1
    jump endings


jump endingm

init:
    $ persistent.bathroomscare = False
    $ de = 0
    $ pe = 0
    $ yye = 0
    $ sae = 0
    $ mpe = 0
    $ sge = 0
    $ yge = 0
    $ vie = 0
    $ ege = 0
    $ dae = 0
    $ lge = 0
    $ endingsseen = 0
    $ endingoverride = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label computer:
    scene bg computer with d
    "Ahh, everything is at my finger tips... Where to begin?"
    menu computermenu:
        "Study" if True:
            "Spend half a day studying?"
            menu:
                "Sure!" if True:
                    "I buckle down and study my course. I feel smarter in the process."
                    call studyquiz from _call_studyquiz
                    play sound success
                    $ smartsgain = 1
                    call smartsgain from _call_smartsgain_1
                    "(+[fsmarts] Smarts)"
                    "Woops, it's starting to get late."
                    jump postworktrans
                "Nah..." if True:
                    jump computermenu
        "LonelyFans" if True:
            if lonelyfans == 0:
                $ lonelyfans = 1
                "So this is it... The website where women sell risque photos of themselves."
                "Could I do something like that...?"
                "I cautiously sign up using my new 'money making' online persona and browse some of the top creators for examples."
                "Wow, this doesn't look as easy as I thought. I'll need to build a large following, market well, and upload consistently."
                "And personally... I don't even know how far I'm willing to take this."
                "Regardless, my account is setup, and with a few social medias linked I should at least get a few clicks if I upload anything."
                play sound success
                "Oh, how interesting, I already appear to have a follower! They must have seen my account on the new users page."
                $ fol += 1
                "(As you build an online presence, you will gain followers!)"
                "(More followers = more money when uploading content!)"
            if lonelyfans == 1:
                jump lonelyfansroute
        "ChatFap" if True:
            if chatfap == 0:
                $ chatfap += 1
                "While doing my research I heard about this 'chat fap' website where 'cam girls', or 'camera girls' earn a lot of money."
                "I have no idea what fapping, or camera girls are, so let's just check..."
                "Oh my goodness! I accidentally saw... well, uhm, {i}everything{/i}!"
                play sound success
                $ sdgain = 1
                call sdgain from _call_sdgain_23
                "(+[fsd] Sexual Desire)"
                call sdgain from _call_sdgain
                if sd < 35 or shame > 70:
                    "There's no way I could do anything like this!"
                elif True:
                    "I guess this is certainly a way to earn money... Filming myself isn't too different from taking pictures."
                    play sound success
                    $ shameloss = 1
                    call shameloss from _call_shameloss_11
                    "(-[fshame] Shame)"

            if chatfap == 1:
                menu cf1:
                    "Sexual Desire: [sd], Shame: [shame]"
                    "Start a stream. (35 Sexual Desire and <70 Shame)" if True:
                        if sd < 35 or shame > 70:
                            "Nuh-uh!"
                            jump cf1
                        jump chatfaproute
                    "Close the website and delete your browser history!" if shame >= 80:
                        jump computermenu
                    "Back." if shame < 80:
                        jump computermenu
        "xTube (Gallery)" if True:
            if xtube == 0:
                $ xtube += 1
                "X... Tube? What's this rabbit hole I've stumbled upon?"
                "Ohh, oh my... It's porn!"
                if sd < 20:
                    "I'm definitely bookmarking this."
                elif True:
                    "Well, I'm not a very sexual person, but even I enjoy some porn once a week or so. I'll add this to my bookmarks."
                play sound success
                "(+1 Sexual Desire)"
                "Oh my goodness! I recognize some people on here... Now I just {i}have{/i} to know what they've been up to."
                "Heyy... Wait a second! A lot of this content is hidden behind a paywall. Well, that's how they get ya."


            if xtube == 1:
                jump gallery
        "Back" if True:
            play music rest
            if morning == 1:
                jump bedroommorning
            elif True:
                jump bedroom
jump bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

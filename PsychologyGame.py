player_name = 'Gandalf'
strikes = 0
patients_not_treated = ['Bogart Grimsby the Lesser', 'Chef Ardee', 'Velimir the Voracious', 'Lana Lupin', 'Geralt the Old Dragonslayer', 'Cateline the Innkeeper']
patients_not_treated = ['Bogart Grimsby the Lesser', 'Chef Ardee', 'Velimir the Voracious'] # Ethan's patients for testing
# patients_not_treated = ['Lana Lupin', 'Geralt the Old Dragonslayer', 'Cateline the Innkeeper'] # Alexa's patients for testing




def patient_select():
    print('\nWhom would you like to help next?\n')
    for i in range(len(patients_not_treated)):
        print(f'Patient {i+1}: {patients_not_treated[i]}')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > len(patients_not_treated)):
        player_choice = input('Please enter a number for one of the patients listed: ')
    if patients_not_treated[int(player_choice) - 1] == 'Bogart Grimsby the Lesser':
        bogart()
    elif patients_not_treated[int(player_choice) - 1] == 'Chef Ardee':
        ardee()
    elif patients_not_treated[int(player_choice) - 1] == 'Velimir the Voracious':
        velimir()
    elif patients_not_treated[int(player_choice) - 1] == 'Lana Lupin':
        lana()
    elif patients_not_treated[int(player_choice) - 1] == 'Geralt the Old Dragonslayer':
        geralt()
    elif patients_not_treated[int(player_choice) - 1] == 'Cateline the Innkeeper':
        cateline()
    return




def bogart():
    print(f'''\nKing: All my soldiers\' weapons have been quite shoddy as of late, and my order for 
more seems to have not gone through. Go to the Blacksmith, Bogart Grimsby the Lesser; I have 
already had one of my lords check in on him. He reported to me that Bogart is suffering from 
demonic possession which has kept him from sleeping. Rid Bogart of this demon and return to me 
afterwards, {player_name}.''')
    print('''\nYou kneel to the king, letting him know you will do his bidding. You summon a portal
and step through, arriving at the blacksmith\'s residence.''')
    print('''\nSmoke is not billowing from the chimney as it usually is. The King was right,
something is wrong with Bogart. You knock on the cottage door and wait. There is no answer,
but some faint shuffling can be heard emanating from a corner of the workshop.''')
    print(f'''\nYou: I am {player_name}, sorcerer of the King's court. Permit me entrance at
once or I will cast a spell to enter!''')
    
    
    print('\nWhat would you like to do?\n')
    print('1. Open the door with your wizardly hands.')
    print('2. Summon an earth sprite to open the door.')
    print('3. Cast eldritch pull to open the door.')
    player_choice = input('Enter the number for your choice: ')
    if int(player_choice) == 1:
        print('''\nYou grasp the knob of the door with your knowledge-imbued hands. You turn the knob and force
the door open. You prepare to enter Bogart\'s residence.''')
    elif int(player_choice) == 2:
        print('''\nYou summon an earth-composed sprite. It erupts from the dirt and immediately opens the door,
after which it collapses into a pile of mud, having completed its life\'s purpose. You step past the
pile of mud and prepare to enter the residence.''')
    elif int(player_choice) == 3:
        print('''\nYou cast eldritch pull; a deep-red tentacle emerges from a purplish-black void and wraps itself
around the muddy door handle. It pushes the door open and retreats back into the void. The portal
dissipates, and you are left with an open doorway to enter.''')
    else:
        print('''\nYou grasp the knob of the door with your knowledge-imbued hands. You turn the knob and force
the door open. You prepare to enter Bogart\'s residence.''')
    
    
    print('''\nYou enter the blacksmith\'s residence. A pungent smell of sweat and onion hits you. 
You find the blacksmith sitting on the edge of his cot, blankly staring off into space. He is 
wearing tattered animal skins. His hair is dark black and greasy. He has deep, sunken bags under 
his eyes. As you approach, you can tell the smell is coming from him. ''')
    print('\nYou: Bogart Grimsby?')
    print('\nBogart briefly looks at you before he returns to staring off into space.')
    
    
    print('\nWhat would you like to do?\n')
    print('1. Investigate Bogart\'s room.')
    print('2. Try to talk to Bogart again.')
    print('3. Refer to parchment')
    print('4. Attempt to treat Bogart')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
        player_choice = input('Please enter a number for one of the choices listed: ')
    while int(player_choice) != 4:
        if int(player_choice) == 1:
            print('''\nThe animal skin blankets and pillows are strewn about the room; You can tell he\'s been restless.
The candles around the room are lit and the wax has melted nearly to the base. They haven\'t been
lit for quite some time, possibly overnight.''')
            print('\nWhat would you like to do?\n')
            print('1. Investigate Bogart\'s room.')
            print('2. Try to talk to Bogart again.')
            print('3. Refer to parchment')
            print('4. Attempt to treat Bogart')
            player_choice = input('Enter the number for your choice: ')   
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
        elif int(player_choice) == 2:
            print('\nYou ask Bogart what has him bothered.')
            print('''\nBogart: I haven\'t slept a wink in days. I can\'t get any work done, and I\'m miserable. Demons
must be after me. You should tell them to go after that slovenly fool Bogart the Greater.''')
            print('\nWhat would you like to do?\n')
            print('1. Investigate Bogart\'s room.')
            print('2. Try to talk to Bogart again.')
            print('3. Refer to parchment')
            print('4. Attempt to treat Bogart')
            player_choice = input('Enter the number for your choice: ')
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
        elif int(player_choice) == 3:
            print('\nYou refer to your notes from the King\'s briefing.')
            print('Notes: Blacksmith order for new weapons not gone through; Bogart Grimsby the Lesser has demons that prevent sleep')
            print('\nWhat would you like to do?\n')
            print('1. Investigate Bogart\'s room.')
            print('2. Try to talk to Bogart again.')
            print('3. Refer to parchment')
            print('4. Attempt to treat Bogart')
            player_choice = input('Enter the number for your choice: ')
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
    
    
    print('\nYou refer to your list of tools to see what might help Bogart.')
    print('What will you use?\n')
    print('1. Salve of Melatonin')
    print('2. The Holy Bible')
    print('3. Incantation List')
    print('4. Spell Book')
    print('5. Talk Therapy')
    print('6. Paarthurnax\'s Prodigious Potion of Pineal Prowess')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 6):
                player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou give Bogart the salve and bid him farewell. After a few days the King summons you to
tell you that the equipment Bogart has been producing is far superior to his previous products.
It can be assumed that you cured Bogart's disorder.''')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
    elif int(player_choice) == 2:
        print('''\nYou read Bogart a few of your favorite verses from the Bible to rid the demons from his mind. 
After you are sure the demons are gone, you bid him farewell. After a few days, the King summons 
you and scolds you for your shoddy work. The only noticeable difference in the poor equipment is 
that there are now crosses carved into the poorly smelted iron.''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        strikes += 1
    elif int(player_choice) == 3:
        print('''\nYou read a few incantations from your list and bid Bogart farewell. After a few days, the King 
summons you and scolds you for your shoddy work.''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        strikes += 1
    elif int(player_choice) == 4:
        print('''\nYou cast a spell that dispels demons. Bogart is satisfied with your work, and you bid him 
farewell. After a few days, the King summons you to scold you for your shoddy work. ''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        strikes += 1
    elif int(player_choice) == 5:
        print('''\nYou talk to Bogart about his sleep issues. He is not satisfied with your treatment, but you do 
not know what else to do, so you bid him farewell. After a few days, the King summons you to 
scold you for your shoddy work''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        strikes += 1
    elif int(player_choice) == 6:
        print('''\nAfter a few days the King summons you to tell you that the equipment Bogart has been producing 
is far superior to his previous products. It can be assumed that you cured Bogart's disorder.''')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
    

    print('\nDisorder reveal: Bogart suffered from an acute case of insomnia.')
    print('\nSolution: Either by bolstering the pineal gland or by dosing him with melatonin, Bogart\'s insomnia is cured.')
    return




def ardee():
    return




def velimir():
    return




def lana():
    print('''\nLord Lanius has been complaining about the state of his wife, Lana. He claims that she was 
attacked by a furry beast. Since this attack, Lana has seemed strange. She cannot remember key details 
about Lanius, their children, or their home. A key to keeping my kingdom happy is keeping my Lords happy; 
I need you to go out to Lord Lanius’ land and cure Lana. Be off!''')

    print('''\nYou dismount your horse and head off the main road onto a cobbled path that leads to a grand cottage. There is no 
mistaking this impressive home; this is Lord Lanius\’ residence. You approach the home and rap your knuckles on the hard wooden door. 
You hear a collection of nigh-inaudible mumbles as a pair of footsteps approaches the door. The door opens, revealing 
Lord Lanius and his wife, Lana. Lanius is well put together; his garb is stunning and of the highest quality. Lana has 
matted long brown hair and a confused look on her face. There is an apparent swelling on the back of her head. She opens 
her mouth to speak, but Lanius precedes her.''')
   
    print('''\nLanius: Ah, court sorcerer! I was told I could expect your arrival. Please, enter!''')
    print('''\nLanius guides you and Lana to the study where you take three a seat.''')
    print('''\nYou: hank you for your hospitality, Lord. Lana, I would like you to recount the attack by the hands of the beast.''')
    print('''\nLana gives Lanius a worried glance. Lanius gestures with his hand, indicating she should tell her story.''')
    print('''\nLana: I cannot seem to recall much these days. My attack least of all. The only things I have to remember it by are my injuries.''')
    print('''\nLana points to the bump on her head you noticed earlier. She then stands up and lowers the back of her bloody shirt to reveal large 
lacerations in the pattern of a claw. They are not quite gaping, but they appear moist; she is still lightly bleeding. The wound seems far from clean.''')
    print('''\nLana: I have no issue forming new memories, but I seem to have trouble recalling other information. I still require guidance around 
Lanius’ land. I don’t know what has happened, but it terrifies me to no end. Please tell me you can help me court sorcerer!''')
    print('''\nYou: Do not fear. I have the cure for what ails you. Firstly, I will cure your injuries.
\nYou cast a spell of cauterization that seals the wounds on her back; both safe and sterile.''')

    print('What will you use?\n')
    print('1. Snake Oil')
    print('2. Potion of Hippocampian Restoration')
    print('3. A shard of pure cold summoned from the deepest depths of the void (a gel icepack from Walgreens)')
    player_choice=input('Enter number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 3):
                player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou: Here. This should cure your memory. Make sure to drink every last drop within the salve.''')
        print('''\nThe couple thanks you for your assistance and sees you out the front door. You return to the 
King’s castle and after a few days you are summoned to the court to hear about your progress.''')
        print('''\nKing: Absolutely nothing has changed! I am not sure what you did, but Lanius is furious. 
My rule over this land grows weaker because of your failings! I can only put up with your incompetence 
for so long. Begone sorcerer. I have no need of you for now.''')
        patients_not_treated.remove('Lana Lupin')
        add_strike()
    elif int(player_choice) == 2:
        print('''\nYou: Here. This should cure your memory. Make sure to drink every last drop within the salve.''')
        print('''\nThe couple thanks you for your assistance and sees you out the front door. You return to the 
King’s castle and after a few days you are summoned to the court to hear about your progress.''')
        print('''\nKing: Excellent work sorcerer. Lana’s wounds are healed, and her memory has returned to normal. 
Lanius has been singing your praises since her curing. Lana now remembers the beast that attacked her and where 
it went. I have tasked my men to take care of the beast. In other news, my rule over this land has been solidified 
due to your work. Well done. I have no need of you for now. Return to your study.''')
        patients_not_treated.remove('Lana Lupin')
    elif int(player_choice) == 3:
        print('''\nYou: Here. This should reduce the swelling of your head. Press this shard to the injury on your 
    head. I am afraid there is nothing I can do about your memory.''')
        print('''\nThe couple thanks you for your assistance and sees you out the front door. You return to the 
King’s castle and after a few days you are summoned to the court to hear about your progress.''')     
        print('''\nKing: Absolutely nothing has changed! I am not sure what you did, but Lanius is furious. 
My rule over this land grows weaker because of your failings! I can only put up with your incompetence 
for so long. Begone sorcerer. I have no need of you for now.''')
        patients_not_treated.remove('Lana Lupin')
        add_strike()
    print('\nDisorder reveal: Lana was suffering from a case of retrograde amnesia.')
    print('\nSolution: The potion of Hippocampian restoration was the correct solution. It repaired damage to the hippocampus, restoring her memories.')

    return




def geralt():
    print('''\nKing: One of my oldest and greatest warriors has been consistently terrorized 
since his retirement. We fought side by side in our youths. I did not give up on him then, and 
I am not going to now. I need you to go to him and cure him. Do not fail me.''')
    print('''\nYou make a turbulent trip up Mount Helmir until you reach Geralt’s cottage. 
He is outside his cottage chopping wood; smoke billows from his cottage’s chimney. It has 
grown quite brisk at such high altitude. Geralt spots you and slowly approaches you before 
his face gleams with relief. He wraps his arms around you and embraces you. Tears stream 
down his cheek.''')
    print('''\nGeralt: You have no idea how glad I am to see you sorcerer. My life has 
been a waking nightmare. I don’t know what to do. I have fought many battles by myself, 
but this is one I cannot seem to win.''')
    print('''\nYou: Be at ease, old dragonslayer. I will do everything in my power to 
save you. Please describe what has been happening to you.''')
    print('''\nGeralt: I feel fine when I am keeping occupied, but whenever my hands 
grow idle, my heart begins to race. I begin to sweat, and my muscles start to tense. 
I recall old battles I have had. Both against beast and man. I feel as if I am there, 
reliving every strike I dealt and every strike dealt to me. I can’t keep living like 
this; my mind grows weary from this constant assault. Someone must have placed a hex 
on me.''')
    print('''\nYou: I think I understand what is going on here, and I have what I need to cure you.''')
    print('\nWhat will you use to cure him?')
    print('1. Spell of Memory Erasure')
    print('2. Spell of Serotonin Reuptake Inhibition')
    print('3. Charm of Hex-Warding')
    print('4. The Holy Bible')
    player_choice=input('Enter number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou cast a spell of memory erasure on Geralt. You bid him farewell, and he retreats into his 
    cottage to rest. You head back to the castle and return to your quarters. After a few days, you are summoned 
    to the King’s court.''')
        print('''\nKing: I am not sure what you have done. My old friend does not complain of his same symptoms, so you have 
    cured him in that aspect. However, he does not seem to remember any of the memories we shared together, or 
    any of the battles he served in for that matter. You have done what I have asked. I am greatly saddened 
    by the results. Begone from my sight.''')
        patients_not_treated.remove('Geralt the Old Dragonslayer')
        add_strike()
    elif int(player_choice) == 2:
        print('''\nYou cast a spell of serotonin reuptake inhibition. The effects on Geralt will not be immediate, 
    you know, but you are certain this will alleviate some of his symptoms. You return to the castle and your 
    quarters therein. After a few days, you are summoned by the King.''')
        print('''\nKing: I am not sure what you have done sorcerer, but the worst of my friend’s symptoms have 
    been taken care of. Thank you for this great deed. Geralt served this nation valiantly in battle and I 
    would not have let him waste away. I am overjoyed with this result. I have no more need of you for now. 
    Begone sorcerer; until I am in need of you next.''')
        patients_not_treated.remove('Geralt the Old Dragonslayer')
    elif int(player_choice) == 3:
        print('''\nAdhering to Geralt’s advice, you give him a charm of Hex-Warding. You are sure that it 
    will rid him of his symptoms. You return to the castle and your chambers therein. After a few days you 
    are summoned to the King’s court.''')     
        print('''\nKing: I am not sure what you have done sorcerer, but the results have been astoundingly 
    bad. My old friend is spiraling into madness and whatever you have done has only made it worse. Words 
    cannot begin to describe the pain you have caused me. If you fail me like this again, I will see you 
    drawn and quartered. I cannot bear to look at you. Get out of my sight.''')
        patients_not_treated.remove('Geralt the Old Dragonslayer')
        add_strike()
    elif int(player_choice) == 4:
        print('''\nYou say a prayer for Geralt and bid him farewell. You return to the castle and your quarters 
    therein. After a few days you are summoned to the King’s court.''')     
        print('''\nKing: I am not sure what you have done sorcerer, but the results could have been better. 
    Geralt’s general state is better than what it was, but he is still severely impaired. He is getting 
    sleep at the very least, so for that I am thankful. This was not your best work. Begone from my sight 
    sorcerer.''')
        patients_not_treated.remove('Geralt the Old Dragonslayer')
        add_strike()
    print('\nDisorder reveal: Geralt the Old Dragonslayer was suffering from PTSD.')
    print('\nSolution: The spell of serotonin reuptake inhibition was the correct answer. This is a common treatment for PTSD patients as it treats some of their negative symptoms like anxiety and depression. SSRIs.')

    
    return




def cateline():
    print('''\nKing: Some of the visitors to my kingdom have been complaining that our largest inn is 
suffering from an uncomfortable and uninviting atmosphere. Head to the Bear Claw inn and talk with Cateline, 
the head innkeeper. See what you can find out and get that inn up and running again. We cannot be losing revenue 
because no one wants to stay in our village when they visit. Be off and do not return until you have 
remedied the situation.''')
    print('''\nYou head to the bustling metropolis that is the center of the kingdom. Among several taverns 
and shops, you spot the Bear Claw inn. You dismount your steed and hitch it to a nearby fence. You enter the 
inn and call out Cateline’s name. Several moments pass with no response. Those in the common area pay you 
little mind. You feel uninvited. You hear some rustling towards the back of the inn before a door closes. 
You investigate and call out Cateline’s name again. This time there is a mumbled response on the other side 
of the door.''')
    print('''\nCateline: You may enter, but please tell me you are alone.''')
    print('''\nYou assure her that you are alone and enter what seems to be her office.''')
    print('''\nYou: The King has sent me here among complaints that your inn is suffering from an uninviting 
atmosphere. What do you think this can be attributed to?''')
    print('''\nCateline: I know what is causing it. I have become a poor hostess as of late. I had an awkward 
exchange with a group of guests a few weeks back. Ever since then, any time I must talk to someone that I do 
not know, I am overcome with dread, I begin to sweat, I start tripping over words, and my face becomes flush 
with shame. I do not know what the cause of this is, but I am sick of it. How am I supposed to be a good hostess 
when I can hardly face my guests?''')
    print('''\nYou: That does seem rather problematic. I believe I know what the issue is, and I will do my best 
    to solve it.''')
    print('\nWhat do you choose?')
    print('1. Magical Book of Self-Help')
    print('2. The Holy Bible')
    print('3. Salve of Memory Repression')
    print('4. Charm of Extroversion')
    player_choice=input('Enter number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou give Cateline the Magical Book of Self-Help and return to your study at the castle. 
    After a few days, you are summoned by the King to review your progress.''')
        print('''\nKing: The Bear Claw is doing a lot better since your intervention. I do not know what 
    you have done, but it seems to have paid off. Guests feel much more welcome at the inn than they did 
    prior. I am not sure if this is a long-term fix, but you have done what I have asked of you. Good work. 
    Begone from my sight.''')
        patients_not_treated.remove('Cateline the Innkeeper')
        
    elif int(player_choice) == 2:
        print('''\nYou say a prayer for Cateline and return to your study. After a few days, the King summons 
    you to review your progress''')
        print('''\nKing: I am not sure what you did, but it has had no effect. Guests do not feel comfortable 
    at the inn. Cateline seems to be the source of this. You have failed me. Keep this up and I will not be so 
    forgiving. Begone from my sight.''')
        patients_not_treated.remove('Cateline the Innkeeper')
        add_strike()
    elif int(player_choice) == 3:
        print('''\nYou give Cateline a salve of memory repression to erase the awkward exchange with the guests 
    that she had a few weeks ago. You deem this to be the cause of her symptoms. You return to your study after 
    bidding her farewell. After a few days, you are summoned to the King.''')     
        print('''\nKing: The Bear Claw is doing a lot better since your intervention. I do not know what you 
    have done, but it seems to have paid off. Guests feel much more welcome at the inn than they did prior. I 
    am not sure if this is a long-term fix, but you have done what I have asked of you. Good work. Begone from 
    my sight.''')
        patients_not_treated.remove('Cateline the Innkeeper')
        add_strike()
    elif int(player_choice) == 4:
        print('''\nYou give Cateline a charm of extroversion and bid her farewell. You hope that this will help 
    with her symptoms. You return to your study at the castle. After a few days, you are summoned by the King.''')     
        print('''\nKing: I am not sure what you did, but it has had no effect. Guests do not feel comfortable 
    at the inn. Cateline seems to be the source of this. You have failed me. Keep this up and I will not be so 
    forgiving. Begone from my sight.''')
        patients_not_treated.remove('Cateline the Innkeeper')
        add_strike()
    print('\nDisorder reveal: Cateline had an acute case of Social Anxiety Disorder caused by awkward exchanges with guests.')
    print('''\nSolution: Provide her a self-care regimen (breathing, mindfulness, gratitude, exercises) that 
would reduce the symptoms of her anxiety. Another solution was to erase the negative memories that led to her social anxiety.''')

    
    return




if __name__ == "__main__":
    print('''\nYou are the sorcerer to King Gregwillyest. You have your own quarters and study in the castle. 
Your duties are to tend to people with issues all around the kingdom at the order of the King.
Unofficially, you are the King's very own problem solver.''')

    player_name = input('\nWhat is your name, sorcerer?\n')
    print(f'''\nOne day, {player_name}, you are in your study and are looking over the pieces of parchment given to you by the King.''')

    patient_select()
    while len(patients_not_treated) != 0 and strikes < 3:
        patient_select()
        # strikes = 3 # strikes built in for testing
        # print(strikes) # num strikes for testing
        # patients_not_treated = [] # all patients treated for testing
    

    if strikes >= 3:
        print('''You are summoned to the King's court. For what, you do not know. You are flanked
by two armed guards as they escort you to the court. You enter the throne room and lock eyes
with a furious king. He barks at the guards to leave you at his feet.''')
        print('''King: You have failed me for the last time, sorcerer. Do not say that I did not 
warn you this would happen. Guards, dispose of him.''')
        print(f'''The same guards that escorted you grab you by the arms and drag you towards a hatch on
the floor. They open the hatch, revealing a long, dark tunnel with an opening at the end leading
outdoors. You scream as they toss you down the hatch. You feel the breeze violently thrashing
against your body as you fall. You close your eyes and brace for impact. You crash into the Earth,
demolishing the ground below and sending dirt and rocks flying. Your broken body lies in a
crater; bones shattered and vitals pulverized, you appreciate the surrounding scenery of the
kingdom as you take your last breath. {player_name} the sorcerer has met their end at the
hands of an angry king.''')
        
        print('Type \'python PsychologyGame.py\' and enter to play again.')


    elif len(patients_not_treated) == 0:
        print(f'''Congratulations, {player_name}! You have dealt with the cases issued to you by the King.
Your job and your life are safe, until your next case load arrives at least. Here is a review of the
psychological conditions that each patient had and their solutions:''')
        
        print('Bogart Grimsby: Insomnia; Potion of Pineal Prowess or salve of melatonin')
        print('Chef Ardee: Hoarding disorder; Charm of Decision Making')
        print('Velimir the Voracious: Pica disorder; Salve of Sour Rock or Potion of the Newt\'s Bottomless Stomach')
        print('Lana Lupin: Retrograde Amnesia caused by head injury')
        print('Geralt the Old Dragonslayer: PTSD; SSRI medication spell')
        print('Cateline: Social Anxiety disorder; Book of Self-help or Memory Erasure spell')
        
        print(f'''Thank you for playing, {player_name}! The Kingdom is happier because of you, and you are revered by the people of the Kingdom!''')
        print('Type \'python PsychologyGame.py\' and enter to play again.')

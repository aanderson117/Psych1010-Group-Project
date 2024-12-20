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
    return




def geralt():
    return




def cateline():
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
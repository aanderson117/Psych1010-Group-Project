player_name = 'Gandalf'
patients_not_treated = ['Bogart Grimsby the Lesser', 'Chef Ardee', 'Velimir the Voracious', 'Lana Lupin', 'Geralt the Old Dragonslayer', 'Cateline the Innkeeper']
patients_not_treated = ['Bogart Grimsby the Lesser', 'Chef Ardee', 'Velimir the Voracious'] # Ethan's patients for testing
# patients_not_treated = ['Lana Lupin', 'Geralt the Old Dragonslayer', 'Cateline the Innkeeper'] # Alexa's patients for testing




def reset_strikes():
    global strikes
    strikes = 0




def add_strike():
    global strikes
    strikes += 1




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
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 3):
                player_choice = input('Please enter a number for one of the choices listed: ')
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
    print('3. Refer to parchment.')
    print('4. Attempt to treat Bogart.')
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
            print('3. Refer to parchment.')
            print('4. Attempt to treat Bogart.')
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
            print('3. Refer to parchment.')
            print('4. Attempt to treat Bogart.')
            player_choice = input('Enter the number for your choice: ')
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
                player_choice = input('Please enter a number for one of the choices listed: ')
        elif int(player_choice) == 3:
            print('\nYou refer to your notes from the King\'s briefing.')
            print('Notes: Blacksmith order for new weapons not gone through; Bogart Grimsby the Lesser has demons that prevent sleep')
            print('\nWhat would you like to do?\n')
            print('1. Investigate Bogart\'s room.')
            print('2. Try to talk to Bogart again.')
            print('3. Refer to parchment.')
            print('4. Attempt to treat Bogart.')
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
        add_strike()
    elif int(player_choice) == 3:
        print('''\nYou read a few incantations from your list and bid Bogart farewell. After a few days, the King 
summons you and scolds you for your shoddy work.''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        add_strike()
    elif int(player_choice) == 4:
        print('''\nYou cast a spell that dispels demons. Bogart is satisfied with your work, and you bid him 
farewell. After a few days, the King summons you to scold you for your shoddy work. ''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        add_strike()
    elif int(player_choice) == 5:
        print('''\nYou talk to Bogart about his sleep issues. He is not satisfied with your treatment, but you do 
not know what else to do, so you bid him farewell. After a few days, the King summons you to 
scold you for your shoddy work''')
        print('\nKing: Keep this up and I will have your head!')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
        add_strike()
    elif int(player_choice) == 6:
        print('''\nAfter a few days the King summons you to tell you that the equipment Bogart has been producing 
is far superior to his previous products. It can be assumed that you cured Bogart's disorder.''')
        patients_not_treated.remove('Bogart Grimsby the Lesser')
    

    print('\nDisorder reveal: Bogart suffered from an acute case of insomnia.')
    print('\nSolution: Either by bolstering the pineal gland or by dosing him with melatonin, Bogart\'s insomnia is cured.')
    return




def ardee():
    print(f'''\nKing: Dear God! What is this placed before me? I need you, {player_name}, to go to my
head chef\'s home and sort him out. I have heard for some time of some problem brewing, but I
did not think it would be this bad! Please hurry! And bring me a new sandwich.''')
    print('''\nYou arrive at the chef\'s place of living. You look around the outside of the house at the
windows. You can\'t see much, but it does seem a bit messy from what you can tell at a glance.
You get to the door and knock...You hear a loud noise, like ten things all fell at once.''')
    print('\nUknown voice: Hey, you out there! Can you assist a poor man in need? I am trapped in my house and cannot open the door!')
    print('''\nYou try to open the door before realizing that it\'s a push and not a pull (that\'s shoddy housework).
You also realize that there is a ton of stuff behind the door blocking you from entering.''')
    

    print('\nWhat would you like to do?\n')
    print('1. Knock the door down with your bear strength.')
    print('2. Use your magic to push away all the clutter behind the door (which could make the mess worse).')
    print('3. You give up and decide to break a window and climb in.')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 6):
        player_choice = input('Please enter a number for one of the choices listed: ')
    
    
    print('''\nYou got into the home and DEAR LORD! You see piles of trash and dishes strewn about
on every surface, toys and trinkets in odd places, and no chef in sight. ''')
    print('\nChef Ardee: Hey, I am over here! Under the horse saddle.')
    print('''\nYou lift the horse saddle and find your missing head chef. He looks terrible. His
clothes are all messy, his hat is torn in several places, and as he gets up, he slips on 
a tiny dagger and falls to the ground. You help him up again and ask him why his home has gone to hell.''')
    print('''\nChef Ardee: Honestly, I am not sure. It started with me getting some things that I thought were
neat, like that suit of armor or that cool-looking sword. Then, I got some extra dishware as I
used to have lots of people come over. Then I kept a lot of other things that could be valuable, (he
picks up a bent fork) like this. I also need to keep making recipes for the King so I do not
disappoint him. ''')
    

    print('\nWhat would you like to do?\n')
    print('1. Try to talk to Ardee again.')
    print('2. Refer to parchment.')
    print('3. Attempt to treat Ardee.')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 3):
        player_choice = input('Please enter a number for one of the choices listed: ')
    while int(player_choice) != 3:
        if int(player_choice) == 1:
            print('\nYou: How long have you been trapped, and how have you not starved?')
            print('''\nChef Ardee: : Oh, I have been stuck in this house for a week and a half now. I'm surprised it 
took that long for someone to check up on me. And for how am I still alive? I was right 
next to the pantry and just got what I needed from where I was stuck.''')
            print('''\nYou look in the pantry to see that the top shelf seems fully stocked, while 
the bottom shelf is completely empty, with only some loose veggies in the back. You also 
realize that there are still some leftover sandwiches that still seem fresh on the closest
counter to where Chef Ardee was laying.''')
            print('\nWhat would you like to do?\n')
            print('1. Try to talk to Ardee again.')
            print('2. Refer to parchment.')
            print('3. Attempt to treat Ardee.')
            player_choice = input('Enter the number for your choice: ')
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 3):
                player_choice = input('Please enter a number for one of the choices listed: ')
        elif int(player_choice) == 2:
            print('\nYou refer to your notes from the King\'s briefing.')
            print('Notes: Sort out Chef Ardee; bring new sandwich')
            print('\nWhat would you like to do?\n')
            print('1. Try to talk to Ardee again.')
            print('2. Refer to parchment.')
            print('3. Attempt to treat Ardee.')
            player_choice = input('Enter the number for your choice: ')
            while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 3):
                player_choice = input('Please enter a number for one of the choices listed: ')
        
    
    print('\nYou: Before we get back to the king, I think we should fix this issue you seem to have.')
    print('\nChef Ardee: As you wish')
    print('''\nAs you were talking, you realized that he is now making another sandwich for the 
King without you even asking.''')
    print('\nWhat will you do?\n')
    print('1. Give Charm of Decision Making.')
    print('2. Attempt to clean Ardee\'s house.')
    print('3. Give Anti-Anxiety Potion')
    print('4. Move trash out of the way of the door.')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 4):
        player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou hand Chef Ardee the Charm of Decision Making. You explain to him that
this should help him with the excessive buying things and making food by making him
explain to the charm why he should get or make a thing. The charm will then respond
with a counter argument as to why he should not. You then tell Ardee to hand you 
the finished sandwich he had prepared for the King as you were speaking. You clean
the entryway and get back to the castle. You hand the King his sandwich. After a 
few days, the King summons you to update you on the issue.''')
        print('''\nKing: Thank you for fetching me my head chef. He seems to be doing well, but
it seems that my meals are still arriving a bit late, almost as if he is questioning
everything he does. Return to your study. I have no need for you at the moment.''')
        print('''\nMostly pleased with your success, you return to your study and get prepared
for when you are needed next.''')
        patients_not_treated.remove('Chef Ardee')
    if int(player_choice) == 2:
        print('''\nYou: Sir, the King has ordered you to get back to the castle as soon as
possible. However, with all this stuff in your way, would you mind if I cleaned 
your home?''')
        print('''\nChef Ardee: What? Why? Everything here has a purpose. I could not part
with any of my things.''')
        print('''\nYou distract Ardee by telling him to make a sandwich while you clean his home.
As Ardee makes the sandwich, you drink a potion that increases your attention makes
you feel quicker. You clean most of his home in five minutes, throwing away anything
you deem useless to the head chef.''')
        print('\nChef Ardee: What happened to all my things?')
        print('''\nYou tell him that you cleaned up his home and that he should now be able
to get to the castle without any hassle now. Ardee looks furious but hands you the 
completed sandwich. After a few days, the King summons you to update you on the issue.''')
        print('''\nKing: Absolutely nothing has changed! I do not know what you did, but it had no
effect. Since you were unable to cure Chef Ardee, I have had another poor sandwich
come my way as he turned up missing again. Keep this up, and I will have your head!''')
        print('''\nYou head back to your quarters and study your psychological scrolls. There must
have been something you were missing. You read that those who hoard a lot of items
do not respond well to having their items taken or thrown away. It could make their
condition worse as it could increase their anxiety and make them less willing to get help.''')
        patients_not_treated.remove('Chef Ardee')
        add_strike()
    if int(player_choice) == 3:
        print('''\nYou take out your Anti-Anxiety potion, explaining it to Chef Ardee. You tell him
that this potion should relieve some of the stress his job is putting on him, as you 
point out that he seems to only focus on making the King new meals and buying anything
that might help him. Chef Ardee nods and swigs the potion down. You tell him to hand you
the finished sandwich he had prepared as you were speaking. You clean the entrance and 
get back to the castle, handing the King his sandwich. After a few days, the King
summons you to update you on the issue.''')
        print('''\nKing: Thank you for fetching me my head chef. He seems to be doing well. Return
to your study. I have no need for you at the moment.''')
        print('''\nOn your way to your study, you encounter Chef Ardee again, and he explains that
with the help of the potion, he has also cleaned up a good chunk of his home. Satisfied,
you go back and get prepared for when you are needed next.''')
        patients_not_treated.remove('Chef Ardee')
    if int(player_choice) == 4:
        print('''\nYou ask the chef for the sandwich that he made as you were taling before you clean
the entrance to his home so you can both leave. You both get back to the king and hand 
him his sandwich. After a week, the King summons you to update you on the issue.''')
        print('''\nKing: Absolutely nothing has changed! I do not know what you did, and I 
honestly think you didn\'t do anything, but it had no effect. Since you were unable to 
cure Chef Ardee, I have had another poor sandwich come my way as he turned up missing 
again. Keep this up, and I will have your head!''')
        print('''\nYou head back to your quarters and study your psychological scrolls. There must
have been something you were missing.''')
        patients_not_treated.remove('Chef Ardee')
        add_strike()
    
    
    print('\nDisorder reveal: Chef Ardee suffered from an anxiety-induced hoarding disorder.')
    print('''\nSolutions: The Anti-Anxiety Potion helps him focus on himself and his home, away from the
King's demand for the best food. The Charm of Decision Making helps the chef make decisions
that will not end up in a pile of leftover test food and helps him realize what he needs for
cooking is to buy only what he thinks will help with cooking. This choice, however, could be 
tainted by the fact that he makes decisions slower as he uses the charm more and more as it 
takes the time to respond to him. Either way, you helped the King get his head chef back, so
this could still be considered a success.''')
    return




def velimir():
    print(f'''\nKing: The roads out there are unsightly and difficult to traverse! My cavalry has an 
acute case of twisted ankles from stepping in the divots! This is decreasing the strength of our 
military, and it must be taken care of at once. I have found the cretin responsible for damaging 
our roads. He is known locally as Velimir the Voracious. Find and take care of him {player_name}.
Your King has declared it so. Be off!''')
    print('''\nYou track Velimir to a local hamlet located on Lord Landbod\'s land. A trail of minced 
stones leads you from the road to a small farmhand\'s shack. As you circle the house, 
you find a man crouched to the ground sitting on his haunches; in his hand he has a 
muddy stone. He is bald and emaciated with tattered cloth for clothes. He eyes you 
as you approach and lifts the stone to his mouth before he takes a large, crunchy 
bite of the rock. He appears to have no shame in doing so.''')
    print('''\nYou: Velimir? The King has sent for you. The roads surrounding your hamlet are weathered 
and inefficient. I noticed you have one of the stones in your hands and I have deduced you 
are responsible. What say you in your defense?''')
    print('''\nVelimir: I wake up every morning with a nagging hunger in the pit of my gut. The only 
thing that quiets it is eating stone, of which there is ample supply on the roads. 
If I don\'t eat them, I will starve to death. I am just looking out for my own survival.''')
    print('''You: While your behavior is certainly unacceptable, I can spare your life if we can find 
a way to stop this hunger of yours. I am sure I can think of something.''')
    

    print('\nYou refer to your list of tools to see what might help Velimir.')
    print('What will you use?\n')
    print('1. The Holy Bible')
    print('2. Charm of Weight Gain')
    print('3. Salve of Sour Rock (makes stone burn the tongue and mouth)')
    print('4. Spell of Landbod\'s Feast (summons food)')
    print('5. Potion of the Newt\'s Bottomless Stomach (causes hunger for insects)')
    player_choice = input('Enter the number for your choice: ')
    while not player_choice.isnumeric() or (int(player_choice) < 1 or int(player_choice) > 5):
        player_choice = input('Please enter a number for one of the choices listed: ')
    if int(player_choice) == 1:
        print('''\nYou decide the best course of action is to recite a few verses and pray for a cure to Velimir\'s 
condition. After you finish your prayers and recitations, you bid Velimir farewell and return to the 
King\'s castle to inform him of the task\'s completion. After a few days, the King summons you to 
update you on the issue.''')
        print('''\nKing: Absolutely nothing has changed! I don\'t know what you did, but it had no effect. Since you 
were unable to cure Velimir, I have no choice but to exile him. Keep this up and I will have your head!''')
        patients_not_treated.remove('Velimir the Voracious')
        add_strike()
    elif int(player_choice) == 2:
        print('''\nYou bestow the Charm of Weight Gain on Velimir. He clasps the charm between his hands before placing 
it in the cloth pouch that hangs around his neck. You leave and head back to the King\'s castle to inform
him of the task\'s completion before returning to your quarters. After a few days, the King summons you 
to update you on Velimir.''')
        print('''\nKing: While he is certainly a lot heavier and healthier than when my men first reported his condition 
to me, there is still the issue of the roads. Nothing has been done to fix them! My men report that he is still 
vandalizing them as well. You have failed me. I have no choice but to exile Velimir from the kingdom. Keep this
up and I will have your head!''')
        patients_not_treated.remove('Velimir the Voracious')
        add_strike()
    elif int(player_choice) == 3:
        print('''\nYou bestow the Salve of Sour Rock upon Velimir and instruct him to drink all of it. He does just that,
swallowing every last drop; when the potion takes effect, any rock that enters his mouth will inflict a 
painful burning sensation. With your task complete, you return to the King\'s castle and update him on 
Velimir. After a few days, the King summons you to update you on Velimir\'s condition.''')
        print('''\nKing: I am not sure what you have done, but you were successful. The roads are no longer being vandalized,
and Velimir has gone back to his normal peasantry. Well done. Return to your study. I have no need 
for you at the moment.''')
        patients_not_treated.remove('Velimir the Voracious')
    elif int(player_choice) == 4:
        print('''\nYou use the spell of Lord Landbod\'s feast to summon Velimir a bounty of food. With you and Velimir satisfied,
you return to the King\'s castle and inform him of Velimir\'s condition. After a few days, the King summons
you to his court to update you on Velimir.''')
        print('''\nKing: I do not know what you did, but absolutely nothing has changed. I have no choice but to exile Velimir. 
Keep this up and I will have your head!''')
        patients_not_treated.remove('Velimir the Voracious')
        add_strike()
    elif int(player_choice) == 5:
        print('''\nYou decide to bestow the Potion of the Newt\'s Bottomless Stomach upon Velimir. The potion will trade his hunger 
for rocks with a hunger for insects. You are satisfied with your work and return to the King\'s castle to 
inform him of your progress. After a few days, the King summons you.''')
        print('''\nKing: I am not sure what you have done, but you were successful. The roads are no longer being vandalized 
and Velimir has gone back to his normal peasantry. Well done. Return to your study. I have no need 
for you at the moment.''')
        patients_not_treated.remove('Velimir the Voracious')
    

    print('\nDisorder reveal: Velimir had Pica.')
    print('''\nSolutions: Velimir\'s Pica can be cured through conditioning with the Salve of Sour Rock. Because of the 
bad taste caused by eating rock, Velimir was conditioned to no longer eat rocks. This is an example of 
positive punishment. The potion of the Newt\'s Bottomless Stomach can cure Velimir by replacing his 
hunger for rocks with a hunger for bugs, a much more edible and nutritious option.''')
    return




def lana():
    return




def geralt():
    return




def cateline():
    return




if __name__ == "__main__":
    reset_strikes()
    print('''\nYou are the sorcerer to King Gregwillyest. You have your own quarters and study in the castle. 
Your duties are to tend to people with issues all around the kingdom at the order of the King.
Unofficially, you are the King's very own problem solver.''')

    player_name = input('\nWhat is your name, sorcerer?\n')
    print(f'''\nOne day, {player_name}, you are in your study and are looking over the pieces of parchment given to you by the King.''')

    patient_select()
    while len(patients_not_treated) != 0 and strikes < 3:
        # print(strikes) # num strikes for testing
        patient_select()
        # strikes = 3 # strikes built in for testing
        # patients_not_treated = [] # all patients treated for testing
    

    if strikes >= 3:
        print('''\nYou are summoned to the King's court. For what, you do not know. You are flanked
by two armed guards as they escort you to the court. You enter the throne room and lock eyes
with a furious king. He barks at the guards to leave you at his feet.''')
        print('''\nKing: You have failed me for the last time, sorcerer. Do not say that I did not 
warn you this would happen. Guards, dispose of him.''')
        print(f'''\nThe same guards that escorted you grab you by the arms and drag you towards a hatch on
the floor. They open the hatch, revealing a long, dark tunnel with an opening at the end leading
outdoors. You scream as they toss you down the hatch. You feel the breeze violently thrashing
against your body as you fall. You close your eyes and brace for impact. You crash into the Earth,
demolishing the ground below and sending dirt and rocks flying. Your broken body lies in a
crater; bones shattered and vitals pulverized, you appreciate the surrounding scenery of the
kingdom as you take your last breath. {player_name} the sorcerer has met their end at the
hands of an angry king.''')
        
        print('\nType \'python PsychologyGame.py\' and enter to play again.')


    elif len(patients_not_treated) == 0:
        print(f'''\nCongratulations, {player_name}! You have dealt with the cases issued to you by the King.
Your job and your life are safe, until your next case load arrives at least. Here is a review of the
psychological conditions that each patient had and their solutions:\n''')
        
        print('Bogart Grimsby: Insomnia; Potion of Pineal Prowess or Salve of Melatonin')
        print('Chef Ardee: Hoarding disorder; Charm of Decision Making or Anti-Anxiety Potion')
        print('Velimir the Voracious: Pica; Salve of Sour Rock or Potion of the Newt\'s Bottomless Stomach')
        print('Lana Lupin: Retrograde Amnesia caused by head injury')
        print('Geralt the Old Dragonslayer: PTSD; SSRI medication spell')
        print('Cateline: Social Anxiety disorder; Book of Self-help or Memory Erasure spell')
        
        print(f'''\nThank you for playing, {player_name}! The Kingdom is happier because of you, and you are revered by the people of the Kingdom!''')
        print('\nType \'python PsychologyGame.py\' and enter to play again.')
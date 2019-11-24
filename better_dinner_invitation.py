# too many redundant/broken things, will definitely be revisited in the future
dinner_party = 'dinner party'
kamulyan = 'mangunharja'
list_variable1 = '-'
when1 = "when"
warning1="!!WARNING: (This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the products of the author’s imagination or used in a fictitious manner."+"\n\t\t\t"+"Any resemblance to actual persons, living or dead, or actual events is purely coincidental."
header = (warning1.lower()+" proceed at your own risk, you have been warned)"+"\n\n\n"+kamulyan.upper()+"'s "+dinner_party+" "+'invitation list'+'\n\n')

# the first list of invited people
invited_people = []
invited_people.append('jayamanggala')
invited_people.append('widyatmaka')
invited_people.append('prabangkara')

# statements for the people
not_coming_msg = (" didn't seem to care sadly, and proceed to disappear among the crowds."+"\n\n")
inviting1_msg = (' seemed mildly interested of the idea of going to my'+" "+dinner_party+".")
inviting2_msg = " wholeheartedly accepted my invitation."
inviting3_msg = " and the others were happy to have more people aboard in this dinner."
inviting4_msg = " was elated to join us, the more people the better he says."
inviting5_msg = " Felt incredibly honored, yet guilty at the same time, especially for those who wouldn't be joining."
monologue1 = "We all ate quietly and parted ways not long after. It was the most awkward dinner ever in their entire life."

# the first invitations
kamulyan_dialog1 = ("\t"+kamulyan.title()+": "+'"Hey you 3. Yes, the ones in pink shirt, blue jeans, and black cap, would you like to go have dinner together?"'+" (THEY SEEM UNDECIDED)")
invitation1_response_msg = ("\n\t\t"+"--> OUTCOME OF BEING INVITED BY A COMPLETE STRANGER:")
full_invitation1_msg = ("\n\t\t\t\t"+list_variable1+" "+invited_people[0].title()+inviting1_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[1].title()+inviting1_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[2].title()+not_coming_msg)

# the new people replacing the ones who couldn't come
invited_people[2] = ('bajrastawa')

# replace statements
replace1_msg=(" was happy to replace that other dude for going to the"+" "+dinner_party+".")

# the second invitations
kamulyan_dialog2 = ("\t"+"UPDATE: (THEY SEEM TO HAVE REACHED A CONCLUSION)"+' "So, are you guys going? Preferably with one more person to replace the pink dude?"')
invitation2_response_msg = ("\n\t\t"+"--> OUTCOME OF BEING INVITED BY THE SAME COMPLETE STRANGER AGAIN:"+"\n\t\t")
full_invitation2_msg = ("\t\t"+list_variable1+" "+invited_people[0].title()+inviting2_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[1].title()+inviting2_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[2].title()+replace1_msg+"\n")

# new people invited due to more available seats
invited_people.insert(0, 'jayengresmi')
invited_people.insert(2, 'pringgakusuma')
invited_people.append('bratalegawa')

# the third invitations
kamulyan_dialog3 = ("\n\t"+'UPDATE: "Wow, It looks like we will get extra seats! Should we add more people?"')
invitation3_response_msg = ("\n\t\t"+"--> OUTCOME OF INVITING EVEN MORE PEOPLE:"+"\n\t\t")
full_invitation3_msg = ("\t\t"+list_variable1+" "+invited_people[0].title()+inviting4_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[1].title()+inviting3_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[2].title()+inviting4_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[3].title()+inviting4_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[4].title()+inviting3_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[5].title()+inviting3_msg)

# everything above is printed down below. i know it's wrong, but I'm too lazy to fix it for now.
print(header.upper()+kamulyan_dialog1+invitation1_response_msg+full_invitation1_msg+kamulyan_dialog2+invitation2_response_msg+full_invitation2_msg+kamulyan_dialog3+invitation3_response_msg+full_invitation3_msg)

# apologizing to people that can't join
apologize_response_msg2 = "--> Outcome of not being invited despite already being invited:"
apologize_response_msg1 = 'UPDATE: "Bad News, There are no extra seats!! I am very sorry I cannot invite all of you. Will you guys accept my apology?" (HEARTBREAKING)'
print("\n\t"+apologize_response_msg1+"\n\t\t"+apologize_response_msg2.upper())
continuous_apologizing = "No matter how much I said sorry,"
sorry_unaccepted = "just brushed me off and go on his way, never to be seen again."
sorry_accepted = "was informed he lost his seat, he immediately get up and left. I can't believe how understanding he is."
angry_people1 = invited_people.pop()
print("\t\t\t\t"+list_variable1+" "+when1.title()+" "+angry_people1.title()+" "+sorry_accepted)
angry_people2 = invited_people.pop()
print("\t\t\t\t"+list_variable1+" "+continuous_apologizing+" "+angry_people2.title()+" "+sorry_unaccepted)
angry_people3 = invited_people.pop()
print("\t\t\t\t"+list_variable1+" "+continuous_apologizing+" "+angry_people3.title()+" "+sorry_unaccepted)
angry_people4 = invited_people.pop()
print("\t\t\t\t"+list_variable1+" "+when1.title()+" "+angry_people4.title()+" "+sorry_accepted)

# the chosen one
kamulyan_dialog4 = ("\t"+'UPDATE: "wow.. I guess that means I can only invite you 2, is that alright?"'+" *AWKWARD SILENCE*")
invitation4_response_msg = ("\n\t\t"+"--> OUTCOME FOR INVITING LESS PEOPLE THAN ORIGINALLY PROMISED (FINAL):")
full_invitation4_msg = ("\n\t\t\t\t"+list_variable1+" "+invited_people[0].title()+inviting5_msg+"\n\t\t\t\t"+list_variable1+" "+invited_people[1].title()+inviting5_msg)
print('\n'+kamulyan_dialog4+invitation4_response_msg+full_invitation4_msg)

# last impression
print("\n"+monologue1+"\n")

# getting rid of guests (wow, how rude)
del invited_people[0]
del invited_people[0]
print(invited_people)

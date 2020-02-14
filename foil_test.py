from foil_parser import get_actions, clean_user_foil, extract_vocab, extract_actions

user_foil = "why deployed big engines firechief Mesa fire Brickyard instead of deploy Small Engines firechief Mesa fire Brickyard"
# user_foil = clean_user_foil(user_foil, vocab)
# user_foil = " ".join(user_foil)
why, why_not = get_actions(user_foil, current_plan=set(['DEPLOY_BIG_ENGINES_FIRECHIEF_MESAFIRE_BYENG']))
print("Why ", why)
print("Why Not ", why_not)
import re

file = 'planner/saved_obs.dat'
with open(file,'r') as files:
    a=files.readlines()
    b=[i.strip('\n') for i in a]
    for i in b:
        action_list.append((re.sub('[(){}<>]', '', i)).replace(' ',''))
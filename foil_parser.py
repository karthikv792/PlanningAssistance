def extract_actions():
    actions = set()
    with open('planner/pr-domain.pddl') as f:
        for line in f:
            if (line.strip().startswith(("(:action"))):
                # print(line.strip()[len("(:action "):])
                actions.add(line.strip()[len("(:action "):])
    return actions
vocab_list = ['media', 'helpline', 'cars', 'casualties', 'bulldozers', 'small', 'evacuation', 'address', 'policemen', 'deploy', 'road', 'extinguish', 'up', 'attend', 'alert', 'set', 'contact', 'local', 'update', 'big', 'fire', 'rescuers', 'engines', 'police', 'ambulances', 'issue', 'prepare', 'search', 'divert', 'traffic', 'ladders', 'helicopters', 'barricade', 'block', 'position', 'evacuate', 'firestation', 'lukes', 'courtstation', 'joseph', 'marketplace', 'substation', 'scottsfire', 'rural', 'policestation', 'hospital', 'medic', 'pois', 'apachestation', 'fire', 'policechief', 'mill', 'medichief', 'firechief', 'police', 'mesafire', 'phxfire', 'adminfire', 'lake', 'byeng', 'transportchief', 'transport']

def extract_vocab(actions):
    vocab = set()
    for action in actions:
        listOfWords = action.lower().split('_')
        vocab.update(listOfWords)

    vocab.add('brickyard')
    vocab.add('brick')
    vocab.add('yard')
    vocab.add('transport')
    vocab.add('medi')
    vocab.add('medical')
    vocab.add('fire')
    vocab.add('chief')
    vocab.add('engine')
    vocab.add('admin')
    vocab.add('apache')
    vocab.add('sub')
    vocab.add('court')
    vocab.add('phoenix')
    vocab.add('scottsdale')
    vocab.add('station')
    vocab.add('help')
    vocab.add('line')
    vocab.add('ambulance')
    vocab.add('mesa')
    vocab.add('ladder')
    vocab.add('car')
    vocab.add('market')
    vocab.add('place')
    vocab.add('helicopter')
    vocab.add('men')
    vocab.add('bulldozer')
    return vocab

def clean_user_foil(user_foil, vocab):
    if "phoenix" in user_foil:
        user_foil = user_foil.replace("phoenix", "phx")
    if "brickyard" in user_foil:
        user_foil = user_foil.replace("brickyard", "byeng")

    words = user_foil.split(" ")
    word_list = []
    word_list.append(words[0])
    for i in range(1, len(words)):
        temp = word_list[len(word_list) - 1] + words[i]
        # print(temp)
        if temp in vocab:
            word_list.pop()
            word_list.append(temp)
        else:
            word_list.append(words[i])
    return word_list

def get_actions_in_foil(word_list, action_set, vocab):
    action_list = []
    action = ""
    for word in word_list:
        if word in vocab:
            if len(action) == 0:
                action += word.upper()
            else:
                action = action + "_" + word.upper()
            if action in action_set:
                action_list.append(action)
                action = ""
            else:
                print(action)

    return action_list

action_set = extract_actions()
vocab = extract_vocab(action_set)
print(vocab)

def get_actions(user_foil, current_plan):
    word_list = clean_user_foil(user_foil, vocab_list)
    print(word_list)
    actions_in_foil = get_actions_in_foil(word_list, action_set, vocab)
    current_plan_actions = []
    user_suggested_actions = []

    for action in actions_in_foil:
        if action in current_plan:
            current_plan_actions.append(action)
        else:
            user_suggested_actions.append(action)

    return current_plan_actions, user_suggested_actions


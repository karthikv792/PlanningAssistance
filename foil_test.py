from foil_parser import get_actions

user_foil = "why reply Rescuers firechief Phoenix fire Brickyard instead of deployed Small Engine fire chief Caught Fire Lake "
why, why_not = get_actions(user_foil, current_plan=set())
print("Why ", why)
print("Why Not ", ''.join(i+' ' for i in why_not))
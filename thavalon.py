import copy
import os
import random
import shutil
import sys

# get_role_descriptions - this is called when information files are generated.
def get_role_description(role):
	return {
		'Tristan'		: 'The person you see is also Good and is aware that you are Good.\nYou and Iseult are collectively a valid Assassination target.',
		'Iseult'		: 'The person you see is also Good and is aware that you are Good.\nYou and Tristan are collectively a valid Assassination target.',
		'Merlin' 		: 'You know which people have Evil roles, but not who has any specific role.\nYou are a valid Assassination target.',
		'Percival'		: 'You know which people have the Merlin or Morgana roles, but not specifically who has each.',
		'Lancelot'		: 'You may play Reversal cards while on missions.\nYou appear Evil to Merlin.',
		'Arthur'		: 'You know which Good roles are in the game, but not who has any given role.\nIf two missions have Failed, and less than two missions have Succeeded, you may declare as Arthur.\nAfter declaring, your vote on team proposals is counted twice, but you are unable to be on mission teams until the 5th mission.\nAfter declaring, you are immune to any effect that can forcibly change your vote.',
		'Titania'		: 'You appear as Evil to all players with Evil roles (except Colgrevance).',
		'Nimue'			: 'You know which Good and Evil roles are in the game, but not who has any given role.\nYou are a valid Assassination target.',

		'Mordred' 		: 'You are hidden from all Good Information roles. \nLike other Evil characters, you know who else is Evil (except Colgrevance).',
		'Morgana'		: 'You appear like Merlin to Percival. \nLike other Evil characters, you know who else is Evil (except Colgrevance).',
		'Maelagant'		: 'You may play Reversal cards while on missions. \nLike other Evil characters, you know who else is Evil (except Colgrevance).',
		'Agravaine'		: 'You must play Fail cards while on missions. \nIf you are on a mission that Succeeds, you may declare as Agravaine to cause it to Fail instead. \nLike other Evil characters, you know who else is Evil (except Colgrevance).',
		'Colgrevance' 	: 'You know not only who else is Evil, but what role each other Evil player possess. \nEvil players know that there is a Colgrevance, but do not know that it is you.',
	}.get(role,'ERROR: No description available.')

# get_role_information: this is called to populate information files
# blank roles:
# - Lancelot: no information
# - Arthur: no information?
# - Guinevere: too complicated to generate here
# - Colgrevance: name,role (evil has an update later to inform them about the presence of a Colgrevance)
def get_role_information(my_player,players):
	return {
		'Tristan' 		: ['{} is Iseult.'.format(player.name) for player in players if player.role is 'Iseult'],
		'Iseult' 		: ['{} is Tristan.'.format(player.name) for player in players if player.role is 'Tristan'],
		'Merlin' 		: ['{} is Evil.'.format(player.name) for player in players if ((player.team is 'Evil' and player.role is not 'Mordred') or player.role is 'Lancelot')],
		'Percival'		: ['{} is Merlin or Morgana.'.format(player.name) for player in players if player.role is 'Merlin' or player.role is 'Morgana'],
        'Lancelot'		: [],
		'Arthur'		: ['{}'.format(player.role) for player in players if player.team is 'Good' and player.role is not 'Arthur'],
		'Titania'		: [],
		'Nimue'			: ['{}'.format(player.role) for player in players if player.role is not 'Nimue'],

		'Mordred'	 	: ['{} is Evil.'.format(player.name) for player in players if (player.team is 'Evil' and player is not my_player and player.role is not 'Colgrevance') or player.role is 'Titania'],
		'Morgana' 		: ['{} is Evil.'.format(player.name) for player in players if player.team is 'Evil' and player is not my_player and player.role is not 'Colgrevance' or player.role is 'Titania'],
		'Maelagant' 	: ['{} is Evil.'.format(player.name) for player in players if player.team is 'Evil' and player is not my_player and player.role is not 'Colgrevance' or player.role is 'Titania'],
		'Agravaine'		: ['{} is Evil.'.format(player.name) for player in players if player.team is 'Evil' and player is not my_player and player.role is not 'Colgrevance' or player.role is 'Titania'],
		'Colgrevance' 	: ['{} is {}'.format(player.name,player.role) for player in players if player.team is 'Evil' and player is not my_player],
	}.get(my_player.role,[])

class Player():
	# players have the following traits
	# name: the name of the player as fed into system arguments
	# role: the role the player possesses
	# team: whether hte player is good or evil
	# type: information or ability
	# seen: a list of what they will see
	# modifier: the random modifier this player has [NOT CURRENTLY UTILIZED]
	def __init__(self,name):
		self.name = name
		self.role = None
		self.team = None
		self.modifier = None
		self.info = []
		self.is_assassin = False

	def set_role(self, role):
		self.role = role

	def set_team(self, team):
		self.team = team

	def add_info(self,info):
		self.info += info

	def generate_info(self,players):
		pass

def get_player_info(player_names):
	num_players = len(player_names)
	if len(player_names) != num_players:
		print('ERROR: Duplicate player names.')
		exit(1)

	# create player objects
	players = []
	for i in range(0,len(player_names)):
		player = Player(player_names[i])
		players.append(player)

	# number of good and evil roles
	if num_players < 7:
		num_evil = 2
	elif num_players < 9:
		num_evil = 3
	else:
		num_evil = 4
	num_good = num_players - num_evil

	# establish available roles
	good_roles = ['Merlin','Percival','Tristan','Iseult','Lancelot']
	evil_roles = ['Mordred','Morgana','Maelagant']

	# additional roles for player-count
	# 5 only 
	if num_players < 6: 
		good_roles.append('Nimue')

	# 7 plus
	if num_players > 6:
		good_roles.append('Arthur')
		good_roles.append('Titania')

	# 8 plus 
	if num_players > 7:
		evil_roles.append('Agravaine')

	# 10 only
	if num_players == 10:
		evil_roles.append('Colgrevance')

	'''
	code for testing role interaction
	if num_players == 2:
		good_roles = ['Merlin']
		evil_roles = ['Maeve']
		num_good = 1
		num_evil = 1
	''' 
	good_roles_in_game = random.sample(good_roles,num_good)
	evil_roles_in_game = random.sample(evil_roles,num_evil)

	# lone lovers are rerolled
	# 50% chance to reroll lone lover
	# 50% chance to reroll another role into a lover
	if sum(gr in ['Tristan','Iseult'] for gr in good_roles_in_game) == 1 and num_good > 1:
		if 'Tristan' in good_roles_in_game:
				good_roles_in_game.remove('Tristan') 
		if 'Iseult' in good_roles_in_game:
				good_roles_in_game.remove('Iseult') 

		if random.choice([True, False]):
			# replacing the lone lover
			available_roles = set(good_roles)-set(good_roles_in_game)-set(['Tristan','Iseult'])
			good_roles_in_game.append(random.sample(set(available_roles),1)[0])
		else: 
			# upgrading to pair of lovers
			rerolled = random.choice(good_roles_in_game)
			good_roles_in_game.remove(rerolled)
			good_roles_in_game.append('Tristan')
			good_roles_in_game.append('Iseult')

	# roles after validation
	#print(good_roles_in_game)
	#print(evil_roles_in_game)

	# role assignment
	random.shuffle(players)

	good_players = players[:num_good]
	evil_players = players[num_good:]

	player_of_role = dict()

	for gp in good_players:
		new_role = good_roles_in_game.pop()
		gp.set_role(new_role)
		gp.set_team('Good')
		player_of_role[new_role] = gp

	# if there is at least one evil, first evil player becomes assassin
	if len(evil_players) > 0:
		evil_players[0].is_assassin = True

	for ep in evil_players:
		new_role = evil_roles_in_game.pop()
		ep.set_role(new_role)
		ep.set_team('Evil')
		player_of_role[new_role] = ep

	for p in players:
		p.add_info(get_role_information(p,players))
		random.shuffle(p.info)
		# print(p.name,p.role,p.team,p.info)

	# Informing Evil about a Colgrevance
	for ep in evil_players:
		if ep.role is not 'Colgrevance' and player_of_role.get('Colgrevance'):
			ep.add_info(['Colgrevance lurks in the shadows. (There is another Evil that you do not see.)'])
		if ep.role is not 'Colgrevance' and player_of_role.get('Titania'):
			ep.add_info(['Titania has infiltrated your ranks. (One of the people you see is not Evil.)'])
		if ep.is_assassin:
			ep.add_info(['You are the Assassin.'])

	# delete and recreate game directory
	if os.path.isdir("game"):
		shutil.rmtree("game")
	os.mkdir("game")

	bar = '----------------------------------------\n'
	for player in players:
		player.string = bar+'You are '+player.role+' ['+player.team+']\n'+bar+get_role_description(player.role)+'\n'+bar+'\n'.join(player.info)+'\n'+bar
		player_file = "game/{}".format(player.name)
		with open(player_file,"w") as file: 
			file.write(player.string)

	first_player = random.sample(players,1)[0]
	with open("game/start", "w") as file:
		file.write("The player proposing the first mission is {}.".format(first_player.name))
		#file.write("\n" + second_mission_starter + " is the starting player of the 2nd round.\n")

	with open("game/DoNotOpen", "w") as file:
		file.write("Player -> Role\n\nGOOD TEAM:\n")
		for gp in good_players:
			file.write("{} -> {}\n".format(gp.name,gp.role))
		file.write("\nEVIL TEAM:\n")
		for ep in evil_players:
			file.write("{} -> {}\n".format(ep.name,ep.role))

if __name__ == "__main__":
	if not (6 <= len(sys.argv) <= 11):
		print("Invalid number of players")
		exit(1)

	players = sys.argv[1:]
	num_players = len(players)
	players = set(players) # use as set to avoid duplicate players
	players = list(players) # convert to list
	random.shuffle(players) # ensure random order, though set should already do that
	if len(players) != num_players:
		print("No duplicate player names")
		exit(1)

	get_player_info(players)

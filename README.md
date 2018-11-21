# What is THavalon?
THavalon is a massive extension of the rules presented in Don Eskridge's social deception game, The Resistance: Avalon. The main point of THavalon is to provide every player of the game with a role and that to ensure every player in the game feels like they can make an impact on the result of the game. Over time, these rules have evolved in an effort to make the game both faster and more fun, as well as to fix some of the playstyles that have been established in my main testing group's metagame. 

You absolutely do not need to play with all the rules changes listed here, and many of them can be independently utilized to improve your experience with the game. However, generally speaking, these rules were designed with the intent to all be used together, so there may be minor issues that arise from separating out components. 

THavalon is balanced around games of 5, 7, 8, or 10 players. 6- and 9-player games are heavily imbalanced in favor of the Good team in the base game (due to the 2:1 ratio of Good to Evil roles), and THavalon's insistence on providing every player with a unique role makes these games even more difficult for Evil.

# Using thavalon.py 
THavalon has a game engine, written in Python3, that is used to generate files containing each player's role information. To use this engine, install Python3 on your machine, download thavalon.py, and the open a terminal (Command Line, Git Bash, etc.). Once the terminal is open, navigate to the directory containing thavalon.py and then enter the code to run the python script, using <code>python3 thavalon.py</code> or <code>py thavalon.py</code> followed by the names of the players separated by spaces, as shown in the example below. 

<code>py thavalon.py Alice Bob Charlie Dave Eve</code>  

After running this code, allow each player to view the text file in the <code>/game/</code> directory that bears their name (e.g. Alice would read the file titled <code>Alice</code>). Once every player has looked at the contents of their information file, view the <code>start</code>, also in the /game/ directory, to see who has the first proposal of the first round, and let the game begin.

The game engine also generates an additional file (<code>/game/DoNotOpen</code>) which provides a list of all of the players' teams and roles. As the name of the file suggests, it should not be opened by players while the game is underway, but it can be interesting to read after the game has finished. 

# Rules 
THavalon follows the same rules as The Resistance: Avalon, with the modifications and exceptions listed below. If there is a conflict between the rules of Avalon and the rules of THavalon, then use the rules of THavalon. (If you encounter such a conflict, please contact me so that I can investigate and resolve the conflict). 

## Good Roles
- *Merlin*: sees all players that are either Evil (except Mordred) or are Lancelot; can be Assassinated.
- *Percival*: sees Merlin and Morgana, but cannot distinguish which role each seen player has.
- *Tristan* and *Iseult*: see each other; always appear together; can be Assassinated as a pair.
- *Lancelot*: may play Reversal cards while on missions; appears Evil to Merlin.
- *Nimue* (5): knows which roles are in the game; can be Assassinated. 
- *Arthur* (7+): knows which Good roles are present; may declare after 2 Failed and 0-1 Successful missions to make their votes on mission proposals count twice, but lose the ability to be on mission teams until the 5th mission.
- *Titania* (7+): appears as Evil to Evil roles (except Colgrevance). 

## Evil Roles
- *Mordred*: is hidden from Merlin.
- *Morgana*: appears like Merlin to Percival. 
- *Maelagant*: may play Reversal cards while on missions.
- *Agravaine* (8+):  must play Fails; may declare after having been on a successful mission to cause it to Fail instead.
- *Colgrevance* (10): is hidden from other Evil roles; knows which player has each Evil role.

## Proposals 
In each round, players take turns proposing teams with the appropriate number of players. During the first round, only two players are permitted to make proposals; in subsequent rounds, there may be a number of proposals up to one more than the number of Evil players in the game (e.g. 3 proposals for 5- and 6-player, 4 proposals for 7-, 8-, and 9- player, and 5 proposals for 10 player). When making a proposal, the leader of the mission selects an appropriate number of people for the mission and submits their final selection for voting. 

## Voting 
Voting in THavalon functions identically to voting in the base game, except with respect to the last mission proposal of a round. If a proposal is the last proposal of the round, the voting phase is skipped and the selected team immediately goes on the mission.

## Going on Missions
Once a team has been sent on a mission, each person on that team may choose which card they wish to play. Good players must play Success cards and Evil players may choose to play either Success or Fail. Lancelot and Maelegant are also able to play Reverse cards, and Agravaine may only play Fail cards. Once all players on the team have submitted their selected card, the result of the mission, including which cards were played, is made publicly available. 

A mission Fails if at least one Fail card and an even number of Reverse cards are played, or if an odd number of Reverse cards and no Fail cards are played. In games with at least 7 players, the fourth mission Fails if at least two Fail cards and an even number of Reverse cards are played, or if one Fail card and an odd number of Reverse cards are played. In all other situations, the mission Succeeds. 

In situations where Agravaine may declare (a mission that Succeeded despite at least one Fail card being played in a game with at least 8 players), the player who is Agravaine may formally declare as Agravaine to cause the mission to Fail. Agravaine must make this declaration before the next team proposal is voted on; Agravaine declaring after a proposal has been finalized but prior to voting allows the current proposer to change their team prior to voting. 

If a mission Succeeding or Failing would result in there being three Successful or Failed missions, the game ends and the winning team is declared. Good wins if 3 missions have Succeeded, and Evil wins if 3 missions have Failed. If Good wins, the game moves into the Assassination phase.

## Assassination 
Once the Good team has won, the Evil team is permitted one final chance at winning the game by correctly identifying one of the priority targets (Merlin; Tristan and Iseult; Nimue). One player on the Evil team is selected as the Assassin, and is given the final say on who the Evil team would like to assassinate. Currently, the Assassin may choose whether to assassinate one person as Merlin, one person as Nimue, or two people as Lovers. Evil is welcome to discuss amongst themselves who they wish to kill, but the decision is not finalized until the Assassin says "I assassinate <player(s)> as <role(s)". If Evil has correctly identified Merlin or both Lovers, Evil wins; otherwise, Good maintains their victory. 

from Player import Player
import os, sys

class Team:

  def __init__(self, teamname, home_or_away, roster, ai):
    self.name = teamname
    self.side = home_or_away
    self.roster = roster
    self.ai = ai
    self.hasball = True
    self.score = 0

    self.players = []
    # Get players from file
    with open(roster) as p:

      for s in p:
        stats = s.split(',')
        self.players.append(Player(home_or_away, stats))
from RPS_game import play, quincy, abbey, kris, mrugesh, random_player
from RPS import player  # Import your player function
from unittest import main  # Import for running unit tests

# Play against each bot for 1000 rounds
print("Playing against Quincy...")
play(player, quincy, 1000, verbose=True)

print("\nPlaying against Abbey...")
play(player, abbey, 1000, verbose=True)

print("\nPlaying against Kris...")
play(player, kris, 1000, verbose=True)

print("\nPlaying against Mrugesh...")
play(player, mrugesh, 1000, verbose=True)

# Uncomment the line below to play interactively against a bot
 #print("\nInteractive play:")
#play(human, quincy, 10, verbose=True)

# Uncomment the line below to play against a bot that plays randomly
# play(human, random_player, 20, verbose=True)

# Run unit tests automatically
print("\nRunning unit tests...")
main(module='test_module', exit=False)

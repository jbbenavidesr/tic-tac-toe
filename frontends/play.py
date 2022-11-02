from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.renderers import ConsoleRenderer

player1 = RandomComputerPlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

print(player1.mark)
print(player2.mark)
print(player2.mark is player1.mark)

TicTacToe(player1, player2, ConsoleRenderer()).play()

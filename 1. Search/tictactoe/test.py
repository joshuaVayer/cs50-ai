import tictactoe as ttt

def test_initial_state():
    assert ttt.initial_state() == [[None, None, None], [None, None, None], [None, None, None]]

def test_player():
    assert ttt.player([[None, None, None], [None, None, None], [None, None, None]]) == "X"
    assert ttt.player([["X", None, None], [None, None, None], [None, None, None]]) == "O"
    assert ttt.player([["X", None, None], ["O", None, None], [None, None, None]]) == "X"
    assert ttt.player([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]) == None

def test_actions():
    assert ttt.actions([[None, None, None], [None, None, None], [None, None, None]]) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert ttt.actions([["X", None, None], [None, None, None], [None, None, None]]) == [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def test_result():
    assert ttt.result([["X", None, None], [None, None, None], [None, None, None]], (0, 1)) == [["X", "O", None], [None, None, None], [None, None, None]]
    assert ttt.result([["X", "O", None], [None, None, None], [None, None, None]], (1, 0)) == [["X", "O", None], ["X", None, None], [None, None, None]]
    assert ttt.result([["X", "O", None], ["X", None, None], [None, None, None]], (2, 0)) == [["X", "O", None], ["X", None, None], ["O", None, None]]
    assert ttt.result([["X", "O", None], ["X", None, None], ["O", None, None]], (0, 2)) == [["X", "O", "X"], ["X", None, None], ["O", None, None]]
    assert ttt.result([["X", "O", "X"], ["X", None, None], ["O", None, None]], (1, 1)) == [["X", "O", "X"], ["X", "O", None], ["O", None, None]]

test_player()
test_result()
test_actions()
test_initial_state()
import global_game_states
import add_clue


def test_add_clue(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'succeeded EnableIcon(ReadClue, Book, test clue item, Read Clue, true)')
    add_clue.add_clue('test clue', 'test clue item')
    print(global_game_states.current_clues)
    assert ['test clue item', 'test clue'] in global_game_states.current_clues
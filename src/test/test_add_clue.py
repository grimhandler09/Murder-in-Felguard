import global_game_states
import add_clue
import action

def test_add_clue(monkeypatch):
    monkeypatch.setattr(action, "action", "True")
    add_clue.add_clue('test clue', 'test clue item')
    assert ['test clue', 'test clue item'] in global_game_states.current_clues
import example_manager

def test_action_succeed(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'succeeded CreateCharacter(Bob, B)')
    output = example_manager.action('CreateCharacter(Bob, B)')
    assert output == True

def test_action_fail(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'failed CreateCharacter(Bob, B)')
    output = example_manager.action('CreateCharacter(Bob, B)')
    assert output == False



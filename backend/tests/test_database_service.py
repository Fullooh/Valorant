from services.database_service import add_player_stats, get_player_stats

def test_add_player_stats():
    add_player_stats('Player1', 1, 10, 5, 2, 1500.0)
    stats = get_player_stats('Player1')
    assert len(stats) > 0
    assert stats[0].player_name == 'Player1'

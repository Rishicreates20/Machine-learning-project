def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    # Simple strategy: Always play "Rock"
    return "R"


'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # 1. Retrieve list of users being followed by from_member and to_member
    from_member_FOLLOWING = social_graph[from_member]["following"]
    to_member_FOLLOWING = social_graph[to_member]["following"]

    # 2.1. Check if from_member follows to_member AND vice versa
    if (from_member in to_member_FOLLOWING) and (to_member in from_member_FOLLOWING):
        return "friends"
    # 2.2. Check if from_member follows to_member ONLY
    elif (from_member in to_member_FOLLOWING) and (to_member not in from_member_FOLLOWING):
        return "followed by"
    # 2.3. Check if from_member is FOLLOWED BY to_member ONLY
    elif (from_member not in to_member_FOLLOWING) and (to_member in from_member_FOLLOWING):
        return "follower"
    # 2.4. If none of the above conditions are met, then neither from_member and to_member follow each other
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # 1. Check board size
    board_size = len(board[0])

    # 2. Set winner variable
    winner = "NO WINNER"

    # 3. Check for any wins on the horizontal axis
    i = 0
    while i < board_size:
        
        # 3.1. Check for "X" win
        if ("X" in board[i]) and ("O" not in board[i]) and ("" not in board[i]):
            winner = "X"
            break
        
        # 3.2. Check for "O" win
        elif ("O" in board[i]) and ("X" not in board[i]) and ("" not in board[i]):
            winner = "O"
            break

        i += 1

    # 4. Check for any wins on the vertical axis
    vertical_axis_result = [] # Keeps track of elements on a given vertical axis
    k = 0

    for j in range(0, board_size): # Cycles through rows on board
        l = j % board_size
        
        for k in range(0, board_size): # Cycles through columns on board
            vertical_axis_result.append(board[k][0+l])
    
        # 4.1. Check for "X" win
        if ("X" in vertical_axis_result) and ("O" not in vertical_axis_result) and ("" not in vertical_axis_result):
            winner = "X"
            break

        # 4.1. Check for "Y" win
        elif ("O" in vertical_axis_result) and ("X" not in vertical_axis_result) and ("" not in vertical_axis_result):
            winner = "O"
            break

        vertical_axis_result = [] # Resets the vertical axis elements tracker
        
        l += 1

    # 5. Check for any diagonal wins

    # 5.1. Retrieves elements on a given diagonal axis (going from top left to bottom right corner of board)
    diagonal_result_slantLeft = []
    for m in range(0, board_size):
        diagonal_result_slantLeft.append(board[m][m])

    # 5.2. Retrieves elements on a given diagonal axis (going from top right to bottom left corner of board)
    startSlantRightCheck = board_size - 1
    diagonal_result_slantRight = []
    for n in range(0, board_size):
        diagonal_result_slantRight.append(board[n][startSlantRightCheck-n])
    
    # 5.3. Check for diagonal winner
   
    # 5.3.1. Check for "X" win (diagonal from top left to bottom right)
    if ("X" in diagonal_result_slantLeft) and ("O" not in diagonal_result_slantLeft) and ("" not in diagonal_result_slantLeft):
        winner = "X"

    # 5.3.2. Check for "X" win (diagonal from top right to bottom left)
    elif ("X" in diagonal_result_slantRight) and ("O" not in diagonal_result_slantRight) and ("" not in diagonal_result_slantRight):
        winner = "X"
        
    # 5.3.3. Check for "O" win (diagonal from top left to bottom right)
    elif ("O" in diagonal_result_slantLeft) and ("X" not in diagonal_result_slantLeft) and ("" not in diagonal_result_slantLeft):
        winner = "O"
    
    # 5.3.4. Check for "X" win (diagonal from top right to bottom left)
    elif ("O" in diagonal_result_slantRight) and ("X" not in diagonal_result_slantRight) and ("" not in diagonal_result_slantRight):
        winner = "O"

    # 6. Returns winner
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    total_travel_time = 0 # Tracks total travel time between first and second stops

    routes_list = list(route_map) # Converts route_map dictionary into list to enable indexing of tuple values

    # If there's an existing shuttle leg from first_stop to second_step, then simply retrieve the already-given travel time from the route_map dictionary
    if (first_stop, second_stop) in routes_list:
        total_travel_time = route_map[(first_stop, second_stop)]["travel_time_mins"]
        return total_travel_time
    else:
        # Otherwise, find the shuttle leg where first_stop is the first stop and then add the given travel time to total_travel_time
        index = 0
        for i in range(0, len(routes_list)):
            if first_stop == routes_list[i][0]:
                total_travel_time += route_map[routes_list[i]]["travel_time_mins"]
                index = i
                break

        # Find the shuttle leg where second_stop is the second stop and then add the given travel time to total_travel_time
        j = index
        rearranged_routes_list = routes_list[j+1:] + routes_list[:j+1]
        for k in range(0, len(rearranged_routes_list)):
            total_travel_time += route_map[rearranged_routes_list[k]]["travel_time_mins"]
            if second_stop == rearranged_routes_list[k][1]:
                break

        # Returns total travel time
        return total_travel_time
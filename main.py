from random import choice

plays = 0
won = False
max_tries = 1_000_000

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    while len(winning_ticket) < 6:
        pulled_item = choice(possibilities)
        # Add pulled item to winning ticket if it hasn't already been pulled
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check if items in the played ticket are in the winning ticket
    for i in played_ticket:
        if i not in winning_ticket:
            return False

    # winner
    return True

def make_random_ticket(possibilities):
    """ Make a random ticket from a set of possibilities"""
    ticket = []

    while len(ticket) < 6:
        pulled_item = choice(possibilities)
        # Add pulled item to winning ticket if it hasn't already been pulled
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket

possibilities = list(range(1, 50))

winning_ticket = get_winning_ticket(possibilities)


while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket! :D")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your final ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

    
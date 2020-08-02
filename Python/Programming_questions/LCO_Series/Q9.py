# Question
# 3 sweaters -> $68 each
# 1 Computer game -> $75
# 2 bracelets -> $43 each
# Returned 1 bracelet for full refund and got $10 rebate on Computer game.
# Calculate Total costs of gifts?

def costs():
    sweaters = 68
    computer_game = 75
    bracelet = 43
    return 68 * 3 + 1 * 75 + 2 * 43 - 1 * 43 - 10


print("Total costs - $", costs())

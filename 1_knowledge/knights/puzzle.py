from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Game rules: 
    
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A's statement: "I am both a knight and a knave."
    # If A is a knight, what A said must be true
    Implication(AKnight, And(AKnight, AKnave)),
    
    # If A is a knave, what A said must be false
    Implication(AKnave, Not(And(AKnight, AKnave))), 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Game rules:
    
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # B is either a knight or a knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A's statement: "We are both knaves."
    # If A is a knight, what A said must be true
    Implication(AKnight, And(AKnave, BKnave)),
    
    # If A is a knave, what A said must be false
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Game rules:
    
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or a knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A's statement: ""We are the same kind."
    # If A is a knight, what A said must be true
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    
    # If A is a knave, what A said must be false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    # B's statement: "We are of different kinds."
    # If B is a knight, what B said must be true
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    
    # If B is a knave, what B said must be false
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Game rules:
    
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or a knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    
    # C is either a knight or a knave, but not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A's statement: "I am a knight." or "I am a knave."
    # If A is a knight, what A said must be true
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is a knave, what A said must be false
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    
    # B's statement: "A said 'I am a knave'."
    # If B is a knight, what B said must be true
    Implication(BKnight, AKnave),
    # If B is a knave, what B said must be false
    Implication(BKnave, Not(AKnave)),
    
    # B's statement: "C is a knave."
    # If B is a knight, what B said must be true
    Implication(BKnight, CKnave),
    # If B is a knave, what B said must be false
    Implication(BKnave, Not(CKnave)),
    
    # C's statement: "A is a knight."
    # If C is a knight, what C said must be true
    Implication(CKnight, AKnight),
    # If C is a knave, what C said must be false
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

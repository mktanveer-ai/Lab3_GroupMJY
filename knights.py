from logic import *

AKnight = Symbol("AKnight")
AKnave = Symbol("AKnave")
BKnight = Symbol("BKnight")
BKnave = Symbol("BKnave")


def person_rules(knight, knave):
    return And(
        Or(knight, knave),
        Not(And(knight, knave))
    )


# Puzzle 0
# A says: "I am both a knight and a knave."

statement0 = And(AKnight, AKnave)

knowledge0 = And(
    person_rules(AKnight, AKnave),
    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

print("Puzzle 0")
for symbol in [AKnight, AKnave]:
    if model_check(knowledge0, symbol):
        print(symbol)


# Puzzle 1
# A says: "We are both knaves."

statement1 = And(AKnave, BKnave)

knowledge1 = And(
    person_rules(AKnight, AKnave),
    person_rules(BKnight, BKnave),
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

print("\nPuzzle 1")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge1, symbol):
        print(symbol)


# Puzzle 2
# A says: "We are the same kind."
# B says: "We are different kinds."

same = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)

different = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)

knowledge2 = And(
    person_rules(AKnight, AKnave),
    person_rules(BKnight, BKnave),

    Implication(AKnight, same),
    Implication(AKnave, Not(same)),

    Implication(BKnight, different),
    Implication(BKnave, Not(different))
)

print("\nPuzzle 2")
for symbol in [AKnight, AKnave, BKnight, BKnave]:
    if model_check(knowledge2, symbol):
        print(symbol)

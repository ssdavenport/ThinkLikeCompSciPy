"""
Are you thinking of an animal? y
Is it a bird? n
What is the animals name? dog
What question would distinguish a dog from a bird? Can it fly
If the animal were dog the answer would be? n

Are you thinking of an animal? y
Can it fly? n
Is it a dog? n
What is the animals name? cat
What question would distinguish a cat from a dog? Does it bark
If the animal were cat the answer would be? n

Are you thinking of an animal? y
Can it fly? n
Does it bark? y
Is it a dog? y
I rule!
Are you thinking of an animal? n
"""
def win():
    print("I rule!")

#start = Tree("Are you thinking of an animal?", )

"""
thinking_animal = 
if thinking_animal == "n":
    print('nevermind then')
elif thinking_animal=="y":
    bird = input("is it a bird?")
"""

class animalTree:
    def __init__(self, last_animal="bird", first=False):
        # If it's the first time, just guess the animal.
        if first == True:
            answer = input("is it a " + last_animal + "?")
            if answer == "y":
                print("I rule!")

        new_animal = input("what is the animal's name?")
        new_question = input("what question would distinguish a " + new_animal + " from a " + last_animal)
        correct_answer = input("If the animal were a " + new_animal + " the answer would be...?")

        self.question = new_question
        self.correct_answer = correct_answer
        self.animal = new_animal
        self.child = None


def ask_question(tree=None):
    play = input("Are you thinking of an animal?")
    if play =="y":
        if tree.question: # if we are not on the end node, ask a narrowing Q
            answer = input(tree.question) # get an answer to your narrowing Q
            # if your narrowing answer is correct.
            if(answer == tree.correct_answer):
                final_guess_answer = input("Is it a " + tree.animal + "?")
                # if your final guess is correct
                if(final_guess_answer=='y'):
                    print("I rule!")
                # if your final guess is wrong.
                else:
                    # make a new question node to store the answer.
                    tree.child = animalTree(last_animal=tree.animal)
            # if your narrowing answer is wrong
            else:
                # and there's a new Q, then ask it
                if tree.child:
                    ask_question(tree.child)
                # but there are no new Q's
                # make a new question node to store the answer.
                else:
                    tree.child = animalTree(last_animal=tree.animal)
        ask_question(first_tree)


# if this is the first time around
play="y"
while play =="y":
    play = input("Are you thinking of an animal?")
    if play =="n": break
    first_tree = animalTree(first=True)
    ask_question(first_tree)


#animalTree()

# would be nice to fix this so that it can branch at the "YES"es instead of just at the no's.


"""
    def give_up(self):
        # Only asked if there is no child node, i.e., we're out of questions.
        lucky_guess = input("is it a " + self.animal + "?")
        if lucky_guess == "y":
            print("I rule!")
            finished = 1
        else:



            self.nextq = animalTree(nextq, correct_answer, new_animal)


starting_tree = animalTree(None, None, "bird")

def ask(tree):
    finished = 0
    while finished == 0:
        # if no questions to ask, give up immediately.
        input("Are you thinking of an animal?")
        if tree.nextq == None:
            tree.give_up()
        else:
            answer = input(tree.nextq)
            # if your answer is correct, go straight to guessing.
            if answer == tree.correct_answer:
                tree.give_up()
                # ac
                ##if not tree.correct_next_question == None:
                  #  ask(tree.correct_next_question)
                #else: tree.give_up()
            # if the answer is wrong, attempt to ask the next Q
            if not answer == tree.correct_answer:
                ask(tree.nextq)
                #if not tree.incorrect_next_question == None:
                #    ask(tree.incorrect_next_question)
                #else: tree.give_up()
            # when there are no new questions to ask, give up.
    print("this game is over! I rule")

ask(starting_tree)


# add in the primer text...
# ask what animal guesses you have. If none work...
#ask_questions()

# start over again, on the new (now bigger) tree.

"""

"""



def start_game():
    win == 0
    first_question: "Are you thinking of an animal?"

    while win == 0:
        first_answer = input(first_question)
        if first_answer == "n":
            return "game over then"
        if first_answer == "y":
            # Start searching the tree.
            # Start from the root.
            output = ask_qs("bird") # this output is a new Tree. attach it to the old tree.






"""
#new_tree = ask_qs("bird")

"""
final_guess = input("is it a " + new_tree.animal+ "?")
if final_guess == "y":
    win()
elif final_guess == "n":
    newer_tree = ask_qs(new_tree.animal)

# now you want to be storing your output, so all qs are saved.

q1 = "Are you thinking of an animal?"
q2 = "Is it a bird?"
q3 = "What is the animal's name?"
q4 = "What question would distinguish a dog from a bird?"
q5 = "If the animal were a "

"""

"""

# Return to this tomorrow.
class Tree():
    def __init__(self, cargo, no=None, yes=None):
        self.cargo= cargo
        self.no = no
        self.yes = yes

    def __str__(self):
        return str(self.cargo)
    # default to indented view




def printTree(Tree, level=0):
    if Tree == None: return
    printTree(Tree.right, level + 1)
    print("  " * level, str(Tree.cargo))
    printTree(Tree.left, level + 1)



printTree(Tree(2, Tree(2, Tree(1, Tree(3), Tree(5)),  Tree(4)), Tree(5, Tree('lrftright'), Tree('farright'))))

"""
import sys

class Program:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
    
    def setChild(self, index, value):
        self.children[index] = value

    def getChildrenLength(self):
        return len(self.children)

    def __str__(self):
        childrenString = "["
        for child in self.children:
            childrenString += str(child)
            childrenString += ", "
        childrenString += "]"
        return f'{self.name} weighing {self.weight} with {childrenString}'

def program_info(inputLine):
    removedCommas = inputLine.replace(',', '')
    removedParentheses = removedCommas.replace(')', '')
    removedParentheses = removedParentheses.replace('(', '')
    elements = removedParentheses.split()
    if (len(elements) < 3):
        return Program(elements[0], int(elements[1]), [])
    else:
        return Program(elements[0], int(elements[1]), elements[3:])

ProgramList = []
ParentsChildren = []
ParentProgramList = [] # Still need this to get our starting point
with open("Program_List.txt", "r") as memoryBlocks:
    for line in memoryBlocks:
        element_info = program_info(line)
        ProgramList.append(element_info)
        if (element_info.getChildrenLength() > 0):
            ParentProgramList.append(element_info.name)
            ParentsChildren.extend(element_info.children)

STARTING_ELEMENT = None

for element in ProgramList:
    if element.name in ParentsChildren:
        continue
    else:
        STARTING_ELEMENT = element

def getProgramByName(aProgramName):
    global ProgramList
    for program in ProgramList:
        if program.name == aProgramName:
            return program

def gatherElementFromTree(anElement):
    global ProgramList
    program = getProgramByName(anElement)
    counter = 0 
    key = program.name
    for subElement in program.children:
        program.setChild(counter, gatherElementFromTree(subElement))
        counter += 1
    return program 

PROGRAM_TREE = gatherElementFromTree(STARTING_ELEMENT.name)

def checkTreeBalance(TreeRoot):
    tempNumbers = []
    uniqueNums = {}
    baseSum = TreeRoot.weight
    # Gather all of the sums from derivative branches
    for child in TreeRoot.children:
        tempSum = checkTreeBalance(child)
        tempNumbers.append(tempSum)
    for aNumber in tempNumbers:
        if aNumber not in uniqueNums:
            uniqueNums.update({aNumber: 1})
        else:
            uniqueNums[aNumber] += 1
    error_amount = 0
    error_index = -1
    if len(uniqueNums) > 1: # This is the error
        for aNumber in list(uniqueNums.keys()):
            if uniqueNums[aNumber] == 1: # Exactly one occurance
                error_amount = aNumber
        error_index = tempNumbers.index(error_amount)
        problem_child = TreeRoot.children[error_index]
        del uniqueNums[error_amount]
        correct_amount = list(uniqueNums.keys())[0]
        difference = correct_amount - error_amount
        correct_weight = problem_child.weight + difference
        print(f'The unbalanced program (Part 2) is {problem_child.name}, it should be offset by {difference} to {correct_weight}')
        exit(0)
    return sum(tempNumbers) + baseSum

checkTreeBalance(PROGRAM_TREE)

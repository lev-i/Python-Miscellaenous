# creates a dictionary to hold names and scores
names = ['Tom','Joe','Alice','Bob','Jane']
scores = [75, 65, 85, 45, 99]
print(names)
print(scores)

# function with two parameters: names and scores, both of which are lists
# returns a dictionary in which the keys are the names and the values are the scores
def make_score_dict(names,scores):
    score_dict={}
    for i in range(len(names)):score_dict[names[i]]=scores[i]
    return score_dict

names=['Tom','Joe','Alice','Bob','Jane']
scores=[75,65,85,45,99]
score_dict=make_score_dict(names,scores)
print(score_dict)

# pulls the score for Joe
print(score_dict["Joe"])

# appends member (Ralph) to dictionary with a score of 80
score_dict["Ralph"] = 80
print(score_dict)

# amends a score (Bob's) to a new value
score_dict["Bob"] = 75
# print updated dictionary
print(score_dict)

# removes a member from the dictionary
del score_dict["Jane"]
# print updated dictionary
print(score_dict)

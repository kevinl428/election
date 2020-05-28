# input number of candidates
from collections import Counter


lst = []
candidate_list = input("What are the candidate names? ")

voter_count = int(input("Number of voters: "))
vote_amount = [voter_count]
for i in range(voter_count):
	vote = input("Vote for one of {}: ".format(candidate_list)) 
	lst.append(vote)

print(lst)
winner = Counter(lst)
for candidate, votes in winner.most_common(1):
	print("The winner is {} with {} votes".format(candidate, votes, sep=': '))






# print out the winner (who has the most votes)

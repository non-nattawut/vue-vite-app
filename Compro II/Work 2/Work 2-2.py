s1 = {'Blue','Black','Green'}
s2 = {'Red','Black','Yellow','Blue','Brown'}

print("Add them all:",s1.union(s2))
print("In s1 and in s2:",s1.intersection(s2))
print("In s1, not in s2:",s1.difference(s2))
print("In s1, not in s2 AND in s2:",s1.symmetric_difference(s2))
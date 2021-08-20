# truth table for q V ~q
# q or not q
truth = [True, False]
print("q   ", "not q  ", "q or not q")
for q in truth:
    print(q, not q, q or not q)

# truth table for (~p V q) ^ (p V ~q)
# (not p or q) and (p or not q)
truth = [True, False]
print("p  ", "q  ", "(not p or q) and (p or not q)")
for p in truth:
    for q in truth:
        print(p,  q, (not p or q) and (p or not q))
    
# (p^q) -> (p V q)
# if (p and q) then (p or q)
# we can evaluate an "if x then y" by "not x or y", as they provide the same output
# when (p and q) is true, (p or q) is also true
# for other outputs, (p and q) is not satisfied, so the output remains true

truth = [True, False]
print("p  ", "q  ", "p ^ q", "p V q", "(p^q) -> (p V q)")
for p in truth:
    for q in truth:
        print(p,  q, p and q, p or q, not (p and q) or (p or q))

'''
What is the proper way to compute the load factor of a hash table?
'''

# Answer:
# The number of items stored in a hash table divided by the total number of slots.

'''
Why is the load factor of a hash table important?
'''

# Answer:
# As the load factor of your hash table increases, so does the likelihood of a collision, which reduces your hash 
# table's performance. It is important to monitor the load factor and resize your hash table when the load factor 
# gets too large.
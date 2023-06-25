
# We are tasked with finding the largest palindrome number
# which is a product of two 3 digit numbers

'''
Brainstorm:

  A B C
x D E F
=======
????


10^ | 5   4   3   2   1   0
====+========================
    |             AF  BF  CF 
    |         AE  BE  CE     
    |     AD  BD  CD         
=============================
    |                        
^^^ This is too complicated lets brute force.
The problem is that each product of digits here *could be* greater than 9.

'''



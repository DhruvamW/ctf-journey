## Password Profiler
**Category:** General Skills  
**Points: 100**   
**What it was:** leverage information to generate a custom password list and recover the original password by matching its hash. 

**How I solved it:** 
->create alice.txt using CUPP
->mv alice.txt passwords.txt
->python3 check_password.py

**What I learned:** CUPP s a Python tool for generating custom wordlists from personal data

**Flag:** picoCTF{Aj_15901990}
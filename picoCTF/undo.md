## Undo
**Category:** General Skills  
**Points: 100**   
**What it was:** reverse a series of Linux text transformations to recover the original flag  

**How I solved it:** 
->base64 -d
->rev
->tr 'a-zA-Z' 'n-za-mN-ZA-M' (rot13)

**What I learned:** rot13 and base64 decode commands

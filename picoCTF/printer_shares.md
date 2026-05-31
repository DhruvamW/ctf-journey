## Printer Shares
**Category:** General Skills  
**Points: 50**   
**What it was:** retrieve an important file sent to a network printer  

**How I solved it:** 
->smbclient -L //mysterious-sea.picoctf.net/ -N -p 55584
->smbclient //mysterious-sea.picoctf.net/shares -N -p 55584
->get flag.txt
->ctrl+d
->cat flag.txt

**What I learned:** smbclient command

**Flag:** picoCTF{5mb_pr1nter_5h4re5_8eb6dd5d}
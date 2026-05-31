## Pice by Piece
**Category:** General Skills  
**Points: 50**   
**What it was:**  parts need to be combined and extracted to reveal the flag  

**How I solved it:** 
-> ssh ctf-player@dolphin-cove.picoctf.net -p 60923
-> cat part_* > combined.zip
-> unzip combined.zip
-> cat flag.txt

**What I learned:** zipping and unzipping a file and grouping files

**Flag:** picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_28d309dc}
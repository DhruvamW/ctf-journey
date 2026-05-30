# OverTheWire: Bandit Notes (Levels 0–15)

## Level 0
**Concept:** Connecting to a remote server via SSH
**Command:** `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
**What I learned:** SSH is how you connect to remote machines. Always need: user, host, port.

## Level 0 → 1
**Concept:** Reading a file
**Command:** `cat readme`
**What I learned:** Password is stored in a file called `readme` in the home directory.

## Level 1 → 2
**Concept:** Reading a file with a special name (`-`)
**Command:** `cat ./-`
**What I learned:** Files starting with `-` are treated as flags by commands. Use `./` prefix to read them.

## Level 2 → 3
**Concept:** Reading a file with spaces in the name
**Command:** `cat "spaces in this filename"`
**What I learned:** Wrap filenames with spaces in quotes or escape with backslash.

## Level 3 → 4
**Concept:** Finding hidden files
**Command:** `ls -a inhere/`
**What I learned:** Files starting with `.` are hidden. Use `ls -a` to see them.

## Level 4 → 5
**Concept:** Finding the only human-readable file
**Command:** `file inhere/-file0*`
**What I learned:** `file` command identifies file types. Look for "ASCII text" — that's human readable.

## Level 5 → 6
**Concept:** Finding a file by specific properties
**Command:** `find inhere/ -type f -size 1033c ! -executable`
**What I learned:** `find` can filter by size (`-size`), type (`-type f`), and permissions (`! -executable`).

## Level 6 → 7
**Concept:** Finding a file anywhere on the server by owner and size
**Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`
**What I learned:** `2>/dev/null` suppresses permission denied errors. Search the whole system with `/`.

## Level 7 → 8
**Concept:** Finding a word in a large file
**Command:** `grep 'millionth' data.txt`
**What I learned:** `grep` searches for a pattern inside a file. Essential for CTFs.

## Level 8 → 9
**Concept:** Finding the one unique line in a file
**Command:** `sort data.txt | uniq -u`
**What I learned:** `uniq -u` shows only lines that appear once. Must sort first for uniq to work.

## Level 9 → 10
**Concept:** Extracting readable strings from a binary file
**Command:** `strings data.txt | grep '=='`
**What I learned:** `strings` pulls human-readable text out of any file, including binaries.

## Level 10 → 11
**Concept:** Decoding base64
**Command:** `base64 -d data.txt`
**What I learned:** Base64 is an encoding scheme, not encryption. Very common in CTFs.

## Level 11 → 12
**Concept:** ROT13 decoding
**Command:** `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
**What I learned:** ROT13 shifts letters by 13. `tr` is used to translate/replace characters.

## Level 12 → 13
**Concept:** Repeatedly decompressing a file
**Commands:** `xxd -r`, `gunzip`, `bunzip2`, `tar -xf`
**What I learned:** Files can be compressed multiple times. Use `file` after each step to know what to do next. Always decompress in `/tmp` since you need write access.

## Level 13 → 14
**Concept:** SSH with a private key instead of a password
**Command:** `ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220`
**What I learned:** Private keys replace passwords for SSH. Fix permissions with `chmod 600 sshkey.private` first.

## Level 14 → 15
**Concept:** Sending data to a port using netcat
**Command:** `echo "password" | nc localhost 30000`
**What I learned:** `nc` (netcat) connects to ports and sends/receives data. Used constantly in CTFs.

---
## Key Takeaways
- Always use `file` when you don't know what something is
- `2>/dev/null` cleans up noisy output
- `find` is powerful — filter by size, owner, permissions, type
- Base64 and ROT13 are the two most common encodings in beginner CTFs
- SSH keys > passwords — know how to use `-i` flag

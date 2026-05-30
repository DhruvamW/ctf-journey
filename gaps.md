# Gaps & Commands — CTF Journey

## SSH
- Connect to a server: `ssh -p <port> user@host`
- Connect with a private key: `ssh -i sshkey.private user@host -p 2220`
- Fix key permissions before using: `chmod 600 sshkey.private`

## File Navigation & Search
- See hidden files: `ls -a`
- Find by size, type, not executable: `find -type f -size 1033c ! -executable`
- Suppress permission errors: `find / -name file 2>/dev/null`

## Reading & Decoding Files
- Decode base64: `base64 -d data.txt`
- ROT13: `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- Reverse text: `rev data.txt`
- Find unique line: `sort data.txt | uniq -u`

## Compressed Files
- gzip: `gunzip file.gz`
- bzip2: `bunzip2 file.bz2`
- tar: `tar -xf file.tar`
- Combine split files then unzip: `cat part_* > combined.zip && unzip combined.zip`

## Networking
- Connect to a port: `nc host port`
- Send a string to a port: `echo "password" | nc localhost 30000`
- SSL connection: `echo "password" | openssl s_client -connect localhost:30001 -quiet`
- List SMB shares: `smbclient -L //host/ -N -p <port>`
- Connect to SMB share: `smbclient //host/shares -N -p <port>`
- Download file from SMB: `get flag.txt`

## Misc
- Reset a broken terminal: `reset`

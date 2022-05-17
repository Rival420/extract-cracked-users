# extract-cracked-users
python tool to extract cracked users from a hashcat job.
you will need to save your cracked passwords along with usernames in a file. 
(hashcat -w hashes.txt --show --usernames)
use this file as the input and choose an output file.

great for when you do a password audit. use this tool to extract users along with the length of their password.
(or change the script to include their password in your results)

example:
```
python3 extract.py -f crackedusers.txt -o results.txt
```

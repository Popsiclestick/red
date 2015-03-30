Pylocker
===
Cryptolocker implemented in python. When pointed at a directory, it will recursively encrypt all files in that directory with AES-128.

### To-Do:
* Randomly generate key and place it in a file (Just kept it static for testing and ease of use).
* Haven't decided if I then want to encrypt the symmetric key with an asymmteric key. 
* ~~While binaries still work, seems to make them smaller. Rather concerning but in a competition scenerio seems less concerning. (Using CFB mode compared to CBC mode would most likely fix this problem).~~
* 
#### Changes:
* Changed CBC mode to CFB mode to avoid padding/stripping complications

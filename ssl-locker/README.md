Pylocker
===
Cryptolocker implemented in Bash. When pointed at a directory, it will recursively encrypt all files in that directory with AES-256.

### Usage:
Be aware of the global varibles. These must be changed for the **target directory**, whatever you want your passphrase to be, and which files **not** to encrypt/decrypt. I would recommend not encrypting all binaries in the event you want to decrypt everything or reboot the system.


### To-Do:
* ~~Add file exclusions~~

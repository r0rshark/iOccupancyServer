Here an example of a script in order to generate beacon packets. 
You can modify all field in order to change uuid major minor and power.

############ EXAMPLE ###############
Reading this in line in the script you can find:
-setup of protocol → NEVER CHANGE IT
hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 1a 1a ff 4c 00 02 15 

- UUID field
e2 c5 6d b5 df fb 48 d2 b0 60 d0 f5 a7 10 96 e0 

- MAJOR field
00 00 

- Minor field
00 00 

- TX Power
c4 

-end NEVER CHANGE IT
00
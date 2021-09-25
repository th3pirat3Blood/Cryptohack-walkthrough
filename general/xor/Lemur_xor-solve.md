# Lemur Solve

Open one of the files in *stegsolve.jar* and xor it with the other image to obtain image containing flag. 

Can also be done using just reading the files as raw bytes in python, just make sure not to xor the header and footer of the files and both being .png will have same bytes in header and footer and will result in 0x00 in place of bytes used to identify file type causing the resulting xor file to be unuseable.
import psutil

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 

print("Memory statistics\n")#, psutil.virtual_memory())
mem = psutil.virtual_memory()
print(mem)
THRESHOLD = 300 * 1024 * 1024 #300MB
if mem.available <= THRESHOLD:
    prRed("Warning")
#   print("\033[5;31;40m Warning\n")
#   print("warning")

print("\n")


print("Swap memory statistics\n", psutil.swap_memory())

import subprocess

subprocess.run('ls')

# To pass the full command we need to use shell argument (but it's a security hazard)
subprocess.run('ls -ltr', shell=True)

# We can use the data as the list of args
subprocess.run(['ls', '-ltr'])

# Checking the return value of the subprocess (default)
p1 = subprocess.run(['ls', '-ltr'])
print(p1)
# o/p of print CompletedProcess(args=['ls', '-ltr'], returncode=0)

# Capturing the o/p in a variable
p1 = subprocess.run(['ls', '-ltr'], stdout=subprocess.PIPE)
print(p1.stdout.decode())

# Capturing the o/p in a file
with open('output.txt', 'w') as f:
    subprocess.run(['ls', '-ltr'], stdout=f)

# For some error in the external command
p1 = subprocess.run(['ls', '-ltr', 'dne'], stdout=subprocess.PIPE)
print(p1)

# Python to throw an error if some issue occurs
p1 = subprocess.run(['ls', '-ltr', 'dne'], stdout=subprocess.PIPE, check=True)
print(p1)

p1 = subprocess.run(['ls', '-ltr', 'dne'], stderr=subprocess.DEVNULL)
print(p1)

# O/p of one command and providing that as input to other command
p1 = subprocess.run(['cat', 'output.txt'], stdout=subprocess.PIPE)
print(p1.stdout.decode())

p2 = subprocess.run(['grep', '-n', '.txt'],
                    stdout=subprocess.PIPE, input=p1.stdout)
print(p2.stdout.decode())

# Also
p1 = subprocess.run('cat output.txt | grep -n .txt',
                    stdout=subprocess.PIPE, shell=True)
print(p1.stdout.decode())

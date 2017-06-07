import subprocess
import time

f = open('phones.txt', 'r')
n = 0
for x in f:
    v_comm = 'add_contact ' + x.strip() + ' ' + str(n) + ' ' + str(n)
    print(v_comm)
    cmd = 'telegram-cli.exe' #консоль
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE, #
                               stdin = subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               cwd = "C:/cygwin64/tg_old/"
                               )
    # process.wait()
    process.stdin.write('{}\r'.format(v_comm).encode('utf-8'))
    out = process.stdout.readlines()
    print(out.decode('CP866', 'replace'))
    time.sleep(1)
    n += 1




'''
import subprocess
import time

f = open('phones.txt', 'r')
n = 0
for x in f:
    v_str = 'add_contact ' + x.strip() + ' ' + str(n) + ' ' + str(n)
    print(v_str)
    cmd = ('telegram-cli.exe',v_str) #консоль
    process = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               stdin=subprocess.PIPE,
                               shell=True,
                               cwd = "C:/cygwin64/tg_old/",
                               bufsize=0)
    #process.stdin.write('{}'.format(v_str).encode('utf-8'))
    out, err = process.communicate()
    print(out.decode('CP866', 'replace'))
    time.sleep(1)
    n += 1
print('done')
'''
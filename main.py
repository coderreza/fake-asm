import os , keyboard
code='''section.data

msg db 'Hello, World!', 10

newline db "\n',0

section.text

global_start

_start:

'm'

:---- Print message ----

'm'

sys_write mov eax, 4

'm'

mov ebx, 1 ; stdout

'm'

mov ecx,msg; message address

mov edx, 14; length (14 chars)

'i'

int 0x80 ; system call

; ---- Print newline ----

mov eax,4

,'m'

mov ebx, 1

'm'

mov ecx, newline

mov edx, 1

'm'

int 0x80

'm'

; ---- Simple addition ----

'i'

mov eax, 10; store 10 in eax

mov ebx,20; store 20 in ebx

add eax, ebx; eax = 30'''
code_is=0
while code_is<=503:
    key=str(keyboard.read_event())[14:15]
    if keyboard.is_pressed(key)==True:
        code_is=code_is+1
        if os.name=='nt':
            os.system('cls')
        else:
            os.system("clear")
        print(code[0:code_is] , end="")

.globl main
 
.data
    inpMsg: .asciz "Enter %c: "
    fmt: .asciz " %d"
    A: .quad 0
    B: .quad 0
    C: .quad 0
    out: .asciz "Result = %d\n"

.section .text

main:  
    pushq %rbp
    movq %rsp,    %rbp

    movq $0,      %rax
    movq $inpMsg, %rdi
    movq $'A',    %rsi
    call printf

    movq $fmt,    %rdi
    movq $A,      %rsi
    call scanf

    movq $0,      %rax
    movq $inpMsg, %rdi
    movq $'B',    %rsi
    call printf

    movq $fmt,    %rdi
    movq $B,      %rsi
    call scanf

    movq $0,      %rax
    movq $inpMsg, %rdi
    movq $'C',    %rsi
    call printf

    movq $fmt,    %rdi
    movq $C,      %rsi
    call scanf

    movq C,       %rax
    movq C,       %rbx
    mulq %rbx
    mulq %rbx
    movq %rax,    C

    movq B,       %rax
    movq $6,      %rcx
    mulq %rcx
    movq %rax,    B

    movq A,       %rax
    mulq %rax

    addq B,       %rax
    divq C

    movq %rax,    %rsi
    movq $out,    %rdi
    movq $0,      %rax

    call printf

    movq $0,      %rdi
    call exit

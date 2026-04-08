.global main

.data
  inputMessage: .asciz "Enter %c: "
  inputFmt:     .asciz " %d"
  outputMessage: .asciz "Result: %d\n"
  
  A: .quad 0
  B: .quad 0
  C: .quad 0
  P: .quad 0

.text
main:
  pushq %rbp
  movq  %rsp,          %rbp
  
  movq  $0,            %rax
  movq  $inputMessage, %rdi
  movq  $'A',          %rsi
  call  printf

  movq  $inputFmt,     %rdi
  movq  $A,            %rsi
  call  scanf

  movq  $inputMessage, %rdi
  movq  $'B',          %rsi
  call  printf

  movq  $inputFmt,     %rdi
  movq  $B,            %rsi
  call  scanf

  movq  $inputMessage, %rdi
  movq  $'C',          %rsi
  call  printf

  movq  $inputFmt,     %rdi
  movq  $C,            %rsi
  call  scanf

  movq  A,             %rax
  movq  B,             %rbx
  addq  %rbx,          %rax
  movq  C,             %rbx
  subq  %rbx,          %rax
  jns   _trueExit
  testq %rax,          %rax

  movq  B,             %rax
  movq  C,             %rax
  addq  %rbx,          %rax
  movq  A,             %rbx
  subq  %rbx,          %rax
  jns   _trueExit
  testq %rax,          %rax

  movq  C,             %rax
  movq  A,             %rbx
  addq  %rbx,          %rax
  movq  B,             %rbx
  subq  %rbx,          %rax
  jns   _trueExit

  jmp  _exit
_trueExit:
  jz   _exit
  movq $1,             P
_exit:
  movq $0,             %rax
  movq $outputMessage, %rdi
  movq P,              %rsi
  call printf
  movq $0,             %rdi
  call exit

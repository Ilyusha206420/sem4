.global main

.data
  inputMessage: .asciz "Enter %c: "
  inputFmt:     .asciz " %d"
  
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
  
exit:
  movq  $0, %rdi
  call  exit

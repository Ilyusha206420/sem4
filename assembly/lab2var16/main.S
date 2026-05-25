.global main

.data
  inputMessage:  .asciz "Enter %c: "
  outputMessage: .asciz "Result: %d\nReminder: %d\n"
  inputFmt:      .asciz " %ld"
  
  Avar: .quad 0
  Bvar: .quad 0
  Cvar: .quad 0

.text

main:
  pushq %rbp
  movq  %rsp,           %rbp

  movq  $0,             %rax
  movq  $inputMessage,  %rdi
  movq  $'A',           %rsi
  call  printf

  movq  $inputFmt,      %rdi
  movq  $Avar,          %rsi
  call  scanf

  movq  $inputMessage,  %rdi
  movq  $'B',           %rsi
  call  printf

  movq  $inputFmt,      %rdi
  movq  $Bvar,          %rsi
  call  scanf

  movq  $inputMessage,  %rdi
  movq  $'C',           %rsi
  call  printf

  movq  $inputFmt,      %rdi
  movq  $Cvar,          %rsi
  call  scanf

  movq  Cvar,           %rax
  movq  Bvar,           %rbx
  imulq %rbx
  pushq %rax

  movq  Bvar,           %rax
  movq  $3,             %rbx
  imulq %rax
  imulq %rbx
  pushq %rax
  
  movq  Avar,           %rax
  movq  Cvar,           %rbx
  imulq %rax
  imulq %rbx
  movq  $2,             %rbx
  imulq %rbx

  popq  %rbx
  addq  %rbx,           %rax

  popq  %rcx
  movq $0, %rdx
  cqo
  idivq %rcx

  movq  $outputMessage, %rdi
  movq  %rax,           %rsi
  movq  $0,             %rax
  call  printf
  
  movq  $0,             %rdi
  call  exit

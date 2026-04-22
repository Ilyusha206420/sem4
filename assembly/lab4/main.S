.global main

.data
  inpNMsg:       .asciz "Input number of values: "
  inpFmt:        .asciz " %d"
  errorAllocMsg: .asciz "Error! Can't allocate memory"
  inputSetMsg:   .asciz "Input your value set: "
  outMsgBegin:   .asciz "Result: [ "
  outMsgEnd:     .asciz "]\n"
  outFmt:        .asciz "%d "
  N:             .quad 0
  outLen:        .quad 0
  inpArrPtr:     .quad 0
  outArrPtr:     .quad 0
.text

main:
  pushq %rbp
  movq  %rsp,            %rbp

  movq  $0,              %rax
  movq  $inpNMsg,        %rdi
  call  printf

  movq  $inpFmt,         %rdi
  movq  $N,              %rsi
  call  scanf

  movq  N,               %rax
  shr   %rax
  movq  %rax,            outLen
  movq  $8,              %rbx
  mulq  %rbx
  movq  %rax,            %rdi
  call  malloc

  cmpq  $0,              %rax
  jz    errorAllocExit

  movq  %rax,            outArrPtr

  movq  N,               %rax
  movq  $8,              %rbx
  mulq  %rbx
  movq  %rax,            %rdi
  call  malloc
  
  cmpq  $0,              %rax
  jz    errorAllocExit

  movq  %rax,            %r13
  movq  %rax, inpArrPtr

  movq  $0,              %rax
  movq  $inputSetMsg,    %rdi
  call  printf

  movq  $0,              %r12
inpLoopStart:
  cmpq  N,               %r12
  jge   inpLoopEnd

  movq  $inpFmt,         %rdi
  leaq  (%r13, %r12, 8), %rsi
  movq  $0,              %rax
  call  scanf

  incq  %r12
  jmp   inpLoopStart
inpLoopEnd:

  movq  $0,              %rax
  movq  outArrPtr,       %r11
  movq  $0,              %rbx
  movq  $2,              %r10
  movq  inpArrPtr,       %r12
  
copyLoopStart:
  cmpq  outLen,          %rax
  jge   copyLoopEnd

  movq  (%r12, %rbx, 8), %rdx
  movq  %rdx,            (%r11, %rax, 8)  

  addq  %r10,            %rbx
  incq  %rax
  jmp   copyLoopStart
copyLoopEnd: 

  movq  inpArrPtr,       %rdi
  call  free

  movq  $0,              %rax
  movq  $outMsgBegin,    %rdi
  call  printf

  movq  $0,              %r12
  movq  outArrPtr,       %r13
outLoopStart:
  cmpq  outLen,          %r12
  jge   outLoopEnd
  
  movq  $0,              %rax
  movq  $outFmt,         %rdi
  movq  (%r13, %r12, 8), %rsi
  call printf 

  incq  %r12
  jmp   outLoopStart
outLoopEnd:

  movq  $0,              %rax
  movq  $outMsgEnd,      %rdi
  call printf

  movq  outArrPtr,       %rdi
  call  free

  movq  $0,              %rdi
  call  exit

errorAllocExit:
  cmpq  $0,              outArrPtr
  jz    err

  movq  outArrPtr,       %rdi
  call  free
err:
  movq  $0,              %rax
  movq  $errorAllocMsg,  %rdi
  call  exit

  movq  $-1,             %rdi
  call  exit
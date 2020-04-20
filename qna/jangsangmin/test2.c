#include <stdio.h>

int main() {
  long i = 0x00000064, j = 1;
  printf("i의 주소: %x\n", &i);
  printf("i의 값: %x\n", i);

  printf("%128d%n\n", j, &i);
  printf("변경된 i의 값: %x\n", i);
}

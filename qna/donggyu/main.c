#include <stdio.h>

int main()
{
  int x;
  scanf("%d", &x);

  printf("%d는 이진수로 ");
  printf("%d", x & 8);
  printf("%d", x & 4);
  printf("%d", x & 2);
  printf("%d", x & 1);
  printf("입니다\n");
}

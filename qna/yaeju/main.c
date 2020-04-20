#include <stdio.h>

int main() {
  FILE * input = fopen("input.txt", "r");

  int n = 0;
  fscanf(input, "%d\n", &n);

  for (int i = 0; i < n; i++) {
    char buff[200];
    fscanf(input, "%s", buff);
    printf("%s\n", buff);
  }

  fclose(input);
}

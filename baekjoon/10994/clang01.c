#include <stdio.h>

typedef const char * str;

int make_lower_then(int num, int standard, int plus)
{
  if (num <= standard)
    return num;
  else
    return 2 * standard - num + plus;
}

void print_halfhalf(str patternA, str patternB, int numA, int numB) {
  for (int i = 0; i < numA; i++)
    printf("%s", patternA);
  for (int i = 0; i < numB; i++)
    printf("%s", patternB);
}

void print_oddline(int n, int linenumber)
{
  int leftnum = make_lower_then(linenumber / 2, n - 1, 0);
  print_halfhalf("* ", "**", leftnum, n - 1 - leftnum);
  printf("*");
  print_halfhalf("**", " *", n - 1 - leftnum, leftnum);
}

void print_evenline(int n, int linenumber)
{
  int leftnum = make_lower_then(linenumber / 2, n - 1, 1);
  print_halfhalf("* ", "  ", leftnum, n - 1 - leftnum);
  printf(" ");
  print_halfhalf("  ", " *", n - 1 - leftnum, leftnum);
}

int main() {
  int n;
  scanf("%d", &n);

  int height = 4 * n - 3;

  for (int i = 1; i <= height; i++)
  {
    if (i % 2 == 0)
      print_evenline(n, i);
    else
      print_oddline(n, i);

    printf("\n");
  }
}

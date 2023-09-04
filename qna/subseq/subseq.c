#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

void print_array(int * arr, size_t n) {
  printf("[");
  if (n == 0) {
    printf("]\n");
  } else {
    for (int i = 0; i < n - 1; i++) {
      printf("%d, ", arr[i]);
    }
    printf("%d]\n", arr[n - 1]);
  }
}

/* a[]에서 b[]에서 나온 숫자만 취한 배열을 다시 만들어 반환한다.
 */
int * shrink_array(int a[], size_t * an, int b[], size_t bn) {
  int flag[101] = {0};

  for (size_t i = 0; i < bn; i++) {
    flag[b[i]] = 1;
  }

  int * n = (int*)malloc(*an * sizeof(int));
  size_t ni = 0;
  for (size_t i = 0; i < *an; i++) {
    if (flag[a[i]]) {
      n[ni] = a[i];
      ni += 1;
    }
  }
  free(a);
  n = (int *)realloc(n, ni * sizeof(int));
  *an = ni;
  
  return n;
}

uint64_t subseq(int a[], size_t an, int b[], size_t bn, uint64_t * buf) {
  if (*(buf + an + bn * 200000) != -1) {
    return *(buf + an + bn * 200000);
  }
  if (bn == 1) {
    uint64_t count = 0;
    for (int ai = 0; ai < an; ai++) {
      if (b[0] == a[ai]) {
        count += 1;
      }
    }
    *(buf + an + bn * 200000) = count;
    return count;
  } else {
    uint64_t count = 0;
    for (int ai = 0; ai < an - bn + 1; ai++) {
      if (b[0] == a[ai]) {
        count += subseq(&a[ai + 1], an - ai - 1, &b[1], bn - 1, buf);
      }
    }
    *(buf + an + bn * 200000) = count;
    return count;
  }
}

int main() {
  int *a, *b;
  size_t n, m;
  scanf("%zu %zu", &n, &m);
  a = (int *)malloc(n * sizeof(int));
  b = (int *)malloc(m * sizeof(int));
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  for (int i = 0; i < m; i++) {
    scanf("%d", &b[i]);
  }

  a = shrink_array(a, &n, b, m);

  if (n < m) {
    printf("0\n");
  } else {
    uint64_t * buf = (uint64_t *)calloc(200000 * 100, sizeof(uint64_t));
    memset(buf, -1, 200000 * 100 * sizeof(uint64_t));
    uint64_t result = subseq(a, n, b, m, buf);
    printf("%d\n", (int)(result % 20221022));
    free(buf);
  }


  free(a);
  free(b);
    
  return 0;
}

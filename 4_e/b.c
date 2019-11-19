// エルガマル暗号のやつ
#include<stdio.h>

int main(){
  const int p = 103;
  int a, c;

  scanf("%d",&a);
  scanf("%d",&c);

  for(int i = 0; i < p; i++){
    int base = a;
    int exp, j = i;
    int ans = 1;

    while(j != 0){
      ans = ans * base;
      --j;
    }

    if((ans % p) == c){
      printf("%d, ",i);
    }
  }

  printf("\n");
  return 0;
}

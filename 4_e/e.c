// エルガマル暗号のやつ
#include<stdio.h>
int main(){
  const int p = 103;
  int a,b;
  int c = 1;

  scanf("%d",&a);
  scanf("%d",&b);

  int i = b;
  while(i!=0){
    c = c * a;
    --i;
  }

  c = c%p;

  printf("%d\n",c);
  return 0;
}

const lmax == 20;
typedef int mass[1..lmax];
void q(mass a,int n)
{
int i,j,k;
mass    c;
mass    b;
bool    flag;
{
  k=0;
  for (i=1;i<n;i++)
    {
      j=1;
        while( (a[i]!=b[j]) && (j<=k) )
          j=j+1;
        if ( j>k )
          {
            k=k+1;
            b[k]=a[i];
            c[k]=1;
          }
       else
        c[j]=c[j]+1;
     }
  for (i=1;i<k;i++)
  {
  printfc[i]:5);
  }
}
void g(mass a,int n)
{
int l,i,j,m;
mass    b;
bool    flag;
{
  l=1;
  b[l]=a[1];
  for (i=2;i<n;i++)
    {
    flag=false;
    m=l;
    while(  (l == m) && (flag == false) )
      {
        for (j=1;j<l;j++)
        if ( a[i] == b[j] )
        if ( flag == false )
        {
          l=l+1;
          b[l]=a[i];
        }
      }
    }
   for (i=1;i<l;i++)
   {
   printfb[i]:5);

   }
}
int main()
{
float a1[1..lmax];
mass    a;
float    n1;
int    n,i;
{
  printf("введите количество элементов массива");
    repeat
      scanf(n1);
      if ( n1<0 )
      if ( n1>lmax )
      if ( n1!=round(n1) )
    until (n1>0) && (n1<lmax) && (n1 == round(n1));
    n=round(n1);
    printf("введите массив размера ",n);
  for (i=1;i<n;i++)
    {
         repeat
            scanfa1[i]);
            if ( a1[i]!=round(a1[i]) )
         until (a1[i] == round(a1[i]));
    }
  for (i=1;i<n;i++)
    a[i]=round(a1[i]);
  g(a,n);
  scanf;
  q(a,n);
}
return 0
}

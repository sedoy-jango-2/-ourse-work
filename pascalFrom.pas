const lmax=20;
type mass=array[1..lmax]of integer;
procedure q(a:mass; n:integer);
var i,j,k:integer;
    c:mass;
    b:mass;
    flag:boolean;
begin
  k:=0;
  for i:=1 to n do
    begin
      j:=1;
        while (a[i]<>b[j]) and (j<=k) do
          j:=j+1;
        if j>k then
          begin
            k:=k+1;
            b[k]:=a[i];
            c[k]:=1;
          end
       else
        c[j]:=c[j]+1;
     end;
  for i:=1 to k do
  begin
  write(c[i]:5);
  end;writeln;
end;
procedure g(a:mass; n:integer);
var l,i,j,m:integer;
    b:mass;
    flag:boolean;
begin
  l:=1;
  b[l]:=a[1];
  for i:=2 to n do
    begin
    flag:=false;
    m:=l;
    while  (l=m) and (flag=false) do
      begin
        for j:=1 to l do
        if a[i]=b[j] then flag:=true;
        if flag=false then
        begin
          l:=l+1;
          b[l]:=a[i];
        end;
      end;
    end;
   for i:=1 to l do
   begin
   write(b[i]:5);

   end;writeln;
end;
int main()
{
var a1:array[1..lmax]of real;
    a:mass;
    n1:real;
    n,i:integer;
begin
  writeln('введите количество элементов массива');
    repeat
      readln(n1);
      if n1<0 then writeln('число n меньше нуля введите другое');
      if n1>lmax then writeln('число n больше ',lmax,', введите другое');
      if n1<>round(n1) then writeln('число n нечётное, введите другое');
    until (n1>0) and (n1<lmax) and (n1=round(n1));
    n:=round(n1);
    writeln('введите массив размера ',n);
  for i:=1 to n do
    begin
         repeat
            read(a1[i]);
            if a1[i]<>round(a1[i]) then writeln('число ',a1[i],' не целое, введите другое');
         until (a1[i]=round(a1[i]));
    end;
  for i:=1 to n do
    a[i]:=round(a1[i]);
  g(a,n);
  readln;
  q(a,n);
end.
return 0
}

f=file("credit.txt","w");
def vaildc(cardno):
	fvnums='';
	fvnum=[];
	fvsum=0;
	fsum='';
	vsum=0;
	cardnos=str(cardno);
	for num in cardnos[::-2]:
		vsum=vsum+int(num);
	for num in cardnos[::2]:
		fvnum.append(str(int(num)*2));
	for num in fvnum:
		fvnums=fvnums+num;
	for num in fvnums:
		fvsum=fvsum+int(num);
	fsum=str(vsum+fvsum);
	if fsum[-1]=='0':
		f.write(str(cardno)),
		f.write(' is a VALID credit card number. \n');
	else:
		f.write(str(cardno)),
		f.write(' is not a VALID credit card number. \n');

finish=0;
while finish==0:
	cardno=input();
	vaildc(cardno);
	finish=input("continue?");
f.close();

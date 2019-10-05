

mode=int(input('1.암호화 2. 암호해석 중 선택 :'))
file_in=input('입력 파일명을 입력하세요 :')
file_out=input('출력 파일명을 입력하세요 :')

f=open(file_in,'r')
data_in=f.read()

if mode == 1:
    data_code=[ord(i)+100 for i in data_in]
elif mode == 2:
    data_code=[ord(i)-100 for i in data_in]
f.close()

data_output=''.join([chr(i) for i in data_code])

f=open(file_out,'w')
f.write(data_output)
f.close()

list(zip([1,2],[3,4]))
dict(zip([1,2],[3,4]))

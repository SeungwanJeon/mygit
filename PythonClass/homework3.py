"""
1. 딕셔너리(dict)
중괄호{ }로 묶여 있으며, key와 value의 쌍으로 이루어짐.
d={key1:value1,key2:value2}
실습1-1) for 문을 사용하여 딕셔너리 타입의 d의 모든 value를 출력해 보시오.
"""
d ={'youn':1,'park':2,'kim':10}
for values in d.values():
    print(values, end=' ')

for key in d:
    print(d[key], end=' ')

for key in d.keys():
    print(d[key], end=' ')

for key, value in d.items():
    print(value, end=' ')


"""
실습1-3)­ PPT 문제
어떤 문장을 입력 받으면 해당 문장에서 각 알파벳이 몇 개씩 나오는지 저장하는 딕셔너리를 만든 후,
아래와 같이 출력하시오.
Enter a sentence : Python is fun!
{'!':1,'':2,'f':1,'i':1,'h':1,'o': 1,'n':2,
'P':1,'s':1,'u':1,'t':1,'y':1}
"""
d={}
sentence='Python is fun!'
for key in set(sentence):
    d[key]=sentence.count(key)
print(d)

d.clear()
sorted(list(sentence))
for key in sentence:
    if key not in d.keys():
        d[key]=sentence.count(key)
print(d)

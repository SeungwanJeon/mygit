import numpy as np

# enumerate()
#- 리스트의 모든 요소를 인덱스와 쌍으로 추출
colors = ['red', 'green', 'blue']
result = list(enumerate(colors))
print(result)

for idx, color in enumerate(colors):
    print(idx, color)

# zip ()
#2개 이상의 리스트를, 각 리스트의 같은 인덱스 원소끼리 묶은 튜플을 요소로 하는 리스트를 만들어 줌
z=zip([1,2,3], [4,5,6]) # 리스트
print(list(z))

z=zip([1,2,3], [4,5,6], ['a','b','c'])
print(list(z))
print(tuple(z))


z=zip((1,2,3), (4,5,6)) # 튜플
print(tuple(z))

[sum(x) for x in zip((1,2,3), (4,5,6))]
(1,2,3)+(4,5,6)
np.array([1,2,3])+np.array([1,2,3])

"""
실습1)
아래와 같이 주어진 2개의 리스트로 딕셔너리를 만들어 출
력하시오. 단, 순서는 다를 수 있음
L1 = ['one', 'two', 'three', 'four']
L2 = [1, 2, 3, 4]
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
"""
L1 = ['one', 'two', 'three', 'four']
L2 = [1, 2, 3, 4]
dict(zip(L1,L2))

{k:v for k,v, in zip(L1,L2)}

"""
3. 과제(종합 문제)
문제1)아래와 같은 문자열을 만들어 보시오.
'0 1 2 3 4 … 997 998 999'
"""
' '.join([str(x) for x in range(5)])

"""
문제2) 최장 단어 검색
다음 조건을 만족하는 computeMaxWordLength(text)
함수를 구현하시오.
- 입력으로 문자열 text가 주어짐 (단, 단어는 공백으로 구분)
- 가장 긴 단어를 찾아서 반환
- 최대 길이의 단어가 여러 개 있는 경우, 알파벳 기준으로 가장 뒤에 나오는 단어를 반환
def computeMaxWordLength(text):
    채우기
text1 = 'which is the longest word'
text2 = 'cat sun dog'
print(computeMaxWordLength(text1))
print(computeMaxWordLength(text2))
>>>
longest
sun
"""
def computeMaxWordLength(text):
    maxlen=0
    for s in text.split():
        if len(s)>=maxlen:
            maxlen=len(s)
            maxs=s
    return maxs

# def computeMaxWordLength_alter(text):
#     d={word:len(word) for word in set(text1.split())}
#     return d
text1 = 'which is the longest word'
text2 = 'cat sun dog'
print(computeMaxWordLength(text1))
print(computeMaxWordLength(text2))


"""
문제3) 최빈도 단어 검색
최빈도 단어의 set 및 해당 빈도수를 반환하는 computeMostFrequentWord(text) 함수를 구현하시오.
(반환값은 tuple 형태로 실행 예시를 참고할 것)
def computeMostFrequentWord(text):
    채우기

text1 = 'the quick brown fox jumps over the lazy fox'
text2 = 'the quick brown fox jumps over the lazy dog'
print(computeMostFrequentWord (text1))
print(computeMostFrequentWord (text2))
({'fox', 'the'}, 2)
({'the'}, 2)
"""
def computeMostFrequentWord(text):
    d=dict()
    text_split=text.split()
    for el in set(text_split):
        d[el]=text_split.count(el)
    maxval=max(d.values())
    return {key for key in d if d[key]==maxval},maxval

def computeMostFrequentWord_alter(text):
    d={key:text.count(key) for key in set(text.split())}
    return {key for key in d if d[key]==max(d.values())},max(d.values())

text1 = 'the quick brown fox jumps over the lazy fox'
text2 = 'the quick brown fox jumps over the lazy dog'
print(computeMostFrequentWord (text1))
print(computeMostFrequentWord (text2))
print(computeMostFrequentWord_alter (text1))
print(computeMostFrequentWord_alter (text2))

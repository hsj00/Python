# Regular expressions
- 복잡한 문자열을 처리할 때 사용하는 기법
- 입력 양식이 올바른지 검사한다거나, 특정 양식의 데이터만 취합한다거나

## Meta characters
- 특별한 목적을 가지고 사용하는 문자
- `.` `^` `$` `*` `+` `?` `{` `}` `[` `]` `\` `|` `(` `)`
  - `-`: 두 문자 사이의 범위 (from/to)
  - `^`: 반대, 여집합 (not)

### 문자 클래스(character class), []
- []: [ ] 사이의 문자들과 매치
- `\d`: 숫자와 매치, `[0-9]`
- `\D`: 숫자가 아닌 것과 매치, `[^0-9]`
- `\s`: whitespace 문자와 매치, `[ \t\n\r\f\v]` 맨 앞 빈칸은 공백문자(space) 의미
- `\S`: whitespace 문자가 아닌 것과 매치, `[^ \T\N\R\F\V]`
- `\w`: 문자+숫자(alphanumeric)과 매치, `[a-zA-Z0-9_]`
- `\W`: 문자+숫자(alphanumeric)가 아닌 문자와 매치, `[^a-zA-Z0-9_]`

### Dot(.)
- Dot(.): 줄바꿈 문자 `\n`을 제외한 모든 문자와 매치
- `a.b`: "a + 모든 문자 + b", a와 b 사이에 어떤 문자가 들어와도 모두 매치된다는 뜻
- `a[.]b`: "a + Dot(.) 문자 + b", 문자로서의 `.`, "a.b"와 매치되고 "a0b"와는 매치되지 않는다

### Iteration
- `*`: `*` 바로 앞에 있는 문자가 0부터 무한대로 반복될 때 사용
  - 메모리 제한으로 2억개 정도까지만 가능
- `+`: `+` 바로 앞에 있는 문자가 최소 1번 이상 반복될 때 사용
- `{m, n}`: m 이상, n 이하 (ex, {3,}, {,3}, {3})
- `?`: `{0, 1}`

## `re` module
- 컴파일할 때 특정 옵션을 주는 것도 가능
- 패턴: 정규식을 컴파일한 결과
- 한 번 만든 패턴 객체를 여러번 사용해야할 때는 `re.compile`을 사용하는 것이 편리함
```py
# re.compile의 결과로 돌려주는 컴파일된 패턴 객체 p에 정규표현식 'ab*'를 컴파일
>>> import re
>>> p = re.compile('ab*')

## re 모듈의 축약형
### 축약 전
>>> p = re.compile('[a-z]+')
>>> m = p.match("python")

### 축약 후
>>> m = re.match('[a-z]+', "python")
```

## 정규식을 이용한 문자열 검색
- `match`, `search`는 정규식과 매치될 때 `match 객체`를 돌려주고, 매치되지 않을 때는 `None`을 돌려준다
- `match 객체`: 정규식의 검색 결과로 돌려주는 객체
Method      |   purpose     |       |
---         |   ---         |   --- |
match()     |   문자열의 처음부터 정규식과 매치되는지 조사  |   |
search()    |   문자열 전체를 검색하여 정규식과 매치되는지 조사 |   |
findall()   |   정규식과 매치되는 모든 문자열(substring)을 리스트로 반환    |   |
finditer()  |   정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 반환  |   |

```py
>>> import re
>>> p = re.compile('[a-z]+')
```

### `match()`
- 문자열 처음부터 검색
```py
>>> m = p.match("python")  # "python" 문자열은 [a-z]+ 정규식에 부합
>>> print(m)
<re.Match object; span=(0, 6), match='python'>  # match 객체 반환

>>> m = p.match("3 python")  # 첫 문자 '3'이 정규식에 부합하지 않음
>>> print(m)
None  # None 반환
```
```py
p = re.compile('regular expressions')
m = p.match('string form')
if m:  # match된 결과값이 있을 때 반환
    print('Match found: ', m.group())
else:  # match된 결과값이 없을 때, None일 때 반환
    print('No match')
```

### `search()`
- 문자열 전체 검색
```py
>>> m = p.search("python")  # "python" 문자열은 [a-z]+ 정규식에 부합
>>> print(m)
<re.Match object; span=(0, 6), match='python'>  # match()와 동일한 결과

>>> m = p.search("3 python")
>>> print(m)
<re.Match object; span=(2, 8), match='python'>
# 문자열 전체를 검색하기 때문에 "3 "이후 문자열과 매치
```

### `findall()`
```py
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']
# 문자열의 단어를 각각 정규식과 매치하여 리스트로 반환
```

### `finditer()'
- `findall`과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 반환
- 반복 가능한 객체가 포함하는 각가그이 요소는 `match` 객체
```py
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x10f7db190>
>>> for r in result: print(r)
... 
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
```

## `match` 객체의 메서드
- `match`, `search` 메서드를 수행한 결과로 match 객체 반환
- 어떤 문자열이 매치 되었는지, 문자열의 위치 정보는 무엇인지 확인할 수 있다

Method      |   Purpose     |       |
---         |---            |---    |
`group()`   |매치된 문자열을 반환   |       |
`start()`   |매치된 문자열의 시작 위치 반환 ||
`end()`     |매치된 문자열의 끝 위치 반환   ||
`span()`    |매치된 문자열의 시작과 끝을 튜플로 반환 `(시작, 끝)`   ||

```py
## match
>>> m = p.match("python")
>>> m.group()  # group()
'python'
>>> m.start()  # start()
0
>>> m.end()    # end()
6
>>> m.span()   # span()
(0, 6)
>>> print(m)   # includes all information
<re.Match object; span=(0, 6), match='python'>
```
```py
## search
>>> m = p.search("3 python")
>>> m.group()  # group()
'python'
>>> m.start()  # start()
2              # p.match와 다른 결과
>>> m.end()    # end()
8
>>> m.span()   # span()
(2, 8)         # match: (0, 6)
>>> print(m)   # includes all information
<re.Match object; span=(2, 8), match='python'>
```

## Compile option

### DOTALL, S
- `re.DOTALL`또는 `re.S` 형태로 사용
- `.`이 줄바꿈 문자(`\n`)를 포함하여 모든 문자와 매치
- 여러 줄로 이루어진 문자 열에서 `\n`에 상관없이 검색할 때 많이 사용
```py
## DOTALL 사용 전
>>> import re
>>> p = re.compile('a.b')
>>> m = p.match('a\nb')
>>> print(m)
None

## DOTALL 사용 후
>>> p = re.compile('a.b', re.DOTALL)
>>> m = p.match('a\nb')
>>> print(m)
<re.Match object; span=(0, 3), match='a\nb'>
```

### IGNORECASE, I
- `re.IGNORECASE`또는 `re.I` 형태로 사용
- 대소문자 관계없이 매치
```py
## '[a-z]+' 정규식은 반복되는 소문자들을 의미하지만 대소문자 구분없이 매치됨을 확인
>>> p = re.compile('[a-z]+', re.I)

### match
>>> p.match('python')
<re.Match object; span=(0, 6), match='python'>
>>> p.match('PYTHON')
<re.Match object; span=(0, 6), match='PYTHON'>
>>> p.match('Python')
<re.Match object; span=(0, 6), match='Python'>

### search
>>> p.search('python')
<re.Match object; span=(0, 6), match='python'>
>>> p.search('PyThOn')
<re.Match object; span=(0, 6), match='PyThOn'>
```

### MULTILINE, M
- `re.MULTILINE`또는 `re.M` 형태로 사용
- `^`, `$` 메타문자를 각 줄마다 적용해주는 옵션
- `^`: 문자열의 처음
  - `^python`: 문자열의 처음은 항상 `python`으로 시작해야 매치
- `$`: 문자열의 마지막
  - `python$`: 문자열의 마지막은 항상 `python`으로 끝나야 매치

```py
>>> import re
## ^python: 문자열 python으로 시작
## \s: 그 다음에 whitespace
## \w+: 그 뒤에 단어가 와야 한다는 의미
>>> p = re.compile("^python\s\w+")
>>> data = """python one
... life is too short
... python two
... you need python
... python three"""
>>> print(p.findall(data))
['python one']  # 첫번째 줄에만 매치
```
```py
## MULTILINE 옵션 적용
>>> p = re.compile("^python\s\w+", re.M)
>>> data = """python one
... life is too short
... python two
... you need python
... python three"""
>>> print(p.findall(data))
['python one', 'python two', 'python three']  # 각 줄의 처음에 매치
```

### VERBOSE, X
- `re.VERBOSE`또는 `re.X` 형태로 사용
- verbose 모드를 사용할 수 있도록 한다 (정규식을 보기 편하게 만들 수 있고, 주석등을 사용할 수 있게 된다)
- `re.VERBOSE` 옵션을 사용할 경우, 문자열에 사용된 whitespace는 컴파일할 때 제거됨
  - 단, `[]` 안에 사용한 whitespace는 제외
- 줄 단위로 # 기호를 사용해 주석문 작성 가능
```py
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
```
```py
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

## Back slash, \
- `"\section"` 문자열을 찾기 위한 정규식을 만든다고 가정
- `\s`문자가 whitespace로 해석되어 의도한대로 매치되지 않음
- 백슬래시 2개를 사용하여 이스케이프 처리 (`\` 문자가 문자열 자체임을 선언)
  - 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 `\\`이 `\`로 변경되어 `\section`이 전달됨
  - `\\`문자를 전달하기 위해서 파이썬에서는 `\\\\`처럼 백슬래시 4개를 사용해야함
- 정규식 표현에서 `\`를 반복 사용되는 문제를 방지하기 위해 `Raw String` 규칙 생겨남
  - 정규식 문자열 앞에 `r` 문자 삽입
  - 백슬래시 2개 대신 1개만 써도 2개를 쓴것과 동일한 의미를 갖는다
```
\section
[ \t\n\r\f\v]ection
```
```
\\section
```
```py
>>> p = re.compile('\\section')  # \section 전달
```
```py
>>> p = re.compile(r'\\section')  # r 문자 삽입
```
1. `int`: 정수형

- `0b`: bit, 2진수
- `0o`: octo, 8진수
- `0x`: hexadecimal, 16진수

```python
>>> int("1000", 3)  # 3진수 to 10진수
27
>>> int("3000", 4)  # 4진수 to 10진수
192
```

2. `float`: 실수형

- 지수표기법 적용 가능
  - ex) 3e+8, 3e8, 1.672+2, 1.616e-10
- `int`에 없는 `nan`(Not a Number), `inf`(+무한), `-inf`(-무한) 변환

3. `None`: 값이 없음을 의미

4. `bool`: `True`/`False`

- `0`, `0.0`을 제외한 모든 `int`, `float` 은 `True`
- `str`, `list`, `set`, `dict`의 `empty value`만 `False`

```python
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
>>> bool([])
False
>>> bool({})
False
>>> bool([0])
True
>>> bool({"a":0})
True

```


# for statement

for statement에 대한 것이 궁금해져서 해보았다.
우선 간단한 for statement를 준비한다.
``` python3
def name():
	for x in range(10):
		print(x)
```

그리고 dis 모듈을 이용하여 bytecode가 어떻게 되어있는지 확인한다.

```python3
import dis
	dis.dis(name)
```

결과물은 다음과 같다.
  2           0 SETUP_LOOP              24 (to 26)
              2 LOAD_GLOBAL              0 (range)
              4 LOAD_CONST               1 (10)
              6 CALL_FUNCTION            1
              8 GET_ITER
        >>   10 FOR_ITER                12 (to 24)
             12 STORE_FAST               0 (x)

  3          14 LOAD_GLOBAL              1 (print)
             16 LOAD_FAST                0 (x)
             18 CALL_FUNCTION            1
             20 POP_TOP
             22 JUMP_ABSOLUTE           10
        >>   24 POP_BLOCK
        >>   26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

여기서 2랑 3은 line number다.
3번째 줄은 print(x)이므로 굳이 상관하지 않고, 2번만 보면,
GET_ITER와 FOR_ITER로 작동하고 있는 것을 알 수 있다.
GET_ITER는 Implements TOS = iter(TOS)이고, (TOS는 Top Of Stack을 의미한다.)

* iter(object[,sentinel]):
	1. iterator 객체를 돌려준다.
	2. sentinel이 없으면, object는 이터레이션 프로토콜 (\_\_iter\_\_() method)를 지원하는 collection 객체거나 시퀀스 프로토콜 (0에서 시작되는 정수 인자를 받는 \_\_getitem\_\_() method)를 지원해야 한다.
		만약 둘 다 없을 경우, TypeError가 일어난다.
	3. sentinel이 있을 경우, object는 callable이어야 한다.
		\_\_next\_\_() 메서드가 호출될 때마다 인자 없이 object를 호출한다.
		반환값이 sentinel과 같으면 StopIteration을 일으키고, 그렇지 않으면 값을 돌려준다.
즉 GET_ITER에서 TOS가 iter의 2번째 조건을 만족하면 그 프로토콜을 반환한다는 뜻이다. 
다시 말하자면, for X in Y에서 Y가 iterable이기만 하면, 문제 없이 잘 돌아간다는 뜻이기도 하다.

FOR_ITER(delta)는 TOS는 iterator고, \_\_next\_\_() method를 부른다.
만약 새로운 Value를 산출한다면, stack에 쌓고, iterator는 그것의 밑에 둔 상태로 남겨둔다.
만약 iterator가 고갈되었다고 한다면, TOS는 pop되고, bytecode counter는 delta에 의해 증가된다.


알고 싶은 것은, enumerate같이, iterator인 객체를 반환하는 (그러나 print로는 enumerate 객체의 위치만 알 수 있는) 함수들은 과연 어떻게 반응하는 지 보는 것이었다.
iterator한 객체를 만들기 귀찮아서, 파일을 open했다.

```python3
def name():
...     with open('ex_dict_get.py',encoding = 'utf-8') as fp:
...             for line_no, line in enumerate(fp,1): 
...                     print(line_no,line)
```

결과는 다음과 같았다.
```
 2           0 LOAD_GLOBAL              0 (open)
              2 LOAD_CONST               1 ('ex_dict_get.py')
              4 LOAD_CONST               2 ('utf-8')
              6 LOAD_CONST               3 (('encoding',))
              8 CALL_FUNCTION_KW         2
             10 SETUP_WITH              40 (to 52)
             12 STORE_FAST               0 (fp)

  3          14 SETUP_LOOP              32 (to 48)
             16 LOAD_GLOBAL              1 (enumerate)
             18 LOAD_FAST                0 (fp)
             20 LOAD_CONST               4 (1)
             22 CALL_FUNCTION            2
             24 GET_ITER
        >>   26 FOR_ITER                18 (to 46)
             28 UNPACK_SEQUENCE          2
             30 STORE_FAST               1 (line_no)
             32 STORE_FAST               2 (line)

  4          34 LOAD_GLOBAL              2 (print)
             36 LOAD_FAST                1 (line_no)
             38 LOAD_FAST                2 (line)
             40 CALL_FUNCTION            2
             42 POP_TOP
             44 JUMP_ABSOLUTE           26
        >>   46 POP_BLOCK
        >>   48 POP_BLOCK
             50 LOAD_CONST               0 (None)
        >>   52 WITH_CLEANUP_START
             54 WITH_CLEANUP_FINISH
             56 END_FINALLY
             58 LOAD_CONST               0 (None)
             60 RETURN_VALUE

```
결론적으로 말하자면, iter()가 정상적으로 작동하기 때문에, 별반 문제가 없었다.
즉, iter()만 작동하는 모든 object라면, for x in Y에서 Y부분에 어떤 object를 넣어도 상관없다는 것이다.

출처 : <https://docs.python.org/ko/3/library/functions.html#iter>

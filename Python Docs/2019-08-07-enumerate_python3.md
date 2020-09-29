# enumberate(iterable, start = 0)

1. return : enumerate object
2. iterable : 
	sequence, iterator, some other object which supports iteration.
3. \_\_next\_\_() method :
	1. returns a tuple containg a count (from *start* which defaults to 0)
	2. the values obtained from iterating over *iterable*

```python
def enumerate(seq,start = 0):
	n = start
	for elem in sequence:
		yield n,elem
		n += 1
```

**warning** : returns **iterable**

* 출처 : <https://docs.python.org/3/library/functions.html#enumerate>


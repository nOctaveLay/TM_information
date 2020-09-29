# 융통성있게 키를 조회하는 방식
1. 평범한 dict 대신 defaultdict를 사용하는 방법
2. 다른 하나는 dict 등의 매핑형을 상속해서 \_\_missing\_\_() method를 추가하는 방법

### defaultdict : 존재하지 않는 키에 대한 또 다른 처리
1. defaultdict -> 존재하지 않는 키로 검색할 때 요청에 따라 항목을 생성하도록 설정되어 있다.

2. 작동하는 방식 :
	* defaultdict 객체를 생성할 때 존재하지 않는 키 인수로 \_\_getitem\_\_() method를 호출할 때마다 기본값을 생성하기 위해 사용되는 콜러블을 제공하는 것이다.

	* dd = defaultdict(list)코드로 기본 defaultdict 객체를 생성
	* dd에 존재하지 않는 키인 'new-key'로 dd['new-key'] 표현식을 실행하면 다음과 같이 처리
		1. 리스트를 새로 생성하기 위해 list()를 호출한다.
		2. 'new-key'를 키로 사용해서 새로운 리스트를 dd에 삽입한다.
		3. 리스트에 대한 참조를 반환한다.

	* 기본값을 생성하는 콜러블은 default_factory라는 객체 속성에 저장된다.

### \_\_missing\_\_() 메서드

1. 매핑형은 \_\_missing\_\_() 메서드를 이용해서 존재하지 않는 키를 처리한다.
2. dict에는 정의되어 있지 않지만, dict는 이 메서드를 알고 있다.
3. dict 클래스를 상속하고, \_\_missing\_\_() 메서드를 정의하면,
4. dict.\_\_getitem\_\_() 표준 메서드가 키를 발견할 수 없을 때,
5. KeyError를 발생시키지 않고 \_\_missing\_\_() 메서드를 호출한다.

* \_\_missing\_\_() 메서드는 
	* d[k] 연산자를 사용하는 경우 등 \_\_getitem\_\_() 메서드를 사용할 때만 호출된다.
	* in 연산자를 구현하는 get()이나 \_\_contains\_\_() 메서드 등 
	  키를 검색하는 다른 메서드에는 \_\_missing\_\_() 메서드가 영향을 미치지 않는다.
	* 따라서 \_\_getitem\_\_() 메서드를 사용할 때만 defaultdict의 default_factory가 작동한다.
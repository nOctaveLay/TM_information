# 시간을 다루는 모듈
1. [calendar](https://docs.python.org/3/library/calendar.html#module-calendar)
2. [time](https://docs.python.org/3/library/time.html#module-time)
3. [dateutil](https://dateutil.readthedocs.io/en/stable/)

# 어웨어(aware)와 나이브(naive) 객체

Aware

- 다른 어웨어 객체와 상대적인 위치 파악 가능
- 자의적으로 해석할 여지 없는 특정 시간. (상대성 이론 고려 x)
- 어웨어 객체가 필요한 응용 프로그램을 위해, tzinfo 추상클래스 안에 시간대 정보 attribute인 tzinfo가 있음

  tzinfo
    - UTC 시간으로부터의 오프셋
    - 시간대 이름
    - 일관 절약 시간 적용
    - datetime 모듈에서는 timezone만 제공.

Naive

- 다른 시간 객체 상대적인 위치 모름
- 자의적 해석 여지 있음. (프로그램에 달려있음)


공통 속성

date, datetime, time 및 timezone 형은 다음과 같은 공통 기능을 공유합니다:
- 이러한 형의 객체는 불변입니다.
- 이러한 형의 객체는 해시 가능합니다. 딕셔너리 키로 사용할 수 있다는 뜻입니다.
- 이러한 형의 객체는 pickle 모듈을 통한 효율적인 피클링을 지원합니다.

# 객체가 어웨어한지 나이브한지 판단하기
- date 형의 객체는 항상 나이브합니다.
- time이나 datetime 형의 객체는 어웨어할 수도 나이브할 수도 있습니다.
- datetime 객체 d는 다음 조건을 모두 만족하면 어웨어합니다:
  - d.tzinfo가 None이 아닙니다
  - d.tzinfo.utcoffset(d)가 None을 반환하지 않습니다
- 그렇지 않으면, d는 나이브합니다.
- time 객체 t는 다음 조건을 모두 만족하면 어웨어합니다.
  - t.tzinfo가 None이 아닙니다
  - t.tzinfo.utcoffset(None)이 None을 반환하지 않습니다
- 그렇지 않으면, t는 나이브합니다.
- 어웨어와 나이브 간의 차이점은 timedelta 객체에는 적용되지 않습니다.

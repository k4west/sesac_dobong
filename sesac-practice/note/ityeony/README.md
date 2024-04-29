DAY7 학습내용
# DAY6 복습

## elif와 if문 사용 시 주의사항

1. **조건의 순서와 범위:**
    - 조건은 상호 배타적이어야 한다.
    - 순서에 주의해야 한다. (잘못된 순서 또는 범위의 조건은 예상치 못한 결과를 초래)

- 잘못된 예제:

```python
age = 15
if age > 10:
	category = "청소년"
if age > 20:
	category = "성인"
# 15세는 청소년으로 분류되지만, 성인 조건도 검사되어 결과가 혼란스러움
```

- 올바른 예제:

```python
age = 15
if age > 20:
	category = "성인"
elif age > 10:
	category = "청소년"
# 15세는 청소년으로만 분류되어 명확한 결과를 얻음
```

1. **변수 값의 덮어쓰기가 되지 않도록 한다.** 
    - 독립적인 if 문을 사용할 때, 같은 변수에 대해 다중 할당이 일어날 수도 있음을 알고 있자.
    - 이는 나중에 나오는 if 조건이 참일 때 이전에 할당된 값이 덮어쓰여질 수 있다는 것을 의미
    한다.

- 잘못된 예제
    
    ```python
    score = 85
    grade = ""
    if score >= 80:
    grade = "B"
    if score >= 70:
    grade = "C"
    ```
    

- 올바른 예제:
    
    ```python
    score = 85
    grade = ""
    if score >= 80:
    grade = "B"
    elif score >= 70 and score < 80:
    grade = "C"
    # 점수가 85점일 때, 'C' 학점으로 올바르게 부여됨
    ```
    
1. **조건의 중첩:**
    1. elif 는 이전 if 또는 elif 조건이 거짓일 때만 평가해야 함.
    2. 반면, 별도의 if 문은 서로 독립적으로 평가되어, 조건이 겹칠 경우 여러 조건이 모두 참이
    될 수 있도록 설계
- 잘못된 열
    
    ```python
    age = 18
    member_grade = "Gold"
    if member_grade=="Gold" :
    	print("골드 회원님, 환영합니다!")
    if age < 19:
    	print("청소년 이용자입니다.")
    if age < 19 and member_grade=="Gold":
    	print("청소년 골드 회원님, 환영합니다!")
    # 18세 골드 회원에게 "청소년 이용자입니다." 와 "청소년 골드 회원님, 환영합니다!" 두 메시지가 출력됨
    
    ```
    
- 올바른 예제
    
    ```python
    age = 22
    member_grade = "Gold"
    if age >= 19 and member_grade == "Gold":
    	print("골드 회원님, 환영합니다!")
    elif age < 19 and member_grade == "Gold":
    	print("청소년 골드 회원님, 환영합니다!")
    elif age < 19:
    print("청소년 이용자입니다.")
    else:
    pass
    # 22세 골드 회원에게는 "골드 회원님, 환영합니다!" 메시지만 출력된다.
    6
    ```
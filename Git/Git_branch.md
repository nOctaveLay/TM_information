# Git branch 
## What is Branch?
- commit을 할 경우, git은 Staging Area에 있는 커밋 객체(커밋 Object)를 저장한다.
- Git의 브랜치는 커밋 사이를 가볍게 이동할 수 있는 포인터이다.
- 기본적으로 master 브랜치를 만든다.
- master 브랜치는 자동으로 가장 마지막 커밋을 가리킨다.
- 한 커밋을 가리키는 40글자의 SHA-1 체크섬 파일에 불과하기 때문에 만들기도 쉽고 지우기도 쉽다.


## 새 브랜치 생성
**git branch [branch name]**
- branch name을 가진 새로운 브랜치를 만든다.
- HEAD는 지금 작업 중인 로컬 브랜치를 가리킨다. 
- branch가 생성되었다고 해도 HEAD를 옮기지 않는다. (기존 master 브랜치를 가리키고 있음)
- ```-b``` 옵션 : 브랜치를 만들면서 checkout까지 한 번에 한다.
  - 즉, 밑의 코드를 줄여 쓴 것과 같다.
    ```$ git branch [branch name]
       $ git checkout [branch name]
    ```

**git log --oneline --decorate**
- 브랜치가 어떤 커밋을 가리키는 지도 알 수 있다.

## 브랜치 이동
**git checkout [branch name]**
- branch name을 가진 branch로 HEAD를 이동시킨다.
- 브랜치를 이동하면 워킹 디렉토리의 파일이 변경된다.
  - 이는 마지막으로 작업했던 파일로 변경된다.
  - 파일 변경시 문제가 있어 브랜치를 이동시키는 게 불가능할 경우 git은 브랜치 이동 명령을 수행하지 않는다.

**git log --oneline --decorate --graph --all**
- 히스토리를 출력한다.

## Merge의 기초
- Merge는 보통 이런 식으로 진행한다.
  1. 웹사이트가 있고 뭔가 작업을 진행하고 있다.
  2. 새로운 이슈를 처리할 새 branch를 하나 생성한다.
  3. 새로 만든 branch에서 작업을 진행한다.

git branch bugFix : git branch bugFix가 생성되었다.<br>
git checkout master : master쪽을 마음껏 움직일 수 있게 되었다.<br>
git merge bugFix master : bugFix를 master 가지로 merge했다.<br>
<br>
리베이스란? (rebase) 브랜치끼리의 작업을 접목하는 방법 중 하나. 커밋들을 모와서 복사한 뒤, 다른 곳에 떨궈 놓는 것.<br>
장점 : 커밋들의 흐름을 보기 좋게 한 줄로 만들 수 있다.<br>
	즉, 저장소의 커밋 로그와 이력이 한결 깨끗해진다.<br>
따로따로 개발한 bugFix와 masteR이라는 브랜치가 있다고 하자. 이 둘을 머지할 수도 있지만 그렇게 하면 커밋 로그가 이리갔다 저리갔다 하기 때문에 이 둘을 순서대로 개발한 것처럼 보이기로 했다. (누가 먼저고 누가 나중이냐는 bugFix에서 개발한 것을 name이 쓰느냐 마느냐에 따라 달려있다.)<br>
같이 있을 때, bugFix를 선택하고 git rebase master라고 치면 bugFix가 밑으로 내려가고 대신 bugFix가 원래 가리키고 있었던 커밋은 남는다. (bugFix가 밑으로 내려가면서 가르키는 건 bugFix가 가리키고 있던 커밋의 복사본)<br>
이걸 해결하기 위해서 master를 checkout으로 선택한 뒤, git rebase bugFix 를 하면 master가 bugFix의 부모쪽에 있었기 때문에 단순히 그 브랜치를 더 앞으로 가리키게 이동하는 것으로 문제가 해결된다. (bugFix가 있었던 원래 commit을 접속할 브랜치가 없기 때문)<br>
*참고 : 너무 헷갈릴 때에는 checkout만 움직인다고 생각하면 편하다. master는 항상 최신것을 가리켜야 하므로라고 하면 이해가 쉽다.<br>
<br>
git에서 작업 되돌리기.<br>
1. git reset : 예전의 커밋을 가리키도록 이동시키는 방식으로 변경 내용을 되돌리는 것. <br>
* 단점 : 히스토리를 고쳐쓰기 때문에 다른 사람이 작업하는 리모트 브랜치에는 쓸 수 없다.<br>
*실행시 : git reset HEAD~1<br>
<br>
<br>
2. git revert : 변경분을 되돌리고 이 되돌린 내용을 다른 사람과 공유하기 위해서 쓰는 것.<br>
자신이 되돌린 내용을 복사한 새로운 브랜치를 만듬.<br>
*실행시 : git revert HEAD<br>
<br>
<br>
cherry-pick? 특정 commit을 branch로 복사하고 싶을 때! 개별 커밋을 골라서 HEAD 위에 떨어뜨릴 수 있음.<br>
git checkout [branch이름]<br>
git cherry-pick [복사하고 싶은 commit]<br>

로컬에 쌓인 커밋<br>
불필요한 디버그용 코드들이 들어가지 않게 하기 위해서 Git의 마법을 사용합니다!<br>
git rebase -i : 어떤 커밋을 취하거나 버릴지를 선택하는 것, 커밋의 순서를 바꾸는 것.<br>
git rebase -i HEAD~# : HEAD에서 #만큼 수를 바꾸거나 버린다.<br>

git commit --amend : 커밋 내용을 정정함.<br>
<br>
<br>

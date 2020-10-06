# Intro
- 이 post는 예전에 github page를 관리할 때 정리한 내용입니다.
- 추가로 github를 실제로 프로젝트에서 써보면서 익혔던 내용들에 대해서도 정리합니다.
- 실제로 인코딩된 내용을 보니 그렇게 깔끔하지 못해서 정리합니다.

# 이론
- git은 version control을 하기 위해 만들어진 도구이다.
  - Version control이란?
    - File에서 일어난 모든 변화를 기록해서 나중에 특정 version을 불러올 수 있는 것.
    - 특정 파일의 이전 상태를 불러오는 것이 가능
    - 전체적인 프로젝트의 이전 상태를 불러오는 것이 가능
    - 누가 프로젝트에 문제가 있도록 수정했는지, 프로젝트가 어떻게 변화했는지, 언제 변화했는지를 파악할 수 있다. 
- git과 다른 version control 도구와의 차이점
  - Data 기반 저장 : 파일이 변화 x -> 저장을 다시 하지 않음
  - 모든 operation을 local에서 관리
    - 프로젝트의 모든 변화를 local 폴더에 저장한다.
    - 업로드 하기 전에는 인터넷이 끊겨있든 말든에 관계 없이 버전 관리 가능
  - Integrity(통일성) 가짐
    - 저장되기 전에 checksum을 검토 => 이는 SHA-1 hash로 검토(file name이 아님)
    - 즉, Git을 알지 못하고선 파일이나 폴더를 바꿀 수 없다는 것을 의미
    - File correption x, 정보 잃지 x
- Git은 일반적으로 data만 저장한다.
  - 따라서 data를 잃기 매우 어렵다.

# 실전
## GIT을 처음 사용할 시
### git config
- configuration variables을 얻거나 설정할 수 있다.
  - configuration variable : Git이 어떻게 보이고 어떻게 동작하는 지에 대한 모든 방법을 control 가능함

  **1. [path]/etc/gitconfig**
  - 시스템과 repository에 있는 모든 유저들에게 적용되는 value를 포함
  - ```--system``` :  이 파일로부터 읽거나 쓸 수 있다.
  - 파일을 바꾸기 위해서 관리자나 슈퍼유저 권한이 필요

  **2. ```~/.gitconfig``` or ```~/.config/git/config```**
  - user에게만 적용되는 설정
  - ```--global``` : Git을 읽고 쓸 수 있다.
    - repository(이하 레포)의 모든것에 영향을 미침

  **3. 현재 사용하는 레포가 뭐든 Git directory에 있는 ```config```**
  - ```.git/config```와 동일하다.
  - 단일 레포에 설정됨
  - ```--local``` : Git을 강제로 읽고 쓰게 할 수 있다. (실제론 이게 기본값)

- 각각의 레벨은 이전 level에 있는 value를 덮어씌운다.
- 즉, .git/config에 있는 value가 [path]/etc/gitconfig를 덮어씌운다.
- 모든 세팅을 보는 방법 

	```$ git config --list --show-origin```
### Identity
- user name과 email address를 세팅하는 방법
```
$ git config --global user.name "clear"
$ git config --global user.email "test@example.com"
```
- ```--global``` 옵션을 줬으니 이 유저자체에 저장되는 속성, 따라서 한 번만 해주면 됨
- 특정 레포에서만 user를 달리하고 싶다면 ```--global```옵션을 빼면 된다.

### Editor
- 잘 쓸 일 없음 (대부분의 Pycharm이나 VScode에서 다 지원해줌)
- git 자체에서 text editor를 쓰고 싶다면
	```
	$ git config --global core.editor emacs
	```
- notepad++를 쓰고 싶을 때
	```
	$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
	```

### Default Branch Name
```$ git config --global init.defaultBranch main```
- 알겠지만, global이기 때문에 user 수준에서 branch default이다.

## GIT 저장소를 처음 사용할 시
- Git 저장소를 얻는 방법은 두 가지가 있다.
  + local directory를 Git repository로 바꾸는 경우
  + 다른 Git repository를 clone하는 경우

### 이미 존재하는 폴더를 Repository로 초기화하는 경우
**1. 일단 그 폴더로 들어간다.**
- ```cd``` 명령어 사용

**2. git init** 
- git을 처음 사용할 때에는 버전 저장소를 만들어야 한다. (git 저장소)
- 이 경우 ```.git``` 파일이 생성된다. (아직 파일 추적은 안 함)
- 이는 master branch로 적용된다 (**곧 main branch로 바뀐다. 인권문제 이슈**)
- 이는 작업할 때는 안보이지만, git에서 일어난 변경사항을 모두 담고있는 폴더이다. 
- 참고: 이 git폴더를 지울 때에는 **관리자 권한 필요**

**3. git에 파일 추가**
```
$ git add [file]
$ git add LICENSE
$ git commit -m [message]
```
- **commit**은 폴더에서 변경된 내용을 저장하는 단위이다.
- ```git commit```만 쓸 경우, 메세지를 쓸 editor가 열린다.
- ```-m``` 커밋에 에디터를 열지 않고 메세지를 추가하는 옵션, 어떤 변화가 일어났는지를 주로 짤막하게 적는다.
- 이전 커밋에 변경 사항을 추가할 경우 
	```git commit --amend```
- 예시, C파일을 추가하고 commit할 경우
	```
	$ git add *.c
	$ git commit -m "add C file all"
	```
**4. git remote add [remote name] [address]**
- 리모트 저장소? : 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다.
  - ex : github, bitbucket
- 자신이 git을 저장할 장소를 설정한다.
- 처음에 생성했을 경우, remote name을 origin으로 많이 설정한다.
- 보통 github는 repository를 생성할 때, url을 ```https://github.com/[Repo leader 닉네임]/[Repo name].git```으로 생성한다. 
	
	```$ git remote add origin https://github.com/[Repo leader 닉네임]/[Repo name].git```

### 다른 Repository에서 가져오는 경우
- 다른 repository의 copy를 가져오는 것이다.
- ```git clone``` 명령어를 쓴다.
- **checkout 명령어가 아니다.**
- 그 repo에 있던 모든 history가 default로 git에 가져와진다.

**git clone [url]**
- url에 있는 git이 가져와진다.
- clone한 정보를 새로운 폴더에 저장하고 싶다면 ```git clone [url] [새로운 폴더 이름]```을 써라.
- url 중에서는 https 기반이 아닌, ssh기반의 ```git://```이나 ```user@server:path/to/repo.git```의 형태도 볼 수 있다.
- 이를 할 경우, remote 저장소가 자동으로 등록된다.

## 리모트 저장소
- 리모트 저장소? : 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다.
- 참고 : remote 저장소가 반드시 네트워크나 인터넷을 통해 있어야 한다는 것을 의미하는 것은 아니다.
	- 그렇다고 하더라도, Push나 Pull 같은 기능은 동일하게 사용한다.
	
### 리모트 저장소 확인하기
**git remote**
- 현재 프로젝트에 등록된 리모트 저장소를 확인할 수 있다.
- 저장소를 clone하면 'origin'이라는 리모트 저장소가 자동으로 등록된다.
- ```-v``` 
	- 단축 이름과 URL을 함께 볼 수 있다.
	- 리모트 저장소가 여러개라면 여러개의 remote 저장소를 보여준다.
	- Push 가능 권한까지는 확인할 수 없다.
	
**git remote add [단축이름] [address]**
- 리모트 저장소? : 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다.
  - ex : github, bitbucket
- 자신이 git을 저장할 장소를 설정한다.
- 처음에 생성했을 경우, remote name을 origin으로 많이 설정한다.
- 보통 github는 repository를 생성할 때, url을 ```https://github.com/[Repo leader 닉네임]/[Repo name].git```으로 생성한다. 
	
	```$ git remote add origin https://github.com/[Repo leader 닉네임]/[Repo name].git```

### 리모트 저장소 가져오기
**git fetch [remote name]**
- 로컬에는 없지만 리모트 저장소에 있는 모든 데이터를 가져온다.
- clone하면 리모트 저장소를 origin이라는 이름으로 추가하기 때문에, git fetch origin이라는 명령을 실행하면 clone 한 이후 수정된 것을 모두 가져온다.
- 자동으로 merge하지는 않는다.

**git pull [remote name]**
- 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 merge 시킨다.

git push : 온라인 상에 git을 올린다. <br><br>
* 주로 git add [file name] 한 뒤 git commit -m "message" 를 하고 git push를 한다.<br><br>
<h3>추가 사항</h3><br>
<h4>address에 관하여 </h4><br><br>
<h5>https://를 쓰는 경우</h5> https://github.com/[github 아이디]/[github에 올릴 레포].git<br>
<h5>ssh키를 쓰는 경우</h5> git@github.com:[github 아이디]/[github에 올릴 레포].git<br><br><br>
<h4>명령어에 관하여 </h4><br>
<h5>git remote set-url origin [address] </h5> 깃의 repo를 바꾸는 명령어이다. 이 명령어를 실행하면 [address]로 origin의 주소가 바뀐다.<br>
<br>
<br>
<h1>Normal </h1><br>
git 브랜치란? 특정 커밋에 대한 참조이다.<br><br>
브랜치를 많이 만들어도 메모리나 디스크 공간에 부담이 되지 않기 때문에, 많이 만들어도 된다. <br><br>
<br>
git branch [브랜치명] : [브랜치명]을 가진 새로운 브랜치를 만든다.<br>
git checkout [브랜치명] : [브랜치명]을 가진 브랜치로 이동한다.<br>
* checkout을 하지 않으면 master가 가리키는 commit과 branch가 가리키는 commit이 의도치 않게 다를 수 있다. 따라서 checkout으로 같은 곳을 가리키게 하거나 의도한데로 가리키도록 checkout을 사용해야 한다.<br>
<br>
브랜치 합치기 (Merge)란? 두 개의 부모를 가리키는 특별한 커밋을 만들어 내는 것. 즉 두 부모의 작업내역과 그 부모의 부모들의 모든 작업내역을 포함해 새로운 브랜치를 만들어 내는 것.<br>
* 순서로 암기하는 것이 좋다.<br>
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
<br>
<br>
<br>
로컬에 쌓인 커밋<br>
불필요한 디버그용 코드들이 들어가지 않게 하기 위해서 Git의 마법을 사용합니다!<br>
git rebase -i : 어떤 커밋을 취하거나 버릴지를 선택하는 것, 커밋의 순서를 바꾸는 것.<br>
git rebase -i HEAD~# : HEAD에서 #만큼 수를 바꾸거나 버린다.<br>
<br>
<br>
git commit --amend : 커밋 내용을 정정함.<br>
<br>
<br>

# 참고 자료
- https://creativecommons.org/licenses/by-nc-sa/3.0/#
- http://learnbranch.uriqit.com/

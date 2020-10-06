# Python Config file 관리

1.	Supported INI File Structure
-	Configuration file은 section으로 구성되고, [section] header를 붙인다.
-	[section] header 밑에는 key/value entries가 따라오며, ([1]에 의해 ‘=’이나 ‘:’로 구분된다. )
-	기본적으로 Section name은 케이스에 민감하지만, key들은 그렇지 않다.
-	공백은 key와 value에서 제거된다.
-	Value 생략 가능, 이 경우 구분기호도 생략 가능
-	Value는 첫 번째 줄보다 indentation이 들어가 있으면 여러 줄을 쓸 수 있다. 
-	Parser’s mode에선, 빈칸이 많은 라인을 가지는 value의 부분으로 다뤄지거나, 무시된다.
2.	Interpolation of values
-	Interpolation 지원
  - Get() call로부터 value가 나오기 전에 preprocess될 수 있다.
-	Class configparser.BasicInterpolation
  - ConfigParser에 의해 사용된다.
  - V같은 section안에 있는 다른 value를 참조하는 format string을 포함하는 value들과 special default 안에 있는 value들을 포함할 수 있도록 한다.
home_dir: /Users
my_dir: %(home_dir)s/lumberjack
my_pictures: %(my_dir)s/Pictures

[Escape]
gain: 80%%  # use a %% to escape the % sign (% is the only character that needs to be escaped)
  - ConfigParser가 %(home_dir)s를 /User로 품
  - 레퍼런스의 chain으로 사용되는 key들은 configuration file에서 어떤 특정한 순서로 분류되지 않는다.
  - Interpolation이 설정되어 있지 않다면 (None이라면) my_picture은 단순히 %(my_dir)s/Pictures가 return이 될 것이다.
-	Class configparser.ExtendedInterpolation
  - Interpolation의 대안책
  - Zc.buildout 안에서 instance를 위해 쓰이는 더 나은 문법
  - ${section:option} : 다른 section에서 value를 참조하기 위함
  - Section: 이 생략되면 현재 section으로 간주함. (혹은 special section의 default value로 간주)
```
[Common]
home_dir: /Users
library_dir: /Library
system_dir: /System
macports_dir: /opt/local

[Frameworks]
Python: 3.2
path: ${Common:system_dir}/Library/Frameworks/

[Arthur]
nickname: Two Sheds
last_name: Jackson
my_dir: ${Common:home_dir}/twosheds
my_pictures: ${my_dir}/Pictures
python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}
```
-	출처 : https://docs.python.org/3/library/configparser.html#supported-ini-file-structure
-	[1] : Config parsers allow for heavy customization 

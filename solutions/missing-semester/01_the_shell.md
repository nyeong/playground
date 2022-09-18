# 01. Courese overview + the shell

https://missing.csail.mit.edu/2020/course-shell/

## 01

쉘 확인하는 법:

- `echo $SHELL`
- `env | grep SHELL`: `env` 명령어로 환경변수를 모두 확인할 수 있으므로.
- `cat /etc/passwd | grep $(whoami)`: macOS에서는 UNIX/LINUX와 다르게
  `/etc/passwd`에서 사용자 관리를 하지 않으므로 쓸 수 없다.

```sh
$ echo $SHELL
/bin/zsh
```
  
`/bin`과 `/usr/bin` 차이점: 오늘날 대부분 리눅스 배포판에서는 신경 쓸 필요 없을듯?

https://lists.archlinux.org/pipermail/arch-dev-public/2012-March/022625.html

쓰는 쉘을 바꾸려면 `chsh -s [쉘 경로]`. 단 해당 쉘이 `/etc/shells`에 등록되어
있어야 한다.

```title={/etc/shells}
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/dash
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
````

여기에 없는 쉘을 설치했다면 해당 파일에 쉘 경로를 추가 후 `chsh` 하면 된다.

## 02

```sh
$ mkdir /tmp/missing
$ exa -alF /tmp
drwxr-xr-x - nyeong 2022-09-13 17:48 missing/
```

나는 `ls`를 `exa`로 alias해서 `exa`를 썼음.

## 03

```sh
$ man touch
$ tldr touch
```

- 상세하고 정확한 정보: touch
- 유용하고 짧은 예제: tldr

`tldr`은 커뮤니티 레벨에서 운영하는 도움말이다.

## 04

```sh
$ pwd 
/tmp
$ touch missing/semester
$ exa -TF .
./
└── missing/
   └── semester
$ ls missing
semester
```

`exa`에 `-T` 옵션을 주면 트리로 볼 수 있다. `tree` 명령어를 써도 된다.

## 05

```
$ pbpaste > missing/semester
$ cat missing/semester
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

`pbpaste`는 GUI에서 복사한 내용을 터미널에서 붙여넣을 때 쓰는 명령어.
리눅스 wayland 환경에서는 `wl-paste` 프로그램으로 대체할 수 있다.

아니면 편한 에디터로 입력해도 된다. 나는 `helix` 선호.

첫째 줄이 tricky 하다는데, 해시뱅(*hash-bang*) 혹은 셔뱅(*shebang*)이라고
부르는 것이다. 해당 파일이 무슨 파일인지 알려주는 용도이다.[^1][^2]

[^1]: https://tldp.org/LDP/abs/html/sha-bang.html
[^2]: https://tldp.org/LDP/abs/html/sha-bang.html

```
#!인터프리터 [옵션]
```

예를 들어 파이썬 코드를 파일 째로 배포했다면 아래와 같은 해시뱅이 주로 쓰인다.

```
#!/usr/bin/env python3
```

파이썬 실행 경로가 시스템마다 다를 수 있으므로 `env` 프로그램으로 찾아서
실행하라는 뜻이다.

bash에서 큰따옴표(`"`)로 감싼 문자열은 내부의 특수문자를 읽어서 처리한다.

```
$ echo "My name is $(whoami)"
My name is nyeong
```

작은따옴표(`'`)로 감싼 문자열은 그대로 문자열로써 다룬다.

```
$ echo 'My name is $(whoami)'
My name is $(whoami)
```

bash에서 !(*bang*)는 이벤트 지정자(*event designators*)로 쓰인다.
`man bash`에서 `!!`으로 검색하면 확인할 수 있다. `!`, `!n`, `!-n`, `!!` 등등 있다.

```title={man bash}
Event Designators
    An event designator is a reference to a command line entry in the history
    list.  Unless the reference is absolute, events are relative to the current
    position in the history list.
```

## 06

```
$ pwd
/tmp/missing
$ ls
semester
$ ./semester
zsh: permission denied: ./semester
```

권한이 없다고 한다. `ls -l` 명령어로 권한을 확인할 수 있다.

```
$ ls -l semester
.rw-r--r-- 61 nyeong wheel 2022-09-13 17:58 semester
```

가장 앞의 `rw-`로 시작하는 9글자가 권한에 대한 설명이다. 세글자씩 끊어서 보면
된다.

- `rw-`: 소유자의 권한. 읽기, 쓰기가 가능하다. 소유자는 `nyeong`이다.
- `r--`: 그룹의 권한. 읽기만 가능하다. 그룹은 `wheel`이다.
- `r--`: 그 외 모든 사람들의 권한. 읽기만 가능하다.

해당 파일은 읽을 수는 있으나 실행할 수는 없다.

## 07

읽을 수는 있으므로 읽어서 인터프리터에 넘기면 프로그램을 실행할 수 있다.

```
# 읽어서 넘기기
$ cat semester | sh

# 인터프리터에게 읽으라고 하기
$ sh semester
```

## 08, 09

파일에 실행권한을 주어서 실행할 수도 있다.
`chmod` 명령어로 권한을 바꿀 수 있다. `chown` 명령어로 소유자/소유그룹을 바꿀
수 있다.

```
$ chmod u+x semester # 유저에게 실행 권한 주기
$ chmod 744 semester # 권한을 rwxr--r--로 설정하기
```

`chmod`는 `chmod [바꿀 권한] 파일명` 꼴로 인자를 받는다.

위의 `u+x`처럼 특정 권한을 고칠 수 있다. `u`는 소유자, `g`는 그룹, `o`는 그 외의
사람을 의미한다. `+`는 권한 추가를, `-`는 권한 삭제를, `=`는 왼쪽의 대상에게
우측의 대상과 동일한 권한을 부여하는 명령이다. `r`은 읽기, `w`는 쓰기, `x`는
실행 권한을 의미한다.

위의 `744`처럼 아예 권한을 지정할 수 있다. `r`을 4, `w`를 2, `x`를 1로 생각하고
합하여 계산하는 것이다. 따라서 744면 `rwxr--r--`을 의미한다.

```
$ chmod 744 semester
$ ls -l semester
.rw-r--r-- 61 nyeong wheel 2022-09-13 17:58 semester
$ ./semester
HTTP/2 200
server: GitHub.com
... 생략 ...
```

## 10

고친 시간 알아내기:

- `date -r [파일 이름]`
- `stat -f %Sm [파일 이름]`

표준 출력을 저장하기:

- `date -r [파일 이름] | tee ~/last-modificated.txt`
- `date -r [파일 이름] > ~/last-modificated.txt`

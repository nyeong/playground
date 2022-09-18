# Shell Tools and Scripting

https://missing.csail.mit.edu/2020/shell-tools/

## 01

아래의 옵션은 `macOS 12.5`, `bash` 기준.

- `-A`: .으로 시작하는 파일도 보기. `.`과 `..`은 생략.
- `-l`: 상세보기. 권한, 소유, 크기도 볼 수 있다.
- `-G`: 색상 입혀서 출력
- `-h`: 크기를 B, KB등 읽기 쉬운 단위로 보여줌
- `-t`: 가장 최근에 수정한 파일부터 보여준다. `-r` 옵션도 주면 반대로.

```
$ ls -AlGht
total 320
drwxr-xr-x  14 nyeong  staff   448B  9 14 21:07 .cache
-rw-------   1 nyeong  staff    18K  9 14 21:05 .zsh_history
-rw-r--r--   1 nyeong  staff   679B  9 14 21:03 .z
-rw-r--r--   1 nyeong  staff    53K  9 14 20:57 .zcompdump
drwx------+  2 nyeong  staff    64B  9 14 08:42 .Trash
drwx------@ 15 nyeong  staff   480B  9 13 23:21 Downloads
-rw-r--r--@  1 nyeong  staff    14K  9 13 23:07 .DS_Store
drwxr-xr-x  12 nyeong  staff   384B  9 13 23:06 .ghcup
```

## 02

```bash title={marco.sh}
# save current working directory
marco() {
  export MARCO_PATH=$(pwd)
  echo "current path saved: $MARCO_PATH"
}

# go flagged directory by `macro`
polo() {
  if [[ ! $MARCO_PATH ]]; then
    echo "do marco first!"
    return
  fi

  cd $MARCO_PATH
}
```

```
$ source marco.sh
$ marco
current path saved: /tmp
$ cd /
$ polo
$ pwd
/tmp
```

## 03

```bash
#!/usr/bin/env bash

is_failed=false
while ! $is_failed
do
  catched_error=$($1 2>&1 > /dev/null)
  catched_number=$?
  if [ $catched_number -ne 0 ]
  then
    echo "$1 failed with: $catched_number"
    echo "$catched_error"
    exit
  fi
done
```

## 04

`find`에 `-exec` 옵션을 주면 찾은 파일 **각각에** 원하는 명령을 먹일 수 있다.
그렇다면 찾은 파일 **모두를** 한 번에 입력으로 명령을 먹이려면 어떻게 해야
하는가?

- 각각의 명령어들은 표준입력(STDIN) 혹은 인자로 입력을 받는다.
- `find`의 결과는 표준출력(STDOUT)이다.
- 입력을 표준입력으로 받는 명령어는 파이프로 넘기면 된다.
- 입력을 인자로 받는 명령어는 `xargs`를 이용해 표준출력 → 표준입력 → 파이프로
  넘기면 된다.
  
```bash
find . -name "*.html" | xargs zip "html.zip"
```

## 05

```bash
find . -exec stat -f "%m %N" {} \; | sort | tail -n 1
```

# 에디터

https://missing.csail.mit.edu/2020/editors/

하지만 난 vim이 싫은걸... [helix]로 해봤음

[helix]: https://helix-editor.com/


## 01

helix도 있다!

```bash
$ helix --tutor
```

## 02

helix는 `~/.config/helix/config.toml` 파일로 설정할 수 있다. 아쉽게도
vim과 같은 플러그인 지원은 아직 없어서 설정할 수 있는 것이 많지 않다.

## 03

대응하는 플러그인은 없지만 `space + f`로 퍼지 파인더를 쓸 수 있다.

## 04

https://youtu.be/a6Q8Na575qc?t=2255

```python
def fizz_buzz(limit):
    for i in range(limit):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('fizz')
        if i % 3 and i % 5:
            print(i)

def main():
    fizz_buzz(10)  
```

파이썬을 잘 몰라서 영상 보고 따라함

- Main is never called
  1. `ge` 파일 끝으로 이동
  2. `o` 다음 줄 추가, 입력모드로 전환
  3. `backspace` 자동으로 들여쓰기가 되므로 들여쓰기 지우기
  4. 다음 코드 입력
     ```python
     if __name__ == '__main__':
       main()
     ```
  5. `:w` 저장
- Starts at 0 instead of 1
  2번째 줄의 `range(limit)`를 `range(1, limit + 1)`로 고쳐야 한다
  1. `2gg`
  2. `f(`
  3. `i`로 입력모드 진입하여 `1, ` 입력
  4. `e`로 다음 단어 `limit`의 끝으로 이동
  5. `i`로 입력모드 진입하여 `+ 1` 입력
- Prints “fizz” and “buzz” on separate lines for multiples of 15
  영상에서는 3으로 나누어 떨어질 때와 5로 나누어 떨어질 때의 `print`에서 줄바꿈을
  없애던데... 일단 그렇게 했다.
  1. `/range`로 4번째 줄의 `range` 선택
  2. `5x`로 현재 커서가 있는 위치부터 5개의 줄 선택
  3. `sprint`로 `print` 다중선택. `s`는 다중선택 단축키이고, Regex로 문자열을
     선택할 수 있다.
  4. `gl`로 오른쪽 끝으로 이동, `)`가 선택된다.
  5. `i`를 눌러 커서 왼쪽에 `, end=''` 삽입한다.
- Prints “fizz” for multiples of 5
  5번째 줄의 `'fizz'`를 `'buzz'`로 바꾸면 된다.
  1. `/fizz`로 `fizz` 검색
  2. `n`으로 두 번째 `fizz` 선택
  3. `c`로 선택된 영역을 지우고 편집모드로 전환, `buzz` 삽입
- Uses a hard-coded argument of 10 instead of taking a command-line argument
  `sys.argv`를 이용한다.
  1. `gg`로 제일 첫 줄로 이동
  2. `O`로 커서 윗줄에 새 줄 삽입, 편집모드로 전환, `import sys` 입력
  3. LSP가 있으면 `space s`로 심볼릭 픽커 열어서 `main` 함수로 이동하면 되는데,
     설치를 안해서 `/main`
  4. `f(`로 괄호시작 선택
  5. `ec`로 괄호 내 숫자 선택 후 지우고 편집모드로 전환, `int(sys.argv[1])` 입력
  
## 05

helix 잘 쓰는 중

## 06

helix에 플러그인 기능이 아직 안 들어와서 helix 자체에서의 확장은 할 것이 없다.

그 외에 vim-binding을 딴 것 중, 웹 브라우저에서 vim 비슷한 단축키를 쓸 수 있는
*vimium*을 써보고 있다.

- https://github.com/philc/vimium
- https://johngrib.github.io/wiki/web-browser-vim/

## 07

아 아직 플러그인이 없다구요 ㅋㅋ..

## 08

helix는 22.08.1 버전에서 매크로가 아직 실험적 기능이며
`@` 레지스터에만 매크로를 녹화할 수 있다.

- `Q`: 매크로 녹화를 시작/중지한다.
- `q`: 매크로를 실행한다.

매크로를 써도 되긴 하는데, `%s` 전체선택 기능으로 `person` 선택해서 편집하는게
더 편하긴 하다.

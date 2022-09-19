# 데이터 랭글링

> 데이터 랭글링은 다양한 데이터 소스의 데이터를 통합하고 쉽게 액세스하고 분석할
> 수 있도록 정리하는 프로세스입니다. -- https://www.tibco.com/ko/reference-center/what-is-data-wrangling

## 01

https://regexone.com/

1. `a`
2. `[0-9]+` 혹은 `\d+`
3. `...\.`
4. `[cmf]an`
5. `[^b]og`
6. `[A-C]`
7. `z{3,5}`
8. `aa+`
9. `\d+ files?`
10. `\s+abc`
11. `^Mission`
12. `^([a-z_\d]+)\.pdf$`
13. `([A-Za-z]+ (\d+))$`
14. `(\d{4})x(\d{3,4})`
15. `I love (cat|dog)s`

## 02

```bash
cat /usr/share/dict/words
  | rg "(.*a){3}.*[^'s]" # 최소 세 개의 a를 포함하고 's로 끝나지 않음
  | rg -o "(..)$"        # 각 단어의 마지막 두글자만 추출
  | sort | uniq -c       # 같은 것끼리 묶고 각각의 갯수를 셈
  | sort | tail -n3      # 정렬하고 갯수가 가장 큰 세 개만 구함

cat /usr/share/dict/words
  | rg "(.*a){3}.*[^'s]" # 최소 세 개의 a를 포함하고 's로 끝나지 않음
  | rg -o "(..)$"        # 각 단어의 마지막 두글자만 추출
  | sort | uniq          # 정렬하고 각각의 유일한 것 하나만 남김
  | wl -c                # 남은 것들의 갯수를 셈
```

## 03

```
sed s/REGEX/SUBSITUTION/ input.txt > input.txt
```

위 명령어를 실행하면 `input.txt`는 빈 파일이 된다. 반면 아래 명령어는
의도대로 작동한다.

```
sed s/REGEX/SUBSITUTION/ input.txt > other.txt
```

리다이렉션(`>`)은 파일의 내용을 지우고 쉘이 다시 그 내용을 채워넣는다.
문제는 쉘의 동작이 리다이렉션부터 인터럽트 하기 때문에, `sed`가 실행되기 전에
`> input.txt`로 인해 `input.txt` 파일이 초기화된다. `-i` 옵션은 임시 파일을
만들어서 이 문제를 해결한다고 한다.

다른 파일로 리다이렉션 할 경우 (`> other.txt`) 다른 파일이 초기화되어도 `sed`의
동작에는 문제가 없기 때문에 이상이 없다.

```
sed -i '' s/REGEX/SUBSITUTION/ input.txt
```

마찬가지로 `tee`를 파이프라인으로 넘길 경우도, `sed`가 끝난 후 `tee`가 동작하기
때문에 의도대로 돌아간다.

## 05

TODO

## 06

TODO

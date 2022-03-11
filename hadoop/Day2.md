# Day2

### 명령어

1. Project/src/Driver.java 수정
   - pgd.addClass("wordcountsort", Wordcountsort.class, "설명");
2. Project 디렉토리에서
   - ant 실행
   - hdfs dfs -rm -r wordcount_test_out(결과 들어올 디렉토리 삭제 - 리셋해주는것)
   - hadoop jar ssafy.jar wordcountsort wordcount_test wordcount_test_out
   - hdfs dfs -cat wordcount_test_out/part-r-00000 | more (cat은 파일 내용보는 명령어)
   - hdfs dfs -cat wordcount_test_out/part-r-00001 | more

- Reduce마다 결과가 만들어지기때문에 모든 결과를 봐야함



------



### Inverted Index 생성

Inverted index => 어떤문서:몇번째위치

ex ) 

Doc1: IMF FINANCIAL 

Doc2: Harry IMF

IMF -> Doc1:1, Doc2:7

Harry -> Doc2:1



## 결과로 inverted index 생성하기

#### Wordcount.java 수정

- 파일이름 InvertedIndex.java

- inverted in dex를 생성하는 코드로 수정



#### 명령어

1. Project/src/Driver.java 수정

   - pgd.addClass("inverted",  InvertedIndex.class, "설명");

2. Project 디렉토리에서

   - ant 실행

   - 이번에는 리듀스 함수의 결과를 출력하는 디렉토리를 멥리듀스 코드에서 자동적으로 삭제하도록 구현할 것이므로 삭제 안함.

     ```
     # main코드 부분
     FileSystem hdfs = FileSystem.get(conf);
     Path output = new Path(otherArgs[1]_;
     if (hdfs.exists(output))
     	hdfs.delete(output, true);
     ```

   - hadoop jar ssafy.jar inverted wordcount_test invertedindex_test_out

   - hdfs dfs -cat invertedindex_test_out/part-r-00000 | more 

   - hdfs dfs -cat invertedindex_test_out/part-r-00001 | more

- Reduce마다 결과가 만들어지기때문에 모든 결과를 봐야함



#### 코드작성에서 필요한 함수

- StringTokenizer(value.toString()," ",true);
  - 단어 단위로 자르기

- Long: ((LongWritable)key).get();

  - 입력파일에 있는 맨앞부터 캐릭터로부터 지금라인의 캐릭터가 몇번째인지 확인하기 위함

    = 파일에서 현재 라인의 시작 위치의 byte offset 가져옴

  - import arg.apache.hadoop.io.LongWritable 추가해야함!

- filename+":"+p;

  - 파일명과 현재 위치를 concatenate

- token.length()

  - String 타입의 variable인 token의 길이를 얻으로면 필요함

- 입력 파일 이름을 알아내는 방법

  - import org.apache.hadoop.mapreduce.lib.input.FileSplit;

    ```java
    private String filename;
    protected void setup(Context context) throws IOException, InterruptedException {
    filename = ((FileSplit)context.getInputSplit()).getPath().getName();
    }
    ```



------



## Matrix Addition

##### 입력파일

​	행렬이름 	 행번호	열번호	원소값

##### 출력파일

​	행번호	열번호	원소값(계산값)  - 꼭 순서대로 나오진 않음

##### 과정

(A 0 0 3) (B 0 0 2) -> **(Map)** -> key(0,0위치) vlaue (3원소값) -> **(Shuffle)** -> key(0,0) value_list([3, 2]) -> **(Reduce)** -> key(0,0) value(5)



####  코드 작성(MatrixAdd.template.java  수정)

- 파일이름 MatrixAdd.java

- Matrix Addition를 생성하는 코드로 수정



#### 명령어

1. Project/src/Driver.java 수정
   - pgd.addClass("matadd",  MatrixAdd.class, "설명");
2. Project 디렉토리에서
   - ant 실행
   - hdfs dfs -mkdir matadd_test
   - hdfs dfs -put data/matadd-data-2x2.txt matadd_test
   - hadoop jar ssafy.jar matadd matadd_test matadd_test_out
   - hdfs dfs -cat matadd_test_out/part-r-00000 | more 
   - hdfs dfs -cat matadd_test_out/part-r-00001 | more

- Reduce마다 결과가 만들어지기때문에 모든 결과를 봐야함

#### 

#### 필요한 함수

- String[] split(String delimeter)
  - String class의 member method
  - String을 delimeter로 분리하여 array에 넣어 리턴
  - ex ) String[] arr = tmpStr.split ("\t");

#### 


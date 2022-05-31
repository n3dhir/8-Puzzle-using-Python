# 8-Puzzle
1. Download the zip file and extract it.
2. Open **main.py** file.

![Sans titre](https://user-images.githubusercontent.com/84473151/171168652-dffbd1c7-3e58-4c2a-bcaf-4f4bee4a1da0.png)
## How to execute
#### 1. you can choose the _initial state_ and the _final state_ in the source code or  you can click **SHUFFLE** to get a random _initial state_   

![image](https://user-images.githubusercontent.com/84473151/171173936-64b0ed22-8c3f-4086-905c-f180721d935a.png)  

#### 2. To run an algorithm, just click **BFS** , **DFS** , **A***, or **Depth Limited**  

#### 3. You can click **RESET** to reset the board to the initial state  

#### 4. You can click **SHUFFLE** to get a new random initial state  
 >sometimes you can get an impossible puzzle (a puzzle that has no solution).
#### 5. When an algorithm is running you should wait for it else the program will crash  

![image](https://user-images.githubusercontent.com/84473151/171176403-dea7d87b-8761-4155-8056-7227a0d45dd2.png)

#### 6. When an algorithm completes, the corresponding fields will have new values

![Sans titre](https://user-images.githubusercontent.com/84473151/171178045-d8a99e34-5fdd-43cf-81d5-4d452317fb55.png)

#### 7. If no solution is found the answer will be **INFINITY**

![Sans titre](https://user-images.githubusercontent.com/84473151/171178781-23294321-07eb-40c7-8048-61f12ef63a7e.png)

#### 8. You can change the maximum depth achievable by the Depth Limited algorithm
      check line 419.

#### 9. To change the speed of the cells, change the value of **latency** in the track function
   **250** milliseconds ![image](https://user-images.githubusercontent.com/84473151/171181930-f342b0b5-c132-4bcd-9b83-703da5154d6e.png)  
 
   **0** milliseconds ![image](https://user-images.githubusercontent.com/84473151/171182377-8a80078b-e40d-4bed-a238-dbf5bce663b0.png)

   >A high latency means slow speed.  

   >A low latency means high speed.

## Conclusion
 The **A*** algorithm is the best, it visits much less nodes than other algorithms.
 
 ![Sans titre](https://user-images.githubusercontent.com/84473151/171180418-880aba0f-a7b3-4b99-b3fd-765d13dfaab5.png)

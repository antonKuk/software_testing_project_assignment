## **Task 1: Test Plan**

#### Test Plan Identifier

##### 10 pin bowling game prototype testing plan TP_1.0

##### *version author* : Anton_K



#### Introduction

This test plan has following objectives:

1. To identify responsible parties, resources and tools to be used during this testing
2.  To define test tasks and expectations
3. To describe the testing process 

#### References

- supporting documents for this testing plan are test cases

-  game prototype back end code files (Main.py and BowlingGame.py) 

- git repository  https://github.com/antonKuk/software_testing_project_assignment.git

- Pythondoc documentation

- game rules described in project assignment instructions:

  - 10 frames for each player

  - in each frame, every player will have 2 chances (plus 1  chance could be awarded in 10th frame) to score as many pins as possible

  - one point is scored for each pin

  - every player will take his/her turn in a predetermined order

  - if a player knocks down all ten pins with their first ball, he is awarded a strike

  - if the bowler knocks down all 10 pins with the two balls of a  frame, it is a spare

  - bonus points are awarded for both a strike and a spare

  - the bonus points  depend on what is scored in the next 2 balls (for a strike) or 1 ball (for a spare)

  - the most points that can be scored in a single frame are 30 points (10 for the original strike, plus strikes in the two subsequent frames)

  - if the bowler knocks down all 10 pins in the 10th frame, the player is allowed to throw  3rd ball

  - a player who bowls a strike in the tenth (final) frame is awarded  two extra balls allowing the playing to gain bonus points. If both these balls also result in strikes, a total of 30 points (10 + 10 + 10) is  awarded for the frame. These bonus points do not count on their own;  they only count as the bonus for the strike

  - there is a potential of 12 strikes in a single game, and a maximum score of 300 points

  - the most points that can be scored in a single frame are 30 points (10 for the original strike, plus strikes in the two subsequent frames)

    

    **examples:** 	 

    |                  |                   |
    | :--------------: | ----------------- |
    | Frame 1, ball 1: | 10 pins (strike)  |
    | Frame 2, ball 1: | 3 pins            |
    | Frame 2, ball 2: | 6 pins            |
    |  Frame 1 score:  | 10 + (3 + 6) = 19 |
    |  Frame 2 score:  | 3 + 6 = 9         |
    |     TOTAL =      | 28                |

    **example of multiple strikes in succession :**

    |                  |                    |
    | :--------------: | ------------------ |
    | Frame 1, ball 1: | 10 pins (strike)   |
    | Frame 2, ball 1: | 10 pins (strike)   |
    | Frame 3, ball 1: | 4 pins             |
    | Frame 3, ball 2: | 2 pins             |
    |  Frame 1 score:  | 10 + (10 + 4) = 24 |
    |  Frame 2 score:  | 10 + (4 + 2) = 16  |
    |  Frame 3 score:  | 4 + 2 = 6          |
    |     TOTAL =      | 46                 |



#### Test items

- game prototype back end code files (Main.py and BowlingGame.py) 
  - **BowlingGame.py** has main score() function which checks each pins value from given list pins[] and follows this logic:
    1. checks if pin has value of 10  (isStrike() function) and if true adds next two pins' values to current frame score (strikeScore() function)
    2. if first step was false, function checks if there is a spare  (isSpare() function) and counts points accordingly  (spareScore() function)
    3. in case of no score or spare two pins' values add together and pins' list index jumps +2
    4. there is also roll() function which appends input values to the pins' list

  - **Main.py** is file with several test functions which feed different pin values to game and check that result is correct. (more details  in section below)

- pycharm IDE will be used mainly for testing, debugging and refactoring python files (Main.py and BowlingGame.py)
- game rules described in project assignment instructions (section above)

#### Features To Be Tested

- any bugs, typos or syntax errors absence in the source code (they should be fixed before testing  code logic)
- game rules are implemented into the code logic:
  - as a player rolling all zeros (test_gutter_game() function in Main.py). Result (score() function in BowlingGame.py) should be zero
  - as a player rolling all ones (test_all_ones() function in Main.py). The result should be 20
  - as a player rolling one  "spare"  plus one more none-zero frame and all other frames as zeros 
  - as a player rolling one "strike " plus one more none-zero frame and all other frames as zeros
  - as a player rolling perfect game. The result should be 300
  - as a player rolling all spares (all fives). The result should be 150

#### Features Not To Be Tested

- ​	Not others than mentioned in section above
- ​    GUI and I/O parts of the software are not developed so not to be tested

#### Approach

- Tests should be run for each test case per  tester
- Tester should execute each step of every test case and mark it as "pass" or "fail"
- In case of failure of any step it should be reported in appropriate comment section
- 
- Once all tests are done test manager should review them and produce the Test Summary Report

#### Item Pass/Fail Criteria

- Every test case step should be considered successful after execution if it matches appropriate  “expected result” description
- In any other case it should be considered and marked as “fail”

#### Suspension Criteria

Testing should be suspended in case of hardware / software failure or any system CRUD (Create, Read, Update and Delete) failure. Failure should be reported and fixed as soon as possible.

#### Test Deliverables 

All test cases run results should be saved  and reported  in test logs

#### Test Tasks

The following must be completed:

- ​	each member of the testing team has read test plan
- ​	environment is suitable for testing
- ​	tests are performed
- ​	test cases run results are documented
- ​    any bug, typo or syntax error fixes are git committed with appropriate comments 
- ​	test summary report is produced

#### **Environmental needs**

- computer with Windows or Mac OS  
- Pycharm IDE, git, GitHub account and text editor installed (Typora, Notepad++)

#### Responsibilities

It is a test manager  responsibility to:

- train team
- communicate risks and expectations to every team member
- make sure that all environmental needs are satisfied
- facilitate testing project as needed

#### Staffing And Training Needs

No particular needs are required

#### Schedule

No particular schedule is required

#### Risks And Contingencies

N/A

#### Approvals

N/A



## **Task 2: Test Cases** (conducted and documented)



#### test case 1: BowlingGame.py

| ID   |           case name            |          pre-requisite           | procedure                                                    | expected result                       | priority | author  | pass/fail |                           comment                            |
| ---- | :----------------------------: | :------------------------------: | :----------------------------------------------------------- | :------------------------------------ | :------: | ------- | :-------: | :----------------------------------------------------------: |
| 1    | BowlingGame.py syntactic fixes | BowlingGame.py file, pycharm IDE | open BowlingGame.py file in pycharm IDE                      | file opened                           |    p1    | Anton_K |   pass    |                                                              |
|      |                                |                                  | go to "problems" tab at  the bottom                          | tab opened                            |    p1    |         |   pass    |                                                              |
|      |                                |                                  | check if  no "weak warnings" are displayed                   | no weak warning messages              |    p2    |         |   fail    |                       24 weak warnings                       |
| 1.1  |                                |                                  | if any "weak warnings" are displayed press alt+Enter and click "reformat the file" option | option was clicked, changes were made |    p1    |         |   pass    | changes are committed to git, notes added to log section below |
| 1.2  |                                |                                  | check for other warnings (typos, wrong indentation, wrong naming format so on) and fix them | no warnings or typo messages          |    p1    |         |   pass    | changes are committed to git, notes added to log section below |



#### test case 2: Main.py 

| ID   |        case name        |       pre-requisite       | procedure                                                    | expected result                       | priority | author  | pass/fail |                           comment                            |
| ---- | :---------------------: | :-----------------------: | :----------------------------------------------------------- | :------------------------------------ | :------: | ------- | :-------: | :----------------------------------------------------------: |
| 2    | Main.py syntactic fixes | Main.py file, pycharm IDE | open Main.py file in pycharm IDE                             | file is opened                        |    p1    | Anton_K |   pass    |                                                              |
|      |                         |                           | go to "problems" tab at  the bottom                          | tab is opened                         |    p1    |         |   pass    |                                                              |
|      |                         |                           | check if  no "weak warnings" are displayed                   | no weak warning messages              |    p2    |         |   fail    |                       20 weak warnings                       |
| 2.1  |                         |                           | if any "weak warnings" are displayed press alt+Enter and click "reformat the file" option | option was clicked, changes were made |    p1    |         |   pass    | changes are committed to git, notes added to log section below |
| 2.2  |                         |                           | check for other warnings (typos, wrong indentation, wrong naming format so on) and fix them | no warnings or typo messages          |    p1    |         |   pass    | changes are committed to git, notes added to log section below |



#### test case 3:  Main.py test modules

| ID   |          case name          |       pre-requisite       | procedure                                                    | expected result             | priority | author  | pass/fail |                 comment                  |
| ---- | :-------------------------: | :-----------------------: | :----------------------------------------------------------- | :-------------------------- | :------: | ------- | :-------: | :--------------------------------------: |
| 3    | test_gutter_game() function | Main.py file, pycharm IDE | open Main.py file as project in pycharm IDE                  | file is opened              |    p1    | Anton_K |   pass    |                                          |
| 3.1  |                             |                           | run Main.py by clicking on green triangle on top of IDE      | test was run                |    p1    |         |   pass    |                                          |
| 3.2  |                             |                           | in a "run" tub select "testAllOnes" module and check for "OK" message | test module passed the test |    p2    |         |   fail    | TypeError: 'list' object is not callable |
|      |                             |                           | in a "run" tub select "testAllSpare" module and check for "OK" message | test module passed the test |    p1    |         |   fail    | TypeError: 'list' object is not callable |
|      |                             |                           | in a "run" tub select "testGutterGame" module and check for "OK" message | test module passed the test |    p1    |         |   fail    | TypeError: 'list' object is not callable |
|      |                             |                           | in a "run" tub select "testOneSpare" module and check for "OK" message | test module passed the test |    p1    |         |   fail    | TypeError: 'list' object is not callable |
|      |                             |                           | in a "run" tub select "testOneStrike" module and check for "OK" message | test module passed the test |    p1    |         |   fail    | TypeError: 'list' object is not callable |
|      |                             |                           | in a "run" tub select "testPerfectGame" module and check for "OK" message | test module passed the test |    p1    |         |   fail    | TypeError: 'list' object is not callable |



#### Test cases log section

####  case 1

Index 1.1:	 24 weak warnings are fixed with pycharm "reformat" option

Index 1.2:	 

- 5 warnings ("rollIndex" Argument name should be lowercase, refactored to "roll_index")
- typo in function name in line 29. renamed to "strikeScore"
- typo in function name in line 13. renamed to "strikeScore"
- wrong identation in line 21 in function score(). it was returning "result" every iteration



#### case 2

Index 2.1:  	

- 20 weak warnings are fixed with Pycharm "reformat" option
- "Redeclared 'testOneSpare' defined above without usage" warning message. Function "testOneSpare" was declared two times. Function checks 150 score in line 39 which is "All Spare" score. Therefore function was renamed to "testAllSpare"












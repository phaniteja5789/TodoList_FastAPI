# TodoList_FastAPI
This repository is an sample ToDoList application developed using **FastAPI, HTML, JavaScript. **

The startup screen will be as below screen.
<img width="290" alt="image" src="https://github.com/phaniteja5789/TodoList_FastAPI/assets/36558484/2d54041d-beda-431f-a85b-1a1f4906881f">

User can be able to enter the task name of length 30 at maximum.

**UseCase-1**

  1.) Once the user submits the task name, 
  2.) The request is sent as post method and carries the data of the task name entered. 
  3.) The corresponding POST request API call which was developed using FAST API will gets hit and it will add the task name to the list.
  4.) The Post Request will Renders the HTML Response, with all the list of tasks.
  
  The below is the screenshot of the **Usecase-1**
  
  ![image](https://github.com/phaniteja5789/TodoList_FastAPI/assets/36558484/84803234-0a21-404f-9666-bb900453964f)

  
 **UseCase-2**

  1.) Once user completes the task, the user can left click on the task name. 
  2.) Based on the click event the corresponding data will be sent using **FETCH API of Javascript** and hits the API developed using FAST API. 
  3.) Such that it will again render the template, with line-through on the task-name
  
  The below is the screenshot of the **UseCase-2**
  
  ![image](https://github.com/phaniteja5789/TodoList_FastAPI/assets/36558484/6632ae10-8f3c-4038-bbad-6383465805b9)

  
  **UseCase-3**
  
  1.) Once user wants to remove the task name enetered, the user can Right Click on the Task Name.
  2.) The default Right Click will give the Context Menu and I have prevented the default Right Click Action
  3.) Based on the right click event the corresponding data will be sent using FETCH API of JAVAScript and hits the API developed using FAST API.
  4.) Such that it will again render the template, with the task name removed
  
  The below is the screenshot of the **UseCase-3**
  
  ![image](https://github.com/phaniteja5789/TodoList_FastAPI/assets/36558484/5e3f37b9-1221-4f5e-b9df-631525c81b87)
  
The application has been hosted on local host

The command to run the application is - uvicorn sourcecode:app --reload

sourcecode ==> Name of the File where the app is initialized

--reload ==> To automatically reload the server based on the changes.


  

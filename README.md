## 💡 Inspiration
For the past year, all of us, similar to many students around the world were forced to switch to an online learning model. Now, spending most of our time in front of our devices, either working, or being distracted. So for JamHacks, we decided to create an application that motivates us to break these unhealthy habits through a competition. Which is why we created workflow, to try and put a measurement to our productivity and motivate ourselves to take health breaks between working sessions, while competing with friends and collogues to see who is "more" productive.

## ⚙️ What it does
Workflow essentially works in the background tracking which applications and processes are running, and based on a predefined list of productive and non-productive apps. After extended work sessions, the application notifies the user that they should take a break, which is tracked by checking the user's activity. The application is able to award the user points for using productivity and work applications, such as Microsoft Word, Excel, PowerPoint, and even Notion. Whilst also tracking some games. These applications are just what is defined right now, but the application bases these apps through the list on our firebase database. Besides that, to motivate the users to get up and walk around for a break, the application starts deducting points slowly. The application is able to then send these stored points to our firebase database, where the points along with the user's username and password are stored. This information is then used to on the website to allow the users to sign in, and check out the leaderboards.

## 🐱‍💻 How we built it
We built the workflow desktop tracking application using python, utilizing the tkinter library to create the log-in and register GUI. This would allow users to create accounts which were added to our database hosted on firebase, or update their points into their preexisting accounts. We then use Html & CSS to create a website which allows the users to sign in, to track their performance and check out the leaderboards. This website would be able to validify the information by fetching necessary information from firebase.

## 🤔 Challenges we ran into
Having no knowledge about firebase or tkinter, and minimal to no knowledge about developing a website that would allow users to sign in. We had to learn how to use these tools in order to finish our project during the duration of the hackathon, and some main challenges that we faced with them were:
1) Accessing the list of open processes and programs to track productive and non productive processes 
2) Creating log-in and registration interfaces for the program
3) Setting up a database to store the user information
4) Adding user information to the database
5) Getting the user's information on startup
6) Accessing the database information through JS for the website
7) Setting up a pop-up to prompt the user to take a break

## 🎉 Accomplishments that we're proud of
Working on workflow, and seeing what we have achieved, we are quite proud of what we were able to learn and implement during the 24 hours. Firstly, we are proud of what learned about what firebase was, and how we used it with python and JS. We are also proud of the GUI we created, as it was our first time using tkinter for a project, having to learn more about how it works and the different elements that can be used. Lastly, we are also proud of being able to connect a python application to a web page that is able to use the data collected by the application locally to display the users' personal points and how they compare to others.

## 📚 What we learned
Being new to whole idea of using databases, creating GUIs and web pages, during the 24 hours for the hackathon we were able to learn quite a bit through the different workshops as well as through our personal research. We were able to increase our understanding of how databases works, what firebase is, and how to use it as a database to store our information. Besides that, we got to experiment and get familiar with the tkinter library and its elements, using it the create the GUI for the desktop workflow application. Lastly, we learned more about web development, implementing and adding upon what we learned during the Html & CSS workshop, by creating a web page for the application. 

## ❓ What's next for Time Flow
We believe that Time Flow can definitely be improved upon with more time. Some next steps would be:
- Creating more leaderboards, which would allow people from different areas or friends to compete privately against each others (i.e school wide, university wide, province wide, etc...)
- Allowing users to gain points during their time of the computer by tracking exercising data possibly through smart devices already in use (i.e smart watches and phones)
- Offer prizes to the top contests on the leaderboards, or allow users to use their points to enter for chances to win possible prizes (i.e raffles)
- Work with schools, universities or institutions  to develop a leaderboard and UI catered towards those specific groups, offering these users prizes from their institutions

Overall, we believe that these ideas would help motivate more people to use Time flow in order to improve upon their time management habits, improve productivity, and compete against friends.
<br/>
💻 Devpost: 


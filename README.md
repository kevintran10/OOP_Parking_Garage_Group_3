# Parking Garage Project

Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). This project would usually be a pair programming project. However, for the size our class we will have groups of 3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
Each of you should share/switch these roles every 30mins-1hr -- Or you may elect to switch "drivers" after creating specific methods of the class.

The Initial Driver needs to Make sure to:
download the files below, create a local folder for the project,  create a github repository, commit the initial files,  share the link

Both navigators should then:
fork the code, clone it.

The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

When code has been updated, you will need to pull down the changes.

Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

Your parking garage class should have the following methods:
- takeTicket
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1
- payForParking
   - Display an input that waits for an amount from the user and store it in a variable
   - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
   - This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
   - If the ticket has been paid, display a message of "Thank You, have a nice day"
   - If the ticket has not been paid, display an input prompt for payment
      - Once paid, display message "Thank you, have a nice day!"
   - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
   - Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)


###### List group responsibilities below:

Adrienne:
The initial driver, downloaded files, created a local folder, created the github repository, committed the initial files and shared the link with the group.
Wrote the initial class function and runner function and helped write the takeTicket, payforParking, and leaveGarage methods.
Added a new method showSpaces to count spaces, edited the grammar, and updated existing loops to run in better order.

Kevin:
wrote a sample code of takeTicket, payforPark and leave garage to see if the code makes sense. Worked together on call with Adrienne and Danny to try and figure out some coding to make our code works properly. Contacted group via Slack/Discord to figure out times to work on the project together.

Danny:

###### Provide name and approximate line numbers where each person wrote their code

Adrienne lines 1 - 83 writing with the group, revising and editing.

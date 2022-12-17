This project was code-named = SchoolIO

Brief Overview:
The project is a portal for school registration, payment of fees, message broadcast to students and interuser message.
This build is based on django, javascript and sqlite (the default database system on django).


Signup:

For signing up/ initial registration
		1. Student must have his/her records with the school, so an ajax request is sent to be sure the student matric number corresponds with school record.
		2. The department on the list is automatically filled using AJAX
		3. A check if username has been taken before registration is made
		4. A check is also made if the matric number has registered before
		5. If all is checked student is allowed to register.


For course registration
		1. Student can only see courses of their level and department only.
		2. Students can easily click on any course to register and they can view courses they have registered for
		3. Students can there after make payment based on the total cost of subjects.

Message:
		Admin can send broadcast of messages to user departments and level, this can be used for the purpose of sending school notices to students
		Students can also message any user registered within the system asking for any information as may be requried by student


There are two models in this system.

1. The User model, this is used for the initial signup process and to create a user profile. Other information can be added for future versions of this project.

2. THe elearn model, this is mostly managed by the administrator, all the students matric numbers are listed there, courses for each department and level are also listed there.


It was a very enjoyable experience



# CLI-_SQL-_FINAL-PROJECT-PHASE_3
 
 <h2> DATUS MANAGEMENT SYSTEM {DMS} </h2>
        


<h3>PROBLEM STATEMENT</h3>

Datu(my dad) faces significant challenges in manually managing records for tea farmers, rental tenants, and milk purchases. These manual processes result in errors, inefficiencies, and difficulties in tracking profits accurately. Without a centralized system,my dad struggles to maintain consistency in record-keeping, perform accurate profit calculations, and generate timely reports. These challenges hinder effective management and decision-making, impeding my dad's ability to optimize business operations and maximize profitability.


<h3>SOLUTION STATEMENT</h3>

Developing a comprehensive Datu's Management System that encompasses tea farming, rental housing, and milk purchasing functionalities will streamline operations and enhance efficiency.This system will automate data management, profit calculations, and reporting, enabling my dad to make informed decisions and optimize his business processes.


<h3>MVPs/FEATURES</h3>


<h5>Milk Purchase Module:</h5>

<ol>-Add new dairy farmers with their names and IDs to a databse.</ol>
<ol>-Record daily liters of milk bought from each farmer.</ol>
<ol>-Calculate total liters bought from all farmers in a day.</ol>
<ol>-Calculate daily profits from milk sales.</ol>
<ol>-Calculate monthly payments to dairy farmers based on the total liters bought.(Buying Price @40ksh per litre)</ol>
<ol>-Generate reports for daily milk purchases, sales, and profits.(Selling Price  @60ksh per litre)</ol>


<h5>Tea Farmers Module:</h5>

<ol>-Add new farmers with their names and IDs to a database.</ol>
<ol>-Record daily, monthly, and yearly kilos of plucked tea for each farmer into a database.</ol>
<ol>-Calculate total kilos plucked by all farmers in a day, month, or year.</ol>
<ol>-Calculate the amount owed by each farmer based on plucking amounts (1 Kilo = 10 Ksh).</ol>
<ol>-Calculate daily profits from tea sales to the tea factory.(30ksh per kilo).</ol>
<ol>-Generate reports for daily, monthly, and yearly tea plucking activities and profits.</ol>


<h5>Rental Houses Module:</h5>

<ol>-Add new tenants with their names, house numbers, and IDs to a database.</ol>
<ol>-Record entry dates and the dates of next payments for each tenant.</ol>
<ol>-Generate reminders for upcoming rental payments.</ol>
<ol>-Track tenant turnover and occupancy rates.</ol>
<ol>-Generate reports for rental income and occupancy rates.</ol>



<h3>CHALLENGES ENCOUNTERED</h3>
<ol>Managing the project within allocated timeframe was challenge as I noticed that my project was huge and needed more time for better features and better improvements </ol>

<ol>Testing and Debugging: Identifying and resolving bugs & errors was a great challenge</ol>


<h3>TECHNOLOGIES USED</H3>

<ol>Sqlite3</ol>
<ol>Python</ol>


<h3>FUTURE PLANS</>
<ol>To add an automatic calculator that calculates and records the amount the Farmer or Plucker owes the Employer.</ol>

<h3> HOW TO RUN THIS PROJECT ON YOUR TERMINAL</h3>
<h4>Assuming you have cloned the Repository:</h4>
<ol>1.Open the terminal and run "pipenv update"</ol>
<ol>2. Run "pipenv shell" to enter into virtual environment</ol>
<ol>3. Seed the database by running "python3 seed.py" on the Terminal {For this project, It is already seeded}</ol>
<ol>4. Run "cli.py" on the terminal to interact with the project options</ol>

<h2>HAPPY CODING</>
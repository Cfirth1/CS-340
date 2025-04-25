# CS-340
## 🐾 Grazioso Salvare Rescue Dog Dashboard
This dashboard provides an interactive data visualization interface for filtering and analyzing animal shelter data, with the specific goal of identifying and selecting dogs suitable for different types of rescue missions — water, mountain, or disaster.
✅ Required Functionality
This project meets the following required functionalities:
•	Data Table Filtering: The data table can be filtered by both "Type of Animal" and "Rescue Type."
•	Pie Chart Filtering: The pie chart dynamically updates based on selected animal type and rescue type, showing breed distribution.
•	Map Integration: A map displays location-related data alongside the pie chart for better spatial insights.
•	Clean UI: Dash and Plotly were used to create a clean and user-friendly interface.
•	Responsive Layout: The layout displays the pie chart and map side-by-side for efficient use of screen space.
📷 Screenshots / Screencast
 
 
 

🛠️ Tools Used
🔸 Python
The primary programming language for building the dashboard and handling data processing.
🔸 MongoDB
MongoDB was used as the model component of the application. It is a NoSQL database that stores JSON-like documents, which made it ideal for storing semi-structured data from the animal shelter dataset.
MongoDB advantages:
•	Flexible schema: easily supports changing data structures.
•	Native support for JSON/BSON format simplifies interfacing with Python.
•	Integration with Python via pymongo allows direct querying and manipulation of collections.
🔸 Dash by Plotly
Dash was used to build the view and controller of the application.
Why Dash?
•	It allows building interactive, web-based dashboards with minimal front-end coding.
•	Built on top of Flask, Plotly, and React.js.
•	Provides simple callback decorators for interactivity and UI updates.
•	Perfect for data-focused web apps with Python.
🔸 Pandas
Used for data manipulation and filtering operations before visualizing data.

🔁 Project Workflow
1.	Connected to MongoDB to pull animal shelter data.
2.	Loaded and pre-processed the data using pandas.
3.	Designed the dashboard layout using Dash components (dcc.Dropdown, dcc.Graph, DataTable).
4.	Implemented callback functions to filter both the data table and pie chart based on dropdown inputs.
5.	Created logic to infer rescue type based on dog breeds rather than adding a new column.
6.	Deployed and tested dashboard locally (or via a platform like Heroku/Render if applicable).
7.	Documented functionality and included usage instructions.
________________________________________
🧩 Challenges and Solutions
Challenge: Duplicate Callback Outputs
Problem: Dash does not allow multiple callbacks with the same output.
Solution: Combined filter callbacks into one by using multiple Input() decorators in a single function and dash.callback_context to determine which input triggered the callback.
________________________________________
Challenge: Mapping Rescue Type to Breed
Problem: Dataset did not include a rescue type column.
Solution: Built a lookup dictionary to infer rescue type from breed keywords and applied it during filtering.

🔗 Resources & References
•	Dash by Plotly Documentation
•	MongoDB Python Driver (PyMongo)
•	Pandas Documentation
•	Plotly Graphing Library


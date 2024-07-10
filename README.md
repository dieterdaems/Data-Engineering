# Data Engineering Project

The task for the course Data Engineering is to scrape data from hackernews and set up a data lake pipeline. Everything runs in docker containers. I am using Dagster to orchestrate the pipeline, running on port 3000. On port 8501 I run a simple streamlit dashboard. The database used is MongoDB

V1.0

- Basic version based on Dagster tutorial setup

V1.1

- Removed mongoDB login credentials from Python script
- Fixed bug where layer and database name were switched
- Updated scheduling and fixed bug in Dagster schedules
- Updated project name from tutorial to dataEngineering
- Made a fix for when you start and RSS feed is empty (on weekends )
- cleaned up code and added documentation

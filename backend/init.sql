CREATE DATABASE learning_dashboard;


CREATE TABLE skills( 
    id SERIAL PRIMARY KEY, 
	title VARCHAR(255) NOT NULL, 
	subtitle VARCHAR(255),
	percentage_done INTEGER, 
	description TEXT, 
	archived BOOLEAN DEFAULT FALSE, 
	completed BOOLEAN DEFAULT FALSE
);


INSERT INTO skills(title, subtitle, percentage_done, description, archived, completed) 
values 
    ('Angular','Frontend',50, 'Building components, routing, and using Angular Material.', false, false), 
    ('TypeScript','Frontend',10,'Learning strong typing, interfaces, and cleaner JavaScript development.', false, false), 
    ('FastAPI','Backend',30,'Creating APIs, routes, and backend services with Python.', false, false)
;
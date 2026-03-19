import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-skill-card',
  templateUrl: './skill-card.component.html',
  styleUrls: ['./skill-card.component.css'],
  
})

export class SkillCardComponent {

title: string = 'Skills in development';

  courses = [
    {
      id: 1,
      title: 'Angular',
      subtitle: 'Frontend',
      percentage_done: 20,
      description: 'Building components, routing, and using Angular Material.',
      archived: false,
      completed: false
    },
    {
      id: 2,
      title: 'TypeScript',
      subtitle: 'Frontend',
      percentage_done: 10,
      description: 'Learning strong typing, interfaces, and cleaner JavaScript development.',
      archived: false,
      completed: false
    },
    {
      id: 3,
      title: 'FastAPI',
      subtitle: 'Backend',
      percentage_done: 30,
      description: 'Creating APIs, routes, and backend services with Python.',
      archived: false,
      completed: false
    },
    {
      id: 4,
      title: 'PostgreSQL',
      subtitle: 'Database',
      percentage_done: 0,
      description: 'Working with relational databases, tables, and SQL queries.',
      archived: false,
      completed: false
    }
  ];
}

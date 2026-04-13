
interface FocusItem {
  label: string;
  value: string;
}

interface SkillProgress {
  skill: string;
  category: string;
  progress: number;
  nextStep: string;
}

interface ProjectCard {
  name: string;
  stack: string;
  status: string;
  nextTask: string;
}

interface StatCard {
  label: string;
  value: number;
  description: string;
}
import { Component } from "@angular/core";
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  title = 'Learning OS';
  subtitle = 'Track skills, projects, and progress in one place';

  currentFocus = {
    title: 'Current Focus',
    summary: 'Building the Learning OS frontend and improving dashboard UX.',
    thisWeek: [
      'Improve visual design',
      'Add progress tracking',
      'Simplify card actions'
    ],
    nextStep: 'Build the Skills page filters and improve card layout'
  };

  stats: StatCard[] = [
    {
      label: 'Active Skills',
      value: 4,
      description: 'Frontend, backend, and database skills in progress'
    },
    {
      label: 'Projects in Progress',
      value: 1,
      description: 'Learning OS'
    },
    {
      label: 'Certifications',
      value: 2,
      description: 'AZ-104 and AZ-305 in progress'
    }
  ];

  skillsInProgress: SkillProgress[] = [
    {
      skill: 'Angular',
      category: 'Frontend',
      progress: 35,
      nextStep: 'Refactor card layout and improve page structure'
    },
    {
      skill: 'TypeScript',
      category: 'Frontend',
      progress: 20,
      nextStep: 'Add typed models for skill and project data'
    },
    {
      skill: 'FastAPI',
      category: 'Backend',
      progress: 10,
      nextStep: 'Build the first GET /skills endpoint'
    },
    {
      skill: 'PostgreSQL',
      category: 'Database',
      progress: 15,
      nextStep: 'Design the first app schema'
    }
  ];

  projects: ProjectCard[] = [
    {
      name: 'Learning OS',
      stack: 'Angular, FastAPI, PostgreSQL',
      status: 'In Progress',
      nextTask: 'Improve dashboard hierarchy and add progress bars'
    }

  ];

  weeklyProgress = {
    done: [
      'Built dashboard layout',
      'Created initial skill cards',
      'Committed version 1'
    ],
    nextUp: [
      'Add progress bars',
      'Improve color system',
      'Build Skills page filters'
    ]
  };
}
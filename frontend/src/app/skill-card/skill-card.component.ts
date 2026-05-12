import { Component, OnInit } from '@angular/core';
import { ApiService, Skill, SkillsResponse } from '../services/api.service';

@Component({
  selector: 'app-skill-card',
  templateUrl: './skill-card.component.html',
  styleUrls: ['./skill-card.component.css']
})
export class SkillCardComponent implements OnInit {
  title = 'Skills in development';

  courses: Skill[] = [];
  isLoading = false;
  errorMessage = '';

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadSkills();
  }

  loadSkills(): void {
    this.isLoading = true;
    this.errorMessage = '';

    this.apiService.getSkills().subscribe({
      next: (response: SkillsResponse) => {
        console.log('Skills response from backend:', response);
        this.courses = response.skills ?? [];
        this.isLoading = false;
      },
      error: (error: unknown) => {
        console.error('Could not load skills:', error);
        this.errorMessage = 'Could not load skills from the backend.';
        this.isLoading = false;
      }
    });
  }
}
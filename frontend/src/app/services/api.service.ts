import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Skill {
  id: number;
  title: string;
  subtitle: string | null;
  percentage_done: number;
  description: string | null;
  archived: boolean;
  completed: boolean;
}

export interface SkillsResponse {
  skills: Skill[];
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getSkills(): Observable<SkillsResponse> {
    return this.http.get<SkillsResponse>(`${this.apiUrl}/skills`);
  }
}
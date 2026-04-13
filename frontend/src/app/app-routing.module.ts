import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SkillCardComponent } from './skill-card/skill-card.component';
import { DashboardComponent } from './dashboard/dashboard.component';

const routes: Routes = [ 
  { path: 'skills-card', component: SkillCardComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: '**', redirectTo: '' },]

  ;

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

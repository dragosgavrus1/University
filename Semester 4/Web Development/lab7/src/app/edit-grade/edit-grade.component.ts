import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-edit-grade',
  standalone: true,
  imports: [HttpClientModule, CommonModule, FormsModule],
  templateUrl: './edit-grade.component.html',
  styleUrl: './edit-grade.component.css'
})
export class EditGradeComponent {
  editGradeId: number | null = null;
  editGradeCourse: string | null = null;
  editGradeValue: number | null = null;
  newCourse: string | null = null;
  newGrade: number | null = null;

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit(): void {
    // Retrieve grade details from session storage
    this.editGradeId = parseInt(sessionStorage.getItem('editGradeId') ?? '');
    this.editGradeCourse = sessionStorage.getItem('editGradeCourse');
    this.editGradeValue = parseInt(sessionStorage.getItem('editGradeValue') ?? '');

    // Initialize newCourse and newGrade with current values
    this.newCourse = this.editGradeCourse;
    this.newGrade = this.editGradeValue;
  }

  submitEdit(): void {
    // Make a POST request to edit_grade.php
    const data = {
      grade_id: this.editGradeId,
      grade: this.newGrade,
      course: this.newCourse
    };

    // this.http.post<any>('http://localhost/school/php/edit_grade.php', data).subscribe(
    this.http.post<any>('http://localhost:5069/edit_grade', data).subscribe(
      response => {
        console.log('Edit grade successful:', response);
        window.history.back();
      },
      error => {
        console.error('Failed to edit grade:', error);
      }
    );
  }

  back(): void {
    window.history.back();
  }
}

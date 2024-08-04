import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list-grades',
  standalone: true,
  imports: [HttpClientModule, CommonModule],
  templateUrl: './list-grades.component.html',
  styleUrl: './list-grades.component.css'
})
export class ListGradesComponent {
  grades: any[];

  constructor(private http: HttpClient) { this.grades = [];}

  ngOnInit(): void {
    const studentId = sessionStorage.getItem('studentId');
    if (studentId) {
      this.fetchGrades(studentId);
    } else {
      console.error('Student ID not found.');
    }
  }

  fetchGrades(studentId: string): void {
    // this.http.get<any[]>('http://localhost/school/php/read_grades.php', { params: { student_id: studentId } })
    this.http.get<any[]>('http://localhost:5069/grades', { params: { student_id: studentId } })
      .subscribe(
        data => {
          this.grades = data;
        },
        error => {
          console.error('Error fetching grades:', error);
        }
      );
  }
}

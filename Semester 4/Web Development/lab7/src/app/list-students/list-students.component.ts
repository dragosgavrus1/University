import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-students',
  standalone: true,
  imports: [HttpClientModule, CommonModule, FormsModule],
  templateUrl: './list-students.component.html',
  styleUrl: './list-students.component.css'
})
export class ListStudentsComponent {
  currentPage: number = 1;
  groupId: number = 923; // Replace with the actual group ID
  studentList: any[] = [];
  selectedStudentId: number = 0;
  studentGrades: any[] = [];

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void {
    this.getStudentList();
  }

  getStudentList(): void {
    // this.http.get<any[]>(`http://localhost/school/php/read_students.php?group_id=${this.groupId}&page=${this.currentPage}`)
    this.http.get<any[]>(`http://localhost:5069/student?group_id=${this.groupId}&page=${this.currentPage}`)
      .subscribe(
        data => {
          this.studentList = data;
        },
        error => {
          console.error('Error:', error);
        }
      );
  }

  nextPage(): void {
    this.currentPage++;
    this.getStudentList();
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.getStudentList();
    }
  }

  // Function to fetch grades for a specific student
  viewGrades(studentId: number): void {
    // Replace the URL with the actual endpoint for retrieving grades
    // this.http.get<any[]>('http://localhost/school/php/read_grades.php?student_id=' + studentId)
    this.http.get<any[]>('http://localhost:5069/grades', { params: { student_id: studentId } })
      .subscribe(
        data => {
          this.selectedStudentId = studentId;
          this.studentGrades = data;
        },
        error => {
          console.error('Error:', error);
        }
      );
  }

  addGrade(): void {
    sessionStorage.setItem('studentId', this.selectedStudentId.toString());
    this.router.navigate(['/add-grade']);
  }

  editGrade(gradeId: number, course: string, grade: number): void {
    sessionStorage.setItem('editGradeId', gradeId.toString());
    sessionStorage.setItem('editGradeCourse', course);
    sessionStorage.setItem('editGradeValue', grade.toString());

    this.router.navigate(['/edit-grade']);
  }
}

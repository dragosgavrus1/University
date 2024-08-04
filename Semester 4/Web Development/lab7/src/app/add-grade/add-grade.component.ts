import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-add-grade',
  standalone: true,
  imports: [HttpClientModule, FormsModule],
  templateUrl: './add-grade.component.html',
  styleUrl: './add-grade.component.css'
})
export class AddGradeComponent {
  grade: number | null = null;
  course: string | null = null;
  studentId: number | null = null; 

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    const studentId = sessionStorage.getItem('studentId');
    if (studentId !== null) {
      this.studentId = +studentId;
    }
  }

  addGrade(): void {
    if (this.grade !== null && this.course !== null && this.studentId !== null) {
      const data = {
        student_id: this.studentId,
        grade: this.grade,
        course: this.course
      };

      // this.http.post<any>('http://localhost/school/php/add_grade.php', data)
      this.http.post<any>('http://localhost:5069/add_grade', data)
        .subscribe(
          response => {
            console.log('Grade added successfully:', response);
          },
          error => {
            console.error('Error adding grade:', error);
          }
        );
    } else {
      console.error('Invalid grade or course');
    }
  }

  back(): void {
    window.history.back();
  }
}

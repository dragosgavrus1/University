import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string;
  password: string;

  constructor(private http: HttpClient , private router: Router) {
    this.username = '';
    this.password = '';
  }

  login(): void {
    const formData = new FormData();
    formData.append('name', this.username);
    formData.append('password', this.password);

    // Make a POST request to the login.php file
    //this.http.post<any>('http://localhost/school/php/login.php', formData).subscribe(
    this.http.post<any>('http://localhost:5069/login', formData).subscribe(
      response => {
        // Handle successful login response
        console.log('Login successful:', response);
        // Redirect or perform any other action as needed
        if (response.userType === 'student') {
          // Redirect to student page
          sessionStorage.setItem('studentId', response.studentId);
          this.router.navigate(['/student']);
        } else if (response.userType === 'teacher') {
          // Redirect to teacher page
          this.router.navigate(['/teacher']);
        }
      },
      error => {
        // Handle error response
        console.error('Login failed:', error);
        // Display error message to the user or perform any other action as needed
      }
    );
  }
}

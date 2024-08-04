import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ListStudentsComponent } from './list-students/list-students.component';
import { ListGradesComponent } from './list-grades/list-grades.component';
import { AddGradeComponent } from './add-grade/add-grade.component';
import { EditGradeComponent } from './edit-grade/edit-grade.component';

export const routes: Routes = [
    {
        path: '',
        redirectTo: '/login',
        pathMatch: 'full'
    },
    {
        path: 'login',
        component: LoginComponent
    },
    { path: 'student', component: ListGradesComponent },
    { path: 'teacher', component: ListStudentsComponent },
    { path: 'add-grade', component: AddGradeComponent },
    { path: 'edit-grade', component: EditGradeComponent }
];

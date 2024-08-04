using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using lab_9.Models;
using Microsoft.AspNetCore.Mvc;

namespace lab_9.Data_Abstraction_Layer
{
    public class DataAbstractionLayer
    {
        private string connectionString = "Server=localhost;Port=3306;Database=school;Uid=root;Pwd=;";

        private MySqlConnection connection;

        public DataAbstractionLayer()
        {
            connection = new MySqlConnection(connectionString);
        }

        public List<Student> GetStudents()
        {
            List<Student> students = new List<Student>();
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM students";
            MySqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                students.Add(new Student
                {
                    id = reader.GetInt32("id"),
                    name = reader.GetString("name"),
                    password = reader.GetString("password"),
                    group_id = reader.GetInt32("group_id")
                });
            }
            connection.Close();
            return students;
        }

        public List<Student> GetStudentsFromGroup(int group_id, int page)
        {
            List<Student> students = new List<Student>();
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM students WHERE group_id = @group_id Limit @offset, @limit";
            command.Parameters.AddWithValue("@group_id", group_id);
            command.Parameters.AddWithValue("@offset", (page-1)*4);
            command.Parameters.AddWithValue("@limit", 4);
            MySqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                students.Add(new Student
                {
                    id = reader.GetInt32("id"),
                    name = reader.GetString("name"),
                    password = reader.GetString("password"),
                    group_id = reader.GetInt32("group_id")
                });
            }
            connection.Close();
            return students;
        }


        public List<Teacher> GetTeachers()
        {
            List<Teacher> teachers = new List<Teacher>();
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM teacher";
            MySqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                teachers.Add(new Teacher
                {
                    id = reader.GetInt32("id"),
                    name = reader.GetString("name"),
                    password = reader.GetString("password"),
                    course = reader.GetString("course")
                });
            }
            connection.Close();
            return teachers;
        }

        public List<Grades> GetGrades()
        {
            List<Grades> grades = new List<Grades>();
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM grades";
            MySqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                grades.Add(new Grades
                {
                    grade_id = reader.GetInt32("grade_id"),
                    student_id = reader.GetInt32("student_id"),
                    course = reader.GetString("course"),
                    grade = reader.GetInt32("grade")
                });
            }
            connection.Close();
            return grades;
        }

        public List<Grades> GetStudentGrades(int student_id)
        {
            List<Grades> grades = new List<Grades>();
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "SELECT * FROM grades WHERE student_id = @student_id";
            command.Parameters.AddWithValue("@student_id", student_id);
            MySqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                grades.Add(new Grades
                {
                    grade_id = reader.GetInt32("grade_id"),
                    student_id = reader.GetInt32("student_id"),
                    course = reader.GetString("course"),
                    grade = reader.GetInt32("grade")
                });
            }
            connection.Close();
            return grades;
        }


        public void addGrade(Grades grade)
        {
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO grades (student_id, course, grade) VALUES (@student_id, @course, @grade)";
            command.Parameters.AddWithValue("@student_id", grade.student_id);
            command.Parameters.AddWithValue("@course", grade.course);
            command.Parameters.AddWithValue("@grade", grade.grade);
            command.ExecuteNonQuery();
            connection.Close();
        }

        public void updateGrade(Grades grade)
        {
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE grades SET student_id = @student_id, course = @course, grade = @grade WHERE grade_id = @grade_id";
            command.Parameters.AddWithValue("@student_id", grade.student_id);
            command.Parameters.AddWithValue("@course", grade.course);
            command.Parameters.AddWithValue("@grade", grade.grade);
            command.Parameters.AddWithValue("@grade_id", grade.grade_id);
            command.ExecuteNonQuery();
            connection.Close();
        }

        internal void AddGrade(int student_id, int grade, string course)
        {
            connection.Open();
            MySqlCommand maxIdCommand = connection.CreateCommand();
            maxIdCommand.CommandText = "SELECT MAX(grade_id) AS max_id FROM grades";
            int maxGradeId = 0;
            object maxIdResult = maxIdCommand.ExecuteScalar();
            if (maxIdResult != DBNull.Value && maxIdResult != null)
            {
                maxGradeId = Convert.ToInt32(maxIdResult);
            }

            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "INSERT INTO grades (grade_id, student_id, grade, course) VALUES (@grade_id, @student_id, @grade, @course)";
            int newGradeId = maxGradeId + 1;

            command.Parameters.AddWithValue("@grade_id", newGradeId);
            command.Parameters.AddWithValue("@student_id", student_id);
            command.Parameters.AddWithValue("@grade", grade);
            command.Parameters.AddWithValue("@course", course);
            command.ExecuteNonQuery();
            connection.Close();
        }

        internal void EditGrade(int grade_id, string course, int grade)
        {
            connection.Open();
            MySqlCommand command = connection.CreateCommand();
            command.CommandText = "UPDATE Grades SET course = @course, grade = @grade WHERE grade_id = @grade_id";
            command.Parameters.AddWithValue("@course", course);
            command.Parameters.AddWithValue("@grade", grade);
            command.Parameters.AddWithValue("@grade_id", grade_id);
            command.ExecuteNonQuery();
            connection.Close();
        }
    }
}

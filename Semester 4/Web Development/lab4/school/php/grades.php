<?php
session_start();
header("Access-Control-Allow-Origin: *");
header("Header Set Access-Control-Allow-Headers *");
?>
<!DOCTYPE html>
<html>
<head>
    <title>Grades List</title>
</head>
<body>
    <h1>Grades List</h1>

    <div id="gradesContainer"></div>
</body>

<script>

function fetchGrades(studentId) {
    fetch('read_grades.php?student_id=' + studentId)
        .then(response => response.json())
        .then(data => {
            student_id = studentId;
            displayGrades(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayGrades(grades) {
    const gradesContainer = document.getElementById('gradesContainer');
    gradesContainer.innerHTML = '';
    
    const gradesTable = document.createElement('table');
    gradesTable.innerHTML = '<tr><th>Course</th><th>Grade</th></tr>';
    
    grades.forEach(grade => {
        const row = gradesTable.insertRow();
        const courseCell = row.insertCell(0);
        const gradeCell = row.insertCell(1);

        courseCell.textContent = grade.course;
        gradeCell.textContent = grade.grade;
    });
    
    gradesContainer.appendChild(gradesTable);
}

const studentId = <?php echo isset($_SESSION['student_id']) ? $_SESSION['student_id'] : 'null'; ?>;
if (studentId) {
    fetchGrades(studentId);
} else {
    console.error('Student ID not found.');
}
</script>
</html>
<?php
include("config.php");

header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");
header("Access-Control-Allow-Methods: POST, OPTIONS");

// Handle preflight requests
if ($_SERVER["REQUEST_METHOD"] === "OPTIONS") {
    http_response_code(200); // OK
    exit();
}

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header("HTTP/1.1 405 Method Not Allowed");
    http_response_code(405);
    exit();
}

$json_data = json_decode(file_get_contents('php://input'), true);

// Retrieve the parameters from the POST request
$student_id = $json_data['student_id'];
$grade = $json_data['grade'];
$course = $json_data['course'];

$sqlMaxId = "SELECT MAX(grade_id) AS max_id FROM Grades";
$resultMaxId = mysqli_query($conn, $sqlMaxId);
$rowMaxId = mysqli_fetch_assoc($resultMaxId);
$maxId = $rowMaxId['max_id'];
$newGradeId = $maxId + 1;

// Prepare and execute SQL query to add the grade to the database
$sql = "INSERT INTO Grades (grade_id,  student_id, grade, course) VALUES (?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("iiis", $newGradeId, $student_id, $grade, $course);

if ($stmt->execute()) {
    // Grade added successfully
    http_response_code(201); // Created
    echo json_encode(array("message" => "Grade added successfully"));
} else {
    // Failed to add grade
    http_response_code(500); // Internal Server Error
    echo json_encode(array("error" => "Failed to add grade"));
}

$stmt->close();
$conn->close();
?>

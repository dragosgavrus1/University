<?php
include("config.php");

header('Content-Type: application/json; charset=UTF-8');
header("Access-Control-Allow-Origin: *");

// Check if the request method is GET
if ($_SERVER["REQUEST_METHOD"] != "GET") {
    header("HTTP/1.1 405 Method Not Allowed");
    http_response_code(405);
    exit();
}

// Check if the group ID and page number are provided in the query string
if (!isset($_GET['group_id']) || !isset($_GET['page'])) {
    header("HTTP/1.1 400 Bad Request");
    http_response_code(400);
    echo json_encode(array("error" => "Group ID and page number are required"));
    exit();
}

// Retrieve the group ID and page number from the query string
$group_id = $_GET['group_id'];
$page = $_GET['page'];

// Calculate the offset and limit for pagination
$limit = 4; // Maximum students per page
$offset = ($page - 1) * $limit;

// Prepare and execute SQL query to retrieve students from the specified group with pagination
$sql = "SELECT * FROM Students WHERE group_id = ? LIMIT ?, ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("iii", $group_id, $offset, $limit);
$stmt->execute();
$result = $stmt->get_result();
$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
$stmt->free_result();
$stmt->close();
$conn->close();

// Return the retrieved data as JSON response
echo json_encode($data);
http_response_code(200);
exit();
?>
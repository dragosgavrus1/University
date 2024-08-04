<!DOCTYPE html>
<html>
<head>
    <title>Game Result</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        h2 {
            margin-top: 50px;
        }
        p {
            font-size: 18px;
            margin-top: 20px;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
<h2>Game Result</h2>
<%
    ubb.project.lab9.model.Game game = (ubb.project.lab9.model.Game) session.getAttribute("game");
    ubb.project.lab9.model.User user = (ubb.project.lab9.model.User) session.getAttribute("user");
    int winner = game.getWinner();
%>
<% if (winner == 0) { %>
<p>Game over: It's a draw!</p>
<% } else if (winner == (game.getPlayer1Id() == user.getId() ? 1 : 2)) { %>
<p>Game over: You win!</p>
<% } else { %>
<p>Game over: You lose!</p>
<% } %>
<a href="game">Start a new game</a>
</body>
</html>

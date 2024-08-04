<!DOCTYPE html>
<html>
<head>
    <title>Tic-Tac-Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        h2 {
            margin-top: 20px;
        }
        p {
            font-size: 18px;
            margin-top: 20px;
        }
        table {
            margin-top: 20px;
            border-collapse: collapse;
            width: 300px;
            margin-left: auto;
            margin-right: auto;
        }
        td {
            width: 100px;
            height: 100px;
            border: 1px solid #ccc;
            font-size: 24px;
            text-align: center;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
<h2>Tic-Tac-Toe</h2>
<%
    ubb.project.lab9.model.Game game = (ubb.project.lab9.model.Game) request.getAttribute("game");
    ubb.project.lab9.model.User user = (ubb.project.lab9.model.User) session.getAttribute("user");
    int currentTurn = game.getCurrentTurn();
    boolean gameFinished = game.getStatus().equals("finished");
    int winner = game.getWinner();
%>
<p>Current player: <%= (currentTurn == (game.getPlayer1Id() == user.getId() ? 1 : 2)) ? "Your turn" : "Opponent's turn" %></p>
<table border="1">
    <%
        for (int i = 0; i < 3; i++) {
            out.println("<tr>");
            for (int j = 0; j < 3; j++) {
                out.println("<td>");
                char cellValue = game.getBoard().charAt(i * 3 + j);
                if (cellValue == '1') {
                    out.println("X");
                } else if (cellValue == '2') {
                    out.println("O");
                } else {
                    if (!gameFinished && currentTurn == (game.getPlayer1Id() == user.getId() ? 1 : 2)) {
                        out.println("<form action='game' method='post'>");
                        out.println("<input type='hidden' name='move' value='" + (i * 3 + j) + "'>");
                        out.println("<input type='submit' value='Move'>");
                        out.println("</form>");
                    } else {
                        out.println("&nbsp;");
                    }
                }
                out.println("</td>");
            }
            out.println("</tr>");
        }
    %>
</table>
</body>
</html>

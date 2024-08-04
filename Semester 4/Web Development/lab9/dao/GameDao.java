package ubb.project.lab9.dao;

import ubb.project.lab9.model.Game;
import ubb.project.lab9.model.User;
import ubb.project.lab9.model.Database;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class GameDao {
    public Game getCurrentGame(User user) {
        try (Connection conn = Database.getConnection()) {
            String query = "SELECT * FROM games WHERE (player1_id = ? OR player2_id = ?) AND status != 'finished'";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, user.getId());
            stmt.setInt(2, user.getId());
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return new Game(
                        rs.getInt("id"),
                        rs.getInt("player1_id"),
                        rs.getInt("player2_id"),
                        rs.getString("board"),
                        rs.getInt("current_turn"),
                        rs.getString("status")
                );
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Game createOrJoinGame(User user) {
        try (Connection conn = Database.getConnection()) {
            String query = "SELECT * FROM games WHERE status = 'waiting' FOR UPDATE";
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                int gameId = rs.getInt("id");
                String updateQuery = "UPDATE games SET player2_id = ?, status = 'in_progress' WHERE id = ?";
                PreparedStatement updateStmt = conn.prepareStatement(updateQuery);
                updateStmt.setInt(1, user.getId());
                updateStmt.setInt(2, gameId);
                updateStmt.executeUpdate();
                return new Game(
                        gameId,
                        rs.getInt("player1_id"),
                        user.getId(),
                        rs.getString("board"),
                        rs.getInt("current_turn"),
                        "in_progress"
                );
            } else {
                String checkInProgressQuery = "SELECT * FROM games WHERE status = 'in_progress'";
                PreparedStatement checkStmt = conn.prepareStatement(checkInProgressQuery);
                ResultSet checkRs = checkStmt.executeQuery();
                if (checkRs.next()) {
                    throw new IllegalStateException("A game is already in progress.");
                }

                String insertQuery = "INSERT INTO games (player1_id, board, current_turn, status) VALUES (?, '000000000', 1, 'waiting')";
                PreparedStatement insertStmt = conn.prepareStatement(insertQuery, PreparedStatement.RETURN_GENERATED_KEYS);
                insertStmt.setInt(1, user.getId());
                insertStmt.executeUpdate();
                ResultSet keys = insertStmt.getGeneratedKeys();
                if (keys.next()) {
                    int gameId = keys.getInt(1);
                    return new Game(gameId, user.getId(), 0, "000000000", 1, "waiting");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean makeMove(Game game, User user, String move) {
        int position = Integer.parseInt(move);
        if (game.getBoard().charAt(position) == '0' && game.getCurrentTurn() == (game.getPlayer1Id() == user.getId() ? 1 : 2)) {
            StringBuilder newBoard = new StringBuilder(game.getBoard());
            newBoard.setCharAt(position, (char) (game.getCurrentTurn() + '0'));
            game.setBoard(newBoard.toString());

            if (checkWin(newBoard.toString())) {
                System.out.println("Win");
                game.setStatus("finished");
                game.setWinner(game.getCurrentTurn());
            } else if (!newBoard.toString().contains("0")) {
                game.setStatus("finished");
                game.setWinner(3); // Draw
            } else {
                game.setCurrentTurn(game.getCurrentTurn() == 1 ? 2 : 1);
            }

            try (Connection conn = Database.getConnection()) {
                String updateQuery = "UPDATE games SET board = ?, current_turn = ?, status = ?, winner = ? WHERE id = ?";
                PreparedStatement updateStmt = conn.prepareStatement(updateQuery);
                updateStmt.setString(1, game.getBoard());
                updateStmt.setInt(2, game.getCurrentTurn());
                updateStmt.setString(3, game.getStatus());
                updateStmt.setInt(4, game.getWinner());
                updateStmt.setInt(5, game.getId());
                updateStmt.executeUpdate();
                return true;
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return false;
    }

    public boolean checkWin(String board) {
        int[][] winConditions = {
                {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // rows
                {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // columns
                {0, 4, 8}, {2, 4, 6} // diagonals
        };

        for (int[] condition : winConditions) {
            if (board.charAt(condition[0]) != '0' &&
                    board.charAt(condition[0]) == board.charAt(condition[1]) &&
                    board.charAt(condition[1]) == board.charAt(condition[2])) {
                return true;
            }
        }
        return false;
    }

}

package ubb.project.lab9.model;

public class Game {
    private int id;
    private int player1Id;
    private int player2Id;
    private String board;
    private int currentTurn;
    private String status;
    private int winner;

    public Game() {
    }

    public Game(int id, int player1Id, int player2Id, String board, int currentTurn, String status, int winner) {
        this.id = id;
        this.player1Id = player1Id;
        this.player2Id = player2Id;
        this.board = board;
        this.currentTurn = currentTurn;
        this.status = status;
        this.winner = winner;
    }
    public Game(int id, int player1Id, int player2Id, String board, int currentTurn, String status) {
        this.id = id;
        this.player1Id = player1Id;
        this.player2Id = player2Id;
        this.board = board;
        this.currentTurn = currentTurn;
        this.status = status;

    }

    public Game(int player1Id, String board, int currentTurn, String status) {
        this.player1Id = player1Id;
        this.board = board;
        this.currentTurn = currentTurn;
        this.status = status;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getPlayer1Id() {
        return player1Id;
    }

    public void setPlayer1Id(int player1Id) {
        this.player1Id = player1Id;
    }

    public int getPlayer2Id() {
        return player2Id;
    }

    public void setPlayer2Id(int player2Id) {
        this.player2Id = player2Id;
    }

    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }

    public int getCurrentTurn() {
        return currentTurn;
    }

    public void setCurrentTurn(int currentTurn) {
        this.currentTurn = currentTurn;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public int getWinner() {
        return winner;
    }

    public void setWinner(int winner) {
        this.winner = winner;
    }
}

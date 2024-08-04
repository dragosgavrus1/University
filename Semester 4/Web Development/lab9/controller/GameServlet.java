package ubb.project.lab9.controller;

import ubb.project.lab9.dao.GameDao;
import ubb.project.lab9.model.Game;
import ubb.project.lab9.model.User;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet(name = "GameServlet", value = "/game")
public class GameServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("user");
        if (user == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        GameDao gameDao = new GameDao();
        Game game = gameDao.getCurrentGame(user);

        if (game == null) {
            game = gameDao.createOrJoinGame(user);
            if (game == null) {
                response.getWriter().write("Error: A third player cannot join the game.");
                return;
            }
        }

        request.setAttribute("game", game);
        request.getRequestDispatcher("game.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("user");
        if (user == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        String move = request.getParameter("move");
        GameDao gameDao = new GameDao();
        Game game = gameDao.getCurrentGame(user);

        if (game != null && gameDao.makeMove(game, user, move)) {
            if (game.getWinner() == 1 || game.getWinner() == 2 || game.getWinner() == 3) {
                request.getSession().setAttribute("game", game);
                request.getRequestDispatcher("result.jsp").forward(request, response);
            }
            response.sendRedirect("game");
        } else {
            response.getWriter().write("Error: Invalid move.");
        }
    }
}

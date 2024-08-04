package ubb.project.lab9.controller;


import jakarta.servlet.ServletConfig;
import ubb.project.lab9.model.User;
import ubb.project.lab9.dao.UserDao;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name="RegisterServlet",value = "/register")
public class RegisterServlet extends HttpServlet {

    @Override
    public void init(ServletConfig config) throws ServletException {
        System.out.println("Register Servlet is being initialized");
        super.init(config);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        UserDao userDao = new UserDao();
        if (userDao.registerUser(new User(username, password))) {
            response.sendRedirect("login.jsp");
        } else {
            response.sendRedirect("register.jsp?error=Username already exists");
        }
    }
}

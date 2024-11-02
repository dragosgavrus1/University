module ubb.a8 {
    requires javafx.controls;
    requires javafx.fxml;


    opens ubb to javafx.fxml;
    //exports ubb;
    exports ubb.controller;
    opens ubb.controller to javafx.fxml;
    exports ubb.view.gui;
    opens ubb.view.gui to javafx.fxml;
    exports ubb.view.gui.list;
    opens ubb.view.gui.list to javafx.fxml;
    exports ubb.view.gui.program;
    opens ubb.view.gui.program to javafx.fxml;
}
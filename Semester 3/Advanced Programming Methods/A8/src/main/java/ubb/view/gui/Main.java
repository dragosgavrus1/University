package ubb.view.gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import ubb.view.gui.list.ListController;
import ubb.view.gui.program.ProgramController;

import java.io.InputStream;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader listLoader = new FXMLLoader();
        listLoader.setLocation(getClass().getResource("/ubb/list.fxml"));
        Parent root = listLoader.load();
        ListController listController = listLoader.getController();
        primaryStage.setTitle("Select");
        primaryStage.setScene(new Scene(root, 600, 400));
        primaryStage.show();

        FXMLLoader programLoader = new FXMLLoader();
        programLoader.setLocation(getClass().getResource("/ubb/program.fxml"));
        Parent programRoot = programLoader.load();
        ProgramController programController = programLoader.getController();
        listController.setProgramController(programController);
        Stage secondaryStage = new Stage();
        secondaryStage.setTitle("Interpreter");
        secondaryStage.setScene(new Scene(programRoot, 800, 800));
        secondaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
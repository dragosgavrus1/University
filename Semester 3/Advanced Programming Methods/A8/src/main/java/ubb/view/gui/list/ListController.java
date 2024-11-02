package ubb.view.gui.list;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.Region;
import ubb.controller.Controller;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.statements.IStatement;
import ubb.model.types.IType;
import ubb.model.utils.MyDictionary;
import ubb.view.Examples;
import ubb.repository.IRepository;
import ubb.repository.Repository;
import ubb.view.gui.program.ProgramController;

public class ListController {
    private ProgramController programController;

    public void setProgramController(ProgramController programController) {
        this.programController = programController;
    }

    @FXML
    private ListView<IStatement> programsList;

    @FXML
    private Button selectButton;

    @FXML
    public void initialize() {
        ObservableList<IStatement> allPrograms = FXCollections.observableArrayList(Examples.getAllExamples());
        programsList.setItems(allPrograms);
        programsList.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);

        selectButton.setOnAction(event -> {
            IStatement selectedProgram = programsList.getSelectionModel().getSelectedItem();
            int index = programsList.getSelectionModel().getSelectedIndex();
            if (index < 0)
                return;
            try {
                selectedProgram.typeCheck(new MyDictionary<String, IType>());
                PrgState prgState = new PrgState(selectedProgram);
                IRepository repo = new Repository(prgState, "log.txt");
                Controller controller = new Controller(repo);
                programController.setController(controller);
            } catch (InterpreterException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage(), ButtonType.OK);
                alert.getDialogPane().setMinHeight(Region.USE_PREF_SIZE);
                alert.showAndWait();
            }
        });
    }

}

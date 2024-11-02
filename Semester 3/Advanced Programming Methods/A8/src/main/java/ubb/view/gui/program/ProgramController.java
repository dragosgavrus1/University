package ubb.view.gui.program;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import ubb.controller.Controller;
import ubb.model.PrgState;
import ubb.model.statements.IStatement;
import ubb.model.types.IValue;
import ubb.model.utils.MyHeap;
import ubb.model.utils.MyIHeap;
import ubb.model.utils.MyIList;
import ubb.model.utils.MyList;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

class Pair<T1, T2> {
    T1 first;
    T2 second;

    public Pair(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }
}
public class ProgramController {
    private Controller controller;

    @FXML
    private TableView<Pair<Integer, IValue>> heapTable;

    @FXML
    private TableColumn<Pair<Integer, IValue>, Integer> addressColumn;

    @FXML
    private TableColumn<Pair<Integer, IValue>, String> valueColumn;

    @FXML
    private ListView<IValue> outputList;

    @FXML
    private ListView<String> fileTable;

    @FXML
    private ListView<Integer> programStateList;

    @FXML
    private ListView<String> executionStackList;

    @FXML
    private TableView<Pair<String, IValue>> symbolTable;

    @FXML
    private TableColumn<Pair<String, IValue>, String> symVariableColumn;

    @FXML
    private TableColumn<Pair<String, IValue>, String> symValueColumn;

    @FXML
    private TextField numberOfProgramStates;

    @FXML
    private Button oneStep;

    @FXML
    public void initialize(){
        addressColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().first).asObject());
        valueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        symVariableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first));
        symValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));

        oneStep.setOnAction(event -> {
            if(controller == null) {
                Alert alert = new Alert(Alert.AlertType.ERROR, "The program was not selected", ButtonType.OK);
                alert.showAndWait();
                return;
            }


            if(getCurrentProgramState() == null){
                Alert alert = new Alert(Alert.AlertType.ERROR, "Nothing left to execute", ButtonType.OK);
                alert.showAndWait();
                return;
            }

            try{
                controller.oneStep();
                populate();
            }
            catch (InterruptedException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage(), ButtonType.OK);
                alert.showAndWait();
            }
        });

        programStateList.setOnMouseClicked(mouseEvent -> populate());
    }


    private PrgState getCurrentProgramState(){
        if (controller.getProgramList().isEmpty())
            return null;
        int currentId = programStateList.getSelectionModel().getSelectedIndex();
        if (currentId == -1)
            return controller.getProgramList().get(0);
        return controller.getProgramList().get(currentId);
    }

    public void setController(Controller controller) {
        this.controller = controller;
        populate();
    }

    @FXML
    private void populate()
    {
        this.populateHeap();
        this.populateOutputList();
        this.populateFileTableList();
        this.populateProgramStatesIdentifiers();
        this.populateSymbolTableView();
        this.populateExecutionStack();
    }

    private void populateHeap()
    {
        MyIHeap currentHeap = new MyHeap();

        if (!controller.getProgramList().isEmpty())
            currentHeap = controller.getProgramList().get(0).getHeap();

        List<Pair<Integer, IValue>> heapTablePairs = new ArrayList<>();

        for (Map.Entry<Integer, IValue> entry : currentHeap.getContent().entrySet())
            heapTablePairs.add(new Pair<>(entry.getKey(), entry.getValue()));

        this.heapTable.setItems(FXCollections.observableArrayList(heapTablePairs));
        this.heapTable.refresh();
    }

    private void populateOutputList()
    {
        MyIList<IValue> outputList = new MyList<>();

        if (!controller.getProgramList().isEmpty())
            outputList = controller.getProgramList().get(0).getOutputList();

        else if (controller.getCopyProgram() != null)
            outputList = controller.getCopyProgram().getOutputList();

        this.outputList.setItems(FXCollections.observableArrayList(outputList.getOutput()));
        this.outputList.refresh();
    }

    private void populateFileTableList()
    {
        List<String> files = new ArrayList<>();

        if (!controller.getProgramList().isEmpty())
            files = new ArrayList<>(controller.getProgramList().get(0).getFileTable().getKeySet());

        else if (controller.getCopyProgram() != null)
            files = new ArrayList<>(controller.getCopyProgram().getFileTable().getKeySet());

        this.fileTable.setItems(FXCollections.observableArrayList(files));
        this.fileTable.refresh();
    }

    private void populateProgramStatesIdentifiers()
    {
        List<PrgState> programStates = this.controller.getProgramList();
        List<Integer> idList = programStates.stream()
                .map(PrgState::getId)
                .collect(Collectors.toList());

        this.programStateList.setItems(FXCollections.observableArrayList(idList));
        this.programStateList.refresh();

        if (programStates.size() > 1)
            this.numberOfProgramStates.setText("There are: " + programStates.size() + " programs!");
        else
            this.numberOfProgramStates.setText("There is one program!");
    }

    private PrgState getCurrentProgram()
    {
        if (this.controller.getProgramList().isEmpty())
            return null;

        int selectedId = programStateList.getSelectionModel().getSelectedIndex();

        if (selectedId == -1)
            return this.controller.getProgramList().get(0);

        return this.controller.getProgramList().get(selectedId);
    }

    private void populateSymbolTableView()
    {
        PrgState currentProgram = this.getCurrentProgram();
        List<Pair<String, IValue>> symbolTableList = new ArrayList<>();

        if (currentProgram != null)
            for (Map.Entry<String, IValue> entry : currentProgram.getSymbolTable().getContent().entrySet())
                symbolTableList.add(new Pair<>(entry.getKey(), entry.getValue()));

        this.symbolTable.setItems(FXCollections.observableArrayList(symbolTableList));
        this.symbolTable.refresh();
    }

    private void populateExecutionStack()
    {
        PrgState currentProgram = this.getCurrentProgram();
        List<String> exeStackList = new ArrayList<>();

        if (currentProgram != null)
            for (IStatement currentStatement : currentProgram.getStackStatements())
                exeStackList.add(currentStatement.toString());

        this.executionStackList.setItems(FXCollections.observableArrayList(exeStackList));
        this.executionStackList.refresh();
    }
}

#include "Matrix.h"
#include <stdexcept>

// Constructor - Theta(1)
Matrix::Matrix(int nrLines, int nrCols) : numRows(nrLines), numColumns(nrCols), root(nullptr) {}

// Destructor - Theta(n)
Matrix::~Matrix() {
    destroy(root);
}

// Private helper function to create a new node - Theta(1)
Matrix::Node* Matrix::createNode(int line, int column, TElem value) {
    Node* newNode = new Node;
    newNode->line = line;
    newNode->column = column;
    newNode->value = value;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

// Private helper function to recursively destroy the binary search tree - Theta(n)
void Matrix::destroy(Node* node) {
    if (node == nullptr)
        return;

    destroy(node->left);
    destroy(node->right);
    delete node;
}

// Private helper function to find a node in the binary search tree
// Best case: - Theta(1) the root is the searched node
// Worst case: - Theta(log n) when the element is far in the matrix 
// Complexity: O(log n)
Matrix::Node* Matrix::findNode(int line, int column) const {
    Node* current = root;

    while (current != nullptr) {
        if (current->line == line && current->column == column)
            return current;
        else if (line < current->line || (line == current->line && column < current->column))
            current = current->left;
        else
            current = current->right;
    }

    return nullptr;
}

// Private helper function to insert a new node into the binary search tree
// Best case: - Theta(1) the root is the element to add
// Worst case: - Theta(log n) the element is added on the last line and last column
// Complexity: O(log n)
void Matrix::insertNode(Node*& node, int line, int column, TElem value) {
    if (node == nullptr)
        node = createNode(line, column, value);
    else if (line < node->line || (line == node->line && column < node->column))
        insertNode(node->left, line, column, value);
    else if (line > node->line || (line == node->line && column > node->column))
        insertNode(node->right, line, column, value);
    else
        node->value = value;
}


// Private helper function to update the value of a node
// Theta(1)
void Matrix::updateNode(Node* node, TElem newValue) {
    node->value = newValue;
}



// Returns the number of lines
// Theta(1)
int Matrix::nrLines() const {
    return numRows;
}

// Returns the number of columns
// Theta(1)
int Matrix::nrColumns() const {
    return numColumns;
}

// Returns the element from line i and column j (indexing starts from 0)
// Throws exception if (i,j) is not a valid position in the Matrix
// Best case: Theta(1) the elemnt of the root is searched
// Worst case: Theta(log n) the element is at the farthest position
// Complexity: O(n)
TElem Matrix::element(int i, int j) const {
    if (i < 0 || i >= numRows || j < 0 || j >= numColumns)
        throw std::exception("Invalid position in matrix.");

    Node* node = findNode(i, j);
    if (node != nullptr)
        return node->value;

    return NULL_TELEM;
}

// Modifies the value from line i and column j
// Returns the previous value from the position
// Throws exception if (i,j) is not a valid position in the Matrix
// Best case: Theta(1) the elemnt of the root is searched
// Worst case: Theta(log n) the node needs to be added
// Complexity: O(n)
TElem Matrix::modify(int i, int j, TElem e) {
    if (i < 0 || i >= numRows || j < 0 || j >= numColumns)
        throw std::exception("Invalid position in matrix.");

    Node* node = findNode(i, j);
    if (node != nullptr) {
        TElem prevValue = node->value;
        if (e == NULL_TELEM)
            removeNode(node);
        else
        {
            updateNode(node, e);
        }
        return prevValue;
    }
    else {
        insertNode(root, i, j, e);
        return NULL_TELEM;
    }
}

// Best case: Theta(1)
// Worst case: Theta(n*m)
// Complexity: O(n) - n nr of connected nodes, max is n*m
void Matrix::resize(int newLines, int newCol)
{
    if (newLines <= 0 || newCol <= 0)
        throw std::exception();

    if (newLines >= this->numRows && newCol >= this->numColumns)
    {
        this->numRows = newLines;
        this->numColumns = newCol;
        return;
    }

    this->numRows = newLines;
    this->numColumns = newCol;
    
    // Adjust the binary search tree if necessary
    adjustTree(root, newLines, newCol);
}

// Best case: Theta(1)
// Worst case: Theta(log n) when the node has both successors and it needs to find a new successor which should be the farthest left one
// Complexity O(log n)
void Matrix::removeNode(Node*& node) {
    if (node == nullptr)
        return;

    if (node->left == nullptr && node->right == nullptr) {
        delete node;
        node = nullptr;
    }
    else if (node->left == nullptr) {
        Node* temp = node;
        node = node->right;
        delete temp;
    }
    else if (node->right == nullptr) {
        Node* temp = node;
        node = node->left;
        delete temp;
    }
    else {
        Node* successor = node->right;
        while (successor->left != nullptr)
            successor = successor->left;

        node->line = successor->line;
        node->column = successor->column;
        node->value = successor->value;
            
        delete successor;
    }
    
}

// Complexity O(n)
void Matrix::adjustTree(Node*& node, int newLines, int newCols) {
    if (node == nullptr)
        return;

    // Check if the node is out of bounds in the new dimensions
    if (node->line >= newLines || node->column >= newCols) {
        removeNode(node);
        adjustTree(node, newLines, newCols);  
        return;
    }

    adjustTree(node->left, newLines, newCols);
    adjustTree(node->right, newLines, newCols);
}
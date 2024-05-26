#pragma once

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
    struct Node {
        int line;
        int column;
        TElem value;
        Node* left;
        Node* right;
    };

    Node* root;
    int numRows;
    int numColumns;

    // Private helper functions
    Node* createNode(int line, int column, TElem value);
    Node* findNode(int line, int column) const;
    void destroy(Node* node);
    void insertNode(Node*& node, int line, int column, TElem value);
    void updateNode(Node* node, TElem newValue);
    void adjustTree(Node*& node, int newLines, int newCols);
    void removeNode(Node*& node);

public:
    // Constructor
    Matrix(int nrLines, int nrCols);

    // Destructor
    ~Matrix();

    // Returns the number of lines
    int nrLines() const;

    // Returns the number of columns
    int nrColumns() const;

    // Returns the element from line i and column j (indexing starts from 0)
    // Throws exception if (i,j) is not a valid position in the Matrix
    TElem element(int i, int j) const;

    // Modifies the value from line i and column j
    // Returns the previous value from the position
    // Throws exception if (i,j) is not a valid position in the Matrix
    TElem modify(int i, int j, TElem e);

    //resizes  a  Matrix  to  a  given  dimension. 
    // If  the  dimensions  are  less  than  the  current dimensions,   elements   from  positions   no   longer   existing   will   disappear.  
    //  If   the dimensions  are  greater  than  the  current  dimensions,  all  new  elements  will  be  by default NULL_TELEM.
    //throws exception if the new dimensions are zero or negative
    void resize(int newLines, int newCol);
};

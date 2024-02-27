#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

typedef enum {
    ADD,
    SUBTRACT,
    MULTIPLY,
    DIVIDE,
    PUSH,
} OpCode;

typedef struct {
    OpCode opCode;
    double operand;
} Instruction;

typedef struct {
    Instruction *code;
    int size;
    int capacity;
} CodeArray;

void initCodeArray(CodeArray *arr, int capacity) {
    arr->code = (Instruction *)malloc(capacity * sizeof(Instruction));
    arr->size = 0;
    arr->capacity = capacity;
}

void resizeCodeArray(CodeArray *arr) {
    arr->capacity *= 2;
    arr->code = (Instruction *)realloc(arr->code, arr->capacity * sizeof(Instruction));
}

void emit(CodeArray *arr, OpCode opCode, double operand) {
    if (arr->size >= arr->capacity) {
        resizeCodeArray(arr);
    }

    Instruction instr;
    instr.opCode = opCode;
    instr.operand = operand;

    arr->code[arr->size++] = instr;
}

int main() {
    CodeArray code;
    initCodeArray(&code, 10);

    char expression[100];

    // Prompt user for input expression
    printf("Enter an expression (e.g., 3 + 4 * 5): ");
    fgets(expression, sizeof(expression), stdin);

    // Tokenize and generate code based on the input expression
    char *token = strtok(expression, " \t\n");
    while (token != NULL) {
        if (isdigit((unsigned char)token[0])) {
            emit(&code, PUSH, atof(token));
        } else {
            if (token[0] == '+') emit(&code, ADD, 0.0);
            else if (token[0] == '-') emit(&code, SUBTRACT, 0.0);
            else if (token[0] == '*') emit(&code, MULTIPLY, 0.0);
            else if (token[0] == '/') emit(&code, DIVIDE, 0.0);
        }

        token = strtok(NULL, " \t\n");
    }

    // Print the generated code
    printf("\nGenerated Code:\n");
    for (int i = 0; i < code.size; ++i) {
        switch (code.code[i].opCode) {
            case ADD:
                printf("ADD\n");
                break;
            case SUBTRACT:
                printf("SUBTRACT\n");
                break;
            case MULTIPLY:
                printf("MULTIPLY\n");
                break;
            case DIVIDE:
                printf("DIVIDE\n");
                break;
            case PUSH:
                printf("PUSH %f\n", code.code[i].operand);
                break;
        }
    }

    // Clean up
    free(code.code);

    return 0;
}

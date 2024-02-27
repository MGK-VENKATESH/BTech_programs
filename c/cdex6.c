#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_RULES 10
#define MAX_SYMBOLS 10

char nonterminals[MAX_RULES];
char firstsets[MAX_RULES][MAX_SYMBOLS];
char followsets[MAX_RULES][MAX_SYMBOLS];

void computefirstset(char nonterminal) {
    // Implementation of computefirstset
}

void computefollowset(char nonterminal) {
    // Implementation of computefollowset
}

int main() {
    int numRules;
    printf("Enter the number of production rules: ");
    scanf("%d", &numRules);

    // Clear newline from the input buffer
    while (getchar() != '\n');

    for (int i = 0; i < numRules; i++) {
        printf("Enter production rule %d (format: nonterminal -> production): ", i + 1);
        scanf(" %c->%s", &nonterminals[i], firstsets[i]);
    }

    for (int i = 0; i < numRules; i++) {
        memset(followsets[i], 0, sizeof(followsets[i]));
    }

    for (int i = 0; i < numRules; i++) {
        computefirstset(nonterminals[i]);
        computefollowset(nonterminals[i]);
    }

    for (int i = 0; i < numRules; i++) {
        printf("First(%c)={%s}\n", nonterminals[i], firstsets[i]);
        printf("Follow(%c)={%s}\n", nonterminals[i], followsets[i]);
    }

    return 0;
}

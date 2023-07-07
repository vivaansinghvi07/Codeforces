#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define __USE_MINGW_ANSI_STDIO 0
typedef struct {
	char data;
	struct node *next;
} node; 

void append(node *head, char c) {
	while (head->next != NULL) {
		head = head->next;
	}
	head->data = c;
	head->next = malloc(sizeof(node)); 
}

void freel(node *head) {
	while(head != NULL) {
		node *temp = head;
		head = head->next;
		free(temp);
	}
}

node *revl(node *head) {
	node *temp = head;
	node *next;
	node *prev = NULL; 
	while(head != NULL) {
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return prev;	
}

void printl(node *head) {
	while (head != NULL) {
		printf("%c", head->data);
		head = head->next;
	}
	printf("\n");
}

int main(void) {
	int t, n, i, s;
	scanf("%d", &t); 
	while (t--) {
		scanf("%d", &n);
		if (n > 45) {
			printf("%d\n", -1);
			continue;
		}
		if (n < 10) {
			printf("%d\n", n);
			continue;
		}
		node *head = malloc(sizeof(node));
		i = 9;
		while (n > i) {
			n -= i;
			append(head, '0' + i--);
		}
		append(head, '0' + n);
		head = revl(head);
		printl(head);
		freel(head);
	}
	return 0;
}

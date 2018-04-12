#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to a head of the list
 * @number: node data
 *
 * Return: the address of a new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);
	new->n = number;
	new->next = NULL;

	if (head == NULL || *head == NULL)
	{
		*head = new;
		return (new);
	}

	if (number < 0 && (*head)->n <= 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (curr->next != NULL &&
		abs(number) >= abs(curr->next->n))
		curr = curr->next;

	new->next = curr->next;
	curr->next = new;

	return (new);
}

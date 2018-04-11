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
	listint_t *new_node;
	listint_t *slow;
	listint_t *fast;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	slow = *head;
	fast = slow->next;

	new_node->n = number;
	new_node->next = NULL;

	if (fast == NULL)
	{
		if (number >= slow->n)
			slow->next = new_node;
		else
		{
			new_node->next = slow;
			*head = new_node;
		}

		return (*head);
	}

	while (slow != NULL)
	{
		if (number >= slow->n
			&& number <= fast->n)
		{
			slow->next = new_node;
			new_node->next = fast;

			return (new_node);
		}

		slow = slow->next;
		fast = fast->next;
	}

	return (NULL);
}

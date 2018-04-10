#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: a pointer to the list
 *
 * Return: 1 (true) if the list has a cycle, 0 (false) otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *head_ptr = list;
	unsigned int count = 0;

	while (current != NULL)
	{
		if (count > 0 && head_ptr == current)
			return (1);

		current = current->next;
		count++;
	}

	return (0);
}
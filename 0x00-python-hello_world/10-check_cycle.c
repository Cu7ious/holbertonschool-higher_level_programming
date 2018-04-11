#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: a pointer to the list
 *
 * Return: 1 (true) if the list has a cycle, 0 (false) otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}

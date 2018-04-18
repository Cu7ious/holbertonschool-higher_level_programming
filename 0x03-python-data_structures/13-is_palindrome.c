#include "lists.h"
#include <stdio.h>

/**
 * list_length - calculates the lenth of the list
 * @head: pointer to a head of the list
 *
 * Return: the length of the list
 */
unsigned int list_length(listint_t *head)
{
	unsigned int c = 0;

	while (head != NULL)
	{
		head = head->next;
		c++;
	}

	printf("list_length: %d\n", c);
	return (c);
}

/**
 * value_at_index - returns the value of a node at the given index
 * @h: pointer to a head of the list
 * @idx: an index of the element
 * Return: value of the node at the given index
 */
int value_at_index(listint_t *h, unsigned int idx)
{
	unsigned int c = 0;

	do
	{
		if (c == idx)
			return (h->n);

		c++;
		h = h->next;
	}
	while (h != NULL);

	printf("value_at_index\n");
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to a head of the list
 *
 * Return: bool - 1 if is palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	unsigned int len, i;
	int a, b;

	if (!head || !(*head))
		return (0);

	len = list_length(*head) - 1;
	i = 0;

	while (!(len == i))
	{
		a = value_at_index(*head, i);
		b = value_at_index(*head, len);

		if (a != b)
			return (0);

		i++;
		--len;
	}

	return (1);
}

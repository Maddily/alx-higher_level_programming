#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: A pointer to the first node in the list
 *
 * Return: 1 if there's a cycle, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *hare;

	tort = hare = list;
	tort = tort->next;
	hare = hare->next->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tort == hare)
			return (1);
		tort = tort->next;
		hare = hare->next->next;
	}

	return (0);
}

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

	if (list == NULL)
		return (0);

	tort = hare = list;

	while (tort != NULL && hare != NULL && hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;

		if (tort == hare)
			return (1);
	}

	return (0);
}

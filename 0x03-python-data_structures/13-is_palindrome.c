#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: A pointer to the pointer pointing to the first node in a list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int length = 0, i = 0, j, *values = NULL;
	listint_t *last, *current;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	last = current = *head;

	while (last != NULL)
	{
		last = last->next;
		length++;
	}

	values = malloc(length * sizeof(int));
	if (values == NULL)
		return (0);

	values[i++] = (*head)->n;

	while (current->next != NULL)
	{
		current = current->next;
		values[i++] = current->n;
	}
	for (i = 0, j = length - 1; i < j; i++, j--)
	{
		if (values[i] != values[j])
		{
			free(values);
			return (0);
		}
	}

	free(values);
	return (1);
}

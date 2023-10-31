#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a node in a sorted list
 *
 * @head: A pointer to the pointer to the first node in the list
 * @number: The number in the new node
 *
 * Return: A pointer to the new node or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *tmp;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}

	current = *head;

	while (current != NULL)
	{
		if (current->n <= number && current->next->n > number)
		{
			tmp = current->next;
			current->next = new_node;
			new_node->next = tmp;
		}
		current = current->next;
	}

	return (new_node);
}

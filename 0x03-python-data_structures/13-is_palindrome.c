#include "lists.h"

/**
 * reverse_linked_list - Reverses a linked list
 * @head: A pointer to the first node in the list
 *
 * Return: A pointer to the first node in the reversed list
 */
listint_t *reverse_linked_list(listint_t *head)
{
	listint_t *temp1, *temp2;

	temp2 = NULL;
	while (head != NULL)
	{
		temp1 = head->next;
		head->next = temp2;
		temp2 = head;
		head = temp1;
	}
	head = temp2;

	return (head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: A pointer to the pointer pointing to the first node in a list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *second_part, *middle = NULL, *tortoise, *hare, *temp1, *temp2;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tortoise = hare = *head;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
	}
	if (hare != NULL)
	{
		middle = tortoise;
		tortoise = tortoise->next;
	}
	second_part = reverse_linked_list(tortoise);

	temp1 = *head;
	temp2 = second_part;
	while (temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			palindrome = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	second_part = reverse_linked_list(second_part);

	if (middle != NULL)
		middle->next = second_part;
	else
		*head = second_part;

	return palindrome;
}

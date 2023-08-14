#include "lists.h"
/**
 * is_palindrome - check if singly linked list is palindome
 * @head: head of ingly linked list
 * Return: 1 if palindome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL, *curr = slow, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
	listint_t *p1 = *head, *p2 = prev;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
			return (0);

		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}

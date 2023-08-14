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

	listint_t *second_half = slow;
	listint_t *prev = NULL, *curr = second_half, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	second_half = prev;
	listint_t *p1 = *head, *p2 = second_half;
	int is_palindrome = 1;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			is_palindrome = 0;
			break;
		}

		p1 = p1->next;
		p2 = p2->next;
	}

	// Restore the original second half
	prev = NULL;
	curr = second_half;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return is_palindrome;
}

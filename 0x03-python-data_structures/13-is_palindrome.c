#include "lists.h"
/**
 * is_palindrome - check if singly linked list is palindome
 * @head: head of ingly linked list
 * Return: 1 if palindome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i = 0, len = 0;
	int arr[100000];
	listint_t *temp = *head;

	if (!*head || !(*head)->next)
		return(1);
	while (temp)
	{
		arr[len] = temp->n;
		len++;
		temp = temp->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
			return (0);
	}
	return (1);
}

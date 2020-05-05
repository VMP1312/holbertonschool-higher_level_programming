#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Head.
 * Return: 1 if is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int cnt_max = 0, cnt = 0;
	int buff[4096];
	listint_t *palin;

	palin = *head;



	if (!*head || (*head)->next == NULL)
		return (1);

	while (palin)
	{
		buff[cnt_max] = palin->n;
		cnt_max++;
		palin = palin->next;
	}
	cnt_max--;
	while (cnt_max > cnt)
	{
		if (buff[cnt_max] != buff[cnt])
			return (0);
		cnt_max--, cnt++;
		
	}
	return (1);
}

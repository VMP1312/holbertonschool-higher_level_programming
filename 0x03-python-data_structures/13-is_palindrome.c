#include "lists.h"

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome.
 * @head: Head.
 * Return:
 */

int is_palindrome(listint_t **head)
{
	int cnt_max = 0, cnt = 0;
	int buff[4096];
	listint_t *palin;

	palin = *head;

	 if ((!*head) || (*head)->next == NULL)
		return(1); 
	
	while (!palin)
	{
		palin = palin->next;
		buff[cnt_max] = palin->n;
		cnt_max++;
	}

	while (cnt_max != cnt)
	{
		if (buff[cnt_max] != buff[cnt])
			return (0);
	}
	return (1);
}
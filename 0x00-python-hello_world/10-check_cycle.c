#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: list.
 * Return: 0 if there is not a cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga = list;
	listint_t *liebre = list;

	while (tortuga != NULL && liebre != NULL && liebre->next != NULL)
	{
		tortuga = tortuga->next;
		liebre = liebre->next->next;
		if (tortuga == liebre)
		{
			return (1);
		}
	}
	return (0);

}

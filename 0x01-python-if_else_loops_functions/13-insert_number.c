#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list.
 * @head: Head.
 * @number: number.
 * Return: Node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL;
	listint_t *move = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	if (*head == NULL || move->n >= number)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (move->next != NULL && move->next->n < number)
	{
		move = move->next;
	}
	newnode->n = number;
	newnode->next = move->next;
	move->next = newnode;

	return (newnode);
}
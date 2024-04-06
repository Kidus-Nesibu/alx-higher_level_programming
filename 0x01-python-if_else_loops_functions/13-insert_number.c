#include"lists.h"
/**
 * insert_node - inserts  the node at the correct order
 * @head: the head of the linked list
 * @number: the data to be stored in the linked list
 * Return: the address of the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	tmp = *head;

	while (tmp->n < number && tmp != NULL)
	{
		prev = tmp;
		tmp = tmp->next;
	}
	prev->next = new;
	new->next = tmp;
	return (new);

}

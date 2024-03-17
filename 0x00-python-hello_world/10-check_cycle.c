#include"lists.h"
/**
 * check_cycle - check if there is a cycle in linked list
 * @list: is the head of the linked list
 * Return: 0 0r one depending on the result
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr1 = list;
	ptr2 = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
		{
			return (1);
		}

	}
	return (0);
}

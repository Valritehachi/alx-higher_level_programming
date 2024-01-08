#include <stddef.h>
#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * list2array - checks a palindrome
 * @head: pointer to list to be freed
 * @length: pointer to list to be freed
 * Return: 0
 */
int *list2array(listint_t **head, int *length)
{
	int *items;
	listint_t *list;

	*length = 0;
	list = *head;
	while (list != NULL)
	{
		(*length)++;
		list = list->next;
	}
	items = (int *)malloc(sizeof(int) * *length);
	if (items == NULL)
	{
		return (NULL);
	}
	*length = 0;
	list = *head;
	while (list != NULL)
	{
		items[(*length)++] = list->n;
		list = list->next;
	}
	return (items);
}

/**
 * is_palindrome - checks a palindrome
 * @head: pointer to list to be freed
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	int *items;
	int length, start, end, p;


	if (head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	items = list2array(head, &length);
	if (items == NULL)
	{
		return (0);
	}

	start = 0;
	end = length - 1;
	p = (items[start] == items[end]) ? 1 : 0;
	while (p == 1 && start < end)
	{
		start++;
		end--;
		p = (items[start] == items[end]) ? 1 : 0;
	}
	free(items);
	return (p);
}

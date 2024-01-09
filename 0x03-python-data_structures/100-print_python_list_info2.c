#include <unistd.h>
#include <stdio.h>
#include <stddef.h>
#include <assert.h>
#include <object.h>
#include <listobject.h>

/**
 *print_python_list_info - check the code for
 *@p: ...
 * Return: Always 0.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i;
	PyObject *element;

	list = (PyListObject *)p;
	if (!PyList_Check(p))
	{
		printf("Error: Not a PyListObject\n");
		return;
	}

	printf("[*] Size of the Python List: %zd\n", PyList_GET_SIZE(list));
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < PyList_GET_SIZE(list); i++)
	{
		element = PyList_GET_ITEM(list, i);
		printf("Element %zd:  %s\n", i, Py_TYPE(element)->tp_name);
	}

}

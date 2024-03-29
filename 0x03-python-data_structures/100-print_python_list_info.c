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
	int i, size, allocated;

	if (!PyList_Check(p))
	{
		return;
	}

	size = (int)PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		const char *type = Py_TYPE(PyList_GetItem(p, i))->tp_name;

		printf("Element %d: %s\n", i, type);
	}
}

#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Print
 * @p: A pointer
 * return: 0
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	char *trying_str = NULL;
	int y;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
PyBytes_AsStringAndSize(p, &trying_str, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (y = 0; y <= size && y < 10; y++)
		printf(" %02hhx", trying_str[y]);
	printf("\n");
}
/**
 * print_python_list - Print
 * @p: A pointer
 * return: 0
 */
void print_python_list(PyObject *p)
{
	int y;
	long int size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (y = 0; y < size; y++)
	{
		type = (list->ob_item[y])->ob_type->tp_name;
		printf("Element %i: %s\n", y, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[y]);
	}
}

